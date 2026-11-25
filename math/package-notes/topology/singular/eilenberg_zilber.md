# `singular_eilenberg_zilber` notes

[Package API](../../../../libs/topology/singular/eilenberg_zilber/README.md) · [Checking](../../../../libs/USAGE.md)

## Construction

Compare product-space singular chains with tensor totals of factor chains.
Expose `singular_products` Alexander–Whitney/shuffle maps with both chain homotopies.

`forward` in `On[A, B, left, right]` is Alexander–Whitney; `backward` shuffle.
`productComposite` is the product-space composite; `tensorComposite` the tensor composite.
`Equivalence.equivalence` returns nonnegative chain equivalences; `Equivalence.Signed.equivalence` integer zero-extended equivalences.

Fill composite differences on diagonal simplices of standard-simplex products.
Tensor-side models are tensors of two standard-simplex chain complexes.
Prove alternating-face model maps commute with boundaries; contractions fill degreewise.
Degree-zero differences vanish, so recursion starts positively.

`TensorEvaluation` evaluates model chains on arbitrary simplex pairs.
`TensorGenerators` gives pure generators of each total degree; `TensorHomotopy` extends model fillings from them.
Generator boundary formulas/linearity prove both homotopy identities.
