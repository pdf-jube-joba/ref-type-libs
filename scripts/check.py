import argparse
from collections import deque
from contextlib import contextmanager
from datetime import datetime, timezone
import fcntl
import hashlib
import json
import math
import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import time
import tomllib


ROOT = Path(__file__).resolve().parents[1]


class CheckError(Exception):
    pass


def load_json(path):
    return json.loads(path.read_text())


def save_json(path, value):
    temporary = path.with_suffix('.tmp')
    temporary.write_text(json.dumps(value, indent=2) + '\n')
    temporary.replace(path)


def file_digest(path):
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def snapshot_digest(path):
    value = json.dumps(load_json(path), sort_keys=True, separators=(',', ':'))
    return hashlib.sha256(value.encode()).hexdigest()


class Workspace:
    def __init__(self, root):
        self.root = root.resolve()
        self.library = self.root / 'libs'
        self.paths = {}
        self.manifests = {}
        for member in tomllib.loads((self.library / 'ref.toml').read_text())['workspace']['packages']:
            path = (self.library / member).resolve()
            if not path.is_relative_to(self.library):
                raise CheckError(f'workspace package is outside libs/: {member}')
            manifest = tomllib.loads((path / 'ref.toml').read_text())
            name = manifest['package']['name']
            if name in self.paths or path in self.paths.values():
                raise CheckError(f'duplicate workspace package: {name}')
            self.paths[name] = path
            self.manifests[name] = manifest
        by_path = {path: name for name, path in self.paths.items()}
        self.dependencies = {}
        for name, manifest in self.manifests.items():
            dependencies = set()
            for alias, dependency in manifest.get('dependencies', {}).items():
                if not isinstance(dependency, dict) or 'path' not in dependency:
                    raise CheckError(f'{name}: dependency {alias} must have a local path')
                destination = (self.paths[name] / dependency['path']).resolve()
                if destination not in by_path:
                    raise CheckError(f'{name}: register dependency {alias} in libs/ref.toml')
                dependencies.add(by_path[destination])
            self.dependencies[name] = dependencies

    def owner(self, path):
        owners = [name for name, directory in self.paths.items() if path.is_relative_to(directory)]
        return max(owners, key=lambda name: len(self.paths[name].parts)) if owners else None

    def closure(self, names, reverse=False):
        selected = set(names)
        pending = list(names)
        while pending:
            name = pending.pop()
            adjacent = {other for other, dependencies in self.dependencies.items() if name in dependencies} if reverse else self.dependencies[name]
            pending.extend(adjacent - selected)
            selected.update(adjacent)
        return selected

    def ordered(self, names):
        remaining = set(names)
        ordered = []
        while remaining:
            ready = sorted(name for name in remaining if not self.dependencies[name] & remaining)
            if not ready:
                raise CheckError('cyclic package dependencies: ' + ', '.join(sorted(remaining)))
            ordered.extend(ready)
            remaining.difference_update(ready)
        return ordered

    def inputs(self, names):
        paths = {self.library / 'ref.toml'} | {path / 'ref.toml' for path in self.paths.values()}
        for name in self.closure(names):
            paths.update((self.paths[name] / 'src').rglob('*.ref'))
        digest = hashlib.sha256()
        for path in sorted(paths):
            digest.update(str(path.relative_to(self.root)).encode() + b'\0')
            digest.update(path.read_bytes() + b'\0')
        return {'sha256': digest.hexdigest(), 'files': len(paths)}


def changed_files(root, since):
    def git(*arguments):
        result = subprocess.run(['git', *arguments], cwd=root, capture_output=True)
        if result.returncode:
            raise CheckError(result.stderr.decode(errors='replace').strip())
        return result.stdout
    revision = git('rev-parse', '--verify', '--end-of-options', since + '^{commit}').decode().strip()
    tracked = git('diff', '--name-only', '--no-renames', '-z', revision, '--', 'libs')
    untracked = git('ls-files', '--others', '--exclude-standard', '-z', '--', 'libs')
    return sorted({os.fsdecode(path) for path in (tracked + untracked).split(b'\0') if path})


