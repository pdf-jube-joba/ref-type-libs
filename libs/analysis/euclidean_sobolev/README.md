# Integer-order Sobolev spaces on Euclidean spaces

`Euclidean[n := n].Signed[s := s]` represents Fourier transforms weighted by \((1+|\xi|^2)^{s/2}\) as complex \(L^2\) elements.
`Order[k := k].Duality[]` gives \(H^{-k}\)–\(H^k\) pairings, \(L^2\) compatibility, and unique bounded-functional representations.

`Weak[].ofSchwartz` sends real Schwartz functions to weak-derivative \(W^{k,2}\).
`Energy[].comparison` equates squared Fourier norms with multiplicity-weighted sums of squared iterated-derivative \(L^2\) norms for complex Schwartz functions.
`Order[k := k].Density[].sequenceExists` approximates arbitrary \(H^k\) elements by these Schwartz images.

`Transport` gives positive/negative-order pullbacks along open diffeomorphisms, multiplied by smooth compact-support coefficients and extended by zero.
`MultiplicationBy` specializes to identity maps, giving multiplication by real smooth compact-support functions.

`EmbeddingTheorem[r := r, p := p, range := range].theorem` proves inverse Fourier integrals of \(H^{r+p}\) elements are \(C^r\) when \(2p>n\).
`Regularity[].smooth` gives common smooth inverse Fourier integrals for elements of every nonnegative integer order.
