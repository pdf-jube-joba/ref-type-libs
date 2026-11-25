# `integration`

Riemann integration, Lebesgue integration via L¹ completion.

Riemann integrals require uniform convergence over all tags in dyadic partitions, including zero-length intervals. Lebesgue integrals use the quotient of L1 Cauchy representations.

| Entry | Purpose |
| --- | --- |
| [Real](src/Real.ref) | Real arithmetic, `Interval` with ordered endpoints |
| `Real.Division` | Dyadic tagged partitions, Riemann sums/laws |
| `Real.Division.Bounds` / `Mesh` / `Refinement` | Uniform estimates, mesh size, refinement errors |
| `Real.Division.Prefix` | Truncated interval lengths/sums, refinement/increment estimates |
| `Real.Riemann[interval].Def` / `Prop` | Boundedness, integral conditions/uniqueness, constants, \(L^1\) estimates |
| `Real.Riemann[interval].Uniform.Of` | Integrals/primitives of bounded uniformly continuous functions |
| `Real.Riemann[interval].Continuous.Of` | Continuous closed-interval integrability, fundamental theorem |
| `Real.Lebesgue[interval].Def` / `Prop` | \(L^1\) Cauchy quotients, integral construction, representative independence |
| `Vector[n, interval].Of` / `Comparison` | Finite-dimensional integrals/primitives, coordinate derivatives, norm estimates |

[Source](src/root.ref) · [Dependencies](ref.toml) · [Checking](../../USAGE.md) · [Notes](../../../math/package-notes/analysis/integration.md)
