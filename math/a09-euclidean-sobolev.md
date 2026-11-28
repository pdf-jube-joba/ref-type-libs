# A09 Sobolev estimates on Euclidean spaces

## Requirements

- Primary implementation: [`euclidean_sobolev`](../libs/analysis/euclidean_sobolev/README.md).
- Construct integer-order \(H^s\) using weighted Fourier norms; compare nonnegative orders with weak-derivative \(W^{k,2}\).
- Prove negative-order duality, multiplication by smooth functions, and boundedness of coordinate changes preserving compact support.
- Expose Sobolev embedding and smoothness from Sobolev regularity in all orders.

## Dependencies

- [A07 Plancherel and Fourier multipliers](../libs/analysis/fourier_l2/README.md)
- [A08 Distributions and weak derivatives](../libs/analysis/distributions/README.md)
- [A04 Change of variables in multiple integrals](../libs/analysis/change_of_variables/README.md)

## Status

Read-only inspection of main `dce3d353e75972c507928253d6c33420f6f55a0f` on 2026-11-19.
`euclidean_sobolev` is registered in the workspace and has a [README](../libs/analysis/euclidean_sobolev/README.md) and 31 `.ref` files.
The following implementations were inspected in addition to the README; completion of the entire plan remains unconfirmed.

| Scope | Implementation and outstanding verification |
| --- | --- |
| Fourier model and duality | [Signed](../libs/analysis/euclidean_sobolev/src/Euclidean/Signed.ref) and `Order` contain integer-order models; [Order.Duality](../libs/analysis/euclidean_sobolev/src/Euclidean/Order/Duality.ref) provides pairings, estimates, and unique representation of bounded functionals. |
| Weak-derivative comparison | [Weak.ofSchwartz](../libs/analysis/euclidean_sobolev/src/Euclidean/Weak.ref) maps real Schwartz functions to weak-derivative spaces; [Energy.comparison](../libs/analysis/euclidean_sobolev/src/Euclidean/Energy.ref) compares norms on complex Schwartz functions. `Order.Density.sequenceExists` gives approximating sequences, but fulfillment of the general two-way \(H^k\)–\(W^{k,2}\) comparison remains unconfirmed. |
| Multiplication and coordinate changes | [Transport](../libs/analysis/euclidean_sobolev/src/Euclidean/Transport.ref) provides pullback with compactly supported coefficients and extension by zero in positive and negative orders. [MultiplicationBy](../libs/analysis/euclidean_sobolev/src/Euclidean/MultiplicationBy.ref) takes real smooth compactly supported functions. Its correspondence with the coefficient class required for multiplication by smooth functions remains to be verified. |
| Embedding and smoothness | [EmbeddingTheorem.theorem](../libs/analysis/euclidean_sobolev/src/Euclidean/EmbeddingTheorem.ref) constructs \(C^r\) representatives of \(H^{r+p}\) when \(2p>n\); [Regularity.smooth](../libs/analysis/euclidean_sobolev/src/Euclidean/Regularity.ref) gives a common smooth representative for elements belonging to all nonnegative orders. |
| Examples | No standalone Examples module has been confirmed. |

The November 19 inspection did not identify a successful type check of the inspected sources and dependency closure.
The scope of inspected records is documented in the [roadmap check status](_roadmap.md#progress-and-checks).

### Fourier and weak-derivative comparison

- For every nonnegative integer order, taking the real part of the physical \(L^2\) class of a Fourier element gives a unique real \(W^{k,2}\) class. The construction uses Schwartz density, the Fourier derivative estimate, and convergence against compactly supported tests. Each constructed weak derivative through order `k` has an `L^2` norm bounded by the Fourier Sobolev norm. [Implementation](../libs/analysis/euclidean_sobolev/src/Euclidean/Weak/Approximation.ref)
- At order zero, the two maps are inverse on real physical classes and preserve the Fourier and \(L^2\) norms. [Implementation](../libs/analysis/euclidean_sobolev/src/Euclidean/Weak/Zero.ref)
- The positive-order converse and the full comparison for complex weak-derivative classes remain open.

On 2026-11-28, the official CLI v0.1.2 accepted all 40 modules in this package with `python3 scripts/check.py run --package euclidean_sobolev`. The package job checked all 40 modules and the checker reused 1,586 dependency module results. The checker reported zero cache-save failures.
