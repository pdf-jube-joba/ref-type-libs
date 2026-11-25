# Bundle homotopy invariance and clutching (B04)

Reuses [B03 metrics/embeddings/images](../bundle_complements/README.md), [K06 nearby-projection comparisons](../../algebra/spectral_splitting/README.md) and interval local-to-global principles, [B02 operations](../bundle_operations/README.md).
Shared real/complex constructions are in `Homotopy.Over`.

## Public API

Entry: `bundle_homotopy.Homotopy[].Over`.

| API | Constructions and proofs |
| --- | --- |
| `Cylinder.endpointIsomorphismExists` | Compare bundle endpoints over compact-Hausdorff/interval products |
| `For.Pullbacks.Along` / `Relative` | Compare homotopic pullbacks, prove identity on fixed subsets |
| `For.Extensions` / `To` | Relative automorphism/isomorphism extension along cofibrations |
| `For.Contractible` / `Disks.Triviality` | Trivialize arbitrary bundles over contractible compact spaces/closed disks |
| `Clutching.With` / `Pullback` | Construct two-open-set transition bundles and pullback comparisons |
| `Clutching.Homotopy` / `With.Sum` / `With.Stabilize` | Send transition homotopies, block sums, stabilization to isomorphisms |
| `Disks.Hemispheres.Cover` | Actual two-disk-pushout/sphere homeomorphisms, closed-hemisphere gluing |
| `Disks.Clutched` / `Homotopy` | Boundary GL clutching and disk-restriction trivializations |
| `Disks.Clutched.Comparison.diskGaugeCriterion` | Equivalence of compatible boundary gauges on both disks and bundle isomorphisms |
| `Homotopy.Examples.Mobius` / `CircleLine` | Real sign-transition and complex unit-circle-transition lines |

[Real-line examples](src/Homotopy/Examples/Mobius.ref) construct circle bundles from signs on two-point boundaries.
[Complex-line examples](src/Homotopy/Examples/CircleLine.ref) construct 2-sphere bundles from complex unit-circle coordinates.
Expose actual `Fiber` and `bundle` respectively.

`alignedIsomorphismExists` in `Clutching.With.Pullback` and `With.Sum` groups comparison isomorphisms and local-frame compatibility `alignment`.
Compatibility: \(h_-g=g' h_+\).
The same real API requires explicit gauges on both disks for isomorphism criteria.

## Checks and integration records

Branch: `math/b04-bundle-homotopy`; [PR #43](https://github.com/pdf-jube-joba/ref-type/pull/43).
Last implementation change: `2f786058`; package baseline: `ca2a13df`; workspace baseline: `ad9d9af9` (documentation-only differences).
Latest-snapshot `work/b04-package-current`: 4,728 target/dependency modules, saved successfully, exit 0.
53,943 source steps, peak RSS roughly 4,415 MiB, one worker; zero recoveries/duplicates/reruns/lost steps/save failures.
Includes real/complex examples, sums/stabilization, disk trivialization, gauge criteria, local-frame comparison compatibility.

- `cargo test --workspace --locked`: 383 passed, exit 0.
- `cargo test -p cli --locked --offline`: 8 passed after time-limit-condition lint fixes, exit 0.
- `cargo clippy --workspace --all-targets --locked --offline -- -D warnings`: exit 0.
- `python3 tests/tests.py --command /workspace/ref-type/target/debug/cli`: 401 passed, exit 0.
- `rustfmt --edition 2024 --check` on 10 changed Rust files and standard build: exit 0.

Checker changes bounded scratch-cache records, improved batched substitution of consecutive lambda applications and transparent-definition comparison.
Ran 78 kernel tests including rejection of invalid captured-argument types/counts.
Earlier allocation/time failures resolved; interrupted checks remain distinguished as exit 130/incomplete.
Temporarily `exec-server transport disconnected`; access to the same workspace recovered and saving exit 0 was confirmed.
Disconnection root cause unknown.

Initial full 7,557-module `work/b04-workspace` processed every module but hit 3600 seconds during final save: exit 2, time-limit, incomplete.
Same-snapshot/cache `work/b04-workspace-retry` reused all 7,557 modules and passed in roughly 26 seconds, saved successfully, exit 0.
Recheck: zero source steps, recoveries, duplicates, reruns, lost steps, save failures.
No implementation/check work remains.
See PR #43 integration status; if unmerged on resume, confirm final CI/source agreement, merge normally, and confirm main inclusion.
Recheck from the repository root:

```sh
target/debug/cli libs --parse-only --save-source-snapshot work/b04-workspace-snapshot.json
target/debug/cli libs --source-snapshot work/b04-workspace-snapshot.json --memory-mib 10240 --cache-budget-mib 12288 --time-limit-seconds 7200 --diagnostics compact --report-json work/b04-workspace-retry.json --cache-stats
```
