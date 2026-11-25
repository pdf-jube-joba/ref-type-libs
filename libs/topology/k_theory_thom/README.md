# Thom classes in complex K-theory

Continuous complex bundles on compact Hausdorff spaces.
Entry: `Thom[].For[X, F, bundle, compact, hausdorff]`.
`thom` lies in total-space \(K^0_c(E)\); `forward` multiplies it by base coefficients.

## Koszul complexes

`Koszul` constructs pulled-back dual exterior algebras \(\Lambda^k\pi^*E^*\) and contraction by tautological sections.
`Contraction` and `Algebra` handle degreewise contraction, square zero, graded wedge Leibniz, Cartan relations.
Continuity uses existing `bundle_operations` exterior/dual/tensor universality.

Off zero sections, wedge with covectors evaluating one gives contractions.
Compact-base uniform rank bounds package complexes as finite parity complexes.
`Finite`, `RelativeComplex`, `For.Using[data]` send actual finite complexes to K10 compact-support classes.
`For.Choices`, `For.Bounds`, `For.ChoicesAny` prove coordinate/truncation independence.
Define `For.thom` as the unique class represented by these complexes.

## Public API

| API | Contents |
| --- | --- |
| `For.thom` / `For.forward` / `For.additive` | Canonical Koszul classes and additive multiplication maps |
| `For.Isomorphism.data` | Thom maps/inverses, both inverse laws/additivity |
| `For.ThomPullback.equation` / `forwardNaturality` | Compatibility with continuous base pullbacks |
| `For.BundleIsomorphism.equation` / `forwardNaturality` | Proper pullback induced by actual isomorphisms, Thom-class comparison |
| `For.Proofs.equation` / `forwardAgreement` | Independence of compactness/Hausdorff proofs |
| `FiberMultiply.multiply` | Products on totals of bundles over common bases |
| `KoszulProduct.equation` | Sum Koszul classes equal products |
| `DirectSumIsomorphism.data` / `composition` | Sum Thom isomorphisms, composition from bases |
| `FiberAssociativity.associativity` / `associationEquivalence` | Triple-product comparisons along sum associators |
| `TrivialThom` / `TrivializedThom` | Trivial/trivialized bundles, external presentations with point bundles |
| `Complexification.Compact.Isomorphism.data` | Canonical complex Thom orientations on real complexifications |

`BundleIsomorphism` explicitly takes target compactness/Hausdorffness too.
Prove total pullbacks proper, using actual compactification maps.

## Bott classes and isomorphism proofs

`Isomorphism.Point[n]` exposes point-trivial complex \(n\)-bundles and actual Koszul classes.
Rank-zero classes equal \(S^0\) units.
For complex lines, compute parity boundary maps in standard coordinates; compare circle-clutching Bott classes.
`Isomorphism.BottExternal[base, n]` gives external-product isomorphisms with point Koszul classes for arbitrary compact pointed spaces.

Sum comparisons transfer exterior degree decomposition/signed contraction to continuous tensors/finite parity sums.
`MetricFoldClass` constructs actual metric contractions and K10 local presentations.
Metric/complement stabilization, quotient descent, and Clifford comparisons identify canonical Koszul classes with external products.

General isomorphisms use finite trivial embeddings from local triviality/compactness and orthogonal complements.
Trivialize complementary sums, transfer to Bott, then use double stabilization/associators for both Thom inverses.
`Cancellation` supplies map cancellation for the final inverse law.
`For.Isomorphism` selects unique preimages, independent of embedding/complement choices.

`Complexification` applies existing continuous complexifications to real bundles, returning complex Koszul classes/Thom isomorphisms.

## Checks

Full APIs, K10/B07/G04/A04 regressions, and standard full-repository checks accepted.
