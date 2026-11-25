# `vector_bundles`

General real/complex bundles, locally constant rank, bundle maps/sections/pullbacks and universality.

APIs specialize `Bundles.Over[K, field, conjugation, scalar]`. Finite rank may vary between components and is proved locally constant.

| Entry | Purpose |
| --- | --- |
| `Over.Morphisms` | Fiber-linear maps over \(f:X\to Y\) with total continuity |
| `Morphisms.total` / `projection` / `onFiber` / `ext` | Total maps, projection compatibility, fiber formulas/extensionality |
| `Morphisms.Composition.compose` / `Over.Identity.map` | Composition/identity bundle maps |
| `Over.ArrowLaws` / `Associativity` | Unit/associative laws, base continuity derived using zero sections |
| `Over.Isomorphisms` | Inverse maps over common bases, total homeomorphisms, inverse bundle isomorphisms |
| `Isomorphisms.inverseExists` | Reverse isomorphism existence from forward existence |
| `Of.Sections` | Sections as dependent vectors giving continuous total maps |
| `Sections.regular` / `zero` | Local-coordinate section continuity, zero sections |

[Source](src/root.ref) · [Dependencies](ref.toml) · [Checking](../../USAGE.md) · [Notes](../../../math/package-notes/geometry/vector_bundles.md)
