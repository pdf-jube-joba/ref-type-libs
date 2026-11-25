# Fredholm operators and the index

Implement Atkinson's theorem and four integer-index laws for bounded operators on complex Hilbert spaces.
Kernels are linear kernels, images actual linear images, cokernels image quotients.
Finite dimensionality factors identity through finite complex coordinates, from which actual bases are constructed.
No additional axioms; uses existing function extensionality.

## Public API

Below `At` denotes `Space[V, space, norm].Operators[W, target, targetNorm].At[f]`; `H` denotes its `Hilbert[inner, targetInner]`.

| API | Contents |
| --- | --- |
| `Operators.After` / `Ideal` | Compact left/right ideals, compact-difference equivalence and composition compatibility |
| `At.kernel` / `image` / `CokernelSpace` | Actual kernels/images/quotient cokernels; also `kernelClosed`, `ClosedRange` |
| `At.Parametrix` / `HasParametrix` | Candidate inverses with compact errors on both sides and their existence |
| `H.Fredholm` | Closed images and finite-dimensional kernels/cokernels |
| `H.atkinsonEquivalence` / `fredholmOfParametrix` / `atkinson` | Fredholm property from parametrices |
| `H.parametrixExists` / `FromFredholm` | Bounded parametrices with finite-rank errors from Fredholm operators |
| `At.Index.Decomposition` | Actual kernel/quotient-cokernel bases |
| `At.Index.fromDecomposition` / `independent` | Integer dimension differences from bases and basis independence |
| `H.index` / `indexFromDecomposition` | Canonical Fredholm index and computation from supplied decompositions |
| `At.Composition.Hilbert.fredholm` / `indexComposition` | Fredholm composition, \(\operatorname{ind}(gf)=\operatorname{ind}f+\operatorname{ind}g\) |
| `H.DirectSum.At.fredholm` / `indexDirectSum` | Operators on constructed Hilbert sums and direct-sum index laws |
| `H.Change.fredholm` / `H.CompactPerturbation.indexInvariant` | Fredholm/index invariance under compact perturbations |
| `H.indexLocallyConstant` | Positive operator-norm neighborhoods with constant Fredholm property/index |
| `Operators.Hilbert.Family.At.locallyConstant` | Local constancy for norm-continuous families over arbitrary topological spaces |
| `FiniteSpace` | Finite bases, unique dimension, subspaces, isomorphism transport, maps through finite spaces |
| `Sum` / `Sum.MapsTo` | Hilbert-sum inner products/norms/completeness, coordinate projections/inclusions, bounded sum maps |
| `Space.Hilbert.Trace` | Finite-rank traces, factorization independence, additivity/scaling/cyclicity |

`H.FiniteParametrix` and `H.defectIndex` are auxiliary trace-difference APIs for finite-rank errors on both sides.
`H.Compare.independent` and `H.Defect.calculate` prove parametrix independence and agreement with actual integer kernel/cokernel dimension differences.

## Minimal examples

[Examples.ref](src/Examples.ref) applies both Atkinson directions, actual bases/index computations, composition/sum/compact-perturbation laws, and norm-neighborhood/family theorems to identity on the zero Hilbert space.
Compute indices from supplied bases as follows.

```ref
\definition decomposition: Index.Decomposition := Index.Decomposition {
  kernelFrame := K.Zero[].frame (\fun (x: Identity.KernelSpace) => Z.isZero x),
  cokernelFrame := Q.Zero[].frame quotientTrivial,
};
\definition indexZero: Fredholm.index fredholm = Integers.zeroInteger :=
  Fredholm.indexFromDecomposition fredholm decomposition;
```

For general finite-dimensional decompositions, supply bases to `FiniteSpace.Frame`.
`fromDecomposition` returns \(\dim\ker f-\dim(W/\operatorname{im}f)\) as `std.Arithmetic.Int.Integer`.

## Proof structure

`FromFredholm` restricts the kernel complement bijectively onto the closed image, constructing parametrices by bounded inverse and image projection.
Both errors factor through kernel/cokernel, hence have finite rank.
Conversely, finite-rank approximation of right errors and Neumann inverses prove closed image; restricting compact errors to kernel and image complement proves finite dimensionality.
Cokernel transport is a separate `CompactQuotient` lemma on compact operators inducing quotient identities.

Index laws follow from finite-rank trace cyclicity and actual-basis formulas.
On norm neighborhoods, correct finite-rank parametrices with Neumann inverses.
Reduce compact perturbations to finite-rank approximation and neighborhood theorems.
`Limits.Near` is uniform norm difference on the unit ball; `Family.NormContinuous` requires open neighborhoods for every positive radius.
Direct-sum norms use square roots of inner products; component Cauchy sequences prove completeness.

## Checks

```sh
source /workspace/ref-type-env.sh
cargo build -p cli --release --locked
target/release/cli libs/analysis/fredholm_operators --module fredholm_operators --full-check-local --diagnostics compact --cache-stats --time-limit-seconds 300 --report-json work/a11-target.json
python3 scripts/check_all.py
```
