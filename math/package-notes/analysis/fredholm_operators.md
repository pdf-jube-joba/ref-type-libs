# `fredholm_operators` notes

[Package API](../../../libs/analysis/fredholm_operators/README.md) · [Checking](../../../libs/USAGE.md)

## Construction

Implement Atkinson's theorem and four integer-index laws for bounded operators on complex Hilbert spaces.
Kernels are linear kernels, images actual linear images, cokernels image quotients.
Finite dimensionality factors identity through finite complex coordinates, from which actual bases are constructed.
No additional axioms; uses existing function extensionality.

### Conventions

Below `At` denotes `Space[V, space, norm].Operators[W, target, targetNorm].At[f]`; `H` denotes its `Hilbert[inner, targetInner]`.

`H.FiniteParametrix` and `H.defectIndex` are auxiliary trace-difference APIs for finite-rank errors on both sides.
`H.Compare.independent` and `H.Defect.calculate` prove parametrix independence and agreement with actual integer kernel/cokernel dimension differences.

### Proof structure

`FromFredholm` restricts the kernel complement bijectively onto the closed image, constructing parametrices by bounded inverse and image projection.
Both errors factor through kernel/cokernel, hence have finite rank.
Conversely, finite-rank approximation of right errors and Neumann inverses prove closed image; restricting compact errors to kernel and image complement proves finite dimensionality.
Cokernel transport is a separate `CompactQuotient` lemma on compact operators inducing quotient identities.

Index laws follow from finite-rank trace cyclicity and actual-basis formulas.
On norm neighborhoods, correct finite-rank parametrices with Neumann inverses.
Reduce compact perturbations to finite-rank approximation and neighborhood theorems.
`Limits.Near` is uniform norm difference on the unit ball; `Family.NormContinuous` requires open neighborhoods for every positive radius.
Direct-sum norms use square roots of inner products; component Cauchy sequences prove completeness.

## Examples

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

## Historical validation

Historical implementation: `58f20c30015fd6d343ff3f77f8dcc7ec1240afc0`.

Full A11, isolated-cache examples, and A19 regressions passed.
The original combined-repository build and workspace driver also exited 0, verifying 9,887/9,887 targets with 0 unverified targets or save failures.
