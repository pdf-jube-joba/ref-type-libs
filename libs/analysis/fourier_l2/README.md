# `fourier_l2`

Parseval, unitary L² Fourier transform, bounded multipliers, weighted norms and integer-derivative comparisons.

The unitary Fourier transform divides the unnormalized transform by (sqrt(2pi))^n. Inner products are linear in the second argument; dimension zero is included.

| Entry | Purpose |
| --- | --- |
| `Euclidean[n].Embedding` | Linear maps from Schwartz functions to existing complex L² quotients |
| `Parseval[f, g].law` | Unnormalized Parseval: \(\langle\widehat f,\widehat g\rangle=M_n^2\langle f,g\rangle\) |
| `Schwartz.parseval` / `norm` | Normalized inner-product/norm preservation |
| `CompactEmbedding[f]` / `Density.dense` | Compact-support smooth functions are Schwartz and dense in complex L² |
| `Extension[map, preserves]` | Approximation-independent extension of dense isometries to complete spaces |
| `Unitary.forward` / `backward` | Inverse complex-linear maps on existing complex L² |
| `Unitary.operator` / `inverseOperator` | Bounded operators with bound one |
| `Unitary.norm` / `parseval` / `adjoint` | Norm/inner-product preservation, \(\mathcal F^*=\mathcal F^{-1}\) |
| `Multiplication.Symbol` / `By[symbol]` | L² multiplication by bounded measurable complex functions |
| `Multiplier[symbol].value` / `bound` | \(T_a=\mathcal F^{-1}a\mathcal F\); \(\|T_af\|_2\le C\|f\|_2\) |
| `Multiplier[symbol].adjoint` | \(T_a^*=T_{\overline a}\) |
| `Conjugation.value` / `fourier` | Quotient conjugation, \(\mathcal F\overline f=\overline{\mathcal F^{-1}f}\) |
| `Weights.Weight` / `Weighted[weight]` | Weighted Fourier spaces for \(w\ge1\) with bounded measurable reciprocals |
| `Weights.Integer[m]` / `Integer[m].ofSchwartz` | Weighted norms for \(w_m(\xi)=(1+\|\xi\|^2)^m\) |
| `Integer[m].norm` | \(\|w_m\mathcal Ff\|_2=\|(1-\Delta)^mf\|_2\) |
| `Derivatives.Comparison[m].derivative` | \(\|D^df\|_2\le\|w_m\mathcal Ff\|_2\) for all iterated partials with \(\|d\|\le2m\) |
| `Expansion.comparison` | Reverse estimates by finite sums of integer-derivative norms |
| `Examples[n]` | Checked examples for arbitrary dimensions, L² classes, Schwartz functions, and symbols |

[Source](src/root.ref) · [Dependencies](ref.toml) · [Checking](../../USAGE.md) · [Notes](../../../math/package-notes/analysis/fourier_l2.md)
