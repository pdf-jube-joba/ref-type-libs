# `inverse_implicit` notes

[Package API](../../../libs/geometry/inverse_implicit/README.md) · [Checking](../../../libs/USAGE.md)

## Construction

Smooth finite-dimensional maps over Dedekind reals.
Construct actual local inverses for `calculus.Maps` open maps, connecting to `manifolds` manifolds/derivatives.
Includes dimension zero and empty regular fibers.

### Constructing inverse functions

Restrict to nonzero Jacobian-determinant opens; postcompose with base linear inverses to normalize derivatives to identity.
`Flat` derives local contraction of zero-derivative residuals from continuous partials/mean values.
`NearIdentity` clips residual coordinates to closed balls, constructing whole-Euclidean contractions.
Existing completeness/contraction selects preimages; bounds keep them inside clipping interiors.
Obtain inverse existence, local uniqueness, and distance bounds.

`InverseDifferential` proves inverse total derivatives from original remainders, linear inverses, and inverse distance bounds.
`InverseRegularity` uses smooth inverse matrices/chain rules to induct on derivative order for smooth scalar functions composed with inverses.
This proves constructed inverses smooth.

### Implicit functions and constant rank

Split \((p,q)\), construct \((p,q)\mapsto(p,F(p,q))\).
`Triangular` explicitly builds two-sided derivative inverses from \(D_qF\) inverses.
Apply inverse functions, restrict images to product neighborhoods, take inverse right components as solutions.
`graphInside` and `coordinates` ensure solution graphs lie in uniqueness neighborhoods.

`Rank.Witness` is purely linear \(L=AB\), with injective \(A:\mathbb R^r\to\mathbb R^m\), surjective \(B:\mathbb R^n\to\mathbb R^r\).
Constant rank uses base \(A\) left inverses to select regular components and construct surjection coordinates.
Pointwise rank factorizations and square one-sided inverses force remaining parameter derivatives zero.
Mean-value estimates give parameter independence.
Finally construct smooth target shears.
`NormalForm.formula` states constructed two-sided diffeomorphisms turn maps into \((p,z)\mapsto(0,z)\).

General surjections use transpose injectivity, Gram–Schmidt, kernel-projection traces/frames.
No particular minor is required instead of surjectivity.

### Regular-value fibers

`Regular` states actual manifold derivatives surject at every fiber point.
Chart tangent isomorphisms give coordinate surjectivity; apply `Submersion` local forms.
Fix target coordinates at regular values to construct fiber charts.
Original transitions, local diffeomorphisms, coordinate fixing/projections prove smooth fiber transitions.
Subspace topology inherits Hausdorffness/second countability.

Inclusions are smooth embeddings.
Tangent/kernel isomorphisms use actual inclusion derivatives forward.
Inverses move ambient vectors into local coordinates, apply local-diffeomorphism derivatives, extract parameter components, return to fiber tangents.
Prove inverse laws on kernels and injective inclusion derivatives.

## Examples

[Examples.ref](../../../libs/geometry/inverse_implicit/src/Examples.ref) applies inverse functions to shear \((u,z)\mapsto(u-z^2,z)\).
`Examples.Implicit` applies parameterized implicit functions to \(F(p,q)=q-p^2\).
`rankNormalForm` gives both local coordinates for rank-one \((u,z)\mapsto(u-z^2,0)\).
`Examples.Manifold` instantiates regular \(u-z^2=0\) submanifolds, inclusion embeddings, tangent/kernel isomorphisms.
`Examples.ZeroDimension` checks dimension-zero inverse functions.
