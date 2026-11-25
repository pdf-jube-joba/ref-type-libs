# Operations in relative Thom cohomology

Construction details and records for [cohomology_thom](../../../libs/topology/cohomology_thom/README.md).
See [building and checking](../../../libs/USAGE.md) for current commands.
The API overview is maintained in the package README; recorded checks describe earlier runs.

`Thom.Real.For[X, F, bundle].With[metric]` uses disk/sphere pairs of real metric bundles.
`Coefficients[R, ring]` takes commutative-ring coefficients; `Additive[M]` integer-module coefficients.

`Thom.StandardFiber[n].With[M]` identifies top cohomology of standard real \(n+1\) disk/sphere pairs with coefficients.
`lift` and `coordinate` are linear maps both ways; `unique` proves specified-coordinate uniqueness.
`Integral.generator` is the coordinate-one integral class; `reverseCoordinate` computes its negative.

`Thom.Real.For.Change[left, right].Additive[M, z].isomorphism` gives relative isomorphisms from metric-change disk homeomorphisms preserving sphere boundaries.

`RelativeMayerVietoris.OpenCover[A, source, subset].On[cover].Cohomology[coefficients].At[z]` gives relative-singular Mayer–Vietoris for open covers.
Exposes `restriction`, `difference`, `connecting` and termwise `exactAtSum`, `exactAtIntersection`, `exactAtWhole`.
Free bases of simplices outside boundaries construct split small-relative-chain short exact sequences.
Apply Hom into arbitrary integer modules; compare small chains/direct sums, transferring to ordinary relative cohomology.

`Cohomology.Gluing[z]` proves compatible local classes glue; when preceding intersection groups vanish, constructs unique `glue`.
`Thom.Real.For.With.ChangeCoefficients[M, N, u].Degree[z].map` changes coefficient modules; `Fiber[x, z].law` proves fiber-restriction naturality.
`CoefficientChange.On[C, M, N, u].Along[D, f].At[z].law` gives general chain-map naturality.

`Thom.Real.For.With.ZeroRank[rankZero].Ring[R, ring]` constructs rank-zero Thom class `class`.
`Degree[p].isomorphism` maps \(a\mapsto\pi^*a\smile u\) forward, zero-section pullback backward.
`euler` proves this Euler class is the unit.
`ZeroRank.With[M, z].isomorphism` compares with base cohomology in arbitrary integer coefficients/degrees.

`RelativeSuspension.On[A, source, subset].Covering.With[M].At[z].isomorphism` is the degree-one shift for cylinder-pair
\((I\times A,\partial I\times A\cup I\times B)\) relative cohomology.

`LocalDisk.On[X, source].With[M].isomorphism n z` gives \(H^z(X;M)\cong H^{\operatorname{shift}(n,z)}(X\times D^n,X\times\partial D^n;M)\).
`shift` applies integer successor \(n\) times.
`With.Negative[n, k].zero` proves vanishing of relative groups from negative base degrees.
`Ring[R, ring].Rank[n].localClass` is the additive-comparison image of units; `coordinateOfClass`, `unique` characterize normalization.

`RelativePullback.On.To.Along.Cup.Cohomology.naturality` gives relative cup naturality for pair maps.
`Thom.Real.For.With.Pullback[Y, source, f, regular].Ring[R, ring]` uses pullback bundles/metrics.
`Product[p, n].law` and `Degree[n].Euler.law` give pullback compatibility for products/zero-section images.

`RelativeMayerVietoris.OpenCover.On.With.Coordinates.Cohomology[z].law` identifies sequence restrictions with ordinary pair-map restrictions.
`Coordinates.Difference[z].law` identifies the next map with difference of intersection restrictions.
`Cohomology.Gluing[z].Ordinary` uniquely glues ordinarily compatible local classes when preceding intersection groups vanish, exposing `left`, `right`, `unique`.

