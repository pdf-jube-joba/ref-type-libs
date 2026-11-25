# `polynomial_linear_algebra`

Polynomial division/Euclidean algorithm, Bézout coefficients, Chinese remainder theorem, Cayley–Hamilton, kernel direct sums, coefficient changes.

Polynomial APIs specialize `Field[K, field]`. Coefficient lists ascend and may have trailing zeros; division requires a nonzero divisor.

| Entry | Purpose |
| --- | --- |
| `Euclid.divide` | Existence of quotients/remainders from ascending coefficients and nonzero divisors |
| `DivisionResult` | Quotients, remainders, nonzero leading coefficients/monic divisors, remainder-degree bounds, division identities |
| `Euclid.exists` | Extended Euclidean algorithm by strong induction on remainder-list length |
| `Gcd` / `Bezout` / `Divides` | Common divisors, both divisibility proofs, Bézout coefficients/identities |
| `Euclid.greatest` | Every common divisor divides the constructed one |
| `Representatives.exists` | Every abstract polynomial has a finite coefficient presentation |
| `Representatives.gcdExists` / `divisionExists` | Euclidean/division algorithms on abstract polynomials |
| `Principal` / `Chinese` | Principal quotients, Chinese-remainder isomorphisms and explicit inverses |
| `Evaluation` / `Field.Action` / `Primary` | Polynomial substitution, coprime kernel sums and choice-independent invariant projections |
| `Field.At` / `Field.Finite` | Matrix/finite-basis characteristic polynomials and Cayley–Hamilton |
| `Field.Change` / `Intertwining` | Coefficient changes and semilinear projection naturality |

[Source](src/root.ref) · [Dependencies](ref.toml) · [Checking](../../USAGE.md) · [Notes](../../../math/package-notes/algebra/polynomial_linear_algebra.md)
