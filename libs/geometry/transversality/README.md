# Smooth approximation and transversality

| Entry | Result |
| --- | --- |
| `Approximation[n].On[M].Of[f,continuous]` | Uniform smooth approximation of continuous real-valued maps on compact smooth manifolds. The relative theorem fixes an open neighborhood of a closed set when the given map is smooth on a neighborhood of that set. |
| `CornerScalars[n].On[M]` | Local extensions, compact cutoffs and finite partitions of unity on G03 manifolds with corners. The `Approximate` and `Euclidean[m].Approximate` entries give relative scalar and Euclidean approximation. |
| `Approximation.On.Euclidean[m].Of[f,continuous]` | Relative and absolute approximation in the Euclidean maximum norm. All coordinates share one fixed neighborhood. |
| `Retraction[m,k].On[M].Of[e]` | Smooth retraction of a G06 tubular image onto the embedded manifold. Approximation in `From[n].On[X,f,continuous]` applies to compact embedded targets and keeps the new graph in any given open neighborhood of the original graph. |
| `Retraction[m,k].On[M].Of[e].Corners[n].On[X,f,continuous]` | Relative approximation from a compact G03 source into a compact G06 embedded target. The approximant is a G03 smooth map, agrees with the original on a neighborhood of the protected closed set and stays in a prescribed graph-open window. |
| `Perturbation[n,m].On[U,f]` | Sard gives translations with a regular zero value. `Supported` multiplies the translation by a squared cutoff and preserves both the map and its derivative at cutoff zeros. `Relative` constructs the cutoff for a compact protected set and gives an arbitrary uniform error bound. |
| `CornerScalars.On.Euclidean[m].Protect[f,K,U,closed,open,included]` | An arbitrarily small Euclidean perturbation of a smooth map on a compact G03 source, tangentially regular at zero. The perturbation preserves a neighborhood of the protected closed set when zero is already tangentially regular on its given neighborhood. G07 boundary and face restrictions inherit regularity. |
| `LevelGeometry.Between.Of.Project[r].To[P].Of[projection]` | Dense parameters at which the differential of the level function is surjective on the kernel of the parameter differential. |
| `Parameters[n,r].Between[M,P].Of[projection].Relative` | Chooses a regular parameter of the level projection in a prescribed nonempty open set. The caller supplies the transfer from projection regularity to transversality away from the protected set. |
| `CornerParameters[n,m].Between[M,T].With[cover].Of[f,right].Window` | Chooses a value that is regular along the lineality of the source tangent cone and on the actual G03 boundary. |
| `CornerDerivative[n,m].Between.Of.At.InCharts` | Tangential surjectivity is equivalent to surjectivity on the active-coordinate tangent subspace for the Jacobian of any chart extension. |
| `FaceParameters[d,r,m].Between.Of.InChart` | One exceptional set controls regularity on every G03 global face of the indicated dimension and codimension. |
| `Normal.Between.Of` and `LevelGeometry[n,m].Between.Of` | The differential induces the normal quotient isomorphism. The tangent space of a regular preimage is identified with the kernel of the differential. |
| `LevelGeometry.Between.Of.SmoothTangent` | Smooth maps on total tangent spaces realize the inclusion into and the differential out of the ambient tangent bundle. Their fiberwise image and kernel agree over the regular level. |
| `Preimage[n,m,p].Between.Of` | A transverse preimage cut out by a smooth defining submersion is an embedded regular level. |
| `BoundaryLinear.On.Of` | Transversality along a face identifies the quotient of the preimage tangent by its boundary tangent with the boundary normal space. An outward vector can be lifted to the preimage tangent at the same height without changing the induced boundary form. |

The approximation proof averages local values with a finite smooth partition of unity. Near the protected set it averages copies of the original map. The supported perturbation applies Sard to the map divided by the cutoff square where the square is nonzero. The derivative of the square vanishes where the cutoff is zero.

## Remaining G08 results

Arbitrary-target approximation via a finite target-chart cover first needs a supported chart replacement that preserves the graph window and smoothness on previously treated regions. The open Euclidean target construction and compact-source graph control are available for that proof.

The Euclidean zero-level theorem applies to compact homotopy domains with corners. Extending it to general targets and transverse submanifolds first needs a family of perturbations that moves the defining coordinates independently near each intersection while keeping the protected region fixed. A local-chart route can restrict the family to each active stratum and apply the ordinary G07 parameter projection. That route also needs a small-perturbation stability lemma for transversality on previously treated compact regions if the chart replacements are made in sequence.

The normal and orientation comparisons are fiberwise. The smooth total-space tangent maps give the kernel comparison over a regular level. A bundle isomorphism with smooth inverse still requires smooth local trivializations of the kernel and quotient of the restricted differential.

## Verification

```sh
REF_TYPE_CHECKER=/workspace/ref-type-tools/v0.1.2/bin/cli \
  python3 scripts/check.py run --scope changed --package transversality --time-limit-seconds 420 --json
```

The published checker was `cli 0.1.2` with SHA-256 `2a435d8ad48acc8f1365d82433861c9a52f6650cc0c5ac1b9849a77cb8eda767`. Both runs used the inherited cache at `/workspace/ref-type-libs/libs/refcache` and the same input digest `ac05f9791e25204320a318491d7158f5e9011b0ee6c4782080d4c6aabd3bbc8b`.

| Run | Package targets | Referenced dependency modules | Wall time | Checker peak RSS |
| --- | ---: | ---: | ---: | ---: |
| Final source | 174 checked | 23 checked, 1,651 reused | 77.865 s | 4,589,036 KiB |
| Same input repeated | 174 reused | 1,674 reused | 19.754 s | 1,334,168 KiB |

The first run resumed one checkpoint. The repeated run reused all 1,848 verified modules. Both runs recorded zero input mismatches, cache corruption, save failures, lost or replayed steps, or checker recoveries. The environment recorded zero OOM events.

### Checker reproduction

The [module-instantiation reproducer](repro/README.md) records the exact adapter from the rejected run, the relocated-source retry, and a library-independent reduction with explicit-argument, direct-index and term-conversion controls. The verified level projection combines the G07 Sard theorem and its kernel transfer with the G02 regular-level tangent identification.

[Checking](../../USAGE.md) · [G08 requirements](../../../math/g08-transversality.md)
