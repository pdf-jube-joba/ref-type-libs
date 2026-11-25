# A09 Sobolev estimates on Euclidean spaces

<a id="status"></a>

## Status

Read-only inspection of main `dce3d353e75972c507928253d6c33420f6f55a0f` on 2026-11-19.
`euclidean_sobolev` is registered in the workspace and has a [README](../../libs/analysis/euclidean_sobolev/README.md) and 31 `.ref` files.
The following implementations were inspected in addition to the README; completion of the entire plan remains unconfirmed.

| Scope | Implementation and outstanding verification |
| --- | --- |
| Fourier model and duality | [Signed](../../libs/analysis/euclidean_sobolev/src/Euclidean/Signed.ref) and `Order` contain integer-order models; [Order.Duality](../../libs/analysis/euclidean_sobolev/src/Euclidean/Order/Duality.ref) provides pairings, estimates, and unique representation of bounded functionals. |
| Weak-derivative comparison | [Weak.ofSchwartz](../../libs/analysis/euclidean_sobolev/src/Euclidean/Weak.ref) maps real Schwartz functions to weak-derivative spaces; [Energy.comparison](../../libs/analysis/euclidean_sobolev/src/Euclidean/Energy.ref) compares norms on complex Schwartz functions. `Order.Density.sequenceExists` gives approximating sequences, but fulfillment of the general two-way \(H^k\)–\(W^{k,2}\) comparison remains unconfirmed. |
| Multiplication and coordinate changes | [Transport](../../libs/analysis/euclidean_sobolev/src/Euclidean/Transport.ref) provides pullback with compactly supported coefficients and extension by zero in positive and negative orders. [MultiplicationBy](../../libs/analysis/euclidean_sobolev/src/Euclidean/MultiplicationBy.ref) takes real smooth compactly supported functions. Its correspondence with the coefficient class required for multiplication by smooth functions remains to be verified. |
| Embedding and smoothness | [EmbeddingTheorem.theorem](../../libs/analysis/euclidean_sobolev/src/Euclidean/EmbeddingTheorem.ref) constructs \(C^r\) representatives of \(H^{r+p}\) when \(2p>n\); [Regularity.smooth](../../libs/analysis/euclidean_sobolev/src/Euclidean/Regularity.ref) gives a common smooth representative for elements belonging to all nonnegative orders. |
| Examples | No standalone Examples module has been confirmed. |

No record confirming successful type checking of the current sources and dependency closure has been found.
The scope of inspected records is documented in the [roadmap check status](_roadmap.md#progress-and-checks).

## Requirements

- Primary implementation: `euclidean_sobolev`.
- Construct integer-order \(H^s\) using weighted Fourier norms; compare nonnegative orders with weak-derivative \(W^{k,2}\).
- Prove negative-order duality, multiplication by smooth functions, and boundedness of coordinate changes preserving compact support.
- Expose Sobolev embedding and smoothness from Sobolev regularity in all orders.

## Dependencies

- [A07 Plancherel and Fourier multipliers](../../libs/analysis/fourier_l2/README.md)
- [A08 Distributions and weak derivatives](../../libs/analysis/distributions/README.md)
- [A04 Change of variables in multiple integrals](../../libs/analysis/change_of_variables/README.md)
