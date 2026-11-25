# G04 Collars and boundary gluing

## Requirements

- Primary implementation: `manifold_gluing`.
- Construct collars on compact manifolds with boundary; prove relative versions in prescribed boundary neighborhoods and compare choices.
- Construct smooth structures on gluings along boundary diffeomorphisms and doubles.
- Expose rounding of product corners, orientation/boundary signs, and gluing of collar-preserving maps.

## Dependencies

- [G01 Smooth bump functions and partitions of unity](g01-smooth-partitions.md)
- [G03 Manifolds with boundary and corners](g03-boundary-manifolds.md)

## Implementation

Implemented.
Public API and theorem scope: [manifold_gluing](../libs/geometry/manifold_gluing/README.md).

| Requirements | Implementation |
| --- | --- |
| Collars of compact manifolds with boundary | `CollarEmbedding.On.With.exists`, global collars with actual local inverses and uniform positive width |
| Relative prescribed-neighborhood version and choice comparisons | Boundary-fixing smooth comparisons in `CollarRelative.On.With.In.exists`, `CollarComparison` |
| Gluing along boundary diffeomorphisms and doubles | Actual quotients, smooth atlases, boundarylessness, smooth left/right/seam inclusions and value laws in `CompactGluing`, `Double` |
| Rounding product corners | Compactly supported rounding in `ProductCollar`; boundary atlas of `RoundedBoundary.Compact.exists` and `Boundary.Cover`; at most one active boundary face at each point |
| Orientation and boundary signs | Frame/top-form signs from actual seam-map derivatives and cancellation of outward boundary forms in `GluingForms`; double specialization via `DoubleForms` |
| Gluing collar-preserving maps | Gluing actual smooth maps and the identity example in `SeamCollar.Image.Compact.Cover.CollarMaps` |

The relative theorem places the entire collar image inside a prescribed open neighborhood of the whole boundary.
Extension agreeing with an existing partial collar is a separate, stronger theorem.
