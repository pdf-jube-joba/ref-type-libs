# General quintic insolubility by radicals

Package: `quintic`.
Use `galois` field extensions, minimal polynomials, automorphism extensions, and derived series to prove radical insolubility of the quintic from five independent roots.

## Theorem

Take algebraically closed constants \(C\) and \(C\)-algebraically independent \(r_a,r_b,r_c,r_d,r_e\).
Ambient \(K\) is countable, algebraically closed, and algebraic over \(C(r_a,r_b,r_c,r_d,r_e)\).
An injection from naturals into constants expresses infinitude.

\[
P(T)=\prod_{i\in\{a,b,c,d,e\}}(T-r_i)
     =T^5+a_4T^4+a_3T^3+a_2T^2+a_1T+a_0,
\qquad F=C(a_0,a_1,a_2,a_3,a_4).
\]

`Generic.Field.Over.Equation` constructs the coefficient list and coefficient field \(F\).
`degree` proves degree five; `over` proves coefficients in \(F\); `firstRoot` proves \(P(r_a)=0\).

`Generic.Field.Over.AbelRuffini` proves:

| Theorem | Conclusion |
| --- | --- |
| `firstRootNotRadical` | \(r_a\) is outside the radical closure over \(F\). |
| `noRadicalFormula` | No expression from \(F\), arithmetic, and finitely many radicals represents \(r_a\). |
| `notSolvableByRadicals` | \(P\) is not solvable by radicals over \(F\). |
| `firstRootNotConstructible` / `noConstruction` | \(r_a\) is not constructible over \(F\) by finite field/square-root operations. |
| `notConstructible` | Not all roots are constructible over \(F\). |

These implications assume `Closure.Conditions` and algebraically closed constants.
`Closure.Conditions` includes algebraic closedness of \(K\), root independence, an injection into constants, and algebraicity of \(K/C(r_a,r_b,r_c,r_d,r_e)\).
Supply an enumeration of all \(K\) elements as a module argument.
Algebraic independence means the multivariate evaluation kernel is zero.
`Distinctness.independentImpliesDistinct` derives distinct roots.

## Proof structure

1. Prove variable permutations preserve polynomial-ring relations.
2. Independence preserves polynomial-fraction relations under permutations, constructing isomorphisms of \(C(r_a,r_b,r_c,r_d,r_e)\).
3. Use minimal polynomials/simple-extension isomorphisms to extend automorphisms back and forth through countable \(K\).
4. Reorder linear factors for three explicit permutations to show automorphisms fix \(P\)'s coefficients.
5. Radical expressions are fixed at some derived-series stage.
   But \([scs^{-1},tct^{-1}]=c\) for \(c=(a\ b\ c)\) and explicit \(s,t\) leaves this 3-cycle action in every stage.
   This contradicts \(r_a\ne r_b\).

Extension of root permutations and radical-fixing properties are proved conclusions.
Classical choice uses existing `classicalIndefiniteChoice`.

## Modules used

```text
\import quintic.Generic[].Field[K := K, field := field]
  .Over[constants := constants, roots := roots] \as Generic;
\import Generic.Equation[] \as Equation;
\import Generic.Closure[enumeration := enumeration, index := index] \as Closure;
\import Generic.AbelRuffini[enumeration := enumeration, index := index] \as AbelRuffini;
```

`K` is the field carrier; `field` is `std.Alg.Field.Field[K]`; `constants` is `galois.Field.Over.Subfield.Subfield`; `roots` is `galois.Quintic.Five -> K`.
`enumeration` is `std.Set.Countability[K].Enumerator`; `index` is `Nat -> K`.
Radical closure, constructibility, and rational algebraic-closure definitions: [galois](../galois/README.md).

## Checks

[Build and check](../../USAGE.md) from the repository root:

```sh
cargo run --manifest-path reftype/Cargo.toml -p cli -- libs/algebra/galois --module galois --full-check-local
cargo run --manifest-path reftype/Cargo.toml -p cli -- libs/algebra/quintic --module quintic --full-check-local
```
