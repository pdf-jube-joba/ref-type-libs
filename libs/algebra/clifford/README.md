# `clifford`

Clifford quotient construction and universality, Pin/Spin and complex-extension group structures.

The specialization is `Field[K, field].On[V, space].Of[form]`. Standard Euclidean forms use positive Clifford squares (Pin+); smooth group structures are in [lie_groups](../../geometry/lie_groups/README.md).

| Entry | Purpose |
| --- | --- |
| `Of.Carrier` / `Of.algebra` | Quotient carrier and associative-algebra structure |
| `Of.iota` / `Of.injection` | Canonical vector inclusion and linearity |
| `Of.cliffordRelation` | \(\iota(v)^2=q(v)1\) |
| `Of.Universal` | Unique homomorphisms from central coefficient maps and linear generator images |
| `Of.Relations` | Polarization anticommutation relations, triple products of generators |
| `Of.Grading` | Involutive grading automorphism negating generators, action on units, twisted adjoint |
| `Of.commutatorLieAlgebra` | Commutator Lie algebra |
| `Of.Pin` | Pin/Spin, complex extensions, group structures |
| `Of.Pin.Grading` / `Of.Pin.Reflection` | Involution preserves Pin and fixes Spin; twisted-adjoint reflection formulas for positive/negative unit vectors |
| `Circle` | Group \(U(1)\) of complex numbers satisfying \(z\overline z=1\) |
| `ComplexExtension.By` | \((G\times U(1))/\langle(-1,-1)\rangle\) using a central order-\(2\) element |
| `Field.Block` | Clifford block operators over coefficient algebras, linearity and square formulas |
| `Euclidean[n]` / `Euclidean.Successor` | Standard-inner-product Clifford algebra acting on two copies of the preceding algebra |
| `EuclideanCoordinates` | Faithful real coordinates in all dimensions, scalar/vector projections |
| `ComplexRepresentation.By` | Faithful two-component representations of complexified Pin subgroups, polynomial products/inverses/phase squares |
| `EuclideanFaithfulness.faithful` | Injectivity of canonical scalar/vector maps in all dimensions |
| `Euclidean.Successor.NormalForm` / `EuclideanCoordinates` | Unique two-component normal forms and faithful real coefficient coordinates |
| `EuclideanCenter` / `Euclidean.PinNorm` / `Euclidean.PinWords` | Scalar twisted centralizers, Pin norms, vector words and parity |

[Source](src/root.ref) · [Dependencies](ref.toml) · [Checking](../../USAGE.md) · [Notes](../../../math/package-notes/algebra/clifford.md)