`CoefficientChange.OnSpace[A, source, R, S, ring, targetRing].Morphism` is an integer-linear unital multiplicative coefficient homomorphism.
`With[morphism].Cup.Cohomology.law` and `Relative[subset].Cup.Cohomology.law` prove absolute/relative cup compatibility.
`Unit.law`, `Along.Degree.law`, `Relative.Degree.Forget.law` give unit, space-pullback, relative-forgetting compatibility.
`RelativeMayerVietoris.OpenCover.On.ChangeCoefficients.At.law` and `RelativeSuspension.On.Covering.ChangeCoefficients.At.law` give coefficient naturality of connecting/suspension maps.

`RelativeMayerVietoris.OpenCover.On.Product[K, ring].Cup[p, q]` constructs cups on small relative cochains.
Its `Compare.law` agrees with ordinary restrictions; `Differential.law` gives signed Leibniz for closed left factors.
`Product.Positive[p, q]` descends to cohomology for positive right degrees.
`Product.Connecting[p, q].Whole.law` gives ordinary relative Mayer–Vietoris \(\delta(a|_{U\cap V}\smile b)=(-1)^p a\smile\delta b\).

`RelativeSuspension.On.Covering.Product[K, ring].Cup[p, q].law` gives signed suspension/cup comparisons.
`LocalDisk.On.Step[n].Product[K, ring, p, q].Base.onClasses` compares disk degree raising with base pullbacks.

`LocalDisk.On[X, source].Ring[R, ring].canonical n` recursively constructs classes from rank-zero units by suspension/disk homeomorphisms.
`thomIsomorphism n p` is an \(R\)-module isomorphism for arbitrary rank and commutative coefficients, with forward map
\[
H^p(X;R)\longrightarrow H^{p+n}(X\times D^n,X\times\partial D^n;R),\qquad
 a\longmapsto\pi^*a\smile\operatorname{canonical}(n)
\]
Rank zero uses empty-boundary forgetting/disk projection; successor ranks prove injectivity/surjectivity via disk shifts/sign involution.

`LocalDisk.On.Change[K, L, ring, targetRing, morphism].canonical n` proves unital coefficient maps preserve all-rank local Thom classes.
`LocalDisk.On.Step.ChangeCoefficients.law` gives disk-shift/coefficient-module naturality.

`RelativeMayerVietoris.OpenCover.On.From.Along.With.Ordinary[z].law` gives ordinary connecting naturality for cover-preserving pair maps.
`RelativeSuspension.On.From.With.At[z].law` proves suspension/pair-pullback compatibility.

`LocalDisk.On.From.Ring.canonical n` gives continuous-base pullback naturality of local classes.
`From.Ring.Degree[n, p].law` proves cup Thom isomorphisms commute with pullback.

`LocalDisk.Point[K, ring].Rank[n]` identifies point-disk generators with coefficient modules.
`LocalDisk.On.Ring.Top[n]` exposes degree-zero normalization/point-evaluation coordinates.
`Ring.Fibers[n].Fiber[x]` constructs disk-pair fiber restrictions; `value` agrees with evaluation coordinates.
`Fibers.detectedOnFibers` and `uniqueNormalized` prove local classes unique by fiber generators.
`RelativePullback.On.To.Homeomorphism.Degree[n].isomorphism` is a coefficient-linear pair-homeomorphism isomorphism.

`Thom.Real.For.With.Chart[c]` constructs radial trivialization-to-standard-disk-pair homeomorphisms.
`Chart.Ring.Degree[p].isomorphism` and `formula` give local cup Thom isomorphisms.
`Chart.Open` identifies restricted-bundle disk pairs with original chart-corresponding opens.
Its `Ring.Degree[p].isomorphism`, `formula`, `Additive.below` expose local isomorphisms/preceding-degree vanishing.

`RelativeMayerVietoris.OpenCover.On.RightAction[K, ring]` constructs right-cup maps from empty-pair to relative sequences with fixed right factors.
`Cup.SumAction.projection`, `Cup.Differential.law`, `Cup.Addition.law` prove projection/differential/addition compatibility.
`Positive.linear` gives positive-cohomology maps from boundary preservation; `Connecting.law` compares connecting maps including regrading.

