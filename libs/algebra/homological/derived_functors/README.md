# Derived functors

Ext/Tor over commutative rings, resolution independence, naturality, universal coefficients.

| Module | Contents |
| --- | --- |
| `Ext.Over.Of` / `Tor.Over.Of` | Degreewise modules from specified projective resolutions |
| `Independence` / `DegreeZero` | Resolution-change isomorphisms, degree-zero Hom/tensor isomorphisms |
| `IntegerCyclicResolution` | Integer cyclic resolutions and Ext/Tor computations |
| `Tor.Over.Balance.With.At` | Comparison isomorphisms identifying Tor from resolving either variable |
| `Balance.Naturality.With.At` / `Balance.With.Swap.At` | Naturality in both variables, double-swap identity |
| `ShortExactFirst.With.On.Balance.With.At` | Compatibility of variable swaps with long-exact connecting maps |
| `Tor.Over.ProjectiveSecond` | Projective-coefficient swaps and positive-degree vanishing |
| `Ext.Over.Extension.With` | Ext¹ as a quotient of homomorphisms from first syzygies |
| `OfExtension.With` / `RepresentationClass` / `Compare` | Extension classes, representatives for every class, correspondence with extension isomorphisms |
| `UniversalCoefficient.Over.Projective.At` | Ext¹/Tor₁ short exact sequences from projective boundaries/cycles |
| `Selected` / `ChoiceIndependence` | Splitting choices and coordinate changes |
| `ExactNaturality` / `ExactIdentity` / `ExactComposition` | Short-exact endpoint maps, identities/composition |

Tor comparison uses total double resolutions; `onComparison` proves agreement with actual induced maps.
Vanishing examples: [Cyclic.ProjectiveCoefficient](../concrete_complexes/src/Cyclic/ProjectiveCoefficient.ref).
