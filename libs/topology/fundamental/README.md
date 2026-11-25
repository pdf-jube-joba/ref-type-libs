# Fundamental groupoids and groups

Quotient continuous real-unit-interval paths by endpoint-fixed homotopies.
Group multiplication follows the left path first, then the right.

| Module | Contents |
| --- | --- |
| `Paths` / `Between` | Specified endpoints, constants/reversals, endpoint-fixed equivalence/quotients |
| `Paths.Concatenation` / `Homotopies` / `Classes` | Half-interval gluing, homotopy compatibility, quotient composition |
| `Paths.GroupoidLaws` | Reparametrization unit/inverse/associative homotopies |
| `Groupoid` / `Maps` | Groupoids, continuous induced maps preserving composition/units/inverses |
| `FundamentalGroup` / `Maps.Along` | Fundamental groups/induced homomorphisms as `std.Alg.Alg.Group`, `algebra.Hom.GroupMap` |
| `IntervalPaths` / `Examples` | Convex interval-path homotopies, trivial interval groups |
| `UnbasedPaths` / `Squares` | Unbased paths, subdivisions, square edges |
| `Neighborhoods` / `SimpleConnectivity` | Local/semilocal neighborhood bases, simple connectedness/trivial groups |
| `Bridges` / `Holonomy` | Base paths, holonomy/naturality from fundamental-group homomorphisms |
| `TwoOpenSets.vanKampen` | van Kampen as two-open-set amalgamated products |
| `VanKampen.Cover.Descent` | Local holonomy descent, homotopy invariance/uniqueness, fundamental-group homomorphisms |

## Descent form of van Kampen

`VanKampen[A, source, G, group].Cover[family]` handles arbitrary open covers.
`SmallPath` is paths lying in single cover members.
`LocalFunctor` stores small-path values, subdivision products, constant units, equal square-boundary products within single members.
Values are assigned to `SmallPath` itself, agreeing on overlaps.

Under open-cover conditions, `Descent.extend` extends local data to all paths.
`restricts` proves small-path agreement; `unique` uniqueness.
Extensions send concatenations to products and are endpoint-homotopy invariant.
`Descent.AtPoint.homomorphism` returns fundamental-group homomorphisms into specified groups.

Uses finite binary interval subdivisions, agreement across subdivisions, finite square subdivisions/boundary-product gluing.
## van Kampen theorem

`TwoOpenSets[A, source, U, V].vanKampen` quantifies basepoints and `Hypotheses`.
Assumes \(X=U\cup V\), open \(U,V\), path-connected \(U,V,U\cap V\), basepoint in intersection.
`Connected` expresses path connectedness by continuous paths within subsets.

Conclusion `At.Data.IsAmalgamatedProduct` states the amalgamated-product universal property for the canonical inclusion homomorphisms:
\[
\pi_1(X,b)\cong\pi_1(U,b)*_{\pi_1(U\cap V,b)}\pi_1(V,b)
\]
For arbitrary groups and two homomorphisms agreeing on intersections, there is a unique common extension.
`algebra.AmalgamatedProduct.Universal` provides universality; `Other.canonicalIsomorphism` canonical isomorphisms with any other universal group.

Choose shared intersection base paths; define small holonomy from both homomorphisms.
Prove overlap/constant/subdivision/square-boundary laws and apply local descent.
Finally prove both restrictions and uniqueness.

```sh
target/debug/cli libs/topology/fundamental --module fundamental_groups
```
