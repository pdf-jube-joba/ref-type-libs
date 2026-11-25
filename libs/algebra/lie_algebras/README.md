# Lie algebras

`Field[K, field]` handles Lie algebras over arbitrary fields.
`LieAlgebra V space` is an alternating bilinear bracket on a vector space satisfying Jacobi.
Jacobi uses \([x,[y,z]]=[[x,y],z]+[y,[x,z]]\).

| Module | Contents |
| --- | --- |
| `Field.On` | Antisymmetry, linear `ad`, derivation law, `adRepresentation` |
| `Field.On.Of` | Induced subalgebra vector spaces and brackets |
| `Field.Hom` | Bracket-preserving linear maps |
| `Field.Abelian` | Zero brackets |
| `Field.Associative` | Associative commutators \([x,y]=xy-yx\), derivation/Jacobi proofs |
| `Field.Endomorphisms` | Associative endomorphism algebras and commutator Lie algebras |

`Field.Endomorphisms.scalarMap` maps coefficients to scalar identity maps; `scalarCentral` proves the image central.

Antisymmetry follows from alternation, so characteristic \(2\) is included.
`Classical.On.Orthogonal.LieAlgebra` in `geometry/lie_groups` proves skew-symmetric endomorphisms closed under commutators, instantiating \(\mathfrak{so}(n)\).

[Build and check](../../USAGE.md) from the repository root:

```sh
cargo run --manifest-path ref-type/Cargo.toml -p cli -- libs/algebra/lie_algebras --module lie_algebras
```
