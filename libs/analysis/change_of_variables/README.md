# Change of variables in multiple integrals

Lebesgue measure, smooth compactly supported functions, and open-set diffeomorphisms over Dedekind reals.
Measure/integration use `euclidean_measure`, `functional_analysis.Measure`, `product_integration`; differentiation/local inverses use `calculus`, `inverse_implicit`.

## Diffeomorphism change of variables

`Change.theorem n U V e f within` applies in arbitrary dimension to smooth \(e:U\to V\) and smooth compactly supported \(f\) supported inside \(V\):
\[
\int_U |\det De_x|f(e(x))\,d\lambda_n(x)=\int_V f(y)\,d\lambda_n(y)
\]
Includes dimension zero and empty open sets.
`Euclidean[n].Diffeomorphism[U,V,e].Compact[f,within]` constructs extension by zero of the left density, smooth compact support, and actual Lebesgue-integrable representatives.
The main integrand is `lp_spaces.Euclidean[n].SmoothCompact`, explicitly supported in \(V\).

Coordinate swaps and local inverses reduce the proof to one-coordinate substitutions and first-coordinate-fixing maps.
The one-coordinate case combines forward/reverse interval substitution by Fubini; the fixed-first-coordinate case inducts using slice diffeomorphisms and determinant minors.
Finally glue local formulas by finite compact-support decompositions.
`Composition` and `Restriction` prove equality of actual weighted-pullback integrals under composition/restriction.
`NonlinearExample.integral` applies the theorem to nonlinear shear \((p,q)\mapsto(p-q^2,q)\).

## Linear maps and Jacobians

`Linear[n].Generated.measure` proves for invertible \(L\) and arbitrary sets \(S\):
\[
\lambda_n^*(L(S))=|\det L|\lambda_n^*(S)
\]
The equality is expressed using lower cuts of extended nonnegative outer measures.
On measurable sets this is the Lebesgue transformation law.
`measurable` proves preservation of Lebesgue measurability.
`Elementary.Elimination.factorization` constructs finite elementary decompositions including dimension zero, connecting diagonal/shear/composite measure formulas.
`OpenTransport` extends open-set scaling under homeomorphisms to arbitrary sets by outer regularity, transporting Carathéodory measurability.
`Permutation.Smooth` gives coordinate-permutation diffeomorphisms, absolute Jacobian one, and preservation of compact-support pullback integrals.

`signed` in `Euclidean[n].Jacobian[U,V,f]` is the actual total-derivative determinant; `absolute` is its modulus.
`signedSmooth`, `Composition.signed/absolute`, `Inverse.nonzero/positive/cancellation` prove smoothness, chain rules, inverse nonvanishing/cancellation.
`Diffeomorphism.Regularity` derives absolute-Jacobian smoothness from square roots of nonzero determinant squares.

## Localization and parameters

`Euclidean.Localization[U]` transfers local smooth functions with compact zero-extended support in \(U\) to global `SmoothCompact` and integrable representatives.
`cutoff` returns smooth cutoffs equal to one near compact sets.
`Decomposition[family,f].exists` constructs finite smooth compact-support decompositions subordinate to open covers of \(\operatorname{supp}f\).
`Data.pointwise` identifies the finite sum with the original; `Sum.theorem` identifies actual integrals with summed integrals.
`BorelCompact` constructs the same function as a Borel-integrable representative, agreeing with completed Lebesgue integration.

`Parameters.derivative` interchanges integration/differentiation by dominated difference quotients and pointwise derivatives.
`Parameters.Compact[function,partial].For[conditions].theorem` constructs dominating functions for parameterized smooth compact-support functions from common finite-measure regions and uniform partial bounds nearby.
`Parameters.Multivariable.At.theorem` transfers this to every partial derivative in arbitrary finite-dimensional parameters.

## Integration by parts and boundaries

`Euclidean.Compact.integralDerivative` proves integrals of partial derivatives of smooth compact-support functions vanish in every coordinate.
`Compact.IntegrationByParts[f,g,i].theorem` applies to compactly supported \(f\) and arbitrary smooth \(g\):
\[
\int (\partial_i f)g=-\int f\partial_i g
\]

`Interval[interval].Fundamental`, `IntegrationByParts`, `Substitution`, `ReverseSubstitution` provide closed-interval formulas.
Substitution covers both orientations; `For.Absolute.theorem` is the Lebesgue equality with absolute derivatives.
`RealLine.Monotone` derives interval/interior-image conditions from derivative signs and the mean value theorem.

`Boundary[n].Strip` gives \(\mathbb R^n\times[a,b]\) boundary formulas; `Rectangle` restricts bases to boxes; `Strip.HalfSpace` gives half-space formulas vanishing above.
`IntegrationByParts` derives boundary integration by parts from the product rule.
Handles Fubini exceptional null sets and concludes boundary-difference integrability.
`Bridge[n]` concatenates product/\(\mathbb R^{n+1}\) coordinates, proving Borel measure comparisons and integrable-representative transport.
`For.theorem` and `Strip.HalfSpace.theorem` in each `Strip`, `Rectangle`, `IntegrationByParts` give actual Euclidean boundary formulas; `Permuted` permutes to arbitrary coordinates.
Coordinate Borel measurability is explicit.

## Densities and top forms

`Euclidean.Density.pullback` is \(h\mapsto |\det Df|h\circ f\), with positivity, composition, and inverse recovery.
`TopCoordinates[U]` gives inverse correspondences between smooth coefficients and top forms \(h\,dx_1\wedge\cdots\wedge dx_n\).
`TopForm.coordinate` proves actual `euclidean_forms` pullback top coefficients equal \((\det Df)h\circ f\).
Densities use absolute determinants; oriented top forms use signed determinants.

`Examples[n].IdentityOn` checks identity Jacobians/density transforms including dimension zero.

## Checks

Use standard release checkers for targets, local source rechecks, dependency regressions, and the full repository.

[Build and check](../../USAGE.md) from the repository root:

```sh
ref-type/target/release/cli libs/analysis/change_of_variables --module change_of_variables --full-check-local --memory-mib 8192
```
