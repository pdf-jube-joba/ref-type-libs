# `relative_k_theory` notes

[Package API](../../../libs/topology/relative_k_theory/README.md) · [Checking](../../../libs/USAGE.md)

## Construction

Compare bundle triples with reduced added-point-quotient K-groups for compact Hausdorff closed pairs.
Entry: `relative_k_theory.Relative`.
Exposes triple/quotient comparisons, negative exactness, excision, Mayer–Vietoris, external products, disk/sphere pairs.

### Groups and comparisons

`Pair` takes space `X`, topology `space`, compactness `compact`, Hausdorffness `hausdorff`, closed subspace `subset` and `closed`.
`Pair.Triple` is two projections and a subspace isomorphism; `Pair.Group` gives relations for extendible isomorphisms/sums/composites/homotopies.
`FromBundles`, `SumConstruction`, `Normalize` construct general presentations/sums/negative stable trivializations.

`Pair.Quotient` adds basepoints then collapses them with closed subspaces.
Includes empty subspaces.
`Pair.Comparison` gives additive triple/reduced comparisons and both inverses.
`Descent`, `FramedClass`, `FramedSum`, `BundleSwitch` construct boundary-framed descent, independence/additivity/stabilization/homotopy invariance.
`Pair.Mapping.Group` pulls triple groups back via comparisons, exposing addition/zero/comparison naturality.

### Negative degrees, exactness, and naturality

`Negative[original, degree]` defines negative degrees by iterated reduced suspensions.
`NegativeMap`, `PullbackIdentity`, `PullbackComposition`, `HomotopyInvariance` give pullback/identity/composition/homotopy laws.
`Absolute` compares added-point degree-zero groups with ordinary K.

`Pair.Augmented.Sequence[degree := n]` gives
\[
K^{-(n+1)}(X)\longrightarrow K^{-(n+1)}(A)\longrightarrow K^{-n}(X,A)
\longrightarrow K^{-n}(X)\longrightarrow K^{-n}(A)
\]
The four maps and image/kernel equality at every internal term are exposed.
`restrictionNegative`, `boundary`, `forget`, `restriction` are additive; `exactSecond`, `exactThird`, `exactFourth` give exactness.
`Pair.Augmented.OrdinaryEnd` compares degree-zero endpoints with ordinary forgetting/restriction.
`Pair.Mapping.Augmented.Negative` gives connecting/forgetting/restriction naturality for general closed-pair maps.
Foundational `PairIteration`, `PairMapping.Iteration` iterate pairs, constructing whole/subspace/quotient suspension comparisons and map compatibility.

### Excision and Mayer–Vietoris

`Pair.Excision` explicitly compares original quotients with pairs removing opens contained in closed subspaces.
Negative-degree comparison: `Excision.Negative`.
`Pair.ClosedCover[V, closedV, covers]` compares closed-cover quotients, treating open excision via complementary closed covers.

`ClosedCover.MayerVietoris[degree]` constructs connecting maps, piece restrictions, intersection differences.
`exactWhole` gives whole-group exactness; `Positive` the next two positions.
`MayerVietorisZero.exactPieces` glues degree-zero classes.
`ClosedCover.Mapping.Negative` exposes excision/restriction/difference/connecting naturality for cover-preserving maps.

Degree-zero gluing: `ClosedCover.Patching`.
Construct both rectangular maps from intersection isomorphisms; use B09 Tietze, invertible shears, closed-cover idempotent gluing, image bundles.
`Patching.Ordinary.existence` uses K01 stable criteria/virtual normal forms to return ordinary classes satisfying both restrictions.

### External products

`Smash` constructs compact Hausdorff quotients collapsing both product axes.
`Smash.External` uniquely lifts degree-zero products relatively, giving biadditivity/zero formulas.
`Smash.Suspension`, `Symmetry` and left/right iterative comparisons give negative products `Smash.Graded`.
Compare fibers on common compact representative spaces for homeomorphisms; prove naturality on actual representatives.

For two closed pairs use `Pair.Product`.
Boundary \(A\times Y\cup X\times B\) compares pair quotients with smash products of quotients.
`External` and `Negative[firstDegree, secondDegree]` give products via comparisons; `Pullback.External`, `Pullback.Negative` naturality.
Negative output degree: `secondDegree + firstDegree`.

### Disk and sphere bundles

`DiskPair[p]` constructs compact projection-model disks, closed norm-one boundaries, relative groups.
`BundleDisk.existence` presents arbitrary compact bundles.
`BundleDisk.With[r]` with chosen `r` exposes continuous injections/norm conditions; `OriginalUnit.homeomorphism` original-unit-disk homeomorphisms; `sphereEquation` sphere agreement.
Thus pass disk/sphere pairs to general sequences/products.

### General triples and pullbacks

`Pair.BundleTriples[F, G, firstModel, secondModel].With[alpha]` constructs triple-group `value` and relative `reduced` from arbitrary bundles isomorphic on closed subsets.
`agreement` agrees with finite projections.
`Framing.With.equation` proves independence of auxiliary complements trivializing negative bundles.
`To.With` compares changes by compatible bundle isomorphisms.

`Pair.Mapping.BundleTriples.With.naturality` and `reducedNaturality` give group/relative pullback compatibility.
`Pair.Mapping.Framed.With.naturality` gives the framed version.
Uses quotient descent, pullback composition, coordinate-frame compatibility.
`PullbackCongruence`, `RestrictedPullback`, `PairPullback` expose required isomorphisms/fiber formulas.
Also used for `compact_support_k` arbitrary-triple localization/naturality.

### Pointed quotients

`Relative.PointPair` exposes pointed equivalences between compact pointed spaces and quotients collapsing their basepoints.
Degree-zero triple comparisons use this independently of Bott periodicity.

## Examples

`Examples.TrivialDisk[n]` constructs point-trivial rank-`n` bundle coordinate homeomorphisms `diskHomeomorphism`.
Rank zero/one registered as check targets.

```ref
\import std.Data[].Nat[] \as Nat;
\import relative_k_theory.Relative[].Examples[] \as Examples;
\import Examples.TrivialDisk[n := Nat.Nat^::zero] \as Zero;
\import Examples.TrivialDisk[n := (Nat.Nat^::succ Nat.Nat^::zero)] \as Line;
```

`Zero.Disk`, `Line.Disk` are disks; `Zero.Relative`, `Line.Relative` corresponding groups.
`Examples.zeroBoundaryEmpty` proves rank-zero sphere boundaries empty.

## Historical validation

Recorded results in this section belong to the original combined repository.
See [validation records](../../../libs/USAGE.md#validation-records) for their scope and current rerun instructions.

Final 2026-10-28 workspace: 9,048 modules accepted, exit 0, cache save/write failures 0.
Checked 308 modules, reused 8,740 matching modules.
Includes K03, all dependencies, shared-lemma consumers, examples.
One worker; zero recoveries/duplicates/reruns/unsaved steps; roughly 1,384 seconds.
16 GiB physical limit; peak RSS 14,399,064 KiB.

Checked remote math commit: `ad55f6f4243e6bc060ec74ef48af363f7a23abc9`; tree: `3ecfdb61538c923656af74f55d283d3cf15de754`.
Preserves main `f8b80a154a3b61d2dccebd0ea13adc44bfaa4bdb` changes, updating Grassmannian separation references to relocated shared APIs.
Report: `work/k03-resume/workspace-audit-15.{log,json,exit}`; fixed input: `workspace-audit-12.source.json`.
Confirmed 7,942 input files match final math/manifests.
Earlier interrupted/resource-limit reports retained in the same directory.
