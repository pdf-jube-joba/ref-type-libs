# `fundamental_algebra`

Complex polynomial bounds at infinity, minima, roots, complete factorization with multiplicities, unique finite root families.

APIs below are under `Complex`. Root lists retain multiplicities; nonzero factorization excludes the zero polynomial, while modulus minima include zero and constants.

| Entry | Purpose |
| --- | --- |
| `Complex.General.Nonconstant` | Inequality with every constant polynomial |
| `General.growth` | For nonconstant polynomials and real \(M\), positive \(r\) with \(\lvert z\rvert\ge r\Rightarrow\lvert p(z)\rvert>M\) |
| `General.Growth[p, form]` | Explicit normal-form radius, positivity, growth at infinity |
| `General.minimum` | Global minimum of the modulus of any polynomial, including zero/constants |
| `General.root` | Every nonconstant complex polynomial has a root |
| `Complex.Roots.exists` | Positive-degree monic coefficient lists have roots |
| `Roots.minimumRoot` | Modulus minima of positive-degree monic polynomials have value zero |
| `Roots.closed` | `AlgebraicallyClosed` for the entire complex field |
| `Complex.Factorization.monic` | Complete monic factorization by degree induction, root-list length equals degree |
| `Factorization.exists` | Nonzero factorization \(c\prod_i(X-a_i)\) with \(c\ne0\) |
| `Factorization.Uniqueness.result` | Two factorizations have equal leading coefficients and permuted root lists |
| `Factorization.Families.Permutation` | Finite-list permutation relation matching roots by successive removal |
| `Families.unique` / `independent` | Both implications between equal root products and permutation |
| `Families.Quotient.Family` / `family` | Finite root families modulo permutation and maps from lists |
| `Families.Quotient.product` / `productOf` | Representative-independent factor products and list computation laws |
| `Families.Quotient.injective` | Factor products uniquely determine finite root families |
| `Factorization.Unordered.exists` / `unique` | Existence/uniqueness of nonzero-polynomial presentations by leading coefficient and finite roots |

[Source](src/root.ref) · [Dependencies](ref.toml) · [Checking](../../USAGE.md) · [Notes](../../../math/package-notes/algebra/fundamental_algebra.md)
