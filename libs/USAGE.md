# Building and checking the libraries

Run commands from the `ref-type-libs` root: libraries are in `libs/`, and the compiler and check driver are in the `ref-type/` Git submodule.
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

For per-scope reports, use the driver on Linux with Python 3.11+.
Pass `--binary`: its default path assumes the old combined repository layout.

```sh
python3 ref-type/scripts/check_all.py libs --binary ref-type/target/release/cli --state-dir /tmp/ref-type-libs-check --memory-mib 3072 --cache-budget-mib 12288
```

Replace `libs` with a package directory for a package run.
Each timestamped attempt stores snapshots, targets, logs, and `report.json`; `latest.json` in the state directory points to the latest report.
`--resume-report PATH` carries forward accepted scopes only after validating identical sources, binary, and targets.
Run `python3 ref-type/scripts/check_all.py --help` for splitting and resource options.

## Cache, resources, and fixed inputs

| Option | Behavior |
| --- | --- |
| `--cache-dir PATH` | Override the shared `libs/refcache/` cache |
| `--cache-budget-mib N` | Limit retained disk cache; protect in-use artifacts |
| `--memory-mib N` | Linux resident-memory paging target, not a hard limit; default 3,072 MiB, `0` leaves reclamation to the OS |
| `--time-limit-seconds N` | Limit one CLI check; the driver applies it per scope |
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
See [Morse-lemma evidence](geometry/morse_lemma/VALIDATION.md) and [Grassmannian-cell evidence](geometry/grassmannian_cells/README.md#type-checking).
