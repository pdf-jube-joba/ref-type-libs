# Complex root clusters and finite symmetric products

Public entry: `complex_polynomial_roots.Roots`.
Uses [K13](../fundamental_algebra/README.md) complete factorization, multiplicity-preserving root-list permutations, and root-to-coefficient `RootProduct`.
Degree-\(n\) monic coefficient space has the usual product topology on ascending coefficients \(\mathbf C^n\), omitting the leading \(1\).
Dimension zero represents constant polynomial \(1\) and empty root families.

## Coefficients and root families

`Roots.Vector n` is `Fin n -> Complex`.
`polynomial n p` is the existing abstract polynomial from coefficients; `product n a` is \(\prod_i(X-a_i)\).

| API | Contents |
| --- | --- |
| `MonicCoordinates.injective` | Equal-degree coefficient lists representing the same abstract polynomial agree in every coefficient. |
| `MonicCoordinates.rootBound` | Root bound \(\lvert z\rvert<1+\sum_i\lvert p_i\rvert\). |
| `At[n].coefficients` / `factorization` | Agreement of symmetric-root coefficients with products of linear factors. |
| `At.onto` | Finite roots for arbitrary coefficients via K13 complete factorization. |
| `At.Equivalent` / `Family` / `family` | Finite symmetric products and quotient maps under root permutations. |
| `At.coefficientMap` / `roots` | Root-family/coefficient maps and inverse identities via `coefficientsRoots`, `rootsCoefficients`. |
| `At.Unordered.forget` / `injective` / `polynomialOf` | Embeddings into arbitrary-length K13 root families and factor-product agreement. |
| `At.Naturality.coefficientNatural` / `rootsNatural` | Compatibility with root/coefficient transport under field automorphisms. |

`At[n]` abbreviates `Roots.At[n := n]`.
`At.topology` is the usual coefficient/ordered-root product topology; `At.symmetricTopology` is its permutation quotient topology.
`At.Topological.homeomorphism` is the finite-symmetric-product/coefficient-space homeomorphism.
`continuous`, `coefficientContinuous`, `rootsContinuous` expose continuity of each map separately.
Root bounds put preimages of sufficiently small coefficient neighborhoods inside compact root boxes.
These estimates prove `closedMap` and `quotientMap`, yielding continuity of the inverse from coefficients to root families.

## Factors in separated regions

`Separated[U := U, V := V]` takes two regions and selects roots in \(U\) with multiplicities.
`At[n].laws` proves selection locally constant within disjoint open regions \(U,V\).
More general Boolean selections are available from `Filtering[test := test]`.

```ref
\import complex_polynomial_roots.Roots[] \as R;
\import R.Separated[U := U, V := V] \as Separation;
\import R.Filtering[test := Separation.test].At[n := n].Regions[U := U, V := V] \as Regions;
\import Regions.Cluster[k := k] \as Cluster;
```

`Regions.RootLaws[k, a]` requires the central root list to lie in \(U\cup V\) with \(k\) roots in \(U\), counting multiplicities.
`Regions.contains` and `Regions.open` construct an open coefficient neighborhood `Domain k` preserving that condition.
`Regions.invariant` ensures independence from root lists representing the same coefficients.
Thus regional root counts are locally constant; splitting repeated roots preserves total multiplicity.

`Cluster.Base` is the coefficient subspace in this open region.
`Cluster.value` gives degree-\(k\) monic coefficients for the product of all \(U\)-roots; `coefficients` returns the usual `Vector k` value.
`exists`, `unique`, `onRoots` give actual root-selection constructions, order independence, and computation laws.
`Cluster.continuous` proves factor-coefficient continuity; `decomposition` proves multiplication with the remaining factor recovers the original polynomial.
For multiple separated clusters, apply to each cluster and the remaining region.
`Cluster.Families[X].pullback`, `regular`, `natural` give application to arbitrary continuous coefficient families and compatibility with base maps.

## Examples and checks

[Examples.ref](src/Roots/Examples.ref) separates \(1,-1\) by positive/negative real part, constructing continuous degree-one factors.
For repeated roots \(1,1\) in one region, constructs a degree-two factor and checks multiplicities using actual root lists.
Also includes continuity from arbitrary monic quadratics to unordered roots and the zero-dimensional homeomorphism.

```sh
cargo build -p cli --locked
target/debug/cli libs/algebra/complex_polynomial_roots --memory-mib 8192 --cache-stats
target/debug/cli libs --module complex_polynomial_roots --memory-mib 8192 --cache-stats
```

Check target constructions/proofs/examples and all dependencies using the shared cache.

Target/dependency checks passed: 27 new modules, 380 source-check steps, 1,456 dependency modules reused.
Full fixed-final-source workspace check also passed, reusing verified caches for 68 packages and 6,936 modules.
One worker; zero recoveries, duplicates, reruns, lost steps, or cache save failures. Peak RSS: target roughly 1,114 MiB, workspace roughly 1,426 MiB.
Checker and dependency proofs unchanged.
