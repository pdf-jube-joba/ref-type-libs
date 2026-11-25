# `lie_algebras`

Lie algebras, adjoint representations, commutators, Lie subalgebras, endomorphism algebras.

APIs specialize `Field[K, field]`. Alternation implies antisymmetry, including in characteristic two.

| Entry | Purpose |
| --- | --- |
| `Field.On` | Antisymmetry, linear `ad`, derivation law, `adRepresentation` |
| `Field.On.Of` | Induced subalgebra vector spaces and brackets |
| `Field.Hom` | Bracket-preserving linear maps |
| `Field.Abelian` | Zero brackets |
| `Field.Associative` | Associative commutators \([x,y]=xy-yx\), derivation/Jacobi proofs |
| `Field.Endomorphisms` | Associative endomorphism algebras and commutator Lie algebras |

[Source](src/root.ref) · [Dependencies](ref.toml) · [Checking](../../USAGE.md)
