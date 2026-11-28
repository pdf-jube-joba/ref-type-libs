# `euclidean_sobolev`

Integer-order Sobolev spaces, weak-derivative comparisons, duality, local coordinate changes and embeddings.

Orders are integers. The C^r embedding requires 2p > n for H^(r+p); local transport includes smooth compact-support coefficients and zero extension.

| Entry | Purpose |
| --- | --- |
| `Euclidean.Signed` / `Order.Duality` | Weighted Fourier spaces and positive/negative-order duality |
| `Euclidean.Weak.Approximation` | Real-part weak-derivative classes of Fourier elements at every nonnegative order |
| `Euclidean.Weak.Zero` | Isometric correspondence between real Fourier elements and weak-derivative classes at order zero |
| `Euclidean.Weak.ofSchwartz` / `Euclidean.Energy` | Weak derivatives of real Schwartz functions and Fourier/derivative energy on complex Schwartz functions |
| `Euclidean.Order.Density` | Schwartz approximation of nonnegative integer-order elements |
| `Euclidean.Transport` / `MultiplicationBy` | Local diffeomorphism pullbacks, compact coefficients and zero extension |
| `Euclidean.EmbeddingTheorem` / `Regularity` | Sobolev embeddings and common smooth inverse Fourier representatives |

The weak-derivative space in this package uses real-valued functions. The map from Fourier elements sends the real part of the physical \(L^2\) class to a weak-derivative class on the whole space. Each constructed weak derivative through order `k` has an `L^2` norm bounded by the Fourier Sobolev norm. The converse for positive orders and the comparison with a complex weak-derivative space remain open.

[Source](src/root.ref) · [Dependencies](ref.toml) · [Checking](../../USAGE.md)
