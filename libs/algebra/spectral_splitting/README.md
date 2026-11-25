# Continuous spectral splitting

K06 public entry: `spectral_splitting.Spectral`.
Completed units: [roadmap](../../../_plans/math/_roadmap.md).
Reuses [root clusters](../complex_polynomial_roots/README.md), [polynomial linear algebra](../polynomial_linear_algebra/README.md), [Hermitian local frames](../hermitian_frames/README.md), [bundle complements](../../geometry/bundle_complements/README.md).

## Projection construction

Split characteristic polynomials into root factors \(p\) inside and \(q\) outside the unit circle.
No common roots gives \(up+vq=1\); Cayley–Hamilton yields decomposition by \(P=v(T)q(T)\), \(R=u(T)p(T)\).
Projections are independent of Bézout choices.
Inverting \(M=p(T)+q(T)\) on the decomposition gives the same projection \(P=q(T)M^{-1}\).
Use this inverse-matrix expression for continuity.
Compare order-independent factors with K05 continuous local factors, connecting Horner evaluation and inverse continuity.

| Public entry | Contents |
| --- | --- |
| `Spectral.Action.With` | Bézout/complement projections, kernel computations, independence |
| `Spectral.At.Characteristic` | Finite coefficients, leading coefficient one, continuous families |
| `Spectral.Circle.At` | Root-order-independent inside/outside factors and coprimality |
| `Spectral.At.Splitting.Separated` | Unit-circle-avoiding matrix projections, idempotence, kernel inclusions |

`Spectral.At.Eigenvalues` equates this condition with vanishing of unit-circle eigenvectors.
`Spectral.InFrame` and `FiniteSpace.On` transport projections through finite frames, choosing unique frame-independent maps.

## Continuous families and bundles

| Public entry | Contents |
| --- | --- |
| `At.Continuous` / `Bundle` | Continuous projections, inside/complement image bundles, inclusions/projections, direct sums |
| `Comparison` / `FiniteSpace.On.Naturality` | Intertwiner/projection compatibility |
| `Idempotents.Image` | Image bundles of continuous idempotents without self-adjointness |
| `Idempotents.Comparison` / `Gap` | Nearby-idempotent image isomorphisms, open invertibility loci |
| `Idempotents.Homotopy` / `At.Homotopy` | Endpoint image-bundle isomorphisms for homotopies over compact bases |
| `BundleCoordinates` | Local bundle-map matrices and coefficient continuity |
| `BundleImage` / `Pullback` | Idempotent-image local trivializations and pullback comparisons |
| `BundleEndomorphism` / `Naturality` / `Pullback` | Spectral projection gluing, image subbundles, naturality |
| `BundleHomotopy` | Spectral-image endpoint comparisons for general bundles over compact Hausdorff bases |

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
Used in [B09](../../geometry/bundle_extension/README.md) real/complex neighborhood extensions; validation records for additions are in that README.

## Validation and resuming

K06 constructions, proofs, naturality, comparisons, and examples are complete.
K06 integration math sources: `1b012836`; final workspace validation used mathematical inputs identical to `cdc57da7`.
Branch: `math/k06-spectral-splitting`; integration status: [PR #42](https://github.com/pdf-jube-joba/ref-type/pull/42).
No Rust changes.

| Check (all shared cache) | Modules | Exit code |
| --- | ---: | ---: |
| `target/debug/cli libs/algebra/spectral_splitting --memory-mib 8192 --cache-stats` | 4,765（328 checked、4,437 reused） | 0 |
| `target/debug/cli libs/geometry/bundle_complements --memory-mib 8192 --cache-stats` | 4,345 reused | 0 |
| `target/debug/cli libs --memory-mib 8192 --cache-stats` | 7,441 reused | 0 |

Fix sources using per-input `--parse-only --save-source-snapshot` and specify `--source-snapshot`, `--diagnostics compact`, `--report-json` at the same input location.
Do not track generated snapshots, JSON, or logs.
K06/full-dependency check: 4,196 steps, peak RSS 5,259,356 KiB.
Confirmed process termination/exit 0; one worker; zero recoveries, duplicates, reruns, lost steps, or cache save failures.
Includes shared B03 basis constructions, all dependencies, and downstream tangent/normal uses.

Next: inspect PR #42 diff/CI/integration and main inclusion, then read B04 plans and this API on latest main.
B04, K01, and K04 implementations were outside K06 scope.
