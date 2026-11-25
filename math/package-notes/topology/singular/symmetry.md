# `singular_symmetry` notes

[Package API](../../../../libs/topology/singular/symmetry/README.md) · [Checking](../../../../libs/USAGE.md)

## Construction

`On[A, source].forward` composes diagonals with Alexander–Whitney.
`backward` follows with Koszul tensor swaps.
`On.Homotopy.homotopy` homotopes both chain maps.

Standard models: \(C_*(\Delta^n)\otimes C_*(\Delta^n)\).
Equal-face transitions, zero degree-zero differences, explicit positive contractions inductively construct model homotopies.
Evaluate by simplex postcomposition and extend by free universality.

`Cochains.Pairing[p, q]` evaluates two commutative-ring cochains on tensor chains.
Closed evaluations annihilate total differentials; `HomComplex.Homotopy` transfers homotopies to cohomology.
`Cochains.GradedCommutativity[p, q].law` proves for arbitrary cohomology classes \(x,y\):

\[
x\smile y=(-1)^{pq}y\smile x
\]

The public formula explicitly includes transport between degrees \(p+q\), \(q+p\).

`Cochains.ExternalCup[p, q]` identifies tensor-cochain Alexander–Whitney pullbacks on products with cups of projection pullbacks.
`Classes[alpha, beta]` identifies closed representatives and gives class formulas.
