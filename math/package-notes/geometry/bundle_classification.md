# `bundle_classification` notes

[Package API](../../../libs/geometry/bundle_classification/README.md) · [Checking](../../../libs/USAGE.md)

## Construction

Classify finite-rank real/complex bundles on compact Hausdorff spaces using finite-dimensional projection families.
Uses [B03](../../../libs/geometry/bundle_complements/README.md) embeddings/image projections, [B04](../../../libs/geometry/bundle_homotopy/README.md) homotopy invariance, [B05](../../../libs/geometry/grassmannians/README.md) finite Grassmannians/universal bundles.
No new axioms added.

### Classifying maps

Entry: `Classification`.
`Over` is shared across real/complex cases, with scalar arguments as in existing `vector_bundles`.

`AtRank.HasRank` requires \(k\)-dimensional fibers, without continuous global frames.

### Choice independence and bijections

`Over.On[X, baseSpace].Between[p, q].Witness` enlarges ambient dimension to the sum of both presentations and joins zero-padded left-block \(p\) to right-block \(q\) by continuous projection homotopies.
`Witness.start` and `end` state actual projection-matrix equalities.
Bundle isomorphisms do not define the relation.

Given an isomorphism, join embeddings by
\[
 v\longmapsto ((1-t)e(v),t f(v))
\]
and project orthogonally onto the images.
Coefficients sum to one, ensuring injectivity at every time.
The converse uses B04 projection-family homotopy invariance.
Thus `On.Compact.criterion` equates stabilization homotopies with bundle isomorphism existence.
This differs from fixed-ambient finite-stage classification or identifying bundles by stable isomorphism.

`On.Compact.toBundles` and `fromBundles` biject stabilized homotopy classes with B03 bundle isomorphism classes.
`On.Compact.For.classification` and `classCriterion` give isomorphism criteria independent of classifying-map/embedding choices.

### Oriented and framed bundles

`Oriented` treats open positive rays in real determinant cotangent lines \(\Lambda^k E^*\) as orientations.
`Orientations.Laws` includes nonvanishing, fiberwise existence, sign separation, positive scaling, and same-ray conditions.
`Oriented.For.With.exists` transports orientations to classified projection images and returns orientation-preserving comparisons.
`With.Compare.independent` proves classification-choice independence.

`Oriented.On.Compact.Between.Homotopy` consists of constant-rank projection homotopies, continuous cylinder orientations, and agreement with standard zero-padded endpoints.
`criterion` equates such homotopies with oriented bundle isomorphism existence.
`Classes` and `BundleClasses` have the same `toBundles`/`fromBundles` bijection API.
Orientation invariance uses B04 cylinder isomorphisms and `Orientations.Path.endpoints` sign constancy along nonzero determinant-covector paths.

`Over.Frames[n, k]` is the finite Stiefel space of \(k\) independent columns.
`Over.Framed.For` constructs continuous maps from globally framed bundles and frame-preserving comparisons.
`Framed.Between.concordance`, `homotopy`, `leftFormula`, `rightFormula` give stabilized homotopies between arbitrary frame families; `preservesFrame` proves frame preservation.
Globally framed rank-\(k\) isomorphism classes and stable Stiefel homotopy classes are both singleton; `Framed.uniqueClass` proves the latter.

### Naturality

- Ordinary classification: `On.Compact.Pullback`, `On.Compact.Hausdorff.Sum.naturality`, `Hausdorff.Stabilization.For.naturality` give pullback/sum/trivial-addition compatibility.
- Oriented pullback: `Oriented.On.Pullback` and `Oriented.On.Compact.Pullback` also transport determinant rays.
- Framed classification: `Framed.Pullback`, `FrameSum`, `FrameStabilization` construct frame composition, block sums, identity-frame addition.
- B05 `Model.DirectSum` and `Model.Stabilization` also provide continuous Grassmannian sums/ambient/rank stabilization and universal comparisons.

`Framed.For` exposes `class`, `classification`, and `independent`; `FromEmbedding.isomorphism` and `preservesFrame` compare finite presentations.
`Framed.Addition.add` descends `FrameSum.presentation` sums to quotients; `onClasses` proves finite-matrix agreement.
`Framed.Addition.For.naturality`, `Framed.Stabilization.For.naturality`, `Framed.For.Pullback.naturality` give compatibility from bundle classes to finite presentations.

`Oriented.WhitneySum.orientation` constructs the product orientation from rank-\(k,l\) factor orientations, without compactness or global frames, including rank zero.
`Oriented.Trivial.orientation` uses normalized top forms; `Oriented.StandardStabilization.orientation` adds this oriented trivial bundle.

Finite-dimensional `DeterminantProduct.product` constructs the unique top form from \(\alpha\in\Lambda^k E^*\), \(\beta\in\Lambda^l F^*\) satisfying
\[
 (\alpha\mathbin{\boxtimes}\beta)((u_1,0),\ldots,(u_k,0),(0,v_1),\ldots,(0,v_l))
 =\alpha(u_1,\ldots,u_k)\,\beta(v_1,\ldots,v_l)
\]
`independent` gives basis independence; `Laws` bilinearity/nonvanishing; `Mapping.naturality` linear-pullback compatibility.
`Blocks.blockDeterminant` proves normalized-top-form determinants of block diagonals equal factor determinant products.

`WhitneySum.Open.open` proves product rays open; `WhitneySum.Pairing.continuous` gives continuity on the determinant-bundle fiber product.

`WhitneySum.classificationExists` and `StandardStabilization.classificationExists` also expose existence of needed finite data on compact Hausdorff bases.

`Oriented.Sum.With` takes two ordinary finite classifications, a determinant orientation of the original sum, and classification data for that sum.
Construct comparison `Sum.comparison` to the sum of classified factors; `targetOrientation` transports the supplied orientation.
`determinantNaturality`, `isomorphism`, `naturality` expose determinant equalities, oriented isomorphisms, and class equalities for transport/classification compatibility.
Orientation preservation is derived. `With.Changing.independent` handles changes of factor classifications; `Oriented.Stabilization.With.naturality` handles trivial addition.
These transport a supplied whole-sum orientation; `WhitneySum` and `StandardStabilization` construct standard product orientations.

## Examples

[Minimal examples](../../../libs/geometry/bundle_classification/src/Classification/Examples/BoolLine.ref) classify real lines on discrete two-point spaces.
[Trivial examples](../../../libs/geometry/bundle_classification/src/Classification/Examples/Trivial.ref) check finite classifying maps, universal comparisons, and stabilized frame homotopies for arbitrary bases/dimensions.
Their `Naturality.sumNaturality` and `stabilizationNaturality` exemplify sum/stabilization naturality of framed classification.
`Naturality.Oriented.volumePositive`, `sumNaturality`, `stabilizationNaturality` exemplify the same compatibility for standard oriented trivial bundles.

```ref
\import bundle_classification.Classification[].Examples[].BoolLine[] \as Example;
```
