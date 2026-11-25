# Homological algebra computations and products

Import name: `homological_algebra`.
Homology of bounded finite-free integer complexes, universal coefficients, and integral Künneth.

| Module | Contents |
| --- | --- |
| `Finite.Pair.Of` | Isomorphisms from boundary images inside kernels to Smith-coordinate cokernels |
| `Finite.Compute.Run` | Two-stage Smith computations, free ranks/diagonal factors/generator and inverse-coordinate matrices |
| `Finite.Pair.Of.Result` | Cycle-quotient/cyclic-module-product round trips, generator formulas |
| `Finite.Bounded.Of.At` / `Of.Dual` | Integer-graded homology / cohomology by transpose |
| `Of.BasisChange.With` / `Mapping.At.With` | Basis changes, chain maps, agreement of computed coordinate matrices with induced maps |
| `UniversalCoefficient.CohomologyKernel.sequence` | Ext¹/cohomology/Hom short exact sequences |
| `UniversalCoefficient.Tensor.Projection.Exactness.Derived.sequence` | Tensor/coefficient-homology/Tor₁ short exact sequences |
| `Finite.Bounded.Mapping.At.With.UniversalCoefficient.On` / `TensorUniversalCoefficient.On` | Full short-exact naturality for complex/coefficient maps |
| `Kunneth.Integer.Theorem.At.sequence` | Integral Künneth short exact sequences with canonical external products and Tor projections |
| `Theorem.At.selectedSplitting` / `smithSplitting` | Chosen splittings and direct-sum Smith-coordinate presentations |
| `Theorem.Mapping.With.At.diagram` | Short-exact naturality for maps on both factors |
| `Kunneth.Integer.Assertions` | Universally quantified exactness, naturality, and splitting theorems |

\[
0\longrightarrow\bigoplus_{p+q=n}H_p(C)\otimes H_q(D)
\longrightarrow H_n(C\otimes D)
\longrightarrow\bigoplus_{p+q=n-1}\operatorname{Tor}^{\mathbb Z}_1(H_p(C),H_q(D))
\longrightarrow0.
\]

`inclusionEq`, `projectionEq` give agreement with canonical maps; `onComputedGenerators` gives actions on computed generators.
Universal-coefficient `Derived.functorAgreement` identifies endpoint maps with existing Ext/Tor maps.
See [field coefficients](../field_kunneth/README.md), [integer-graded totalization](../tensor_chains/README.md), and [examples](../concrete_complexes/README.md).
