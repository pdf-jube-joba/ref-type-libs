# A10 Rellich compactness

## Requirements

- Primary implementation: [`sobolev_compactness`](../libs/analysis/sobolev_compactness/README.md).
- Prove relative compactness in lower-order Sobolev spaces for Sobolev-bounded families with common compact support.
- Expose frequency cutoff and translation estimates and compactness of operators with smooth kernels.
- Prove compatibility with direct sums, restrictions, and cutoffs for gluing over finitely many coordinate neighborhoods.

## Dependencies

- [A09 Sobolev estimates on Euclidean spaces](a09-euclidean-sobolev.md)

## Status

The Fourier model has a uniform high-frequency tail estimate for nonnegative integer orders, with compact retained frequency regions for a positive order gap. For a bounded family in \(L^2\) with common compact support, the real and imaginary parts of the Fourier integrals restricted to any compact frequency region are relatively compact in the uniform topology.

The identification with the normalized weighted \(L^2\) blocks and the passage to relative compactness in the lower-order Sobolev norm remain open. General smooth-kernel operators and compatibility with direct sums, restrictions, and cutoffs also remain open.
