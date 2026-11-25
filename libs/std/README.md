# Standard library

`std` has no package dependencies and provides logic, data, sets, arithmetic, and algebraic structures.

| Module | Contents |
| --- | --- |
| [Logic](src/Logic.ref) | Propositions, equality, classical logic, relations, orders, termination |
| [Data](src/Data.ref) | Bool, Nat, Pair, List, Option, Sum, finite sets |
| [Set](src/Set.ref) | Quotients and finite subsets |
| [Arithmetic](src/Arithmetic.ref) | Integers and rationals |
| [Alg](src/Alg.ref) | Monoids, groups, rings, fields, modules, algebras |
| [Program](src/Program.ref) | Implementation/specification correspondence, terminating state transitions |

`Data.FinSet.Tuples.Omission` exposes removal of one vertex from a sequence, prepend formulas, and interchange of two removals.
`Tuples.Mapping.omitMap` expresses commutation of mapping and removal.
`Data.FinSet.Choice.exists` constructs a satisfying function from finitely many existential propositions.

## Equality and congruence

Specify the carrier as a macro argument.

```text
\import std.Logic[].Equality[] \as E;
\use E.trans;
\use E.congr;
\use E.eq_reason;
\use E.eq_reason_in;

trans!{A} a b c ab bc
congr!{A B} f a b ab
congr!{A B C} f a b c d ab cd
congr!{A B C D} f a b c d e g ab cd eg

congr!{f a "=" b "in" A "by" ab "and" c "=" d "in" B "by" cd}
congr!{f a "=" b "by" ab c "=" d "by" cd}

eq_reason!{a "=" b "by" ab "=" c "by" bc}
eq_reason!{{ f a } "=" { f b } "by" { congr!{A B} f a b ab }}
eq_reason_in!{A a "=" b "by" ab "=" c "by" bc}
```

`congr!` replaces arguments of nondependent functions in order.
Forms accept either a sequence of types to obtain congruence or an explicit list of argument equalities; no arity-specific macros are needed.
`"in"` in the explicit form may be omitted when its type can be inferred.
`eq_reason_in!` chains equalities over a specified carrier even when intermediate terms have subset types.

Named APIs for fixed carriers are in `E.Prop[A := X]`.

```text
\import E.Prop[A := A] \as Laws;

Laws.congr[B] f a b ab
Laws.congr2[B, C] f a b c d ab cd
Laws.congr3[B, C, D] f a b c d e g ab cd eg
```

Instantiate the relation and its three laws to chain equivalences.

```text
\import std.Logic[].Equivalence[A := A, R := R,
  refl := reflexive, sym := symmetric, trans := transitive] \as ER;
\use ER.equiv_reason;
\use ER.equiv_reason_terms;

equiv_reason!{"by" ab "by" bc}
equiv_reason_terms!{a "~" b "by" ab "~" c "by_sym" cb}
equiv_reason_terms!{a}
```

`"by_sym"` uses a proof of the reverse relation; empty chains use reflexivity.
For nonempty chains requiring only transitivity, pass a transitivity proof to the `Transitive` macro.

```text
\import std.Logic[].Transitive[] \as TR;
\use TR.trans_reason;
\use TR.trans_reason_terms;

trans_reason!{transitive "by" ab "by" bc}
trans_reason_terms!{transitive a "~" b "by" ab "~" c "by" bc}
```

Use `cast F a b same value` in `E.Transport[A := A]` for transport in set-valued families.
`cast` exposes transport along set-valued `\idelim`; `castRefl`, `castComposition`, `castInverse`, `Constant.law` expose identity, composition, round-trip, and constant-family laws.
`natural`, `pointNatural`, `binaryNatural`, `reindex` prove compatibility of transport with family maps, elements, binary operations, and index maps.
Use `Logic.Proposition.orElim` and `either` for disjunction elimination.
`either` infers both propositions from the scrutinee and accepts a conclusion and two branches.

```text
\import std.Logic[].Proposition[] \as Logic;
\use Logic.either;

\definition fold[P, Q, R: \Prop]:
  (P -> R) -> (Q -> R) -> Logic.Or[P, Q] -> R :=
  \fun (left: _) (right: _) (value: _) => either!{value R left right};
```

`Logic.existsIntro[A, S] x member` proves `\exists \Cast[A] S` from `x: A` and `member: \In[A] S x`.

```text
\definition singletonInhabited[A: \Set][a: A]:
  \exists ( x: A \where x = a ) :=
  Logic.existsIntro[A, { x: A \where x = a }] a (\refl(a));
```

## Program and arithmetic

