# `morse_lemma` notes

[Package API](../../../libs/geometry/morse_lemma/README.md) · [Checking](../../../libs/USAGE.md)

## Construction

Finite-dimensional symmetric bilinear forms and smooth functions over Dedekind reals.
Includes dimension zero.
Entry: `morse_lemma`; differentiation/smooth maps share `calculus`; local inverses/parameterized implicit functions share `inverse_implicit`.

### Bilinear forms and inertia

`Inertia[n].Form` is existing `linear_algebra.Commutative.Form.Bilinear`.
`Symmetric` means argument-swap invariance; `Nondegenerate` means vectors annihilating all vectors are zero.
`normalFormExists` constructs `NormalForm[h]` from arbitrary nondegenerate symmetric forms.

`sign: Fin n -> Bool` in `NormalForm` represents negative coordinates by `true`.
`change.forward` is a standard-to-original linear isomorphism; `formula` is
\[
h(Cv,Cw)=\sum_i\epsilon_i v_iw_i,\qquad \epsilon_i\in\{-1,1\}
\]
`Normalized[h, normal].formula` gives original-coordinate formulas using `change.backward`.

Existence inducts on dimension.
Polarization gives nonisotropic vectors; Euclidean normalization/complement frames select first coordinates.
Shears remove cross terms; prove residual nondegeneracy and induct.
Normalize nonzero diagonal coefficients with real square roots.

`Inertia[n].Index` counts negative/positive coordinates.
Negative-projection traces/Gram–Schmidt frames compare negative dimensions under arbitrary invertible congruences.
Inverse congruences give reverse bounds, proving both indices independent of normal forms.

### Smooth form families

For smooth symmetric \(A(x)\) with nonsingular \(A(a)\), `Normalization[d, n].On[U].At[A, a].localExistence` constructs a smooth matrix family \(C(x)\) on an open neighborhood satisfying
\[
A(x)=C(x)^T A(a)C(x),\qquad C(a)=I
\]
`localInvertibleExistence` also retains local nonsingularity of \(C(x)\).

Encode matrix spaces as finite Euclidean spaces, set \(B=A(a)\), and apply the inverse function theorem to the polynomial map
\[
F(H)=2BH+H^TBH
\]
At zero the derivative is \(H\mapsto2BH\).
Antisymmetric parts of local preimages of \(A(x)-B\) yield \(BH=H^TB\); \(C=I+H\) gives the congruence.

`IndexFamily[d, n].On[U, A, a].localExistence` uses congruence/inertia invariance to prove locally constant negative/positive indices.
Returned `Local` stores opens, inclusion, basepoint membership, classified pointwise forms, central-index equalities.

### Local normal forms of functions

`Euclidean[n].Function[U, f]` constructs gradients/Hessians of smooth scalars.
`Critical x` is vanishing of all partials, proved equivalent to zero total derivative.
`Nondegenerate x` means nonzero determinant of the actual gradient derivative.
`hessianEntriesValue` identifies its entries with chosen second partials; `hessianSymmetric` proves Schwarz symmetry.

`Hadamard[n, U, f, a].localExistence` constructs smooth symmetric \(B_{ij}(x)\) near critical points with
\[
f(x)=f(a)+\sum_{i,j}B_{ij}(x)(x_i-a_i)(x_j-a_j),\qquad B(a)=\tfrac12\operatorname{Hess}_a f
\]
The coefficients are \(\int_0^1(1-t)\operatorname{Hess}f(a+t(x-a))\,dt\) along straight homotopies.
From closed-interval continuous Riemann integrals, prove differentiation under integrals, joint continuity of all partials, then smooth coefficients.
Quadratic Taylor identities follow from fundamental calculus/product rules.

`NormalForm[n, U, f, a].localExistence` takes `Critical a` and `Nondegenerate a`.
Result `Local` stores open `domain` and zero-containing `target`, original-domain inclusion, smooth two-sided inverse `equivalence`, basepoint-to-zero equality, and
\[
f(x)=f(a)+\sum_i\epsilon_i y_i(x)^2
\]
`equivalence.forward` is Morse coordinates; `equivalence.backward` parametrizes the original neighborhood.
`Indices[local].negative` and `positive` identify normal-form negative/positive counts with original Hessian indices.
Normalize Taylor families by local congruences; invertible base derivatives of \(x\mapsto C(x)(x-a)\) construct diffeomorphisms.

