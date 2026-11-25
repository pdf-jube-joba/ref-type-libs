# `std`

Logic, data, integers/rationals, quotients, algebraic structures.

No package dependencies. Natural-number conventions are div(a,0)=0, mod(a,0)=a and 0^0=1; executable types and mathematical specifications are related by correspondence proofs.

| Entry | Purpose |
| --- | --- |
| [Logic](src/Logic.ref) | Propositions, equality, classical logic, relations, orders, termination |
| [Data](src/Data.ref) | Bool, Nat, Pair, List, Option, Sum, finite sets |
| [Set](src/Set.ref) | Quotients and finite subsets |
| [Arithmetic](src/Arithmetic.ref) | Integers and rationals |
| [Alg](src/Alg.ref) | Monoids, groups, rings, fields, modules, algebras |
| [Program](src/Program.ref) | Implementation/specification correspondence, terminating state transitions |
| `Data.Nat.Basic` | Addition, subtraction, multiplication, powers, comparison |
| `Data.Nat.Division` | Division, remainders, divisibility laws |
| `Data.Nat.Iteration` / `Parity` / `Gcd` | Finite iteration, parity, greatest common divisors |
| `Arithmetic.Int.Math` | Formal differences of natural pairs and group completion |
| `Int.Math.Specification` | Normal-form integers, group-completion correspondence and laws |
| `Arithmetic.IntAlgebra` | Additive abelian group of integers |
| `Arithmetic.Rat.Fractions` | Positive-denominator fractions and cross-product equivalence |
| `Rat.Fractions.Quotient` | Quotient arithmetic and agreement with representative computations |
| `Logic.Equality` / `Equivalence` / `Transitive` | Congruence, equality/relation chains and set-valued transport |
| `Arithmetic.ExtendedEuclid` / `IntegerSum` / `NaturalSum` | Verified Bézout computation and finite-sum machines |
| `Data.Nat.Find` / `Logic.Termination.Results` | Finite searches and invariant-based return-value proofs |

[Source](src/root.ref) · [Dependencies](ref.toml) · [Checking](../USAGE.md) · [Guide](USAGE.md)
