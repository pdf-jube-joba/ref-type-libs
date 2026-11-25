# C01 implementation and validation summary

Historical work on branch `codex/c01-cap-products`, through the 2026-10-28 integration of upstream main `e0f1db4f` in merge `1c39f1af`.
See the [package README](../libs/topology/singular/cap/README.md) for APIs and [current checking instructions](../libs/USAGE.md) for new runs.

## Implemented scope

- Integral cap products: bilinearity, units, cup–cap adjunction, Alexander–Whitney boundary formulas, relative actions, and descent in all positive/zero degree cases.
- Relative cup and Kronecker products, coefficient/pair-map naturality, and union-valued products under the open-cover condition, using subdivision comparisons.
- Relative homology external products and naturality in all nonnegative degrees, unified in `Cross.Homology.All` and `Cross.Natural.On.All`.
- Signed cap compatibility with both connecting maps on arbitrary classes, including positive/positive degrees.
- `ProjectionClasses` formulas with independent external degrees and explicit total-degree equalities; examples in `cap_models.RelativeCross` and `cap_models.Connecting`.

## Final recorded checks

After integration, the full `singular_cap` check accepted 3,017 newly checked modules and 173 reused modules, with zero cache save failures.
Regressions for `singular_cohomology`, `singular_products`, `singular_excision`, and `singular_subdivision` also exited 0.
A later fixed-snapshot `singular_cap` recheck accepted 3,685 reused modules with zero save failures.

The post-integration workspace run failed while saving `relative_k_theory.Relative.Pullback`, reporting `The serialize buffer is full`, 78 save failures, and `No space left on device`.
The preserved [report](c01-integrated-workspace-report.json) has outcome `internal-error`; see the [log](c01-integrated-workspace.log).
Full post-integration workspace success remains unconfirmed.
An earlier 8,287-module workspace pass preceded this integration and does not cover it.

For a new run, generate fresh inputs with adequate storage and retain the existing evidence.
The old `/tmp` snapshots and environment-specific storage measurements are not current resume instructions.
