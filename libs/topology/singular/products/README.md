# Cup products in singular cohomology

`Cochains[A, source, R, ring]` handles singular cochains/products valued in commutative \(R\).
`Cup[p, q]` uses first \(p+1\)/last \(q+1\) vertices, extending values linearly from free chains.

| Module | Constructions and proofs |
| --- | --- |
| `Cup.Bilinear` | Additivity/scaling in both variables, zero products. |
| `Unit` | Constant-one cocycles, left/right units. |
| `Associativity` | Associativity from compatible three-way vertex restrictions. |
| `Pullback.Cup` / `Pullback.Unit` | Pullbacks preserve products/units. |
| `Leibniz` | \(\delta(\alpha\smile\beta)=\delta\alpha\smile\beta+(-1)^p\alpha\smile\delta\beta\)。 |
| `Cup.Closed` / `Boundaries` | Closed products; boundary times closed is boundary. |
| `Cohomology.Cup` | Bilinear cocycle-quotient products, representative formulas. |
| `Cohomology.Unit` / `Cohomology.Associativity` | Cohomology units/associativity. |
| `Cohomology.Pullback` | Coefficient-linear pullbacks preserve products/units. |

`Cohomology.Group n` and `moduleSpace n` are `singular_cohomology.Cochains.OverRing.With` cohomology/module structures.
`Cohomology.Cup[p, q].onClasses` identifies products with actual representative cup classes.
`Cohomology.DegreeTransport` handles degree-addition equality transport.

[Build and check](../../../USAGE.md) from the repository root:

```sh
ref-type/target/debug/cli libs/topology/singular/products --module singular_products.Cochains --diagnostics compact
```
