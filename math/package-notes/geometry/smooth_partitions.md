# `smooth_partitions` notes

[Package API](../../../libs/geometry/smooth_partitions/README.md) · [Checking](../../../libs/USAGE.md)

## Construction

Construct flat functions, Euclidean compact cutoffs, and smooth partitions on second-countable Hausdorff manifolds over Dedekind reals.

### Analytic constructions

`Exponential.Global.value` is globally positive exponential with \(E(0)=1\), \(E'=E\).
Extend existing smooth local ODE solutions by doubling intervals; quotient derivatives/mean values prove agreement.
Also prove addition and \(t\le E(t)\) for \(t>0\).
`Global.Smooth.family` means all partial orders equal the same exponential.

`Exponential.Flat.Polynomial.Smooth.value` equals \(E(-1/t)\) for \(t>0\), zero for \(t\le0\).
Derivatives retain form \(P(1/t)E(-1/t)\).
`Polynomial.rapid` proves zero-extended positive-side \(P(1/t)E(-c/t)\) tends to zero for arbitrary polynomial expressions and positive \(c\).
Splitting exponential coefficients in half for products proves boundary convergence of all derivatives.
`Smooth.family` and `allDerivativesZero` expose all-order derivative specifications and nonpositive vanishing.

`Exponential.Step.value` is a smooth step, zero at \(t\le0\), one at \(t\ge1\), valued in \([0,1]\).
`Plateau.value` is one on \([-1,1]\), zero outside \((-2,2)\).

### Euclidean spaces

`CompactCutoff.Data` stores functions, open neighborhoods of \(K\), value-one proofs, support containment/compactness, range bounds.
Smoothness uses existing `calculus.Open.Smooth` all-partial specifications.
Includes dimension zero; empty coordinate products equal one.

### Manifolds

Entry: `Manifold[n].On[M]`.
`IsSmooth f` states actual coordinate functions smooth in every maximal-atlas chart.
`Continuity.continuous` and `Locality.smooth` give continuity/local criteria.

`Partitions[family].existsPartition` returns `Scalars.Using.SmoothPartition` for arbitrary open covers.
Includes smooth nonnegative terms bounded by one, compact subordinate supports, local finiteness, total sum one.
`region` in `Refinement[family, partition]` is each positive locus; `open`, `covers`, `within`, `locallyFinite` give locally finite open refinements.
`target` assigns each nonempty refinement inclusion into an original cover member.
Empty indexed sets are permitted.

Choose compact chart bumps equal to one at every point; second countability gives countable subcovers.
For chosen bumps \(b_i\), set
\[
r_0=1,\qquad r_{i+1}=r_i(1-b_i),\qquad \phi_i=b_i r_i
\]
Near each point one \(b_i\) equals one, so all later \(\phi_j\) supports avoid that neighborhood.
Finite-partial-sum/remainder identities prove total sum one.

`existsFinitePartition` returns finite versions for compact manifolds.
Exposes `FinitePartition.size` and functions/assignments/sum specifications below that count.
`Scalars.Using.Sequence.FiniteCover` extracts finite initial segments of countable covers by compactness.

`OnOpen[U, open].IsSmooth` handles scalar functions on opens.
Its `ZeroExtension.smooth` and `ZeroExtension.Closed.smooth` give support-conditional zero extensions.
`LocallyFinite.Sum.smooth` constructs locally finite manifold sums by local agreement with finite partial sums.

### Extension by zero of sections

`Sections[F, zero]` takes fiber sets/zeros and finite local coordinates `Frame`.
Frames have open domains, coordinates/inverses, both inverse laws, and zero preservation.
`Over[atlas].IsSmooth` sections have smooth coordinate components on every frame domain.
Applies to bundles with zero-preserving local coordinates, including linear trivializations.

`Over.Open[U, open].ZeroExtension` zero-extends inside dependent fibers; `inside` and `outside` compute values.
Supports are closures of nonzero-vector loci.
`smooth` proves smoothness when support lies in \(U\); `Closed.smooth` when vanishing off closed \(F\subset U\).
Uses frame zero preservation and local gluing via `GluingOn.smooth`.

## Examples

Examples: [real line](../../../libs/geometry/smooth_partitions/src/Examples/Line.ref) and [zero-dimensional compact manifolds](../../../libs/geometry/smooth_partitions/src/Examples/Point.ref).

## Historical validation

Standard checks at implementation commit `51799530317db36f73adc63a2d9b2aa743378414` passed all 1,883 target/dependency modules and all 10,233 repository modules.
Full check: 9,538 newly checked, 695 reused, 0 save failures or corrupt reads; source agreement confirmed.
Final `periodic_k_theory` recovered one worker under a 10 GiB virtual-memory limit, resumed from a checkpoint, and passed.
