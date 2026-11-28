# Parameter-level module instantiation in cli 0.1.2

The retry used a temporary export of commit `73e66e481e3188a4cc0da83c9c96f78b57c40687` with the [adapter patch](parameter-level.patch) applied. The patch reconstructs the failing adapter from the previous run's recorded source writes. The earlier whole-worktree digest and cache state are unavailable. This retry uses the final commit for files outside the adapter.

| Item | SHA-256 |
| --- | --- |
| Published `cli 0.1.2` | `2a435d8ad48acc8f1365d82433861c9a52f6650cc0c5ac1b9849a77cb8eda767` |
| Retry source inventory | `db47924e4bb57bce55e715eff49b5ac2345f81e8196d109fc67f6549462f01db` |
| Reconstructed `Level.ref` | `ce9b6f3cba3fdd7549d86ed9b3b2fb7baa6de088b411a8f03162a0949853534f` |
| Adapter patch | `9f5a7bacda71d84d07de2b631a3f1f4d420dbfc740edf9d6ad1cc7108d47eccb` |
| Standalone input | `cb2dbb7646f576eee958d4475ef348549994d197418a36f8ab2a85a557aae5b7` |

The inventory SHA hashes the relative filenames and content hashes of 14,496 files under `libs/`. It is computed from the exported directory with `find libs -type f \( -name '*.ref' -o -name ref.toml \) -print0 | sort -z | xargs -0 sha256sum | sha256sum`.

The single full-size retry command was run from `/workspace/ref-type-libs` on the temporary export.

```sh
REF_TYPE_CHECKER=/workspace/ref-type-tools/v0.1.2/bin/cli
"$REF_TYPE_CHECKER" /tmp/g08-level-retry.9plQTNa9/libs/geometry/transversality \
  --module transversality.Parameters.Between.Level --module-only \
  --cache-dir /workspace/ref-type-libs/libs/refcache --diagnostics detailed \
  --no-progress --time-limit-seconds 180 \
  --report-json /tmp/g08-level-retry.9plQTNa9/retry.json
```

The inherited cache contained 8,442,717,031 logical bytes, 16,438 artifact files, 16,438 input files, 12 checkpoint files, 113 instance files, 336,374 object files and zero lease files before the retry. The temporary source path yielded zero result hits, checkpoint resumptions, input mismatches, corruptions or save failures. The run rejected after 70.988 seconds with checker peak RSS 1,955,644 KiB and 1,018 referenced modules checked.

The diagnostic points to line 1 of `Parameters/Between/Level.ref`. The constraint compared the caller's instantiated `sard.Parameters[n := n, m := m, r := r].dimension` against the imported signature's uninstantiated `sard.Parameters.dimension`.

## Standalone reduction

Copy [the standalone input](parameter-level.ref.txt) to a temporary directory as `alias.ref`. It uses built-in syntax and has no library imports. The following commands check the same narrow entry point for the reproducer and three controls.

```sh
REF_TYPE_CHECKER=/workspace/ref-type-tools/v0.1.2/bin/cli
sed 's/import Lib\.Between/import \\root.Repro[].Library[n := n].Between/' alias.ref > explicit.ref
sed -e 's/n := dimension/n := n/' -e 's/n := Lib\.dimension/n := n/' alias.ref > inline-index.ref
sed -e 's/\\import Lib\.Between\[M := M\]\.Level\[\] \\as Value;/\\import \\root.Repro[].Models[n := n] \\as Direct;/' \
    -e 's/\\definition answer: Nat\^ := Value\.answer;/\\definition convertible: Direct.Model := M;/' alias.ref > convertible.ref
for file in alias explicit inline-index convertible; do
  "$REF_TYPE_CHECKER" "$file.ref" --module Repro.Caller.Between.Level --module-only \
    --diagnostics detailed --no-progress --time-limit-seconds 15
done
```

| Input | Result |
| --- | --- |
| `alias.ref` | Rejects the import at line 20 with the same rigid constraint. |
| `explicit.ref` | Rejects with the same constraint when the library module argument is explicit at the import site. |
| `inline-index.ref` | Accepts when both signatures use the index directly. |
| `convertible.ref` | Accepts the original aliased argument as a term of the directly indexed type. |

The term-level control verifies convertibility. The explicit-import control rules out a missing argument at the failing import site. The reduction demonstrates a v0.1.2 module-instantiation elaboration bug involving an index expressed through a definition in the imported module. It does not require Sard, a manifold, or a proof obligation.
