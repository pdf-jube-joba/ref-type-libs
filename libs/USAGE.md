# Building and checking the libraries

Run commands from the `ref-type-libs` root: libraries are in `libs/`, and the compiler is in the `ref-type/` Git submodule.
Use [scripts/check.py](../scripts/check.py) to automate selection, cached checks and reports through the compiler's public CLI.
The submodule tracks `pdf-jube-joba/ref-type` at a pinned revision.
See the [library index](README.md) for APIs, [ref.toml](ref.toml) for workspace packages, and [roadmap](../math/_roadmap.md) for requirements and gaps.

## Build the checker

Initialize the compiler submodule and build its CLI:

```sh
git submodule update --init --recursive
cargo build --manifest-path ref-type/Cargo.toml -p cli --release --locked
```

Use a Rust toolchain supporting the compiler's Rust 2024 edition and locked dependencies.
Binary paths assume Cargo's default `ref-type/target/`; adjust them for `CARGO_TARGET_DIR`.
For debug builds, omit `--release` and use `ref-type/target/debug/cli`, or run through Cargo:

```sh
cargo run --manifest-path ref-type/Cargo.toml -p cli --release -- libs/std --module std.Data.Nat
```

Run from this repository root so `libs/` selects these libraries rather than the copy inside `ref-type/`.

## Check a package or module

```sh
ref-type/target/release/cli libs/geometry/morse_lemma --full-check-local --diagnostics compact --cache-stats --report-json /tmp/morse-lemma-check.json
ref-type/target/release/cli libs/std --module std.Data.Nat --diagnostics compact
ref-type/target/release/cli libs --list-modules
```

| Option | Scope |
| --- | --- |
| `--module NAME` | Selected module, children, and referenced declarations |
| `--module-only` | Exclude unrelated children of the selected module |
| `--full-check-local` | Recheck input package/workspace members; allow matching external-dependency caches |
| `--full-check` | Recheck all loaded sources and save results |
| `--no-cache` | Check without persistent caches |
| `--parse-only` | Syntax and module loading only; no name-resolution or type-check guarantee |

## Check the workspace

```sh
ref-type/target/release/cli libs --diagnostics compact --cache-stats --report-json /tmp/ref-type-libs-check.json
```

## Automated checks

Use Python 3.11+ and Git on Linux.
The script defaults to `ref-type/target/release/cli`; use `--checker PATH` or `REF_TYPE_CHECKER` for a different executable.

```sh
python3 scripts/check.py plan --json
python3 scripts/check.py run --module std.Logic.Proposition --time-limit-seconds 120
python3 scripts/check.py run
python3 scripts/check.py run --scope all
python3 scripts/check.py status --json
```

| Option | Selection or behavior |
| --- | --- |
| Default | Packages with changed `.ref` or `ref.toml` files, plus transitive consumers |
| `--scope changed` | Changed packages only |
| `--scope all` | All registered workspace packages |
| `--package NAME` | Explicit seed package by its manifest name; repeat for several packages |
| `--since REV` | Include committed changes since the revision, working-tree changes and untracked sources |
| `--module NAME` | One module and its children; implies `--scope changed` |
| `--module-only` | Selected module's own declarations and references |
| `--time-limit-seconds N` | Total budget for preparation, checking and validation |
| `--json` | Machine-readable plans and compact result summaries |

Changes are relative to `HEAD` by default and include staged, unstaged, deleted and untracked sources.
Changes to `libs/ref.toml` select all registered packages; documentation changes select no checks.
`nothing-selected` means that no verification ran.
Dependency paths determine impact and execution order; register new packages in `libs/ref.toml`.

Checks share the fixed `libs/refcache/` directory and use the checker's defaults for memory paging, cache budgets and checkpoint intervals.
Cache validity and reuse are the checker's responsibility; the script supplies the shared directory and reports the checker's results.
Rerun the same command after edits or interruptions to reuse valid artifacts and checkpoints.
Runs execute sequentially under a lock and stop at the first failure.
Whole-workspace checks start as one checker invocation; memory-limit results split packages and modules while retaining their own declarations and children.
Execution stops when less than 1 GiB remains on the cache or report filesystem.

Each attempt stores opaque CLI source snapshots, commands, raw reports and logs in `.checks/`; `latest.json` contains the latest run.
Success requires an accepted CLI report, successful exit, complete target coverage and zero cache-save failures.
Final validation compares live snapshots, source inventory and executable identity with the inputs used for checking.
`status --json` reports counts, errors and log locations; earlier accepted results become `stale` when relevant inputs, the executable or the orchestration script change.

The [script tests](../scripts/test_check.py) exercise command results and reports using an external CLI fixture:

```sh
python3 -B -m unittest discover -s scripts -p 'test_*.py' -v
```

## Cache, resources, and fixed inputs

The following options apply to direct checker CLI commands.

| Option | Behavior |
| --- | --- |
| `--cache-dir PATH` | Override the shared `libs/refcache/` cache |
| `--cache-budget-mib N` | Limit retained disk cache; protect in-use artifacts |
| `--memory-mib N` | Linux resident-memory paging target, not a hard limit; default 3,072 MiB, `0` leaves reclamation to the OS |
| `--time-limit-seconds N` | Limit one CLI invocation; automation applies a total run budget |
| `--checkpoint-seconds N` | Set checkpoint intervals |
| `--cache-stats` / `--no-progress` | Report cache reuse / suppress progress output |

To check fixed inputs:

```sh
ref-type/target/release/cli libs/std --parse-only --save-source-snapshot /tmp/std.source.json
ref-type/target/release/cli libs/std --source-snapshot /tmp/std.source.json --report-json /tmp/std.report.json
```

Save and load with the same input entry; regenerate snapshots after source changes.

## Validation records

Record the library revision/snapshot, compiler revision and binary identity, targets, dependency coverage, outcome, and report location.
Distinguish newly checked modules from reused results and partial runs from complete checks; snapshots, parsing, and cache presence alone do not prove acceptance.

Historical summaries refer to the original combined `ref-type` repository.
Their commits, PRs, counts, and `work/...` or `/workspace/...` paths describe those runs, not acceptance of this checkout; some artifacts are unavailable here.
Machine-readable records retain their original commands and hashes.
See [Morse-lemma evidence](../math/package-notes/geometry/morse_lemma.md#historical-validation) and [Grassmannian-cell evidence](../math/package-notes/geometry/grassmannian_cells.md#historical-validation).
