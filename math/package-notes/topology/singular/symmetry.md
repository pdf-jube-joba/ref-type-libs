# Commutation homotopies of singular cochains

Construction details and records for [singular_symmetry](../../../../libs/topology/singular/symmetry/README.md).
See [building and checking](../../../../libs/USAGE.md) for current commands.
The API overview is maintained in the package README; recorded checks describe earlier runs.

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