`RightAction.Cup.Compare.Cohomology` identifies small cochain products with ordinary relative cups.
`RightAction.Positive.Compare.law` and `Connecting.Whole.law` give regraded cohomology/connecting comparisons.
`RelativeMayerVietoris.OpenCover.On.Cohomology.Vanishing[z].whole` proves global vanishing from both pieces and preceding intersection vanishing.
`Thom.Real.For.With.Coefficients.ProjectionIso[p]` exposes absolute disk-projection cohomology isomorphisms.
`Chart.Open.Ring.Degree[p].ordinaryIsomorphism` is the absolute-to-relative local cup isomorphism; `Chart.Open.Additive.Negative[k].zero` vanishes below rank.

`RelativeAction[A, source, subset, K, ring].Degree[p, q]` gives right cup with fixed relative classes from empty-boundary groups.
`integerMap` and `ringMap` provide integer/coefficient linear structures; `Along.Degree.law` proves pair-pullback compatibility.

`RelativeMayerVietoris.OpenCover.On.RightAction.Native[p, q]` constructs ordinary relative restriction/difference cup diagrams.
`Diagram` structures simultaneous regrading; `Five` constructs five-term sequences from Mayer–Vietoris.
`Gluing[p, q].With[u].isomorphism` derives degree-\(p+1\) cup isomorphisms from piece/intersection local isomorphisms.
`Zero[q].With[u].isomorphism` handles degree zero using preceding intersection vanishing.

`Thom.Real.For.With.Chart[c].Restrict[U, open, contained].chart` constructs charts by restricting original frames to smaller opens.
`Chart.Fiber[x].fiberPair` identifies bundle fibers with point-standard-disk pairs.
`Fiber.Ring[K, ring].generator` transports generators; `isomorphism`, `normalized` normalize by coefficient one.
`Fiber.Ring.Normalization.normalized` proves chart Thom fiber restrictions equal these generators.
`Open.Ring.Fibers.detected` proves fibers jointly detect local classes.

`Thom.Real.For.With.Atlas.existsFiniteCW` gets finite bundle-chart covers from finite-CW compactness.

`Thom.Real.For.With.Local[K, ring].Rank[n].Orientation.SignedOrientation` orientation data consists of fiber classes agreeing with normalized chart generators or negatives.
Chart dimensions equal \(n\); signed local classes come from disk-pair constructions.
Finite Mayer–Vietoris gluing constructs classes and isomorphisms while preserving fiber normalization and below-rank vanishing.

`Thom.Real.For.With.Oriented[K, ring, n, orientation, complex]` is the global finite-CW-base entry.

`Local.Rank[n].Fiber[x].Generator` states a coefficient-ring/top-fiber-group module isomorphism sends one to the class.
`Orientation.generates` proves orientation fiber classes are generators from signed local compatibility.

`Thom.Real.For.With.ModTwo[n, constantRank, complex]` takes no orientation argument.
Over `algebra.Two`'s two-element field, prove unique fiber generators and choose them.
Normalized chart classes agree, giving the same class, Euler, Thom isomorphism, and fiber normalization APIs over finite CW bases.

`CoefficientChange.FromIntegers[K, ring]` constructs \(\mathbb Z\to K\) from integer action on one.
`linear`, `multiply`, `unit` prove addition/product/unit preservation; `OnSpace[A, source].morphism` canonical arbitrary-ring coefficient changes.

`Oriented.Change[L, targetRing, morphism]` sends fiber generators through coefficients, constructing new orientation `targetOrientation` with the same charts/signs.
`classLaw` changes global Thom coefficients; `Degree[p].law`, `inverseLaw` give both Thom-direction diagrams; `eulerLaw` Euler changes.