def make_plan(workspace, args):
    scope = args.scope or ('changed' if args.module else 'affected')
    files = []
    seeds = set(args.package)
    unknown = seeds - workspace.paths.keys()
    if unknown:
        raise CheckError('unknown package: ' + ', '.join(sorted(unknown)))
    if args.module:
        owner = args.module.split('.')[0]
        if owner not in workspace.paths or seeds - {owner} or scope != 'changed':
            raise CheckError('--module requires its own package and --scope changed')
        seeds.add(owner)
    if scope == 'all':
        selected = set(workspace.paths)
    else:
        if not seeds:
            files = changed_files(workspace.root, args.since)
            for filename in files:
                path = workspace.root / filename
                if path == workspace.library / 'ref.toml':
                    seeds.update(workspace.paths)
                elif path.suffix == '.ref' or path.name == 'ref.toml':
                    owner = workspace.owner(path.resolve())
                    if not owner:
                        raise CheckError(f'register changed source in libs/ref.toml: {filename}')
                    seeds.add(owner)
        selected = workspace.closure(seeds, reverse=True) if scope == 'affected' else seeds
    return {
        'scope': scope, 'since': args.since, 'changed_files': files,
        'seeds': sorted(seeds), 'packages': workspace.ordered(selected),
        'module': args.module, 'module_only': args.module_only,
    }


def resolve_checker(value):
    candidate = shutil.which(value)
    if not candidate:
        raise CheckError('checker executable not found; set --checker or REF_TYPE_CHECKER')
    return [str(Path(candidate).resolve())]


def module_names(report, field):
    values = report[field]
    if not isinstance(values, list) or any(not isinstance(path, list) or not path or any(not isinstance(part, str) for part in path) for path in values):
        raise CheckError(f'invalid CLI report field: {field}')
    return {'.'.join(path) for path in values}


