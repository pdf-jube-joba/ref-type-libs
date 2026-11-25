# Periodic K-theory

`periodic_k_theory` constructs relative/reduced Bott and integer complex K-theory from K08.
Relative groups use closed quotients, negative degrees reduced suspensions, integers parity normal forms.
`Integer.Comparison` compares original negative degrees.

| API | Contents |
| --- | --- |
| `Periodicity.beta` | K08 Bott elements of basepoint rank zero |
| `Reduced` / `Reduced.Inverse` | \(a\mapsto a\boxtimes\beta\), inverses/both laws/additivity/zero |
| `RelativePair` | Closed-pair external \(K(X,A)\to K((X,A)\wedge(S^2,*))\), both inverses |
| `TwoShift` / `Negative` | \(\widetilde K^{-n}(X)\cong\widetilde K^{-(n+2)}(X)\) |
| `Integer.At` / `Absolute` / `Pair` | All integer groups, two-periodicity, pullbacks |
| `SixTerm` / `SixTerm.Naturality` | Closed-pair six-term exact sequences, six exact positions/squares |
| `Product` / `Commutativity` | Integer external products, biadditivity, Koszul swaps |
| `SwapSphere` / `OddProduct` | Bott negation under double-suspension swaps, odd-product signs |
| `Point.At` / `Spheres.At` | Point/reduced-sphere integer computations |
| `RankSplit` / `OrdinaryOdd` | Ordinary/reduced rank splitting, degree-minus-one comparisons |
| `Spheres.Ordinary` / `Spheres.OrdinaryOdd` | Integer coordinates for ordinary spheres |
| `BottSpheres` | Iterated Bott generators, integer isomorphisms, odd vanishing |

`Reduced.Naturality`, `TwoShift.Naturality`, `Negative.Naturality` expose Bott/pullback compatibility.
`RelativePair.Formula.productFormula` identifies quotient-built relative isomorphisms with existing relative external products.

`SquareSphere` and `SuspensionSphere` explicitly identify collapsed square boundaries with pointed \(S^2\).
`DoubleComparison` transfers to \(\Sigma^2X\cong X\wedge S^2\) for arbitrary compact pointed spaces.
Constant complex matrices compare projective lines/complements to prove swap signs.
`SwapSphere.On.Twist.Coordinates.equation` identifies this self-map with double-suspension time swapping.
Combining `ExternalSymmetry` and `MixedProduct`, `Product.gradedCommutative` proves swapped reversed products equal \((-1)^{ij}\) times originals.
`reverseProduct` normalizes reversed products to common \(i+j\); `koszulParity` identifies parity with integer products.

Point degree-minus-one vanishing uses polygonal paths avoiding finite complex sets to connect general linear groups.
Extend endpoint isomorphisms along paths, proving interval/boundary relative groups zero.
Identify quotients with circles to get \(K^{-1}(*)=0\), \(\widetilde K^0(S^1)=0\).

`Spheres.sphere n` is \(n\)-fold reduced suspension of \(S^0\).
Computations:
\[
K^j(*)\cong
\begin{cases}\mathbb Z&j\equiv0\pmod2,\\0&j\equiv1\pmod2,\end{cases}
\qquad
\widetilde K^j(S^n)\cong
\begin{cases}\mathbb Z&j+n\equiv0\pmod2,\\0&j+n\equiv1\pmod2.\end{cases}
\]
`Coefficients.Carrier false` is all integers; `Coefficients.Carrier true` the zero subgroup.
`Spheres.At.parityFormula` and `isomorphism` give typed versions of this table.
`RankSplit` constructs \(K^0(X)\cong\mathbb Z\oplus\widetilde K^0(X)\) for compact pointed spaces.
`OrdinaryOdd` constructs \(K^{-1}(X)\cong\widetilde K^{-1}(X)\) from split point-pair sequences.
Thus `Spheres.Ordinary` gives \(\mathbb Z^2\) in even and \(\mathbb Z\) in odd dimensions; `Spheres.OrdinaryOdd` gives zero in even and \(\mathbb Z\) in odd dimensions.
`BottSpheres.comparison` identifies iterated-smash even-sphere models with suspensions.
`iteratedBott` identifies successive generators as Bott products; `normalized` gives integer coordinate one.

Minimal examples: [Examples.ref](src/Periodicity/Examples.ref), [Examples/Reduced.ref](src/Periodicity/Examples/Reduced.ref).

```ref
\import periodic_k_theory.Periodicity[] \as K;
\import K.Point[] \as Point;
\definition pointMinusOne:
  \forall (x: Point.Odd) -> x = Point.oddGroup.base.unit := Point.oddZero;
```

Run `cargo build -p cli --release --locked` and `python3 scripts/check_all.py` at the repository root for standard checks.
Large comparison diagrams may need `--memory-mib 10240`.