`CriticalPoints[n, U, f].At[a].isolated` proves nondegenerate critical points isolated.
Neighborhood `unique` states every critical point inside equals the basepoint.
Uses local gradient inverses.
`CriticalPoints.index` and `coindex` are numerical Hessian indices; `At[a].locallyConstant` gives their local constancy.

### Parameters

`Parametric[p, n].Function[U, f]` splits \((p,q)\), using unknown-\(q\) gradients/Hessians.
`criticalBranchExists` constructs smooth critical families \(q=c(p)\) through nondegenerate points by implicit functions.
`CriticalBranch` stores graph smoothness, original-neighborhood membership, criticality, base agreement, local uniqueness.

`Morse[a].localExistence` constructs these families and parameter-preserving local coordinates.
In new coordinates,
\[
f(p,q)=f(p,c(p))+\sum_i\epsilon_i z_i(p,q)^2
\]
`FiberHadamard` constructs Taylor coefficients centered on smooth critical families; `FiberCoordinates` proves \(q-c(p)\) smooth with identity unknown derivative.
`Indices[a].locallyConstant` gives local constancy of both unknown-Hessian indices.
`Morse[a].Indices[local]` connects parameterized normal-form signs to original unknown-Hessian indices.

## Examples

Standalone examples: `Examples`.
Each computes partials/Hessians, proves nondegeneracy by explicit inverses, then applies local theorems.

For example, packages depending on `morse_lemma`, `calculus`, `std` obtain local coordinates from nonlinear-example proofs.

```ref
\module Example {
  \import std.Data[].Nat[] \as N;
  \definition dimension: N.Nat^ := N.Nat^::succ N.Nat^::zero;
  \import calculus.Real[].Multivariable[n := dimension].Open[] \as Open;
  \import morse_lemma.Examples[].Nonlinear[] \as Nonlinear;
  \import morse_lemma.NormalForm[n := dimension, U := Open.whole,
    f := Nonlinear.function, a := Nonlinear.point] \as Morse;
  \definition coordinatesExist: \exists Morse.Local :=
    Morse.localExistence Nonlinear.critical Nonlinear.nondegenerate;
}
```

## Historical validation

Historical checks from 2026-11-19, based on upstream main `6e2106dfaf0a5370e84213a1c60fccf126d359a4`, using a rebuilt Rust 1.100.0 release checker.
[The machine-readable record](../../records/g13-validation.json) preserves source/binary hashes, metrics, and raw-record locations.
These results do not establish acceptance of the current checkout.

### Targets and dependency closure

`--full-check-local` rechecked all 137 `morse_lemma` modules, including ordinary/parameterized existence, index comparisons, local constancy, and standalone examples.
The dependency closure accepted 1,926 modules: 142 newly checked and 1,784 reused.
README examples also passed as standalone packages.
Cache corruption/save failures, worker recoveries, duplicates, reruns, and missing steps were all zero.
No cold run rechecked every dependency proof without cache.

No new axioms or unproved parts were added; the implementation uses existing function/set extensionality.

### Workspace check

The workspace driver accepted 68 scopes/7,522 of 15,524 targets across 111 packages, then failed in `euclidean_sobolev` at [Euclidean/Order/Weight.ref:14](../../../libs/analysis/euclidean_sobolev/src/Euclidean/Order/Weight.ref#L14):

```text
Resolution Error: module arguments do not allow inference holes (`_` or `?`)
```

The failing `positiveNonzero _ (positive x)` module argument matched the upstream base; sources and targets were unchanged during the run.
The remaining 8,002 targets, including the failed scope, were unverified by this run.
G13 and its closure passed in the separate focused check above.

### Rust checks

The upstream workspace tests passed: 34 suites, 384 tests, zero failures or ignored tests.
`git diff --cached --check` also passed; no Rust/checker source changes were made.
