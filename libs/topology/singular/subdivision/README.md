# Singular subdivision and small chains

Using [singular foundations](../cohomology/README.md), construct barycentric subdivision/small-chain/open-cover comparisons.
Direct dependencies: [ref.toml](ref.toml); public modules: [root.ref](src/root.ref).
Open-cover equivalences serve [excision](../excision/README.md) and finite-model comparisons.

| Module | Constructions and proofs |
| --- | --- |
| `SimplexChains` / `Subdivision` / `Face` | Simplex affine evaluation, equal-weight subdivision/homotopies, face compatibility. |
| `Subdivision` / `Natural` / `Coefficients` | Singular subdivision/identity homotopies, continuous naturality, identity actions in arbitrary cohomology. |
| `Subdivision.Iterated` / `Homotopy` | Iterated subdivision maps/identity homotopies. |
| `Small` / `FromSubset` / `With` | Cover-contained simplex complexes, injections, member lifts, restrictions. |
| `Small.Subdivision` | Small-preserving subdivision/homotopies, full-inclusion compatibility. |
| `Small.Pullback.Over` / `Square` | Pulled-cover small maps commuting with ordinary chains. |
| `OpenCover.On.Subspace` | Subspace cover pullbacks, degreewise split small inclusions. |
| `OpenCover.On.Subspace.Degree.Lift` | Small subspace-simplex lifts, recovery after inclusion. |
| `OpenCover.On.Subspace.Relative` / `With` | Ordinary relative comparisons, long-exact compatibility, homology/arbitrary-cohomology isomorphisms. |
| `SubdivisionCells` / `Comparison` | Signed subdivision cells, affine-vertex evaluation, barycentric agreement. |
| `SubdivisionCells.Words` / `Length` / `Evaluation.Comparison` | Iterated cell-list chains, length submodules, subdivision-compatible evaluations. |
| `Small.Cover.On.Eventually` | Pulled-cover Lebesgue numbers/metric bounds make sufficiently subdivided cells small. |
| `Small.Cover.On.WordChains.Support` | Sufficient subdivision of each simplex lies in small-chain images. |
| `Small.Persistence` / `Small.Cover.Chains` | Iteration preserves small chains; every chain has sufficient subdivision counts. |
| `Small.HomotopyPersistence` / `OpenCover.On.Selection` | Iterated small homotopies, minimal subdivision choices. |
| `OpenCover.On` | Actual inclusion inverses, face-compatible recursion, strict left inverses on small chains. |
| `OpenCover.On.With.At` | Arbitrary-coefficient cohomology isomorphisms via small restriction. |
| `OpenCover.On.With.Homotopies` | Restriction/extension composites cochain-homotopic to identity. |

`SimplexChains` handles standard-simplex affine chains; `Subdivision` singular subdivision/identity homotopies.
`Small` is cover-contained simplices; `OpenCover.On` its inclusion homotopy inverse.
`OpenCover.On.Subspace.Relative` has subspace comparisons/arbitrary coefficients.

[Build and check](../../../USAGE.md) from the repository root:

```sh
cargo run --manifest-path ref-type/Cargo.toml -p cli -- libs/topology/singular/subdivision
```