Bool, Nat, and Int are Program data; their reflected types are `Bool^`, `Nat^`, `Int^`.
Bool/Int operations group implementations, Set specifications, and agreement proofs in `program`, `specification`, `coherence` of `Program.Correspondence`.
Nat mathematical functions are in `Def`, executable implementations in `Program`, and correspondence in `ProgramProp`.
Iterative computations use `step`, `terminates`, `run` in `Program.Machine`.

| Module | Contents |
| --- | --- |
| `Data.Nat.Basic` | Addition, subtraction, multiplication, powers, comparison |
| `Data.Nat.Division` | Division, remainders, divisibility laws |
| `Data.Nat.Iteration` / `Parity` / `Gcd` | Finite iteration, parity, greatest common divisors |
| `Arithmetic.Int.Math` | Formal differences of natural pairs and group completion |
| `Int.Math.Specification` | Normal-form integers, group-completion correspondence and laws |
| `Arithmetic.IntAlgebra` | Additive abelian group of integers |
| `Arithmetic.Rat.Fractions` | Positive-denominator fractions and cross-product equivalence |
| `Rat.Fractions.Quotient` | Quotient arithmetic and agreement with representative computations |

Nat laws are in `Prop`; generic Set iteration is in `Data.Nat.Iteration.Def`.
For natural numbers, use `div a 0 = 0`, `mod a 0 = a`, `0^0 = 1`.
Unary representation is unsuitable for evaluating large concrete values.
Int has normal forms `ofNat n` / `negSucc n`; `toMath` / `fromMath` relate them to group completion.
Fraction `denominatorIndex d` represents denominator `d+1`.

## Pairs and sets

`Data.Pair.Times[A, B]` is the Program pair; `Times^[A, B]` is a reflected type over arbitrary Set carriers.
On the Set side, use `pair`, `first`, `second`, `swap`, `map`, `curry`, `uncurry`, `assoc`, `unassoc`.
Program-side type operations return computations; receive results with `\bind`.

```text
\import std.Data[].Pair[] \as P;
\definition swap[A, B: \VType][p: P.Times[A, B]]: \F(P.Times[B, A]) :=
  \program {
    \bind a: A <- P.Times::first p \then
    \bind b: B <- P.Times::second p \then
    \return P.Times[B, A]::pair b a
  };
```

`Def`, `Mapping.Def`, `Functions.Def` in `Pair.Program` provide the same operations as correspondence declarations.
[FiniteSubset](src/Set/FiniteSubset.ref) is the subset type generated by the empty set and finitely many `insert` operations.
`Data.FinSet` provides enumeration and coverage, and round trips between `Fin(n+1)` and `Option[Fin(n)]`.
`Data.FinSet.Permutations` defines finite-set bijections and swap sequences; `PermutationDecomposition.decomposition` proves every bijection is a swap sequence.
`Data.FinSet.Scope.finiteWhole` proves finiteness from enumerations; `Set.FiniteSubset.Enumeration.finiteOfEnumeration` derives set finiteness from arbitrary finite lists.

## Quotients and algebraic structures

[Quotient](src/Set/Quotient.ref) provides equivalence classes/representatives, quotient induction, and unary/binary operation lifting.
Quantify equivalence-relation laws as `EquivalenceLaws` in theorem assumptions.
[Logic.Rel](src/Logic/Rel.ref) groups carriers and relations as `RelationData` / `EquivalenceRelation`; [QuotientOf](src/Logic/Rel/QuotientOf.ref) treats their quotients as bundles.

Algebraic structures group data and laws in `\structure`.
`Alg.Monoid`, `Alg.Alg`, `Alg.Ring`, `Alg.Field` provide Monoid, Group, Semiring, Ring, Field, and commutative variants.
`RingModule` / `RingAlgebra` specify scalar rings and carriers.

## Verified integer computation and finite search

`Arithmetic.ExtendedEuclid` computes natural/signed-integer Bézout coefficients and exposes correspondence with mathematical specifications returning gcd and divisibility proofs.
`Signed.Division` computes signed quotients/remainders and proves decreasing remainder magnitude for nonzero divisors.
`Arithmetic.IntegerSum` and `Arithmetic.NaturalSum` provide terminating finite-sum machines and specification correspondence.
Natural finite sums bound each component and can measure decrease in integer-matrix pivot searches.
`Data.Nat.Induction.Termination` proves termination from lexicographic decrease of two natural numbers.
`Logic.Termination.Results` proves return-value properties from state invariants preserved by every transition.
`Data.Nat.Iteration.Program[A := T]` provides iteration on executable types; `Data.Nat.Find` and `Find.Grid` provide one/two-dimensional finite searches.
Proves result ranges/conditions and universal failure of the condition when searches are empty.


`Data.FinSet.elementsLength` proves standard finite-index enumeration length equals index size.