`Thom.Real.For.With.Integral[n, orientation, complex]` is the integral entry.
`Coefficients[K, ring]` gives canonical \(\mathbb Z\to K\) orientation/Thom changes and Thom/Euler comparisons.
`Oriented.Integer.isomorphism z` gives in every integer degree
\(H^z(X;K)\cong H^{\operatorname{shift}(n,z)}(D(E),S(E);K)\).
Nonnegative orders restrict cup isomorphisms to integer modules; negative orders use both groups' vanishing.

`Additive[M].Degree[z].forget` and `sphereRestriction` expose two disk-pair long-exact maps.
`forgetCycles` and `forgetOnClass` compute the first on cochain representatives.
`Coefficients[R, ring].SphereSequence.Sphere.homeomorphism` identifies sphere bundles with disk boundaries; `isomorphism z` identifies integer boundary/sphere cohomology.
`SphereSequence.zeroSectionAt z` is integer-linear forgetting/zero pullback; `Natural[t].law` agrees with ordinary zero-section maps in nonnegative degrees.
`SphereSequence.Functor.At[z].law` proves integer pullbacks preserve composition.

`Oriented.Reverse.reversed` constructs orientations negating every generator/chart sign.
`classLaw` and `eulerLaw` negate Thom/Euler classes; `Degree[p].law` and `inverseLaw` negate both Thom directions.
`ModTwo.Compare[given].classLaw` identifies arbitrary signed mod 2 classes with standard classes.
`Integral.ModTwo.classLaw` and `eulerLaw` identify canonical reductions of integral classes with standard mod 2 classes.

`Oriented.Gysin.Degree[z].sequence` exposes the actual-sphere integer five-term sequence
\[
H^z(X;R)\xrightarrow{\smile e}H^{z+n}(X;R)
\xrightarrow{\pi^*}H^{z+n}(S(E);R)
\xrightarrow{\pi_!}H^{z+1}(X;R)
\xrightarrow{\smile e}H^{z+n+1}(X;R)
\]
Groups/maps are integer modules; `LocalDisk.shift n z` implements degree \(z+n\).
`cupEuler`, `pullback`, `integration`, `higherCupEuler` are its four maps.
`Positive[p].law` identifies the first with Euler cup in nonnegative base degrees; `Negative[k].law` handles negative bases.
`Degree[z].higherLaw` regrades the final Euler term.
`Degree[z].Pullback.law` identifies the second with sphere-projection pullback.
`Integral.Gysin` and `ModTwo.Gysin` are integral and canonical-mod-2 entries.

`Pullback.Fiber[y].Ring[K, ring].Degree[n].law` gives actual-fiber restriction compatibility for pullback/original bundles.
`Pullback.Ring.Chart[c].Fiber[y].generator` identifies pulled-chart standard generators with pullbacks of originals.
`Pullback.Ring.Oriented[n, orientation, complex, sourceComplex].pulledOrientation` constructs signed pullback orientations from these fiber maps.
`classLaw`, `eulerLaw`, `Degree[p].law`, `inverseLaw` give naturality for global Thom/Euler/forward/inverse Thom respectively.
`Pullback.ModTwo[n, constantRank, complex, sourceComplex]` compares standard pullback mod 2 classes.

`MixedCup[A, source, first, second, K, ring].Cup[p, q].Both.Cohomology` descends relative cochain cups to common-vanishing cochains.
`Union.Cover.On[conditions].Cup[p, q].apply` constructs ordinary \(H^p(A,\mathrm{first};K)\otimes H^q(A,\mathrm{second};K)\to H^{p+q}(A,\mathrm{first}\cup\mathrm{second};K)\) when both parts are open in their union.
`bilinear` gives underlying integer bilinearity; `CommonIso.Cohomology.Canonical.law` identifies small-chain comparison with ordinary cochain maps.
Geometry reuses `singular_cap.Triple`; coefficients/cups use the specified commutative ring.

