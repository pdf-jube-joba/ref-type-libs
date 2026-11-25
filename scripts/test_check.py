from contextlib import redirect_stderr, redirect_stdout
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch


spec = importlib.util.spec_from_file_location('library_check', Path(__file__).with_name('check.py'))
check = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check)


FAKE_CHECKER = r'''
import argparse
import json
import os
from pathlib import Path
import signal
import sys
import time
import tomllib

parser = argparse.ArgumentParser()
parser.add_argument('entry', type=Path)
parser.add_argument('--list-modules', action='store_true')
parser.add_argument('--save-source-snapshot', type=Path)
parser.add_argument('--source-snapshot', type=Path)
parser.add_argument('--module')
parser.add_argument('--module-only', action='store_true')
parser.add_argument('--cache-dir', type=Path)
parser.add_argument('--report-json', type=Path)
args, remaining = parser.parse_known_args()
control_path = Path(__file__).with_name('control.json')
control = json.loads(control_path.read_text())

def capture(entry):
    data = tomllib.loads((entry / 'ref.toml').read_text())
    entries = [entry / p for p in data['workspace']['packages']] if 'workspace' in data else [entry]
    seen, records, modules = set(), [], []
    while entries:
        package = entries.pop().resolve()
        if package in seen:
            continue
        seen.add(package)
        manifest = package / 'ref.toml'
        data = tomllib.loads(manifest.read_text())
        records.append([str(manifest), manifest.read_text()])
        entries.extend(package / dependency['path'] for dependency in data.get('dependencies', {}).values())
        for source in sorted((package / 'src').rglob('*.ref')):
            records.append([str(source), source.read_text()])
            parts = source.relative_to(package / 'src').with_suffix('').parts
            if parts[-1] == 'root':
                parts = parts[:-1]
            modules.append('.'.join([data['package']['name'], *parts]))
    return {'opaque_format': 91, 'payload': sorted(records), 'names': sorted(modules)}

if args.list_modules:
    payload = capture(args.entry)
    args.save_source_snapshot.write_text(json.dumps(payload))
    print('\n'.join(payload['names']))
    sys.exit(0)

payload = json.loads(args.source_snapshot.read_text())
wanted = [name for name in payload['names'] if args.module is None or name == args.module or (not args.module_only and name.startswith(args.module + '.'))]
mode = control.get('mode') if control.get('module', args.module) == args.module else None
if mode in ['sleep', 'cancel']:
    def stopped(_signum, _frame):
        Path(__file__).with_name('stopped').write_text('terminated')
        sys.exit(130)
    signal.signal(signal.SIGTERM, stopped)
    if mode == 'cancel':
        os.kill(os.getppid(), signal.SIGTERM)
    time.sleep(10)
outcome = 'memory-limit' if mode == 'memory' and not args.module_only and len(wanted) > 1 else 'rejected' if mode == 'reject' else 'accepted'
result = {
    'outcome': outcome,
    'verified_modules': [] if mode == 'coverage' else [name.split('.') for name in wanted],
    'checked_modules': [name.split('.') for name in wanted],
    'storage': {'save_failures': 1 if mode == 'storage' else 0},
}
if mode == 'edit':
    source = next(Path(path) for path, _ in payload['payload'] if path.endswith('.ref'))
    source.write_text(source.read_text() + '\nchanged\n')
if mode == 'snapshot':
    payload['changed'] = True
    args.source_snapshot.write_text(json.dumps(payload))
if mode != 'missing':
    args.report_json.write_text(json.dumps(result))
sys.exit(0 if outcome == 'accepted' else 1)
'''


class CheckTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.directory = Path(self.temporary.name)
        self.root = self.directory / 'repo'
        self.root.mkdir()
        library = self.root / 'libs'
        library.mkdir()
        (library / 'ref.toml').write_text('[workspace]\npackages = ["base", "client", "other"]\n')
        for name in ['base', 'client', 'other']:
            package = library / name
            (package / 'src').mkdir(parents=True)
            manifest = f'[package]\nname = "{name}"\n'
            if name == 'client':
                manifest += '[dependencies]\nan_alias = { path = "../base" }\n'
            (package / 'ref.toml').write_text(manifest)
            (package / 'src/root.ref').write_text('value\n')
        for name in ['One', 'Two']:
            (library / 'base/src' / f'{name}.ref').write_text('proof\n')
        (self.root / '.gitignore').write_text('refcache/\n.checks/\n')
        self.git('init', '-q')
        self.git('add', '.')
        self.git('-c', 'user.name=Check Tests', '-c', 'user.email=check@example.invalid', 'commit', '-qm', 'Initial sources')
        self.fake = self.directory / 'external-checker.py'
        self.fake.write_text(FAKE_CHECKER)
        self.control = self.directory / 'control.json'
        self.configure()

    def git(self, *args):
        return subprocess.run(['git', *args], cwd=self.root, check=True, capture_output=True)

    def configure(self, **values):
        self.control.write_text(json.dumps(values))

    def plan(self, *args):
        code, result = self.invoke('plan', *args)
        self.assertEqual(code, 0, result)
        return result

    def invoke(self, action, *args, fake_checker=False):
        output = io.StringIO()
        with redirect_stdout(output), redirect_stderr(io.StringIO()):
            if fake_checker:
                with patch.object(check, 'resolve_checker', return_value=[sys.executable, str(self.fake)]):
                    code = check.main([action, '--json', *args], root=self.root)
            else:
                code = check.main([action, '--json', *args], root=self.root)
        return code, json.loads(output.getvalue())

    def run_check(self, *args):
        code, result = self.invoke('run', '--package', 'base', '--scope', 'changed', *args, fake_checker=True)
        self.assertEqual(code == 0, result['outcome'] == 'accepted', result)
        return json.loads(Path(result['report']).read_text())

    def test_reverse_dependencies_follow_paths_and_aliases(self):
        self.assertEqual(set(self.plan('--package', 'base')['packages']), {'base', 'client'})
        self.assertEqual(set(self.plan('--package', 'base', '--scope', 'changed')['packages']), {'base'})

    def test_staged_deleted_untracked_sources_and_docs(self):
        (self.root / 'libs/base/src/One.ref').unlink()
        (self.root / 'libs/client/src/New.ref').write_text('new\n')
        (self.root / 'libs/other/README.md').write_text('Documentation.\n')
        self.git('add', 'libs/base/src/One.ref')
        plan = self.plan()
        self.assertEqual(set(plan['seeds']), {'base', 'client'})
        self.assertEqual(set(plan['packages']), {'base', 'client'})

    def test_committed_changes_can_be_selected_since_revision(self):
        (self.root / 'libs/base/src/One.ref').write_text('new\n')
        self.git('add', '.')
        self.git('-c', 'user.name=Check Tests', '-c', 'user.email=check@example.invalid', 'commit', '-qm', 'Edit')
        self.assertEqual(self.plan()['packages'], [])
        self.assertEqual(set(self.plan('--since', 'HEAD~1')['packages']), {'base', 'client'})

    def test_manifest_change_selects_whole_workspace(self):
        path = self.root / 'libs/ref.toml'
        path.write_text(path.read_text() + '\n')
        self.assertEqual(set(self.plan()['packages']), {'base', 'client', 'other'})

    def test_no_changes_does_not_require_checker_or_claim_acceptance(self):
        code, result = self.invoke('run', '--checker', 'unavailable-checker')
        self.assertEqual(code, 0)
        self.assertEqual(result['outcome'], 'nothing-selected')

    def test_module_focus_infers_package(self):
        plan = self.plan('--module', 'base.One')
        self.assertEqual(plan['scope'], 'changed')
        self.assertEqual(plan['packages'], ['base'])
        result = self.run_check('--module', 'base.One')
        self.assertEqual(result['outcome'], 'accepted')
        self.assertEqual(result['jobs'][0]['verified'], ['base.One'])

    def test_missing_checker_is_an_error_when_checks_are_selected(self):
        code, result = self.invoke('run', '--package', 'base', '--checker', 'unavailable-checker')
        self.assertNotEqual(code, 0)
        self.assertEqual(result['outcome'], 'error')
        self.assertTrue(result['error'])

    def test_incomplete_report_is_rejected(self):
        self.configure(mode='coverage')
        result = self.run_check()
        self.assertEqual(result['outcome'], 'failed')
        self.assertTrue(result['error'])

    def test_storage_failure_is_rejected_even_with_success_exit(self):
        self.configure(mode='storage')
        result = self.run_check()
        self.assertEqual(result['outcome'], 'failed')
        self.assertTrue(result['error'])

    def test_missing_report_cannot_reuse_previous_success(self):
        self.assertEqual(self.run_check()['outcome'], 'accepted')
        self.configure(mode='missing')
        result = self.run_check()
        self.assertEqual(result['outcome'], 'failed')
        self.assertTrue(result['error'])

    def test_memory_limit_splits_without_omitting_parent(self):
        self.configure(mode='memory')
        result = self.run_check()
        self.assertEqual(result['outcome'], 'accepted')
        self.assertEqual(set(result['jobs'][0]['verified']), {'base', 'base.One', 'base.Two'})

    def test_whole_workspace_completes_after_memory_limit(self):
        self.configure(mode='memory')
        result = self.run_check('--scope', 'all')
        self.assertEqual(result['outcome'], 'accepted')
        verified = {name for job in result['jobs'] for name in job['verified']}
        self.assertEqual(verified, {'base', 'base.One', 'base.Two', 'client', 'other'})

    def test_live_edits_make_result_fail_and_status_stale(self):
        self.assertEqual(self.run_check()['outcome'], 'accepted')
        code, current = self.invoke('status')
        self.assertEqual(code, 0)
        self.assertTrue(current['inputs_current'])
        (self.root / 'libs/base/src/Added.ref').write_text('added\n')
        code, stale = self.invoke('status')
        self.assertEqual(code, 0)
        self.assertEqual(stale['outcome'], 'stale')
        self.configure(mode='edit')
        result = self.run_check()
        self.assertEqual(result['outcome'], 'failed')
        self.assertTrue(result['error'])

    def test_snapshot_changes_are_detected(self):
        self.configure(mode='snapshot')
        result = self.run_check()
        self.assertEqual(result['outcome'], 'failed')
        self.assertTrue(result['error'])

    def test_cancellation_stops_checker(self):
        self.configure(mode='cancel')
        self.assertEqual(self.run_check()['outcome'], 'interrupted')
        self.assertTrue((self.directory / 'stopped').exists())

    def test_total_time_limit_stops_checker(self):
        self.configure(mode='sleep')
        result = self.run_check('--time-limit-seconds', '1')
        self.assertEqual(result['outcome'], 'failed')
        self.assertTrue(result['error'])

    def test_failure_stops_later_packages(self):
        self.configure(mode='reject', module='base')
        result = self.run_check('--scope', 'affected')
        self.assertEqual(result['outcome'], 'failed')
        self.assertFalse(any(job.get('verified') for job in result['jobs']))


if __name__ == '__main__':
    unittest.main()
