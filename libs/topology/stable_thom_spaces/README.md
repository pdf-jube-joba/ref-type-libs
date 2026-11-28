# stable_thom_spaces

Pointed homotopy classes and their stabilization, with finite Grassmannian Thom spaces.

| Entry under `Stable` | Purpose |
| --- | --- |
| `Sphere.Disk` | The quotient of the round disk by its boundary, with a disjoint basepoint before collapsing to include dimension zero. |
| `Sphere.Disk.Successor` | Pointed homeomorphism between the next disk quotient and the reduced suspension. |
| `Sphere.Classes` | Based maps out of a sphere, their homotopy classes, and the equivalence between class equality and existence of a based homotopy. |
| `Suspension` | Suspension on maps and classes. Along constructs a continuous based homotopy between suspended maps. |
| `Sphere.Classes.Suspend` | Suspension from dimension n to dimension n+1, with the sphere comparison incorporated. |
| `Spectrum.At` | The direct limit for a sequence of pointed spaces and suspension structure maps. The starting spectrum level and the starting sphere dimension determine the degree. |
| `Spectrum.Degree` | The stable class set in an integer degree. |
| `Spectrum.At.Representatives` | Two pointed maps represent the same stable class exactly when their iterated transition maps become pointed homotopic at some common stage. |
| `Sequential.Descend` / `Sequential.Tail` | The direct limit universal property and the bijection obtained by dropping the first stage. |
| `Framed` | The sphere spectrum with the inverse of the pointed disk suspension comparison as its structure map. |
| `FiniteThom` / `Grassmannian` | Finite disk and sphere bundles of pullbacks of the tautological projection bundle. Includes the unoriented and oriented Thom spaces and the orientation-forgetting pointed map. |
| `Grassmannian.RankStep` | Finite unoriented rank stabilization from the suspension of the rank-k Thom space. The map adds a line to the underlying plane and sends the two cylinder ends and the original disk boundary to the target basepoint. |

The stable class sets have a distinguished zero class. The abelian group laws, finite ambient factorization for Thom representatives, compatibility of the finite rank structure maps with ambient stabilization, oriented rank structure maps, and products and signs are further T02 requirements.

[Source](src/root.ref) · [Plan](../../../math/t02-stable-thom.md) · [Checking](../../USAGE.md)
