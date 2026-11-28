# `compact_support_cohomology`

For a space \(X\) and an abelian coefficient module \(M\), the package constructs
\[
H_c^z(X;M)=\varinjlim_{K\subseteq X\text{ compact}} H^z(X,X\setminus K;M).
\]
The construction uses all compact subsets and applies in particular to locally compact Hausdorff spaces. The degree \(z\) is an integer.

| Entry | Purpose |
| --- | --- |
| `On` | Compact supports, empty and whole supports, finite union, and reversal of inclusion on complements |
| `On.With.Degree` | Relative cohomology at each support, transitions, their identity and composition laws, and the direct limit |
| `Directed.System.With` | Common-stage equality of representatives, elimination on representatives, and compatibility with the structure maps |
| `On.With.Degree.Descend` | Factor a compatible family of maps out of the stages through the direct limit |
| `On.With.Degree.Compact` | Compare the direct limit with its terminal stage at the whole support |
| `Proper.With.WithCoefficients` | Pull back along a continuous map with compact inverse images of compact sets, with a representative formula |
| `On.Excision.With` | Restriction to an open neighborhood of a compact support is an isomorphism |
| `On.Open.With.AtSupport` | Excision for an open subspace at a chosen compact support |
| `On.Open.With.Extension` | Extension by zero using inverse excision, with a representative formula |

For \(K\subseteq L\), the transition is pullback along the identity map of pairs from
\((X,X\setminus L)\) to \((X,X\setminus K)\). For a proper map \(f\), the
stage at \(K\) pulls back to the stage at \(f^{-1}(K)\). The proper pullback
descends because the two relative pullbacks in the square for \(K\subseteq L\)
compose to pullback by the same map of pairs.

For an open subspace of a Hausdorff space, extension by zero sends a class at
a compact support in the subspace to the inverse excision class at its image
in the ambient space. The fixed-support comparison uses the complement of
the open subspace as the excised closed set. Naturality of restriction under
support enlargement also gives naturality of the inverse excision maps.

Run the package check from the repository root.

```sh
python3 scripts/check.py run --package compact_support_cohomology
```

[Sources](src/root.ref) · [Dependencies](ref.toml) · [C12 requirements](../../../math/c12-compact-support-cohomology.md)
