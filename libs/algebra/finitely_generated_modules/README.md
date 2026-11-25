# Finitely generated modules

Bases of integer kernels/images/submodules, cyclic modules, finite-dimensional subspaces over fields.

| Module | Public contents |
| --- | --- |
| `finitely_generated_modules.IntegerDiagonal` / `finitely_generated_modules.IntegerKernel` / `finitely_generated_modules.IntegerBasis` | Diagonal kernels, free kernel coordinates from Smith form, executable basis/inverse-coordinate matrices, component/kernel-isomorphism correspondence, image rank and free bases. |
| `finitely_generated_modules.IntegerIdeals` / `finitely_generated_modules.IntegerSubmodules` | Principal-ideal presentations of integer submodules, finite generation of submodules of finite-free integer modules, free bases from generating matrices and submodule isomorphisms. |

`finitely_generated_modules.FieldSubspaces.Over` proves existence of linear retractions onto submodules of finite coordinate spaces over fields.
`Dimension.Of.Retraction` has a map to the subspace and a left-inverse law with inclusion.
`existence` constructs retractions by dimension induction; `projective` proves subspaces projective as finite-free direct summands.
