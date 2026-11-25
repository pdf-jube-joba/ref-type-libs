# B08 Grassmannian cell decompositions

## Work status

[grassmannian_cells](../libs/geometry/grassmannian_cells/README.md) contains definitions and proof terms for all requirements.
The table maps the requirements to their implemented APIs.

| Requirement | Implemented API |
| --- | --- |
| Schubert coordinates, total dimension, echelon decomposition, coverage and disjointness | `Symbols.FreeCount`, `Canonical.FiniteCoordinates`, `Reduction`, `DecompositionReal` and `DecompositionComplex` |
| Identification of products of closed balls with standard disks | `Rotations.Parameters.Disk`, `Characteristic.diskExists` |
| Interior homeomorphism of characteristic maps; boundary inclusion in lower-dimensional cells | `StandardDisk.interiorImage` and `interiorHomeomorphism`, `Characteristic.boundaryLower` |
| Real and complex finite CW structures | `CWReal.exists` and `CWComplex.exists`, existing `algebraic_topology.CW.FiniteComplex` |
| Standard ambient inclusions and CW-structure comparison | `cellular`, `reflects`, `cellHomeomorphism` of `AmbientReal.CW` and `AmbientComplex.CW`; `With.filtrationEquals` |
| Coverings of oriented real Grassmannians | `OrientedReal.covering` and `twoSheets`, `Atlas.In.homeomorphism` |
| Lifted finite CW structures and comparisons on coverings | `OrientedReal.CW.exists`, `With.projects` and `filtrationEqualsPreimage` |
| Stabilization limits and finite stages for sphere maps/homotopies | `weakTopology`, `Maps.exists`, `Spheres.sphereMap`, `sphereHomotopy` of `StableReal` and `StableComplex` |

The later 2026-11-20 [upstream validation record](../reftype/work/b08-type-check/README.md) supersedes the earlier parse-only supplement and incomplete 300-second run.
At upstream source commit `5deadd6563878d1a010b9b628b7e9d68229a9cfe`, all 225 B08 modules were actually checked successfully, and a separate driver run accepted all 7,852 dependency-closure modules using verified caches.
No new axioms or unproved replacements were added.

The full-workspace run stopped at a G06 name-resolution error after 11,895/15,749 modules; a temporary G06 integration reached 13,276/15,750 before resource-related interruptions.
Neither run established full-workspace success.
These are historical upstream results, not a new check of the current checkout; see the [package validation summary](../libs/geometry/grassmannian_cells/README.md#type-checking) and [current checking instructions](../libs/USAGE.md).

## Requirements

- Primary implementation: `grassmannian_cells`.
- Construct Schubert coordinates for finite real and complex Grassmannians; prove finite CW structures by attaching closures.
- Give CW structures and comparisons for standard ambient inclusions and coverings of oriented Grassmannians.
- Equip stabilization direct limits with weak topology; expose finite-stage representation lemmas for maps and homotopies from compact spheres.

## Dependencies

- [B05 Finite Grassmannians and universal bundles](b05-grassmannians.md)
- [K02 CW cofibrations and Puppe sequences](../libs/topology/puppe_sequences/README.md)
