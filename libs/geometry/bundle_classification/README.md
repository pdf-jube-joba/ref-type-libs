# Bundle classifying maps and stabilization (B06)

Classify finite-rank real/complex bundles on compact Hausdorff spaces using finite-dimensional projection families.
Uses [B03](../bundle_complements/README.md) embeddings/image projections, [B04](../bundle_homotopy/README.md) homotopy invariance, [B05](../grassmannians/README.md) finite Grassmannians/universal bundles.
No new axioms added.

## Classifying maps

Entry: `Classification`.
`Over` is shared across real/complex cases, with scalar arguments as in existing `vector_bundles`.

| API | Contents |
| --- | --- |
| `Over.For.AtRank.exists` | Finite classification data/comparison isomorphisms from compact Hausdorffness and rank-\(k\) evidence |
| `Real.From` / `Complex.From` | Continuous maps to B05 `Model.Carrier` and universal-pullback isomorphisms from classification data |
| `Over.For.Graded.exists` / `From` | Classifying maps for componentwise varying ranks |
| `Over.ProjectionSpace` | All-rank orthogonal projection space in one finite-dimensional space and universal image bundle |
| `RealGeometry.Finite` / `ComplexGeometry.Finite` | Projection presentations from continuous Grassmannian maps |
| `RealGeometry.Between` / `ComplexGeometry.Between` | Stabilization homotopies in fixed-rank finite Grassmannians from isomorphic rank-\(k\) images |

`AtRank.HasRank` requires \(k\)-dimensional fibers, without continuous global frames.
For varying ranks use `Graded`.
Uses all-rank finite-dimensional projections; constant ranks map into B05 Grassmannians.

## Choice independence and bijections

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
`leftInverse`, `rightInverse` prove both round trips.
`On.Compact.For.classification` and `classCriterion` give isomorphism criteria independent of classifying-map/embedding choices.

## Oriented and framed bundles

`Oriented` treats open positive rays in real determinant cotangent lines \(\Lambda^k E^*\) as orientations.
`Orientations.Laws` includes nonvanishing, fiberwise existence, sign separation, positive scaling, and same-ray conditions.
`Oriented.For.With.exists` transports orientations to classified projection images and returns orientation-preserving comparisons.
`With.Compare.independent` proves classification-choice independence.

`Oriented.On.Compact.Between.Homotopy` consists of constant-rank projection homotopies, continuous cylinder orientations, and agreement with standard zero-padded endpoints.
`criterion` equates such homotopies with oriented bundle isomorphism existence.
`Classes` and `BundleClasses` bijections have `toBundles`, `fromBundles` and both inverse proofs as for ordinary bundles.
Orientation invariance uses B04 cylinder isomorphisms and `Orientations.Path.endpoints` sign constancy along nonzero determinant-covector paths.

`Over.Frames[n, k]` is the finite Stiefel space of \(k\) independent columns.
`Over.Framed.For` constructs continuous maps from globally framed bundles and frame-preserving comparisons.
`Framed.Between.concordance`, `homotopy`, `leftFormula`, `rightFormula` give stabilized homotopies between arbitrary frame families; `preservesFrame` proves frame preservation.
Globally framed rank-\(k\) isomorphism classes and stable Stiefel homotopy classes are both singleton; `Framed.uniqueClass` proves the latter.

## Naturality and examples

- Ordinary classification: `On.Compact.Pullback`, `On.Compact.Hausdorff.Sum.naturality`, `Hausdorff.Stabilization.For.naturality` give pullback/sum/trivial-addition compatibility.
- Oriented pullback: `Oriented.On.Pullback` and `Oriented.On.Compact.Pullback` also transport determinant rays.
- Framed classification: `Framed.Pullback`, `FrameSum`, `FrameStabilization` construct frame composition, block sums, identity-frame addition.
- B05 `Model.DirectSum` and `Model.Stabilization` also provide continuous Grassmannian sums/ambient/rank stabilization and universal comparisons.

`Framed.For.class` exposes framed classification classes; `classification` and `independent` prove finite embedded presentations give the same classes.
Finite-presentation comparisons/frame preservation remain in `For.FromEmbedding.isomorphism` and `preservesFrame`.
`Framed.Addition.add` descends `FrameSum.presentation` sums to quotients; `onClasses` proves finite-matrix agreement.
`Framed.Addition.For.naturality`, `Framed.Stabilization.For.naturality`, `Framed.For.Pullback.naturality` give compatibility from bundle classes to finite presentations.
Singleton framed classes use existing `uniqueClass` to prove quotient maps well-defined.