@contextmanager
def run_lock(state):
    state.mkdir(parents=True, exist_ok=True)
    with (state / 'lock').open('a') as stream:
        try:
            fcntl.flock(stream, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise CheckError(f'another check is running; inspect {state / "latest.json"}') from None
        yield


class Runner:
    def __init__(self, workspace, plan, args, checker):
        self.workspace, self.plan, self.args, self.checker = workspace, plan, args, checker
        self.state = workspace.root / '.checks'
        self.cache = workspace.library / 'refcache'
        self.child = None
        self.cancelled = False
        self.started = time.monotonic()
        self.deadline = self.started + args.time_limit_seconds if args.time_limit_seconds else None
        stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ')
        self.attempt = self.state / stamp
        self.report = {
            'version': 1, 'outcome': 'running', 'plan': plan, 'jobs': [],
            'checker': checker, 'checker_sha256': file_digest(Path(checker[0])),
            'script_sha256': file_digest(Path(__file__)), 'inputs': workspace.inputs(plan['packages']),
            'cache_dir': str(self.cache), 'report': str(self.attempt / 'report.json'),
        }

    def persist(self):
        self.report['elapsed_seconds'] = round(time.monotonic() - self.started, 3)
        save_json(self.attempt / 'report.json', self.report)
        save_json(self.state / 'latest.json', self.report)

    def cancel(self, _signum, _frame):
        self.cancelled = True
        if self.child is not None and self.child.poll() is None:
            self.child.terminate()

    def available(self, check_binary=True):
        for path in [self.state, self.cache]:
            if shutil.disk_usage(path).free < 1024**3:
                raise CheckError(f'free disk space below 1 GiB: {path}')
        if self.cancelled:
            raise CheckError('interrupted; rerun the same command to reuse saved caches')
        if self.deadline and time.monotonic() >= self.deadline:
            raise CheckError('total time limit reached; rerun to reuse saved caches')
        if check_binary and file_digest(Path(self.checker[0])) != self.report['checker_sha256']:
            raise CheckError('checker executable changed during the run')

    def invoke(self, entry, arguments, label):
        self.available()
        command = [*self.checker, str(entry), *arguments]
        if self.deadline:
            command.extend(['--time-limit-seconds', str(max(1, math.ceil(self.deadline - time.monotonic())))])
        stdout, stderr = self.attempt / f'{label}.stdout', self.attempt / f'{label}.log'
        self.report['active'] = {'label': label, 'command': command, 'log': str(stderr), 'stdout': str(stdout)}
        self.persist()
        print(f'{label}; log {stderr}', file=sys.stderr, flush=True)
        with stdout.open('wb') as out, stderr.open('wb') as err:
            self.child = subprocess.Popen(command, cwd=self.workspace.root, stdout=out, stderr=err)
            stopping = None
            stopping_error = None
            last_message = time.monotonic()
            while self.child.poll() is None:
                try:
                    self.available(check_binary=False)
                except CheckError as error:
                    if stopping is None:
                        stopping_error = error
                        self.child.terminate()
                        stopping = time.monotonic()
                    elif time.monotonic() - stopping >= 10:
                        self.child.kill()
                if time.monotonic() - last_message >= 30:
                    print(f'{label}: still running; log {stderr}', file=sys.stderr, flush=True)
                    last_message = time.monotonic()
                time.sleep(.2)
            code = self.child.returncode
            self.child = None
        if stopping_error is not None:
            raise stopping_error
        self.available()
        self.report.pop('active', None)
        return code, stdout, stderr, command

    def enumerate(self, job, label):
        snapshot = self.attempt / f'{label}.source.json'
        code, output, log, _ = self.invoke(Path(job['entry']), ['--list-modules', '--save-source-snapshot', str(snapshot)], label)
        if code:
            raise CheckError(f'module enumeration failed; see {log}')
        targets = output.read_text().splitlines()
        if not targets or len(targets) != len(set(targets)):
            raise CheckError(f'empty or duplicate module list; see {output}')
        return snapshot, targets

    def prepare(self):
        all_packages = set(self.plan['packages']) == set(self.workspace.paths)
        entries = [('workspace', self.workspace.library)] if all_packages and not self.plan['module'] else [(name, self.workspace.paths[name]) for name in self.plan['packages']]
        for name, entry in entries:
            job = {'name': name, 'entry': str(entry), 'outcome': 'pending', 'attempts': []}
            self.report['jobs'].append(job)
            snapshot, targets = self.enumerate(job, f'{name}-enumerate')
            if name != 'workspace':
                targets = [target for target in targets if target == name or target.startswith(name + '.')]
            requested = self.plan['module']
            if requested:
                targets = [target for target in targets if target == requested or (not self.plan['module_only'] and target.startswith(requested + '.'))]
            if not targets:
                raise CheckError(f'no matching modules in {name}')
            job.update(snapshot=str(snapshot), snapshot_sha256=snapshot_digest(snapshot), targets=targets)
            self.persist()
        if self.workspace.inputs(self.plan['packages']) != self.report['inputs']:
            raise CheckError('sources changed while preparing checks; rerun')

    def check_job(self, job):
        targets = set(job['targets'])
        roots = sorted(target for target in targets if '.' not in target)
        initial = self.plan['module'] or (None if job['name'] == 'workspace' else job['name'])
        pending = deque([(initial, self.plan['module_only'])])
        verified, checked = set(), set()
        job['outcome'] = 'running'
        while pending:
            module, only = pending.popleft()
            wanted = targets if module is None else {target for target in targets if target == module or (not only and target.startswith(module + '.'))}
            if wanted <= verified:
                continue
            label = f'{job["name"]}-{len(job["attempts"]):04d}-{module or "all"}'
            result_path = self.attempt / f'{label}.json'
            arguments = [
                '--source-snapshot', job['snapshot'],
                '--cache-dir', str(self.cache),
                '--report-json', str(result_path), '--diagnostics', 'compact', '--no-progress',
            ]
            if module is not None:
                arguments.extend(['--module', module])
            if only:
                arguments.append('--module-only')
            if snapshot_digest(Path(job['snapshot'])) != job['snapshot_sha256']:
                raise CheckError('saved source snapshot changed; rerun')
            code, _, log, command = self.invoke(Path(job['entry']), arguments, label)
            if snapshot_digest(Path(job['snapshot'])) != job['snapshot_sha256']:
                raise CheckError('saved source snapshot changed during checking; rerun')
            result = load_json(result_path) if result_path.exists() else {}
            outcome = result.get('outcome', 'missing-report')
            save_failures = result.get('storage', {}).get('save_failures', 0)
            job['attempts'].append({'module': module, 'module_only': only, 'outcome': outcome, 'exit_code': code, 'log': str(log), 'report': str(result_path), 'command': command})
            if save_failures:
                raise CheckError(f'{module}: {save_failures} cache-save failures; see {log}')
            if code == 0 and outcome == 'accepted':
                coverage = module_names(result, 'verified_modules')
                if not wanted <= coverage:
                    raise CheckError(f'incomplete coverage for {module}; see {result_path}')
                verified.update(coverage & targets)
                checked.update(module_names(result, 'checked_modules') & targets)
            elif outcome == 'memory-limit' and not only and len(wanted) > 1:
                if module is None:
                    pending.extend((root, False) for root in roots)
                else:
                    children = sorted({target[len(module) + 1:].split('.')[0] for target in wanted if target != module})
                    pending.extendleft(reversed([(module, True), *[(module + '.' + child, False) for child in children]]))
            else:
                raise CheckError(f'{module}: {outcome} (exit {code}); see {log}')
            job.update(verified=sorted(verified), newly_checked=sorted(checked), reused=sorted(verified - checked))
            self.persist()
        if verified != targets:
            raise CheckError(f'incomplete target coverage for {job["name"]}')
        job['outcome'] = 'accepted'

    def run(self):
        self.attempt.mkdir()
        self.cache.mkdir(parents=True, exist_ok=True)
        handlers = {value: signal.signal(value, self.cancel) for value in [signal.SIGINT, signal.SIGTERM, signal.SIGHUP]}
        current_job = None
        try:
            self.persist()
            self.prepare()
            for job in self.report['jobs']:
                current_job = job
                self.check_job(job)
                current_job = None
            for job in self.report['jobs']:
                snapshot, targets = self.enumerate(job, f'{job["name"]}-validate')
                if snapshot_digest(snapshot) != job['snapshot_sha256']:
                    raise CheckError('source snapshot changed during checking; rerun')
                if not set(job['targets']) <= set(targets):
                    raise CheckError('target list changed during checking; rerun')
            if self.workspace.inputs(self.plan['packages']) != self.report['inputs']:
                raise CheckError('sources changed during checking; rerun')
            self.report['outcome'] = 'accepted'
        except (CheckError, OSError, ValueError, KeyError, TypeError) as error:
            if current_job is not None:
                current_job.update(outcome='failed', error=str(error))
            self.report.update(outcome='interrupted' if self.cancelled else 'failed', error=str(error))
        finally:
            if self.child is not None and self.child.poll() is None:
                self.child.terminate()
                try:
                    self.child.wait(timeout=10)
                except subprocess.TimeoutExpired:
                    self.child.kill()
                    self.child.wait()
            for value, handler in handlers.items():
                signal.signal(value, handler)
            self.persist()
        return self.report


def status(root):
    path = root / '.checks/latest.json'
    if not path.exists():
        raise CheckError('no recorded run yet')
    report = load_json(path)
    try:
        current = Workspace(root).inputs(report['plan']['packages']) == report['inputs']
        current = current and file_digest(Path(report['checker'][0])) == report['checker_sha256']
        current = current and file_digest(Path(__file__)) == report['script_sha256']
    except (OSError, ValueError, KeyError, CheckError):
        current = False
    report['inputs_current'] = current
    if report['outcome'] == 'accepted' and not current:
        report['outcome'] = 'stale'
    if report['outcome'] == 'running':
        try:
            with run_lock(path.parent):
                report['outcome'] = 'interrupted'
        except CheckError:
            pass
    return report


def summary(report):
    jobs = []
    for job in report.get('jobs', []):
        value = {key: job[key] for key in ['name', 'outcome', 'error'] if key in job}
        value.update({key: len(job.get(key, [])) for key in ['targets', 'verified', 'newly_checked', 'reused']})
        if job.get('attempts'):
            value['log'] = job['attempts'][-1]['log']
        jobs.append(value)
    value = {key: report[key] for key in ['outcome', 'elapsed_seconds', 'inputs_current', 'cache_dir', 'report', 'error', 'active'] if key in report}
    value.update(scope=report['plan']['scope'], packages=report['plan']['packages'], module=report['plan']['module'], jobs=jobs)
    value.update({key: sum(job[key] for job in jobs) for key in ['targets', 'verified', 'newly_checked', 'reused']})
    return value


def arguments(argv):
    parser = argparse.ArgumentParser(description='Plan and run cached library checks through an external checker CLI.')
    parser.add_argument('action', choices=['plan', 'run', 'status'])
    parser.add_argument('--scope', choices=['changed', 'affected', 'all'])
    parser.add_argument('--package', action='append', default=[], metavar='NAME')
    parser.add_argument('--since', default='HEAD')
    parser.add_argument('--module')
    parser.add_argument('--module-only', action='store_true')
    parser.add_argument('--checker', default=os.environ.get('REF_TYPE_CHECKER', str(ROOT / 'ref-type/target/release/cli')))
    parser.add_argument('--time-limit-seconds', type=int)
    parser.add_argument('--json', action='store_true')
    args = parser.parse_args(argv)
    if args.time_limit_seconds is not None and args.time_limit_seconds < 1:
        parser.error('time-limit-seconds must be positive')
    if args.module_only and not args.module:
        parser.error('--module-only requires --module')
    return args


def display(value, json_output):
    if json_output:
        print(json.dumps(value, indent=2))
        return
    plan = value.get('plan', value)
    if 'outcome' in value:
        print(f'Outcome: {value["outcome"]}')
    print(f'Scope: {plan["scope"]}; {len(plan["packages"])} packages')
    if 'jobs' not in value:
        for package in plan['packages']:
            print(package)
    for job in value.get('jobs', []):
        print(f'{job["name"]}: {job["outcome"]}; {job["newly_checked"]} checked, {job["reused"]} reused')
        if job.get('error'):
            print(job['error'])
    if value.get('error'):
        print(value['error'])
    if value.get('report'):
        print('Report: ' + value['report'])
    if value.get('active'):
        print('Log: ' + value['active']['log'])


def main(argv=None, root=ROOT):
    args = arguments(argv)
    try:
        if args.action == 'status':
            display(summary(status(root)), args.json)
            return 0
        workspace = Workspace(root)
        plan = make_plan(workspace, args)
        if args.action == 'plan':
            display(plan, args.json)
            return 0
        if not plan['packages']:
            display(summary({'outcome': 'nothing-selected', 'plan': plan}), args.json)
            return 0
        checker = resolve_checker(args.checker)
        with run_lock(root / '.checks'):
            report = Runner(workspace, plan, args, checker).run()
        display(summary(report), args.json)
        return 0 if report['outcome'] == 'accepted' else 130 if report['outcome'] == 'interrupted' else 1
    except (CheckError, OSError, ValueError, KeyError, TypeError) as error:
        if args.json:
            print(json.dumps({'outcome': 'error', 'error': str(error)}))
        else:
            print(str(error), file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
