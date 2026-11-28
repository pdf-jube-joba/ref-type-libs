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
| `On.With.Degree.Module` | Abelian group operations on the direct limit and linear structure maps from the relative stages |
| `On.With.Supported` | Subcomplex of singular cochains vanishing off some compact support |
| `On.With.Supported.Vanishing` | Characterization of the support predicate by vanishing on the relative subspace |
| `On.With.Supported.Comparison` | Linear isomorphism from the direct limit to cohomology of the supported cochain complex |
| `Proper.With.WithCoefficients` | Pull back along a continuous map with compact inverse images of compact sets, with a representative formula |
| `On.Excision.With` | Restriction to an open neighborhood of a compact support is an isomorphism |
| `On.Open.With.AtSupport` | Excision for an open subspace at a chosen compact support |
| `On.Open.With.Extension` | Extension by zero using inverse excision, with a representative formula |
| `On.Cup.Degree` | Cup product with coefficients in a commutative ring, with a representative formula at the intersection of the supports |
| `External.Degree` | External product with a representative formula at the product of the supports |
| `Homeomorphic.With.Isomorphism` | Mutually inverse proper pullbacks along a homeomorphism and its inverse |
| `On.Collar.With.Linear` | Compact-support comparison of an open complement with the cohomology of a compact pair admitting a collar deformation |
| `On.Exact.Between.With` | Exactness after taking direct limits of stagewise exact pairs |

For \(K\subseteq L\), the transition is pullback along the identity map of pairs from
\((X,X\setminus L)\) to \((X,X\setminus K)\). For a proper map \(f\), the
stage at \(K\) pulls back to the stage at \(f^{-1}(K)\). The proper pullback
descends because the two relative pullbacks in the square for \(K\subseteq L\)
compose to pullback by the same map of pairs.

For an open subspace of a Hausdorff space, extension by zero sends a class at
a compact support in the subspace to the inverse excision class at its image
in the ambient space. Both proper pullback and extension by zero expose linear maps through their `Linear` modules. The fixed-support comparison uses the complement of
the open subspace as the excised closed set. Naturality of restriction under
support enlargement also gives naturality of the inverse excision maps.

The cochain comparison sends a relative class to the class of its cochain on
the ambient space. Every supported cocycle lifts to a relative stage. A
supported primitive witnesses zero after enlarging to a compact support
containing both the original cocycle support and the primitive support.

For commutative ring coefficients the cup product is defined in nonnegative
degrees by the relative mixed cup product of C03 with its two-open-cover
comparison. Both support transitions commute with the product, which
gives a map of the direct-limit carriers in each pair of degrees. The external
product also uses C01 pullback along the projections of the relative pairs.

The collar comparison enlarges each compact support by the projection of the
points in the compact cylinder that pass through that support. At the enlarged
support the collar motion is a relative homotopy, which proves the inverse law
on the direct limit. Exactness of stagewise sequences passes to the direct
limit by lifting a class from a stage where its image vanishes.

Run the package check from the repository root.

```sh
python3 scripts/check.py run --package compact_support_cohomology
```

[Sources](src/root.ref) · [Dependencies](ref.toml) · [C12 requirements](../../../math/c12-compact-support-cohomology.md)