`Oriented.WhitneySum` constructs standard sum orientation `orientation` from orientations of rank-\(k,l\) real factors.
Factor orientations are inputs; the sum orientation is constructed.
No compact base or global frame required.
`Oriented.Trivial.orientation` is the standard normalized-top-form orientation; `Oriented.StandardStabilization.orientation` adds this oriented trivial bundle.
Rank zero uses the same definitions/proofs.

Finite-dimensional `DeterminantProduct.product` constructs the unique top form from \(\alpha\in\Lambda^k E^*\), \(\beta\in\Lambda^l F^*\) satisfying
\[
 (\alpha\mathbin{\boxtimes}\beta)((u_1,0),\ldots,(u_k,0),(0,v_1),\ldots,(0,v_l))
 =\alpha(u_1,\ldots,u_k)\,\beta(v_1,\ldots,v_l)
\]
Existence/uniqueness uses existing `FiniteCoordinates.Top` normalization, one-dimensionality, and argument-restriction lemmas.
`independent` gives basis independence; `Laws` bilinearity/nonvanishing; `Mapping.naturality` linear-pullback compatibility.
`Blocks.blockDeterminant` proves normalized-top-form determinants of block diagonals equal factor determinant products.

Sum positive rays are products of positive factor forms.
`WhitneySum.Open.open` extends positive local forms in rank-compatible trivializations, gluing positive open rays from continuous coefficient products to prove openness.
Prove nonvanishing, fiberwise existence, sign separation, positive scaling, same-ray conditions to construct `Orientations.Orientation`.
`WhitneySum.Pairing.continuous` proves this bilinear product continuous on the determinant-bundle fiber product.
Local top-form coordinates equal basis evaluation; product coordinates multiply continuous coefficients.

| API | Standard product-orientation compatibility |
| --- | --- |
| `WhitneySum.Mapping.With.preserves` | Sums of factor-orientation-preserving isomorphisms preserve constructed product orientations |
| `WhitneySum.Pullback.naturality` | Products of pulled-back orientations equal pullbacks of products under canonical comparisons |
| `WhitneySum.Classifying.WithSum.naturality` / `homotopy` | Classify factors then sum agrees in class with classifying oriented sums, joined by actual oriented homotopies |
| `Classifying.WithSum.Changing.independent` / `ChangingSource.independent` | Independence of factor/sum finite-classification choices |
| `StandardStabilization.Classifying.WithSum.naturality` / `homotopy` | Standard oriented-trivial addition commutes with classification |

`WhitneySum.classificationExists` and `StandardStabilization.classificationExists` also expose existence of needed finite data on compact Hausdorff bases.

`Oriented.Sum.With` takes two ordinary finite classifications, a determinant orientation of the original sum, and classification data for that sum.
Construct comparison `Sum.comparison` to the sum of classified factors; `targetOrientation` transports the supplied orientation.
`determinantNaturality`, `isomorphism`, `naturality` expose determinant equalities, oriented isomorphisms, and class equalities for transport/classification compatibility.
Orientation preservation is not an input assumption.
`With.Changing.independent` proves classes unchanged when factor classification data change.
`Oriented.Stabilization.With.naturality` gives the same comparison for trivial-bundle addition.
These APIs take orientations of the entire sum.
Use `WhitneySum` and `StandardStabilization` above to construct standard product orientations.

[Minimal examples](src/Classification/Examples/BoolLine.ref) classify real lines on discrete two-point spaces.
[Trivial examples](src/Classification/Examples/Trivial.ref) check finite classifying maps, universal comparisons, and stabilized frame homotopies for arbitrary bases/dimensions.
Their `Naturality.sumNaturality` and `stabilizationNaturality` exemplify sum/stabilization naturality of framed classification.
`Naturality.Oriented.volumePositive`, `sumNaturality`, `stabilizationNaturality` exemplify the same compatibility for standard oriented trivial bundles.

```ref
\import bundle_classification.Classification[].Examples[].BoolLine[] \as Example;
```
