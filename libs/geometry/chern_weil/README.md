# `chern_weil`

Curvature and trace forms for smooth real vector bundles with connection.

| Entry | Purpose |
| --- | --- |
| `Local.On.Curvature` | The matrix-valued curvature (F = dA + A \wedge A), its adjoint covariant derivative in degree two, and the Bianchi identity |
| `Local.On.Curvature.Coordinates` | Comparison with the expansion in the Euclidean coordinate basis |
| `Global.On.Family.Of.Curvature` | Bundle curvature assembled from the local matrices and their overlap laws, with the Bianchi identity in every bundle chart |
| `Global.On.Family.Of.Curvature.TraceForm` | The global closed form `tr(F)` and its de Rham class |
| `Global.On.Family.Of.Curvature.QuadraticTrace` | The global closed form `tr(F ∧ F)`, its de Rham class, and closed evaluations of quadratic trace polynomials |
| `Global.On.Family.Of.Transgression` | The trace of the connection difference as a primitive of the difference of the degree-two trace forms, and connection independence of their classes |
| `Pullback.Between.Family.Of.Naturality` | Pullback of the trace forms and their de Rham classes along smooth maps |

The local curvature and covariant derivative use the convention (D_A F = dF + A \wedge F - F \wedge A).

[D02 requirements](../../../math/d02-chern-weil.md) · [Dependencies](ref.toml) · [Checking](../../USAGE.md)
