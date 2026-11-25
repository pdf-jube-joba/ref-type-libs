# G13 Local analysis of the Morse lemma

## Implementation

Implemented in [morse_lemma](../libs/geometry/morse_lemma/README.md).
The public theorems below construct actual linear isomorphisms, smooth two-sided inverses, and open neighborhoods without assuming their conclusions.

| Requirements | Public API |
| --- | --- |
| Nondegenerate symmetric-form decomposition and inertia | `Inertia.normalFormExists`, `Inertia.Index.negativeIndex` / `positiveIndex`; congruence invariance and index choice independence |
| Local normal forms at nondegenerate critical points | `Hadamard.localExistence`, `NormalForm.localExistence`, `NormalForm.Indices` |
| Local parameterized version | `Parametric.Function.criticalBranchExists`, `FiberHadamard.localExistence`, `Morse.localExistence` |
| Critical-point properties | `CriticalPoints.At.isolated` / `locallyConstant`, `Parametric.Function.Indices.locallyConstant` |

`Examples` contains standalone nonlinear one-variable, saddle, nonconstant critical-family, and zero-dimensional examples.
Implementation/use and type-check scope, reproduction, and limitations are documented separately in [README](../libs/geometry/morse_lemma/README.md) and [validation records](../libs/geometry/morse_lemma/VALIDATION.md).
Rechecks of all 137 target modules and verification of the dependency closure passed.
The full-library check fails with the same `euclidean_sobolev/Euclidean/Order/Weight.ref:14` as base main; distinguish this from a full pass.

## Requirements

- Primary implementation: `morse_lemma`.
- Handle inertia and nondegeneracy of real symmetric bilinear forms; prove decomposition into positive and negative squares under coordinate changes.
- Construct coordinates expressing a smooth function near a nondegenerate critical point as its critical value plus the standard quadratic form.
- Expose local parameterized forms, isolation of critical points, and local constancy of their indices.

## Dependencies

- [G02 Inverse and implicit functions and local forms of regular values](g02-inverse-implicit.md)
- [Hermitian matrices and continuous local frames](../libs/algebra/hermitian_frames/README.md)
