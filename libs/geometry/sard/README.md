# Sard's theorem

| Entry | Result |
| --- | --- |
| `Proof.theorem n m` | Critical values of every smooth map between Euclidean opens have zero Lebesgue outer measure. |
| `RegularValues[n,m].On[U,V,f]` | The critical-value null theorem and existence of regular values in every nonempty Euclidean open set. |
| `Manifold[n,m].Between[M,N].Of[f]` | Critical values are null in every target chart. Regular values meet every nonempty target open set. |
| `Parameters[n,m,r].Between[M,T,P].Level[f,y,regular,projection]` | Chartwise null exceptional parameters and density of values where the slice derivative is surjective on the kernel of the parameter derivative. For a submersive parameter map, these values are exactly the regular values of the parameter projection restricted to the level. |
| `Corners[n,m].Between[M,N].Of[f]` | Chartwise null critical values for manifolds with corners, using local smooth extensions and their invariant derivatives. |
| `Corners.Between.Of.InChart.tangentialNull` / `tangentialRegularAt` | One null set outside which the derivative is surjective on the lineality of the source tangent cone at every preimage. |
| `Boundary[n,m].Between[M,T].With[cover].Of[f].InChart[right]` | Simultaneous regularity for the ambient map and its restriction to the actual G03 boundary constructed from the half-chart cover. |
| `Faces.Global.In.regularAt / regularOfTangential` | Every G03 global face is regular outside the same tangential exceptional set. The theorem takes the geometric face itself as an argument. |
| `Faces[n,m].Between[M,T].Of[f].All[right,boundary,faces]` | A chartwise null set for a supplied countable family of restrictions. This aggregator applies to the family it is given. The restriction certificates are obtained by composing with the smooth inclusions. `Faces.Global.In.restrict` constructs one from a G03 global face. |

The Euclidean proof inducts on source dimension. At a critical point with a nonzero derivative entry, a single output coordinate is a submersion. The G02 submersion chart makes it a coordinate projection, and the remaining output on each slice has a smaller-dimensional source. The critical image is exhausted by compact images so that the product-measure argument applies to Borel sets.

At a point where the first derivative vanishes, the strata are defined by successive orders of vanishing. A derivative that vanishes on one stratum and has a nonzero differential at the point defines a local hypersurface. Restricting to it lowers the source dimension. On the terminal stratum, iterated mean value estimates bound the oscillation by a power of the cube diameter. Dyadic subdivision and the Euclidean box-volume bound then give outer measure zero.

In each source chart the active coordinates determine one of finitely many masks. Freezing these coordinates at zero gives an ordinary smooth map on an open preimage, so Euclidean Sard supplies the null sets for that chart. Second countability reduces the local union to a countable one. The G03 local form of a global face places its normal coordinates among the active coordinates. Consequently its inclusion differential contains the lineality of the ambient tangent cone. The G03 boundary inclusion has the same property for a half-chart cover. The `Examples.IntervalIdentity.InChart` example proves that both endpoint values belong to the exceptional set in every chart that contains them.

[Source](src/root.ref) · [Dependencies](ref.toml) · [Checking](../../USAGE.md)
