# Bott's basic product

`Bott.ProjectiveLine.Homeomorphism.homeomorphism` explicitly identifies rank-one orthogonal projections on complex two-space with \(S^2\).
Forward maps use matrix entries as three real coordinates; inverses construct trace-one Hermitian idempotents from sphere points.
`ProjectiveLine.SphereLine` pulls universal lines back to spheres along this homeomorphism.

`Bott.generator` is unit-circle-coordinate clutching lines minus trivial lines.
`Rank.zero` and `Restriction.vanishes` prove zero rank/point restriction.
`Product.forward` gives \(a+b u\) by two projection pullbacks/products; `Product.At.restrictForward`, `Product.Naturality.equation` give basepoint restriction/naturality.

`Product.Loops.With.forwardFormula` connects K07 matrix-loop inverse classes to this product.
`Product.Bundle.Preparation.With` stabilizes basepoint restrictions with complements, trivializing both hemispheres.
`Transition.With` constructs continuous invertible boundary loops from trivializations.
`Product.Surjective.exists` proves every \(K^0(X\times S^2)\) class has a standard-product presentation.

`Product.At.Kernel` identifies basepoint-restriction kernels with generator-multiple images.
`Product.At.Slice` identifies basepoint slices with \(X\); `Slice.Relative.imageRepresentation` places forgotten K03 relative classes in these images.
`Slice.Relative.Retraction.injective` uses slice retractions/exact sequences to prove relative forgetting injective.
`Slice.Relative.Retraction.Comparison` bijects relative classes with \(K^0(X)\) coefficients additively.

`Product.Injective.injective` and `Product.Surjective.exists` prove the standard product an additive bijection.
`Product.Inverse.first` returns basepoint restrictions; `coefficient` unique reconstructing coefficients.
Actual-bundle boundary-loop/K07-inverse constructions `Product.Bundle.Decomposition`, `Product.Surjective` compute these coefficients.
`Inverse.ofRepresentation` proves independence from construction choices.

`Bott.Powers.squareLoop` identifies reduced \(z^2\)-clutching classes with \(2u\).
`Bott.TensorLine` compares tensor-square hemisphere frames, constructing global \(z^2\)-clutching isomorphisms.
`Bott.Square.zero` proves \(u^2=0\); `Product.Multiplication.formula` standard-product coefficient multiplication.
`Bott.Sign.negative` identifies conjugate-circle clutching classes with \(-u\).
`Bott.ProjectiveLine.SphereLine.Comparison.universalIsomorphism` identifies sphere-pulled projective universal lines with conjugate clutching lines.
`Comparison.Class.sign` proves \([H]-1\) is negative `Bott.generator`.
`Product.Coefficients` gives coefficient-pair addition/multiplication, standard maps/inverses and compatibility.
`Product.Coefficients.Ring` makes coefficient pairs commutative rings with standard-product homomorphisms.
`Product.Polynomial` constructs polynomial quotients by \(u^2=0\) and standard-product homomorphisms; `Polynomial.Normal` proves normal forms/explicit inverse maps.
With universal reduced generators, `Product.Hopf` gives sign-adjusted products/coefficient inverses; `Product.Hopf.Polynomial` corresponding quotient-ring isomorphisms.
`Product.Naturality.Hopf` proves product/inverse naturality; `Slice.Relative.Retraction.Comparison.Hopf` relative coefficient correspondence with matching signs.
