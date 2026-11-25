# `inverse_implicit`

Local inverses, parameterized implicit functions, constant-rank coordinates, regular-value submanifolds and tangent kernels.

| Entry | Purpose |
| --- | --- |
| `Euclidean[n].InverseFunction[U, f, a]` | At nonzero basepoint derivative determinant, `localExistence` proves existence of `LocalInverse[U, f, a]` |
| `Euclidean.LocalInverse` | Open source/image neighborhoods, basepoint membership, smooth two-sided inverses agreeing with original maps |
| `Product[n, m].Implicit[U, f, a]` | Solutions on parameter/equation-value product neighborhoods from invertible unknown-direction derivatives |
| `Product.Implicit.Solution` | Solution/graph maps, equations, local uniqueness, neighborhood/product diffeomorphisms |
| `Rank[n, m, r]` | Proved rank factorizations `Witness` into image injections/surjections, existence `HasRank` |
| `ConstantRank[k, r, l].On[U, f, a]` | `localExistence` and `NormalForm` for everywhere-rank-\(r\) maps \(\mathbb R^{k+r}\to\mathbb R^{l+r}\) |
| `Product.Submersion[U, f, a]` | `LocalForm` making original maps right-coordinate projections from derivative surjectivity |
| `Product.LocalFiber[U, f, a, local]` | Smooth constant-fiber parametrizations and both coordinate laws |
| `Product.LocalFiber.Tangent` | Parameter/kernel encoding/decoding by coordinate derivatives/inverse derivatives |
| `Product[n, m].RegularValue[M, T].Of[f, y]` | Regular fibers for \(\dim M=n+m\), \(\dim T=m\) |
| `RegularValue.Of.manifold` / `Smooth.embedding` | Smooth subspace-topology/saturated-atlas manifolds and ambient embeddings |
| `RegularValue.Of.Smooth.At[x].identificationExists` | Tangent/kernel linear isomorphisms with inclusion derivatives as forward maps |

[Source](src/root.ref) · [Dependencies](ref.toml) · [Checking](../../USAGE.md) · [Notes](../../../math/package-notes/geometry/inverse_implicit.md)
