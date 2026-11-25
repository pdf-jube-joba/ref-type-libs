# `bundle_extension` notes

[Package API](../../../libs/geometry/bundle_extension/README.md) · [Checking](../../../libs/USAGE.md)

## Construction

Extend real/complex functions, bundles, maps, and isomorphisms from closed \(A\) in compact Hausdorff \(X\).
Extend bundles to open neighborhoods of \(A\), constructing restriction comparisons.
No assumptions exclude empty subspaces, dimension zero, or componentwise varying ranks.

### Conventions

Entry: `bundle_extension.Extension`.
`Real`, `Complex` take base set `A`, topology `source`, closed subset `subset`.

`RealMaps`, `ComplexMaps` take common topology `baseSpace` and agreement with bundle topologies via `sourceSame`, `same`.
Usually set `baseSpace := source.baseSpace`, `sourceSame := \refl(source.baseSpace)`.
Bundle-extension `Witness` stores finite projections/matrix extensions; `With` exposes `domain`, `open`, `contains`, `Fiber`, `extended`, `restricted`, `comparison`.
Isomorphism-extension `Result` stores open neighborhoods, isomorphisms with continuous inverses, and agreement with supplied closed-subspace isomorphisms.

### Construction

Real Tietze uses normality/Urysohn functions and continuous limits of uniform geometric-error approximations.
Apply separately to real/imaginary parts for complex functions.
Select each component extension; group continuity/restriction laws for families/rectangles.

Bundles use [B03 finite embeddings and projections](../../../libs/geometry/bundle_complements/README.md).
For idempotent \(P\), \(2(I-P)\) has spectrum zero/two; [K06 spectral projections](../../../libs/algebra/spectral_splitting/README.md) recover \(P\).
After matrix extension, restrict to the open unit-circle-avoiding locus to obtain image bundles.
For real bundles, complexify matrices and return conjugation-preserving spectral projections to real coordinates.
`RealLinear` proves complexification/restriction/products/projection-recovery compatibility.

Bundle maps use finite embeddings and retractions of both bundles.
Encode closed-subspace maps as rectangular matrices, extend entries, project back to bundles.
For isomorphisms, extend both maps and restrict to common open neighborhoods where both composites invert.
`Over.Endomorphisms` extends endomorphisms by identity on trivial complements, constructing inverses from nonzero determinant loci and continuous matrix inverses.

### Extension comparison and relative triples

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
`Examples.ComplexLine` applies the same construction to [B04 unit-circle-transition complex lines](../../../libs/geometry/bundle_homotopy/README.md) on closed faces in \(S^2\times[0,1]\).
`Examples.EmptyRealBundle`, `EmptyComplexBundle` instantiate extensions from empty closed subspaces.
Also checks real/complex identity matrices in dimensions zero/one.

## Historical validation

Historical upstream [PR #49](https://github.com/pdf-jube-joba/ref-type/pull/49): implementation `fb8cc1a36a3f343e4e88fbd44ae75790e5c8567f`, fixed-input baseline `c5632cf7bf185d6c0d47ea290e7e8973c32c1c04`.

| Check | Accepted modules |
| --- | ---: |
| Package and dependency closure | 5,580 |
| Workspace | 8,287 |

Both exited 0 with zero save failures, recoveries, duplicate/rerun checks, or lost steps.
Original reports: `work/b09-resume/{package,workspace}-final.*`.
