# Finite CW complexes and singular chains

Construction details and records for [singular_cellular](../../../../libs/topology/singular/cellular/README.md).
See [building and checking](../../../../libs/USAGE.md) for current commands.
The API overview is maintained in the package README; recorded checks describe earlier runs.

`On[A, source, complex]` uses actual Euclidean closed balls for finite-CW characteristic domains.
`complex` requires continuous characteristic maps/interior inverses, closed images, lower-cell boundaries, cellular weak topology.

- `Filtration.Stage[limit]` is the skeleton of cells below `limit`.
- `Layer[n].sequence` is the adjacent-skeleton singular short exact sequence.
- `Layer[n].Basis.isomorphism` connects free abelian \(n\)-cell bases with relative skeleton homology.
  Bases use oriented balls/boundaries, punctured deformations, excision.
- `Cellular.complex` boundaries compose connecting maps with projection to the next lower relative group.
- `Cellular.Representatives.selectionExists` chooses cell fundamental representatives compatible with cellular boundaries.
  `Selected[selection].integerMap` and `equivalenceExists` compare singular chains.
- `Selected[selection].With[coefficients].At[z].isomorphism` gives arbitrary-coefficient cohomology comparisons.
  `Homology[coefficients].At[z].isomorphism` compares homology by tensoring comparison maps with coefficients.
- `Selected[selection].Coefficients[input, output, coefficientMap].cochainNaturality` proves coefficient/cochain compatibility.
- `Selected[selection].Native[e].Diagonal.map` transfers singular Alexander–Whitney diagonals to cellular chains by equivalences.
  `Diagonal.Cup[R, ring, p, q].realizes` and `agreement` identify resulting/singular products.
- `Naturality[B, target, targetCW].Chosen[sourceSelection, targetSelection].Chain[e].Along[f, continuous].With[coefficients].At[z].naturality` connects actual chosen-inverse cellular maps with singular comparisons.
  `recoveryExists` provides needed inverse existence.
  `Along[f, continuous].Homology[coefficients].At[z].naturality` gives homology naturality of actual \(\chi\otimes\mathrm{id}\) induced maps.
- `Naturality[B, target, targetCW].Chosen[sourceSelection, targetSelection].Coefficients[input, output, coefficientMap].At[z].Along[f, continuous]` constructs continuous-map cellular pullbacks and comparison naturality.
- `CellCollapse[cell, member, point].Pair.Basis.Incidence[sourceCell].Degree.Normalized[k, positive, h].Spherical.incidence` identifies positive-dimensional boundary entries with actual sphere degrees.
  Sphere maps use attaching maps/other-cell collapse, correcting homeomorphism orientations.
  `CellCollapse[cell, member, point].Positive[k, positive].Orientation.existence` gives orientation-corrected homeomorphisms.
- `CellCollapse[cell, member, point].Pair.Basis.orientationEquation` identifies dimension-transported cell orientations with standard disks by reflexive-transport computation.
- `ZeroCollapse[cell].Basis.Incidence[sourceCell].Degree.incidence` identifies one-cell boundaries with actual \(S^0\) degrees.
  `endpoints` gives positive-endpoint indicators minus negative-endpoint indicators.
- `Coordinates.indexingExistence` and `With[indexing].Bounded.model` give finite cell enumerations/integer matrices.
  `Bounded.Compared[selection].equivalenceExists` compares finite matrices with actual singular chains.

`DiskLocal[n].Attachment[neighborhood]` directly handles single closed-ball attachments.
Takes characteristic maps, actual punctured-neighborhood retractions, open-ball/complement homeomorphisms; derives relative comparisons.
`DiskSphere[n].Quotient.homeomorphism` identifies \(D^{n+1}/\partial D^{n+1}\) with \(S^{n+1}\).

Shared sums, relative splits, excision naturality, representative corrections: `singular_cellular_algebra`.
