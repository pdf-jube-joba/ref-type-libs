# Finite Grassmannians

Finite-dimensional real/complex Grassmannians and universal bundles.
Public `Real[n, k].Model[].Carrier` and `Complex[n, k].Model[].Carrier` are standard \(n\)-space orthogonal projections whose images have \(k\)-element bases.
Reuse `Projection` and `OnProjection.Rank.HasRank` in `hermitian_frames` for projections/rank.
`Examples` constructs identity projections/bases in arbitrary dimensions, giving explicit dimension-zero Grassmannian and rank-one projective-space points.

Entry-induced topologies and continuous-projection image bundles give universal/orthogonal-complement bundles.
Continuous local orthonormal frames exist near every point.
`Real.Model` and `Complex.Model` store linear maps subject to projection/rank conditions.
Proved entry injectivity, Hausdorffness, compactness via continuous orthonormal-frame surjections; constructed universal/complement bundles and continuous sums.
`ProjectiveReal` and `ProjectiveComplex` specialize rank one, exposing canonical lines/complements.
`Family.map` constructs continuous Grassmannian maps from continuous constant-rank projections.
`Pullback.isomorphism` compares universal pullbacks by arbitrary continuous maps with composed-projection images.
Prove block-sum rank addition/map continuity.
`Graph` represents nearby images as graphs from reference planes to complements, proving image reconstruction.
`Model.Graph.Reconstruction.homeomorphismExists` proves homeomorphisms with local graph coordinates as forward maps; `Model.Charts.exists` gives existence at every point.
Sums with zero/identity projections construct continuous ambient/rank stabilizations.
Construct complement maps and universal-pullback/original-complement isomorphisms.
Compare universal sum pullbacks with sums of factor universal pullbacks.
Stabilization likewise compares universal pullbacks with factorwise pulled-back sums.
Existing `bundle_complements.Projection` constructs continuous projection images; `Projection.Pullback` compares pullbacks.
`hermitian_frames` provides orthogonal complements/block sums.
Original `Real.Grassmannian`, `Complex.Grassmannian` are projection-structure auxiliary models, with continuous maps both ways and Model round trips.

Right sides of `Stabilization.ambientBundleIsomorphism` and `dimensionBundleIsomorphism` sum factor universal bundles pulled back successively from sum bases to stabilization bases.
`ambientMapFormula` and `dimensionMapFormula` identify isomorphism base maps with public stabilization maps.

For current check and resume commands, see [checking the libraries](../../USAGE.md).
The original `work/b05-resume.md` handoff is not included in this repository.
