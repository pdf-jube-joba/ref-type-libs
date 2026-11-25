# Chain and cochain complexes

Natural/integer-graded complexes over rings, homology, maps, and homotopies.

| Module | Contents |
| --- | --- |
| `Cochain.Over` | Natural-graded cochains, cycles modulo boundaries, induced maps |
| `Integer.Over` | Integer-graded cochain complexes |
| `Cochain.Over.ZeroExtension` / `Recovery` | Extension by zero in negative degrees, restriction round trips, cohomology isomorphisms |
| `Chain.Over.At` / `Map.At` | Integer-graded chains, homology, induced maps |
| `Chain.Over.Homotopy` / `Equivalence.At` | \(f-g=dh+hd\), isomorphisms from homotopy equivalences |
| `Chain.Over.Shift` / `Cone` / `ConeIdentity` | Shifts with differential \(-d\), mapping cones, contraction of identity cones |
| `Chain.Over.Zero` / `Concentrated` / `ZeroDifferential.At` | Homology of zero, concentrated, and zero-differential complexes |
| `Chain.Over.Map.Kernel` | Termwise kernels, homology isomorphisms from exact kernels of surjective comparison maps |
| `Chain.Over.QuotientMapping.On` | Quotient-complex maps induced by commutative squares, generator formulas |
| `Chain.Over.ShortExact.Morphism.Diagram` / `Integer.Over.ShortExact.Morphism.Diagram` | Long-exact naturality and relative-group comparison via five-term exact sequences |
| `Chain.Over.Reverse` / `Reversal.Over.ToChain` | Chain/cochain conversion by degree negation |
| `ModuleCategory.Over.On` / `ShortExactCategory.Over.On` | Preadditive module-family categories, short-exact-sequence categories, connecting-map naturality |
| `CochainEquivalence.Over.Of.With` | Cohomology isomorphisms from cochain homotopy equivalences |

Degree-zero cochain boundaries are the zero submodule.
Zero-extension `PositiveCohomology`, `NegativeCohomology` return original-cohomology isomorphisms and negative-degree vanishing.
Field-coefficient splittings/contractions are in [field_kunneth](../field_kunneth/README.md).
