# `smooth_partitions`

Flat functions, compactly supported cutoffs, locally finite smooth partitions of unity, extension by zero and locally finite sums.

| Entry | Purpose |
| --- | --- |
| `Euclidean[n].LocalBump[a, q]` | Smooth functions one on maximum-norm \(B(a,q)\), supported in \(\overline B(a,2q)\), for positive \(q\) |
| `LocalBump.Support` | Support inclusion, compact closed balls/supports |
| `CompactCutoff[K, U].existsCutoff` | For compact \(K\subset U\), open \(U\), cutoffs one near \(K\), compactly supported in \(U\) |
| `Jets[f].allOrdersZero` | All partial families vanish off supports |
| `ZeroExtension[U, f].smooth` | Smooth zero extensions when extended support lies in \(U\) |
| `ZeroExtension.Closed[F].smooth` | Zero extension when vanishing off closed \(F\subset U\) |
| `LocallyFinite[f].Sum[local].smooth` | Smooth countable sums with finitely many surviving terms locally |
| `Manifold.On.Sections.Over.Open.ZeroExtension` | Smooth zero extension of sections in zero-preserving local frames |

[Source](src/root.ref) · [Dependencies](ref.toml) · [Checking](../../USAGE.md) · [Notes](../../../math/package-notes/geometry/smooth_partitions.md)
