# Connecting topology and algebra

Reduce scalar/coordinate/matrix continuity to componentwise conditions.

| Module | Contents |
| --- | --- |
| `Topology` / `Topology.Functions` | Topological abelian groups/rings, continuous-function operations |
| `Coordinates` / `Universal` / `Update` | Arbitrary-index product topologies, universality, single-coordinate replacement |
| `FinitePower` | Compact finite products |
| `Euclidean.Dimension.Completeness` | Complete finite maximum-norm coordinates, component limits |
| `Real` / `Complex` / `Complex.Functions` / `Complex.Ring` | Real/complex topologies and continuous arithmetic |
| `Matrix` / `Universal` / `Operations` / `Operations.Composition` | Double-index matrix topologies, component criteria, sums/transpose/finite products |
| `FiniteDimensional.Over.Functions` | Finite sums valued in topological scalar rings |
| `FiniteDimensional.Over.Space` / `Space.Functional` / `Space.Linear` / `Space.Comparison` | Finite-basis topologies, coordinate homeomorphisms, continuous linear maps, basis independence |

Coordinate indices need not be finite or enumerated.
Matrix carriers use `linear_algebra` function representations.
`Over` parameters are field structures; continuity is quantified in theorem assumptions.

Examples: [matrices](../examples/cells/src/Matrix.ref) and [finite-dimensional spaces](../examples/cells/src/Finite.ref).


`Euclidean.Blocks.Joining` concatenates two continuous coordinate families over arbitrary bases into one finite family.
