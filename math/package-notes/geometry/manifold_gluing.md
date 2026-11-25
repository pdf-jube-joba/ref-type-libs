# `manifold_gluing` notes

[Package API](../../../libs/geometry/manifold_gluing/README.md) · [Checking](../../../libs/USAGE.md)

## Construction

Construct compact-boundary collars, diffeomorphism gluings/doubles, and supported product-corner rounding from actual maps/inverses/charts.
Uses `boundary_manifolds` corner manifolds and `smooth_partitions` smooth bumps.
Existence does not assume global collars or post-gluing smooth structures.

### Collars

The relative theorem contains collar images in prescribed neighborhoods.
Stronger extensions agreeing with existing partial collars are not exposed.
`GlobalPush` smoothly connects compactly supported coordinate push-ins with identity and composes finitely many.
Positive initial normal velocities yield actual half-space local inverses; compact boundaries uniformize time widths.

### Boundary gluing and doubles

`BoundarySeam` constructs quotients from actual boundary diffeomorphisms, proving compact Hausdorffness/second countability.
`SeamCollar` identifies signed collars homeomorphically with open quotient seams.
Construct smooth transitions for all nine left/right-interior/seam overlap types.
`CompactGluing.Between.With.Along.Compact.exists` exposes actual quotient smooth atlases and absence of residual boundaries.
Results retain collars, atlas/construction agreement, actual smooth whole-left/right/signed-seam inclusions, and pointwise values.
`Double.Compact.left` and `right` also directly extract corresponding smooth inclusions.
`Double.On.With.Compact.exists` doubles along boundary identity diffeomorphisms.
`SeamCollar.Image.Compact.Cover.Inclusions` constructs whole-left/right and signed-seam inclusions as actual smooth maps.
`CollarMaps` in the same `Cover` glues collar-preserving smooth maps into quotient maps and includes an identity example.

### Rounding products

`SupportedRounding` constructs \(\psi(d)=\sqrt{d^2+b(d)}\) from smooth bumps.
`Higher` regular sublevel \(u+v-\psi(u-v)\geq0\) lies in the orthant, agreeing when \(u\geq3\) or \(v\geq3\).
`Quarter.Outside` constructs actual outer-open identity diffeomorphisms.
`ProductCollar` chooses positive scale \(q\), constructing product collars with \(3q<4q<\varepsilon\leq1\).
`Rounded` removes opens where normalized rounding functions are negative from actual products.
The region is closed/compact, modifications stay inside compact interiors, removing original corners.
`NearModel.Image` constructs actual homeomorphisms of open corner neighborhoods with boundary products times rounded normal models.
`Rounded.Global.Using.Cover` constructs all four inner/outer smooth transition types.
`ProductCollar.Between.With.Compact.exists` constructs collars/scales/regions/global atlases from compactness/boundary covers.
`Compact.Of` exposes manifolds/compactness, exterior agreement, and original-corner removal.
`RoundedBoundary.Between.With.Compact.exists` constructs normalized boundary atlases on the same rounded region.
`Compact.Of.boundaryCover` returns actual `Boundary.Cover`; `noHigherCorners` ensures charts with at most one active boundary coordinate per point.
`Compact.Of` also exposes compactness, exterior agreement, corner removal.

### Orientations and auxiliary theorems

`Reflection.Orientation` proves normal-reflection determinants/sign reversal of arbitrary top forms.
`BoundarySigns` proves outward-normal reversal, two-normal contraction swap, boundary-cancellation signs.
`BoundaryForms` applies these to actual boundary-inclusion derivative pullbacks.
`GluingForms.Between.With.Along.Compact.For` takes returned `CompactGluing.Result`, proving `leftSide`, `rightSide` identify actual seams with left/right inclusions on signed collars.
`For.At.In` constructs both normal-coordinate frames from actual seam derivatives at arbitrary boundary charts/points.
`frameCoordinates` and `recoverForm` prove coordinate isomorphisms retain top-form information.
`orientationCoherence` proves right-frame pullbacks equal \(-1\) times left pullbacks.
`normalOpposite`, `horizontal`, `outwardOpposite`, `boundaryCancellation` prove inward-normal reversal, common tangents, outward-form signs/cancellation.
`DoubleForms.On.With.Compact.For.At.In` specializes signs/cancellation to actual doubles.
`DiffeomorphismCones` derives boundary/tangent preservation from actual smooth inverses.
`OpenManifoldCones` proves open-inclusion boundary agreement and derivative criteria for tangent/strict normal directions.
`OpenSmoothExtension` glues actual smooth maps on opens and off closed sets when agreeing on overlaps.
