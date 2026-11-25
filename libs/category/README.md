# Category theory

`category` handles categories with sets of objects and families of morphism sets.
Store identity/composition data, category laws, functor maps, and functor laws separately.
Natural transformations are component functions satisfying naturality; equality uses function extensionality.

| Module | Contents |
| --- | --- |
| `Category` | Categories, opposite categories, morphism congruence, isomorphisms and cancellation |
| `Constructions` | Terminal category, functors to it, categories of functions on set families |
| `Functor` | Functors, identities, composition, opposites, constants |
| `Natural` | Natural transformations, vertical composition, left/right whiskering, natural isomorphisms |
| `FunctorCategory` | Functor categories and precomposition restriction |
| `Universal` | Initial/terminal objects, universal morphisms, uniqueness up to isomorphism |
| `Limits` | Cones, cocones, limits, colimits, uniqueness up to isomorphism |
| `Adjunction` | Adjunctions via natural Hom bijections, units/counits, triangle identities, universal morphisms from units |
| `SetValued` | Set-valued functors, representable functors, Yoneda bijections |
| `Kan` | Left/right Kan extensions, extension along identities, uniqueness up to natural isomorphism |
| `Preadditive` | Additive abelian morphism groups, biadditive composition, composition with zero |
| `Additive` | Zero objects and binary biproducts, map comparisons via projections/inclusions |
| `Abelian` | Kernel/cokernel universality, normal monomorphisms/epimorphisms, uniqueness up to isomorphism |

## Kan extensions

`Kan.Along` accepts functors \(K:A\to B\) and \(F:A\to C\).
`Left` bundles a functor \(L:B\to C\), a transformation \(\eta:F\Rightarrow LK\), and unique transformations \(L\Rightarrow G\) factoring arbitrary \(\alpha:F\Rightarrow GK\).
`Right` bundles the dual universal property using a transformation \(RK\Rightarrow F\).
Extract extension functors from `extension` and transformations to comparison functors from `factor`.
Naturality and factorization equalities quantify over every object and morphism.
`leftUnique` and `rightUnique` in `Kan.Along.Prop` construct natural isomorphisms between two extensions of the same \(K,F\).

[Examples](src/root.ref) check categories, functors, transformations, and universal properties.
