# `cohomology_thom`

Relative Thom-class products/zero sections, fiber restrictions, standard-disk generators.

| Entry | Purpose |
| --- | --- |
| `Coefficients.Degree[n].Class` | Disk/sphere relative cohomology |
| `Coefficients.Product[p, n].linear u` | Linear \(a\mapsto\pi^*a\smile u\) for specified relative \(u\) |
| `Coefficients.Product.Forget.law` | Relative forgetting/cup compatibility |
| `Coefficients.Product.ZeroSection.law` | Zero-section \(s^*(\pi^*a\smile u)=a\smile s^*u\) |
| `Coefficients.Product.addClass` / `scaleClass` | Products under relative-class addition/scaling |
| `Coefficients.Degree[n].zeroSection` | Linear relative-to-absolute then zero-section pullback |
| `Coefficients.Degree[n].euler u` | Specified-class zero-section pullback |
| `Additive.Degree[z].thomComparison` | Reduced Thom-quotient/disk-pair isomorphisms |
| `Additive.Degree[z].diskComparison` | Disk contraction/base cohomology isomorphisms |
| `Additive.Degree[z].connecting` | Disk-pair long-exact connecting maps |
| `Fiber[x].Additive[M, z].restriction` | Actual disk-fiber/sphere relative restrictions |
| `class` | Global Thom classes in \(H^n(D(E),S(E);K)\) |
| `normalized` | Disk-fiber restrictions agree with specified classes |
| `uniqueNormalized` | Uniqueness for equal fiber values |
| `Degree[p].isomorphism` | \(H^p(X;K)\cong H^{p+n}(D(E),S(E);K)\), forward \(a\mapsto\pi^*a\smile u\) |
| `euler` | Zero-section Thom pullbacks |
| `Degree[p].zeroSection` | Zero-section pullbacks of Thom images multiply by Euler classes |
| `Below[k].zero` | Vanishing in \(\operatorname{shift}(n,-k-1)\) |
| `IntegralProduct.classLaw` | Integral Thom products equal global Thom classes for constructed sum orientations |
| `IntegralProduct.Degree[p].isomorphism` | Thom isomorphisms by cups with classes |
| `IntegralProduct.Euler.law` | Sum Euler classes equal cups of factor Euler classes |
| `IntegralProduct.Compare[given, fiberLaw]` | Class/Euler/Thom comparisons with signed-chart orientations having equal fiber orientations |
| `ModTwoProduct.canonicalProductLaw` | Products of canonical mod 2 Thom classes equal canonical sum classes |
| `IntegralProduct.ModTwo.classLaw` | Coefficient changes of constructed integral classes equal canonical sum mod 2 classes |
| `IntegralProduct.ModTwo.Degree[p].law` / `inverseLaw` | Forward/inverse Thom compatibility with canonical integral-to-mod-2 changes |

[Source](src/root.ref) · [Dependencies](ref.toml) · [Checking](../../USAGE.md) · [Notes](../../../math/package-notes/topology/cohomology_thom.md)
