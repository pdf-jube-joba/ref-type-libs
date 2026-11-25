# B08 Grassmannian cell decompositions

## Work status

[grassmannian_cells](../../libs/geometry/grassmannian_cells/README.md) contains definitions and proof terms for all requirements.
The following distinguishes implemented scope from scope lacking type-check confirmation.

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

In the 2026-11-20 supplement, the target package's `--parse-only --diagnostics compact` and `git diff --check` completed with exit code 0.
Neither target nor full type checking was run.
Parsing does not check name resolution or type consistency, so the entire supplement above lacks type-check confirmation.
The initial pre-handoff type check also remained incomplete after 300 seconds; B08 formal verification is not declared complete.
No new axioms or unproved replacements added.
Continue collecting results in the existing [Draft PR #81](https://github.com/pdf-jube-joba/ref-type/pull/81).

## Requirements

- Primary implementation: `grassmannian_cells`.
- Construct Schubert coordinates for finite real and complex Grassmannians; prove finite CW structures by attaching closures.
- Give CW structures and comparisons for standard ambient inclusions and coverings of oriented Grassmannians.
- Equip stabilization direct limits with weak topology; expose finite-stage representation lemmas for maps and homotopies from compact spheres.

## Dependencies

- [B05 Finite Grassmannians and universal bundles](b05-grassmannians.md)
- [K02 CW cofibrations and Puppe sequences](../../libs/topology/puppe_sequences/README.md)
