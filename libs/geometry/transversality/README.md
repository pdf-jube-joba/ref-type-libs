# Smooth approximation and transversality

| Entry | Result |
| --- | --- |
| `Approximation[n].On[M].Of[f,continuous]` | Uniform smooth approximation of continuous real-valued maps on compact smooth manifolds. The relative theorem fixes an open neighborhood of a closed set when the given map is smooth on a neighborhood of that set. |
| `Approximation.On.Euclidean[m].Of[f,continuous]` | Relative and absolute approximation in the Euclidean maximum norm. All coordinates share one fixed neighborhood. |
| `Retraction[m,k].On[M].Of[e]` | Smooth retraction of a G06 tubular image onto the embedded manifold. Approximation in `From[n].On[X,f,continuous]` applies to compact embedded targets and keeps the new graph in any given open neighborhood of the original graph. |
| `Perturbation[n,m].On[U,f]` | Sard gives translations with a regular zero value. `Supported` multiplies the translation by a squared cutoff and preserves both the map and its derivative at cutoff zeros. `Relative` constructs the cutoff for a compact protected set and gives an arbitrary uniform error bound. |
| `LevelGeometry.Between.Of.Project[r].To[P].Of[projection]` | Dense parameters at which the differential of the level function is surjective on the kernel of the parameter differential. |
| `Parameters[n,r].Between[M,P].Of[projection].Relative` | Chooses a regular parameter of the level projection in a prescribed nonempty open set. The caller supplies the transfer from projection regularity to transversality away from the protected set. |
| `CornerParameters[n,m].Between[M,T].With[cover].Of[f,right].Window` | Chooses a value that is regular along the lineality of the source tangent cone and on the actual G03 boundary. |
| `FaceParameters[d,r,m].Between.Of.InChart` | One exceptional set controls regularity on every G03 global face of the indicated dimension and codimension. |
| `Normal.Between.Of` and `LevelGeometry[n,m].Between.Of` | The differential induces the normal quotient isomorphism. The tangent space of a regular preimage is identified with the kernel of the differential. |
| `Preimage[n,m,p].Between.Of` | A transverse preimage cut out by a smooth defining submersion is an embedded regular level. |
| `BoundaryLinear.On.Of` | Transversality along a face identifies the quotient of the preimage tangent by its boundary tangent with the boundary normal space. An outward vector can be lifted to the preimage tangent at the same height without changing the induced boundary form. |

The approximation proof averages local values with a finite smooth partition of unity. Near the protected set it averages copies of the original map. The supported perturbation applies Sard to the map divided by the cutoff square where the square is nonzero. The derivative of the square vanishes where the cutoff is zero.

Remaining G08 work includes approximation for arbitrary manifold targets from compact domains, global relative perturbation of homotopies with boundary and corners, and smooth bundle comparisons on general transverse preimages. The tangent, normal and orientation comparisons here are fiberwise.

## Verification

```sh
REF_TYPE_CHECKER=/workspace/ref-type-tools/v0.1.2/bin/cli \
  python3 scripts/check.py run --scope changed --package transversality --time-limit-seconds 420 --json
```

The published checker was `cli 0.1.2` with SHA-256 `2a435d8ad48acc8f1365d82433861c9a52f6650cc0c5ac1b9849a77cb8eda767`. Both runs used the inherited cache at `/workspace/ref-type-libs/libs/refcache`. The input digest was `40cee5945b8f2dbe84882be2700cfbab9388deccc125fc449787b4e9bb3f183a`.

| Run | Package modules | Referenced dependency modules | Wall time | Checker peak RSS |
| --- | ---: | ---: | ---: | ---: |
| After the final source edits | 88 checked | 1,641 reused | 52.2 s | 4,407,144 KiB |
| Same input repeated | 88 reused | 1,641 reused | 19.2 s | 1,321,548 KiB |

The first run resumed one checkpoint and recorded one input mismatch. The repeat recorded zero input mismatches. Both runs reported zero cache corruption and save failures, zero lost or replayed steps, and zero checker recoveries. The environment recorded zero OOM events.

### Checker diagnostic during development

An external import of `sard.Parameters[n := n, m := m, r := r].Between[…].Level[…]` was rejected with `incompatible rigid expressions in metavariable constraint`. Detailed output compared `sard.Parameters[…].dimension` from the caller against uninstantiated `sard.Parameters.dimension` from the imported signature. The reduced module-only run reproduced the rejection after 20.339 seconds at 2,752,012 KiB peak RSS. The final projection proof combines Sard's regular-value theorem and kernel transfer with the G02 regular-level tangent identification.

The command below targeted the temporary adapter before that adapter was replaced.

```sh
REF_TYPE_CHECKER=/workspace/ref-type-tools/v0.1.2/bin/cli
"$REF_TYPE_CHECKER" /workspace/ref-type-libs/libs/geometry/transversality \
  --module transversality.Parameters.Between.Level --module-only \
  --cache-dir /workspace/ref-type-libs/libs/refcache --diagnostics detailed \
  --no-progress --time-limit-seconds 180 --report-json /tmp/g08-param-detailed2.json
```

[Checking](../../USAGE.md) · [G08 requirements](../../../math/g08-transversality.md)
