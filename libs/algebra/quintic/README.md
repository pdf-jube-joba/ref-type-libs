# `quintic`

Insolubility of the general quintic by radicals and nonconstructibility.

The named conclusions are under `Generic.Field.Over.AbelRuffini`. They assume algebraically closed constants, five algebraically independent roots and an enumerated algebraically closed ambient field algebraic over the generated field.

| Entry | Purpose |
| --- | --- |
| `firstRootNotRadical` | \(r_a\) is outside the radical closure over \(F\) |
| `noRadicalFormula` | No expression from \(F\), arithmetic, and finitely many radicals represents \(r_a\) |
| `notSolvableByRadicals` | \(P\) is not solvable by radicals over \(F\) |
| `firstRootNotConstructible` / `noConstruction` | \(r_a\) is not constructible over \(F\) by finite field/square-root operations |
| `notConstructible` | Not all roots are constructible over \(F\) |
| `Generic.Field.Over.Equation` / `Closure` | Coefficient fields and hypotheses for the generic quintic |

[Source](src/root.ref) · [Dependencies](ref.toml) · [Checking](../../USAGE.md) · [Notes](../../../math/package-notes/algebra/quintic.md)
