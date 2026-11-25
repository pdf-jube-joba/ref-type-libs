# `complex_polynomial_roots`

Root boundedness, finite symmetric-product/coefficient-space homeomorphism, continuous factors for separated root clusters.

`At` abbreviates `Roots.At[n]`. Monic coefficients ascend and omit the leading one; degree zero represents the constant one and empty roots.

| Entry | Purpose |
| --- | --- |
| `MonicCoordinates.injective` | Equal-degree coefficient lists representing the same abstract polynomial agree in every coefficient |
| `MonicCoordinates.rootBound` | Root bound \(\lvert z\rvert<1+\sum_i\lvert p_i\rvert\) |
| `At[n].coefficients` / `factorization` | Agreement of symmetric-root coefficients with products of linear factors |
| `At.onto` | Finite roots for arbitrary coefficients via K13 complete factorization |
| `At.Equivalent` / `Family` / `family` | Finite symmetric products and quotient maps under root permutations |
| `At.coefficientMap` / `roots` | Root-family/coefficient maps and inverse identities via `coefficientsRoots`, `rootsCoefficients` |
| `At.Unordered.forget` / `injective` / `polynomialOf` | Embeddings into arbitrary-length K13 root families and factor-product agreement |
| `At.Naturality.coefficientNatural` / `rootsNatural` | Compatibility with root/coefficient transport under field automorphisms |
| `Roots.At.Topological` | Homeomorphism between finite symmetric products and monic coefficient spaces |
| `Roots.Separated` / `Filtering.At.Regions.Cluster` | Locally constant root counts and continuous multiplicity-preserving cluster factors |

[Source](src/root.ref) · [Dependencies](ref.toml) · [Checking](../../USAGE.md) · [Notes](../../../math/package-notes/algebra/complex_polynomial_roots.md)
