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
| `Proper.With.Cup.Degree` | Compatibility of proper pullback with cup products |
| `ProperIdentity.Degree` and `Proper.With.Then.Degree` | Identity and composition laws for proper pullback |
| `OpenEmbedding.With` | Linear extension by zero along an open embedding presented by a homeomorphism onto its image |
| `On.Excision.With` | Restriction to an open neighborhood of a compact support is an isomorphism |
| `On.Open.With.AtSupport` | Excision for an open subspace at a chosen compact support |
| `On.Open.With.Extension` | Extension by zero using inverse excision, with a representative formula |
| `On.Cup.Degree` | Cup product with coefficients in a commutative ring, with a bilinear map and a representative formula at the intersection of the supports |
| `External.Degree` | Bilinear external product with a representative formula at the product of the supports |
| `On.OpenCover` | Split each compact support into compact pieces in the two members of a Hausdorff open cover |
| `On.OpenCover.With` | Represent every compact-support class on a union of two supports subordinate to the cover |
| `On.OpenCover.Exteriors` | Compare relative cohomology of the union of the two exteriors with its small-chain model |
| `Homeomorphic.With.Isomorphism` | Mutually inverse proper pullbacks along a homeomorphism and its inverse |
| `On.Collar.With.Linear` | Compact-support comparison of an open complement with the cohomology of a compact pair admitting a collar deformation |
| `On.Collar.With.LongExact` | Long exact sequence of a compact collared pair, with arrow agreement for extension by zero and boundary pullback |
| `On.With.Supported.Compact.Cohomology` | Comparison with ordinary cohomology on a compact space |
| `RealBundle.With.Finite.With` | Disk/sphere-relative, reduced Thom-space, and total-space compact-support comparisons for a real vector bundle over a finite CW complex |
| `RealBundle.With.CompactBase.Cohomology` | Disk/sphere-relative, reduced Thom-space, and total-space compact-support comparisons over any compact Hausdorff base |
| `On.Exact.Between.With` | Exactness after taking direct limits of stagewise exact pairs |

For \(K\subseteq L\), the transition is pullback along the identity map of pairs from
\((X,X\setminus L)\) to \((X,X\setminus K)\). For a proper map \(f\), the
stage at \(K\) pulls back to the stage at \(f^{-1}(K)\). The proper pullback
descends because the two relative pullbacks in the square for \(K\subseteq L\)
compose to pullback by the same map of pairs.

For an open subspace of a Hausdorff space, extension by zero sends a class at
a compact support in the subspace to the inverse excision class at its image
in the ambient space. Their `Linear` modules expose the induced module maps.
The fixed-support comparison uses the complement of
the open subspace as the excised closed set. Naturality of restriction under
support enlargement also gives naturality of the inverse excision maps.

The cochain comparison sends a relative class to the class of its cochain on
the ambient space. Every supported cocycle lifts to a relative stage. A
supported primitive witnesses zero after enlarging to a compact support
containing both the original cocycle support and the primitive support.

For commutative ring coefficients the cup product is defined in nonnegative
degrees by the relative mixed cup product of C03 with its two-open-cover
comparison. Both support transitions commute with the product, which
gives a map of the direct-limit carriers in each pair of degrees. The
`bilinear` declarations package this same map with the two additivity and
two integer scalar laws. The external product uses C01 pullback along the
projections of the relative pairs.

The collar comparison enlarges each compact support by the projection of the
points in the compact cylinder that pass through that support. At the enlarged
support the collar motion is a relative homotopy, which proves the inverse law
on the direct limit. Exactness of stagewise sequences passes to the direct
limit by lifting a class from a stage where its image vanishes.

The collared-pair sequence transports the singular pair exact sequence
through the open-complement comparison and the ordinary-cohomology
comparisons on the compact ambient space and its closed boundary.
`extensionAgreement` and `nextExtensionAgreement` identify the inclusion
arrows with extension by zero. `restrictionAgreement` identifies the
restriction arrow with proper pullback along the boundary inclusion.

The bundle comparison combines the radial homeomorphism from the total space
to the open disk bundle with the C03 shell deformation and the reduced
Thom-space comparison. For a compact Hausdorff base, a bundle embedding
into a trivial bundle gives compactness of the disk of an induced metric.
The comparison of sphere bundles for two metrics and the mapping cylinder
of the sphere projection give compactness of the disk for the chosen metric.

For a two-member open cover of a Hausdorff space, the union of the two
compact pieces supplied by `split` is the original support. At a pair of
supports \(K,L\), the union of their open exteriors is the exterior of
\(K\cap L\), and the intersection of their exteriors is the exterior of
\(K\cup L\). The union comparison used here is C01's relative small-chain
comparison for arbitrary abelian coefficients.
The remaining Mayer–Vietoris work is to prove the relative short exact
sequence with the common exterior-vanishing term, descend its connecting
map through support enlargements, and transport filtered exactness to the
compact-support groups of the open sets and their intersection.

Run the package check from the repository root.

```sh
python3 scripts/check.py run --package compact_support_cohomology
```

[Sources](src/root.ref) · [Dependencies](ref.toml) · [C12 requirements](../../../math/c12-compact-support-cohomology.md)
