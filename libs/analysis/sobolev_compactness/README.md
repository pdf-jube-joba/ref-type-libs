# Sobolev compactness

Frequency truncation and compactness of Fourier integral families on Euclidean space.

| Entry | Result |
| --- | --- |
| [Euclidean.Mask](src/Euclidean/Mask.ref) | Multiplication by the indicator of a measurable set is an \(L^2\) contraction. |
| [Euclidean.Gap](src/Euclidean/Gap.ref) | The order-lowering map \(H^{k+q} \to H^k\) is a contraction and preserves the physical \(L^2\) element. A common norm bound gives a common cutoff threshold for any positive tail tolerance. |
| [Euclidean.Gap.High](src/Euclidean/Gap/High.ref) | Splits the lower-order vector at \(w_q(\xi) = t\), where \(w_q(\xi) = (1 + \lvert \xi \rvert^2)^{q/2}\). The tail has \(H^k\) norm at most \(t^{-1}\) times the \(H^{k+q}\) norm. |
| [Euclidean.Gap.High.CompactRegion](src/Euclidean/Gap/High/CompactRegion.ref) | The retained frequency region is compact when \(q>0\). |
| [Euclidean.Kernel](src/Euclidean/Kernel.ref) | The Fourier kernel difference is bounded by \(2\lVert x\rVert_1\lVert \xi-\eta\rVert_\infty\). |
| [Euclidean.Support](src/Euclidean/Support.ref) and [LowRegion](src/Euclidean/Support/Equicontinuity/LowRegion.ref) | Masking an \(L^2\) class to a fixed compact set gives an integrable representative. Its Fourier integral descends to the \(L^2\) quotient. The real and imaginary parts of a norm-bounded family have compact closure in the uniform topology on each compact frequency region. |

The Sobolev statements use the complex weighted Fourier model of [A09](../euclidean_sobolev/README.md) for nonnegative integer orders \(k\) and \(k+q\). The low-frequency statements concern the unnormalized integral with kernel \(\exp(-i x\cdot\xi)\). The remaining step for Rellich compactness is to identify these integral representatives with the low-frequency blocks of the normalized weighted \(L^2\) transform and pass to the lower-order Sobolev norm. Signed orders, general smooth-kernel compactness and the finite-chart gluing operations remain open here.

```sh
python3 scripts/check.py run --scope changed --package sobolev_compactness --checker /path/to/cli
```
