# Bundle extension from closed subspaces (B09)

Extend real/complex functions, bundles, maps, and isomorphisms from closed \(A\) in compact Hausdorff \(X\).
Extend bundles to open neighborhoods of \(A\), constructing restriction comparisons.
No assumptions exclude empty subspaces, dimension zero, or componentwise varying ranks.

## Public API

Entry: `bundle_extension.Extension`.
`Real`, `Complex` take base set `A`, topology `source`, closed subset `subset`.

| API | Contents |
| --- | --- |
| `Real.tietze`, `Complex.tietze` | Extend real/complex continuous functions to all \(X\) |
| `Real.Components`, `Complex.Components` | Extend arbitrarily indexed component families |
| `Real.Matrices`, `Complex.Matrices` | Entrywise extension of finite rectangular matrices |
| `Real.Square`, `Complex.Square` | Invertible extensions to open neighborhoods, continuous inverses/restriction laws |
| `RealProjections`, `Complex.Projections` | Idempotent neighborhood extensions, image bundles/restriction comparisons |
| `RealBundleExtension`, `Complex.BundleExtension` | Neighborhood extension of arbitrary finite-rank bundles |
| `Sections`, `RealSections.extend`, `ComplexSections.extend` | Extend closed-subspace sections of \(X\)-bundles globally |
| `RealMaps.extend`, `ComplexMaps.extend` | Extend closed-subspace maps between \(X\)-bundles globally |
| `RealIsomorphisms.extend`, `ComplexIsomorphisms.extend` | Extend closed-subspace isomorphisms to open neighborhoods |
| `RealLocalIsomorphisms.extend`, `ComplexLocalIsomorphisms.extend` | Extend isomorphisms between neighborhood bundles to smaller common neighborhoods |
| `CompactNeighborhood` | Compact closed neighborhoods inside open ones; lift relatively open neighborhoods to \(X\) |

`RealMaps`, `ComplexMaps` take common topology `baseSpace` and agreement with bundle topologies via `sourceSame`, `same`.
Usually set `baseSpace := source.baseSpace`, `sourceSame := \refl(source.baseSpace)`.
Bundle-extension `Witness` stores finite projections/matrix extensions; `With` exposes `domain`, `open`, `contains`, `Fiber`, `extended`, `restricted`, `comparison`.
Isomorphism-extension `Result` stores open neighborhoods, isomorphisms with continuous inverses, and agreement with supplied closed-subspace isomorphisms.

## Construction

Real Tietze uses normality/Urysohn functions and continuous limits of uniform geometric-error approximations.
Apply separately to real/imaginary parts for complex functions.
Select each component extension; group continuity/restriction laws for families/rectangles.

Bundles use [B03 finite embeddings and projections](../bundle_complements/README.md).
For idempotent \(P\), \(2(I-P)\) has spectrum zero/two; [K06 spectral projections](../../algebra/spectral_splitting/README.md) recover \(P\).
After matrix extension, restrict to the open unit-circle-avoiding locus to obtain image bundles.
For real bundles, complexify matrices and return conjugation-preserving spectral projections to real coordinates.
`RealLinear` proves complexification/restriction/products/projection-recovery compatibility.

Bundle maps use finite embeddings and retractions of both bundles.
Encode closed-subspace maps as rectangular matrices, extend entries, project back to bundles.
For isomorphisms, extend both maps and restrict to common open neighborhoods where both composites invert.
`Over.Endomorphisms` extends endomorphisms by identity on trivial complements, constructing inverses from nonzero determinant loci and continuous matrix inverses.

## Extension comparison and relative triples

Restrict two extensions to common neighborhoods, compose closed-subspace comparisons, and pass to `RealLocalIsomorphisms` or `ComplexLocalIsomorphisms`.
`extend` constructs isomorphisms on smaller neighborhoods agreeing with specified comparisons.
Open neighborhoods need not be compact: restrict to `CompactNeighborhood` closed neighborhoods, then extend back.
This also extends relative-K triple isomorphisms \(\alpha\) in \((E,F,\alpha)\).

`Over.Isomorphisms.With.Pullback` pulls back specified extensions and compares iterated/single pullback.
`With.Stabilize[n]` sums with trivial \(n\)-bundles, agreeing with \(\alpha\oplus\mathrm{id}\) on closed subspaces.
Shrinking comparisons also use `Over.LocalIsomorphisms.With.Stabilize[n]`.
Bundle-extension `With.Pullback` pulls back original/extended restriction comparisons along continuous maps into the original closed subspace.
These transport specified extensions without requiring uniqueness of choices in existence proofs.

## Examples

`Examples.RealBundle`, `ComplexBundle` extend real/complex trivial bundles over points, instantiated in dimensions zero/one.
`Examples.Mobius` extends Möbius bundles from closed \(S^1\times\{0\}\) in \(S^1\times[0,1]\) to open neighborhoods.
`Examples.ComplexLine` applies the same construction to [B04 unit-circle-transition complex lines](../bundle_homotopy/README.md) on closed faces in \(S^2\times[0,1]\).
`Examples.EmptyRealBundle`, `EmptyComplexBundle` instantiate extensions from empty closed subspaces.
Also checks real/complex identity matrices in dimensions zero/one.

## Validation and resuming

Base: PR #48-integrated main `d6ecc14d499efbd782a70ae5c837c4da97c7abc8`.
Ancestors include K07 `76e6084094f810eaf51e18663bb33d111dd409d7`, K02 `29f3f43b7a760485ad516dec1c6835d6e09aa41e`, initial B09 `96731109fb2466c72de286aee73ab659e30743a2`.
Continuation branch: `math/b09-complete-extension`; [PR #49](https://github.com/pdf-jube-joba/ref-type/pull/49).

Last implementation change: `fb8cc1a36a3f343e4e88fbd44ae75790e5c8567f`; math-input baseline after trailing-blank cleanup: `c5632cf7bf185d6c0d47ea290e7e8973c32c1c04`.
Current math inputs match the full-check fixed snapshot.

| Check | Modules | Exit code |
| --- | ---: | ---: |
| Package and dependency closure | 5,580 | 0 |
| Full workspace | 8,287 | 0 |

Shared cache: `libs/refcache`; fixed snapshots/reports: `work/b09-resume/package-final.*`, `workspace-final.*`.
Full check completed 100,406 source steps, one worker, peak RSS 9,040,752 KiB.
Both confirmed cache saving; zero recoveries, duplicates, reruns, unsaved steps, save failures.
When interruption invalidated the full-check handle, kept the process running and recovered original-shell exit 0 and accepted reports.
No further math fixes or check restarts.
No B09 implementation/validation work remains; see PR #49 for integration.

Recheck from the repository root.

```sh
target/debug/cli libs/geometry/bundle_extension --memory-mib 10240 --cache-dir libs/refcache --cache-budget-mib 12288 --cache-stats --diagnostics compact --report-json work/b09-resume/package.json
target/debug/cli libs --memory-mib 10240 --cache-dir libs/refcache --cache-budget-mib 12288 --cache-stats --diagnostics compact --report-json work/b09-resume/workspace.json
```

CLI built with `cargo build -p cli --locked` (exit 0).
