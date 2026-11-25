# A11 Fredholm operators and the index

## Requirements

- Primary implementation: `fredholm_operators`.
- Prove the compact-operator ideal property and Atkinson's theorem, identifying existence of a parametrix with the Fredholm property.
- Prove finite-dimensional kernels and cokernels and index laws for composition, direct sums, compact perturbations, and local constancy in norm-continuous families.
- Expose index computation from actual kernels, images, cokernels, and finite-dimensional decompositions.

## Dependencies

- [A19 Complex Hilbert spaces and compact operators](a19-complex-hilbert.md)

## Completion status

All requirements implemented and checked.
Implementation sources: `58f20c30015fd6d343ff3f77f8dcc7ec1240afc0`.

| Requirement | Status and public API |
| --- | --- |
| Compact-operator ideal and Atkinson equivalence | Complete. `Operators.Ideal`, `At.Hilbert.atkinsonEquivalence` |
| Finite-dimensional kernels and cokernels | Complete. Uses the actual `kernel`, `image`, and quotient `CokernelSpace` |
| Composition and direct-sum index laws | Complete. `At.Composition.Hilbert.indexComposition`, `At.Hilbert.DirectSum.At.indexDirectSum` |
| Compact-perturbation invariance and local constancy in norm-continuous families | Complete. `CompactPerturbation.indexInvariant`, `indexLocallyConstant`, `Operators.Hilbert.Family.At.locallyConstant` |
| Computation from actual finite-dimensional decompositions, minimal examples, and documentation | Complete. `At.Index.Decomposition`, `indexFromDecomposition`, `Examples.indexZero`, public README |

Full A11, isolated-cache examples, and A19 regressions passed.
Standard `cargo build -p cli --release --locked && python3 scripts/check_all.py` also exited 0, verifying 9,887/9,887 targets with 0 unverified targets or save failures.
