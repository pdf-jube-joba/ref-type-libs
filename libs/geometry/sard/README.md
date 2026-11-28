# Sard's theorem

| Entry | Result |
| --- | --- |
| `Proof.theorem n m` | Critical values of every smooth map between Euclidean opens have zero Lebesgue outer measure. |
| `RegularValues[n,m].On[U,V,f]` | The critical-value null theorem and existence of regular values in every nonempty Euclidean open set. |
| `Manifold[n,m].Between[M,N].Of[f]` | Critical values are null in every target chart. Regular values meet every nonempty target open set. |
| `Parameters[n,m,r].Between[M,T,P].Level[f,y,regular,projection]` | Chartwise null exceptional parameters and density of values where the slice derivative is surjective on the kernel of the parameter derivative. For a submersive parameter map, these values are exactly the regular values of the parameter projection restricted to the level. |
| `Corners[n,m].Between[M,N].Of[f]` | Chartwise null critical values for manifolds with corners, using local smooth extensions and their invariant derivatives. |
| `Faces[n,m].Between[M,T].Of[f].All[right,boundary,faces]` | A single chartwise null set outside which the ambient map, boundary restriction, and every restriction in a countable family of faces are regular. The restriction certificates are obtained by composing with the smooth inclusions. `Faces.Global.In.restrict` constructs one from a G03 global face. |

The Euclidean proof inducts on source dimension. At a critical point with a nonzero derivative entry, a single output coordinate is a submersion. The G02 submersion chart makes it a coordinate projection, and the remaining output on each slice has a smaller-dimensional source. The critical image is exhausted by compact images so that the product-measure argument applies to Borel sets.

At a point where the first derivative vanishes, the strata are defined by successive orders of vanishing. A derivative that vanishes on one stratum and has a nonzero differential at the point defines a local hypersurface. Restricting to it lowers the source dimension. On the terminal stratum, iterated mean value estimates bound the oscillation by a power of the cube diameter. Dyadic subdivision and the Euclidean box-volume bound then give outer measure zero.

[Source](src/root.ref) · [Dependencies](ref.toml) · [Checking](../../USAGE.md)
