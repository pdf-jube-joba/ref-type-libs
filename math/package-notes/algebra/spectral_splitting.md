# Continuous spectral splitting

Construction details and records for [spectral_splitting](../../../libs/algebra/spectral_splitting/README.md).
See [building and checking](../../../libs/USAGE.md) for current commands.
The API overview is maintained in the package README; recorded checks describe earlier runs.

K06 public entry: `spectral_splitting.Spectral`.
Completed units: [roadmap](../../_roadmap.md).
Reuses [root clusters](../../../libs/algebra/complex_polynomial_roots/README.md), [polynomial linear algebra](../../../libs/algebra/polynomial_linear_algebra/README.md), [Hermitian local frames](../../../libs/algebra/hermitian_frames/README.md), [bundle complements](../../../libs/geometry/bundle_complements/README.md).

## Projection construction

Split characteristic polynomials into root factors \(p\) inside and \(q\) outside the unit circle.
No common roots gives \(up+vq=1\); Cayley–Hamilton yields decomposition by \(P=v(T)q(T)\), \(R=u(T)p(T)\).
Projections are independent of Bézout choices.
Inverting \(M=p(T)+q(T)\) on the decomposition gives the same projection \(P=q(T)M^{-1}\).
Use this inverse-matrix expression for continuity.
Compare order-independent factors with K05 continuous local factors, connecting Horner evaluation and inverse continuity.

`Spectral.At.Eigenvalues` equates this condition with vanishing of unit-circle eigenvectors.
`Spectral.InFrame` and `FiniteSpace.On` transport projections through finite frames, choosing unique frame-independent maps.

## Continuous families and bundles

Nearby comparisons use \(H=QP+(I-Q)(I-P)\).
At \(Q=P\), this is identity; where invertible, \(HP=QH\) gives image isomorphisms.
On compact bases, the tube lemma gives common time neighborhoods; subdivide the interval and compose endpoint comparisons.
General image trivializations apply the matrix construction in bundle frames, lifting open-subspace charts to the base.
For general homotopies, apply B03 finite embeddings to cylinder image bundles, composing projection-family comparisons with embedded-image isomorphisms.
Matrix families use base compactness; general bundles need compact Hausdorffness for finite embeddings.

## Examples

`Examples.Empty` constructs zero-dimensional projections.
`Examples.MovingNilpotent` varies \(T_a=\begin{pmatrix}0&a\\0&0\end{pmatrix}\) over the complex plane, derives spectral conditions from \(T_a^2=0\), and constructs image bundles.
Its `Homotopy` applies to interval families and uses endpoint image comparisons.
`Examples.MixedRanksHomotopy` pulls a rank-zero/rank-one two-component bundle to a cylinder, applying general comparison to zero-endomorphism spectral images.

## Projection recovery and conjugation for B09

`Circle.At.domainOff` obtains `OffSpectrum` from points in the unit-circle-avoiding region.
`At.Neighborhood.open` proves the unit-circle-avoiding spectral locus open in matrix space.
`At.ProjectionRecovery[P, idempotent]` exposes \(2(I-P)\), unit-circle avoidance, and `recovers` recovering spectral projection \(P\).
`Conjugation.At.On[A, off, real].natural` proves real-matrix actions commuting with coordinate conjugation have conjugation-compatible spectral projections.
Used in [B09](../../../libs/geometry/bundle_extension/README.md) real/complex neighborhood extensions; see its [validation records](../geometry/bundle_extension.md#validation-and-resuming).

## Validation and resuming

Historical upstream [PR #42](https://github.com/pdf-jube-joba/ref-type/pull/42): implementation `1b012836`, workspace inputs matching `cdc57da7`.

| Check | Result |
| --- | --- |
| K06 and dependencies | 328 modules checked, 4,437 reused |
| B03 regression | 4,345 modules reused |
| Workspace | 7,441 modules reused |

All exited 0 with zero save failures, recoveries, duplicate/rerun checks, or lost steps.
B09-specific additions are covered by its [validation summary](../geometry/bundle_extension.md#validation-and-resuming).
See [checking the libraries](../../../libs/USAGE.md) for fresh runs and historical-record scope.
