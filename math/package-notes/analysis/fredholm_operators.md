# Fredholm operators and the index

Construction details and records for [fredholm_operators](../../../libs/analysis/fredholm_operators/README.md).
See [building and checking](../../../libs/USAGE.md) for current commands.
The API overview is maintained in the package README; recorded checks describe earlier runs.

Implement Atkinson's theorem and four integer-index laws for bounded operators on complex Hilbert spaces.
Kernels are linear kernels, images actual linear images, cokernels image quotients.
Finite dimensionality factors identity through finite complex coordinates, from which actual bases are constructed.
No additional axioms; uses existing function extensionality.

## Public API

Below `At` denotes `Space[V, space, norm].Operators[W, target, targetNorm].At[f]`; `H` denotes its `Hilbert[inner, targetInner]`.

`H.FiniteParametrix` and `H.defectIndex` are auxiliary trace-difference APIs for finite-rank errors on both sides.
`H.Compare.independent` and `H.Defect.calculate` prove parametrix independence and agreement with actual integer kernel/cokernel dimension differences.

## Minimal examples

[Examples.ref](../../../libs/analysis/fredholm_operators/src/Examples.ref) applies both Atkinson directions, actual bases/index computations, composition/sum/compact-perturbation laws, and norm-neighborhood/family theorems to identity on the zero Hilbert space.
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