`RelativeDisk.On[X, source, subset].With[M].isomorphism n z` constructs the relative-base disk isomorphism
\(H^z(X,B;M)\cong H^{z+n}(X\times D^n,X\times\partial D^n\cup B\times D^n;M)\).
Uses all-rank relative suspensions; `From.With.law` gives base-pair naturality.
`Thom.Real.For.With.Shell` gives open \(\|v\|>1/2\) shells and continuous zero-section-fixing `clip`.
`Shell.Over[U].equivalence` gives pair equivalences between sphere-boundary-plus-\(U\) and open-shell-plus-\(U\) pairs.

`MixedCup.Union.Cover.On.Cup.Forget.law` proves mixed products become ordinary cups after forgetting relative conditions.
`MixedCup.From[Y, target, firstPart, secondPart, f, regular, firstContained, secondContained].Covers[conditions, newConditions].Cup[p, q].law` gives naturality for maps preserving both parts.
`MixedCup.Change[L, targetRing, morphism].Covers[conditions].Cup[p, q].law` gives coefficient/mixed-relative-product compatibility.

`Thom.Real.DirectSum[X, F, G, left, right, same, leftMetric, rightMetric].With[metric]` exposes sum-metric/box-disk homeomorphism `pair`.
`Additive[M, z].isomorphism` is its relative isomorphism; `thomHomeomorphism` compares iterated Thom quotients.
`Ring[K, ring].Product[n, m].apply u v` defines products of two relative classes on direct sums.
Continuous `clip` sends open factor shells to sphere boundaries; pull both classes back and take mixed cup.
Shell unions contain box boundaries; restrict to box pairs and transport to specified-metric disk pairs.

`DirectSum.With.Ring.Product[n, m].Euler.law` proves zero-section images of arbitrary sum products equal cups of individual images.
Align right base topology by identity pullback through `same`.
`DirectSum.With.Fiber[x].Ring[K, ring].Product[n, m].Naturality.law` proves global-product fiber restriction equals the product of fiber restrictions.
`Fiber.homeomorphism` and `pair` compare direct-sum metric fibers with box-fiber pairs.

`FamilyMayerVietoris[A, source, family, cover]` is Mayer–Vietoris for small chains relative to specified subspace families.
`With[M].sequence` and `At[z].connecting` cover arbitrary integer modules/degrees.
`FamilyPair.InCover.With[M].quasiIsomorphism` compares ordinary chains using subdivision homotopies/replacement maps preserving families.
No need to identify every simplex in two closed parts' union with a simplex in one part.

`Local.Rank[n].Models.Orientation` groups fiber generators and local Thom models restricted to every open subset.
`With.Modeled[K, ring, n, orientation, complex]` constructs global classes by finite Mayer–Vietoris gluing.
Its class, normalization, Thom isomorphism, and below-rank vanishing APIs match `Oriented`; `Models.Signed` compares signed-chart orientations.

`DirectSum.With.IntegralProduct[n, m, leftOrientation, rightOrientation, complex]` constructs sum-fiber orientation `orientation` from products of integral Thom classes.
Standard-disk product generators follow from degree-zero units/signed suspension through local coordinates.
Relativize both closed faces as separate family members; identify with `Ring.Product.apply` products by open-shell homotopy comparison.

`DirectSum.With.Ring[K, ring].Change[L, targetRing, morphism].Product[n, m].law` proves arbitrary relative sum products commute with coefficients.
`Change.Euler[n].law` gives zero-section/coefficient compatibility.
`fiberLaw` in `Compare` asserts fiber agreement of supplied orientations; global Thom equality is derived.

Standard-disk comparisons distinguish coefficient-ring modules from underlying integer modules.
`IntegralComparison.Point[n].isomorphism` identifies integral point-disk relative groups with standard integers as integer modules.
`normalized` sends one to standard generators; `forwardLaw` and `backwardLaw` agree with coefficient-ring standard comparisons.
`RelativePullback.On.To.Homeomorphism.Degree[n].native` gives integer-module isomorphisms; same-degree `isomorphism` gives coefficient-ring module isomorphisms.
