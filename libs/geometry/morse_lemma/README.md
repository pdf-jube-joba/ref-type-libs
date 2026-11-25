# Morse lemma and inertia

Finite-dimensional symmetric bilinear forms and smooth functions over Dedekind reals.
Includes dimension zero.
Entry: `morse_lemma`; differentiation/smooth maps share `calculus`; local inverses/parameterized implicit functions share `inverse_implicit`.

## Bilinear forms and inertia

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

| API | Contents |
| --- | --- |
| `Index.negative` / `positive` | Negative/positive sign-coordinate counts |
| `Index.NonsingularForm` | Symmetric nondegenerate forms |
| `Index.negativeIndex` / `positiveIndex` | Numerical indices by unique choice |
| `Index.negativeIndexOfNormal` / `positiveIndexOfNormal` | Agreement with signs of arbitrary normal forms |
| `Index.negativeIndexInvariant` / `positiveIndexInvariant` | General invertible-congruence invariance |
| `Index.indexDimension` | Negative plus positive index equals dimension |
| `MatrixForm[n]` | Matrix-to-form conversion, symmetry, nondegeneracy from nonzero determinants |
| `MatrixForm.Quadratic` / `Congruence` | Double-sum representations, matrix-congruence/form connection |
| `MatrixForm.HalfCongruence` | Positive scaling by \(1/2\) preserves indices |

## Smooth form families

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

## Local normal forms of functions

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

## Parameters

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

| Example | Contents |
| --- | --- |
| [Examples.Nonlinear](src/Examples/Nonlinear.ref) | Normal form/isolation at zero for \(f(t)=(t+t^2)^2\) |
| [Examples.Saddle](src/Examples/Saddle.ref) | Nondegenerate saddle \(f(u,v)=uv\) |
| [Examples.Parametric](src/Examples/Parametric.ref) | Critical family \(q=p^2\) and normal forms for \(f(p,q)=(q-p^2)^2\) |
| [Examples.ZeroDimension](src/Examples/ZeroDimension.ref) | Zero-dimensional constants |
| [Inertia.Examples](src/Inertia/Examples.ref) | Dimension zero, negative lines, mixed-sign planes, shear pullbacks |
| [Inertia.Index.Examples](src/Inertia/Index/Examples.ref) | Numerical indices for dimension zero/negative lines/saddles |

## Checks

```sh
cargo build -p cli --release --locked
target/release/cli libs/geometry/morse_lemma --full-check-local --memory-mib 4096 --cache-stats --time-limit-seconds 1800 --report-json work/g13-target.json
python3 scripts/check_all.py libs --memory-mib 4096 --cache-budget-mib 12288 --min-free-mib 512 --time-limit-seconds 3600 --state-dir work/g13-repository-check
cargo test --workspace --locked -j 4
```

Use shared caches to check all target modules/loaded dependencies.
`--full-check-local` rechecks package proofs, reusing matching dependency caches.
2026-11-19 recheck accepted all 137 target modules and 1,926 modules including dependencies.
Full checks stopped at existing `euclidean_sobolev/Euclidean/Order/Weight.ref:14`.
Passed/failed/unreached scope: [validation records](VALIDATION.md).
