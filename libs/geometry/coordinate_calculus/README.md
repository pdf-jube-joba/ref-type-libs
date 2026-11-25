# Coordinate calculations for manifolds and de Rham cohomology

Instantiate public libraries from another package to check analysis/exterior/manifold/cohomology connections.

| Module | Constructions and laws used |
| --- | --- |
| `Calculus` / `OpenCalculus` / `MeanValue` | Limits, open derivatives, mean value theorem, smooth composition |
| `Alternating` / `LocalForms.On.CoefficientExpression` | Arbitrary-degree alternating forms, finite coefficients, exterior-derivative coefficients |
| `Geometry` | Standard atlases, open submanifolds, point/empty manifolds, saturation, standard/empty smooth identities |
| `PlaneForms` | \(x\,dy\), \(d(x\,dy)=dx\wedge dy\), \(d^2=0\), exact classes vanish |
| `Shear.Forms` | Jacobian of \(F(u,v)=(u,v+u^2)\), \(F^*dy=dv+2u\,du\), exterior-derivative compatibility |
| `ShearCharts` | Nonidentity transitions, tangent representatives, distinct global-form coordinates |
| `ShearCharts.SmallForms` / `SmallSmooth` | Unique small-atlas extensions, form/cohomology isomorphisms, smoothness criteria |
| `ShearCharts.Representations` | Canonical form/cohomology isomorphisms for presentations generating equal maximal atlases |
| `Point` | Point \(H^0\cong\mathbb R\), positive-degree vanishing |
| `Contravariance` | Contravariant composition for forms/cohomology |
| `Pointwise` / `Cohomology` | Point/degree-dependent quotient carriers, extensionality, quotient APIs |

[Build and check](../../USAGE.md) from the repository root:

```sh
ref-type/target/debug/cli libs/geometry/coordinate_calculus --module coordinate_calculus --full-check-local --diagnostics compact
```
