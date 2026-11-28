# Libraries

Dependencies are in each `ref.toml`; public modules are in `src/root.ref`.
The workspace [ref.toml](ref.toml) registers 112 packages, all linked below.
Build and check them using the separately installed compiler; see [checking the libraries](USAGE.md).
Requirements and known gaps are tracked in the [mathematics roadmap](../math/_roadmap.md).
Except for `std`, aim for roughly 5,000 lines per package, organized by dependencies from shared foundations to applications.

## Foundations

| Location | Package | Contents |
| --- | --- | --- |
| [std](std/README.md) | `std` | Logic, data, integers/rationals, quotients, algebraic structures |
| [category](category/README.md) | `category` | Categories, functors, natural transformations, universal properties, adjunctions, additive and abelian categories |

## Number systems

| Location | Package | Contents |
| --- | --- | --- |
| [real/axiomatic](real/axiomatic/README.md) | `ordered_fields` | Shared ordered-field and supremum-completeness structures |
| [real/dedekind](real/dedekind/README.md) | `dedekind_reals` | Reals from rational cuts, arithmetic, order, completeness |
| [real/cauchy](real/cauchy/README.md) | `cauchy_reals` | Reals from rational Cauchy-sequence quotients, arithmetic, order, completeness |
| [real/basic](real/basic/README.md) | `real` | Constructed real arithmetic, distance estimates, sequences, square roots, finite sums |
| [complex](complex/README.md) | `complex` | Complex numbers as real pairs and field structure |

Standard reals pass from `dedekind_reals` to `real`.
Use `real.Analysis` for shared numerical lemmas, `Def` / `Prop` to separate operations from laws, and [eq_reason!](std/USAGE.md#equality-and-congruence) for equality chains.

## Algebra

| Location | Package | Contents |
| --- | --- | --- |
| [algebra/basic](algebra/basic/README.md) | `algebra` | Homomorphisms, group completion, quotients, polynomial rings |
| [algebra/characteristic_series](algebra/characteristic_series/README.md) | `characteristic_series` | Rational symmetric polynomials, Newton identities, truncated series, finite Chern-character/Todd/L/A-hat polynomials and coefficients |
| [algebra/galois](algebra/galois/README.md) | `galois` | Field extensions, minimal polynomials, automorphism extensions, Galois connections, radicals, constructibility, definition of the algebraic closure of the rationals |
| [algebra/quintic](algebra/quintic/README.md) | `quintic` | Insolubility of the general quintic by radicals and nonconstructibility |
| [algebra/module_theory](algebra/module_theory/README.md) | `module_theory` | Modules over rings, free modules, direct sums, tensor products, exact sequences |
| [algebra/commutative_algebra](algebra/commutative_algebra/README.md) | `commutative_algebra` | Hom and tensor products, projectivity, matrices of finite free modules |
| [algebra/integer_matrices](algebra/integer_matrices/README.md) | `integer_matrices` | Integer matrix operations, Smith normal form, transformation matrices |
| [algebra/finitely_generated_modules](algebra/finitely_generated_modules/README.md) | `finitely_generated_modules` | Bases of integer kernels/images/submodules, cyclic modules, finite-dimensional subspaces over fields |
| [algebra/linear_algebra](algebra/linear_algebra/README.md) | `linear_algebra` | Linear, multilinear, and exterior algebra over commutative rings; real/complex specializations |
| [algebra/matrix_invariants](algebra/matrix_invariants/README.md) | `matrix_invariants` | Determinants, cofactors/adjugates, inverses, continuity and openness of real/complex matrix families |
| [algebra/polynomial_linear_algebra](algebra/polynomial_linear_algebra/README.md) | `polynomial_linear_algebra` | Polynomial division/Euclidean algorithm, Bézout coefficients, Chinese remainder theorem, Cayley–Hamilton, kernel direct sums, coefficient changes |
| [algebra/fundamental_algebra](algebra/fundamental_algebra/README.md) | `fundamental_algebra` | Complex polynomial bounds at infinity, minima, roots, complete factorization with multiplicities, unique finite root families |
| [algebra/complex_polynomial_roots](algebra/complex_polynomial_roots/README.md) | `complex_polynomial_roots` | Root boundedness, finite symmetric-product/coefficient-space homeomorphism, continuous factors for separated root clusters |
| [algebra/hermitian_frames](algebra/hermitian_frames/README.md) | `hermitian_frames` | Hermitian forms, continuous orthonormalization, local projection frames and inverse coordinates, unitary groups |
| [algebra/spectral_splitting](algebra/spectral_splitting/README.md) | `spectral_splitting` | Root factors inside/outside the unit circle, continuous spectral projections, image bundles, homotopy comparisons |
| [algebra/lie_algebras](algebra/lie_algebras/README.md) | `lie_algebras` | Lie algebras, adjoint representations, commutators, Lie subalgebras, endomorphism algebras |
| [algebra/clifford](algebra/clifford/README.md) | `clifford` | Clifford quotient construction and universality, Pin/Spin and complex-extension group structures |
| [algebra/spinor_representations](algebra/spinor_representations/README.md) | `spinor_representations` | Clifford modules, spinor representations and Spin/Spin-c actions |
| [algebra/homological/chain_complexes](algebra/homological/chain_complexes/README.md) | `chain_complexes` | Natural/integer-graded complexes, homology, maps, homotopies, categories of complexes |
| [algebra/homological/double_complexes](algebra/homological/double_complexes/README.md) | `double_complexes` | Nonnegative chain complexes, double complexes, totalization, exact comparisons, signed swaps |
| [algebra/homological/resolutions](algebra/homological/resolutions/README.md) | `resolutions` | Projective resolutions, comparison theorem, Hom/tensor complexes, double-total resolution comparisons |
| [algebra/homological/tensor_chains](algebra/homological/tensor_chains/README.md) | `tensor_chains` | Integer-graded tensor totalization, external products and naturality, signed shifts, commutative squares |
| [algebra/homological/derived_functors](algebra/homological/derived_functors/README.md) | `derived_functors` | Ext/Tor, resolution independence and naturality, cyclic-module resolutions, universal coefficients |
| [algebra/homological/field_kunneth](algebra/homological/field_kunneth/README.md) | `field_kunneth` | Finite free field-coefficient cochain complexes, canonical external-product isomorphisms, naturality, swap signs, units |
| [algebra/homological/computations](algebra/homological/computations/README.md) | `homological_algebra` | Homology computations for finite integer complexes, natural universal-coefficient/integral-Künneth short exact sequences |
| [algebra/homological/concrete_complexes](algebra/homological/concrete_complexes/README.md) | `concrete_complexes` | Finite-complex, universal-coefficient, tensor-product and integer-homology examples |

## Analysis

| Location | Package | Contents |
| --- | --- | --- |
| [analysis/uniform_approximation](analysis/uniform_approximation/README.md) | `uniform_approximation` | Real/complex Stone–Weierstrass, Laurent approximation on circles/products, uniform matrix/bundle-endomorphism estimates |
| [analysis/calculus](analysis/calculus/README.md) | `calculus` | Limits, mean value theorem, multivariable differentiation, smooth maps |
| [analysis/euclidean_measure](analysis/euclidean_measure/README.md) | `euclidean_measure` | Euclidean Lebesgue measure, regularity, integral comparisons |
| [analysis/change_of_variables](analysis/change_of_variables/README.md) | `change_of_variables` | Invertible linear measure transformations, compact-support diffeomorphism substitution, localization, parameter integrals, boundary terms, densities/top forms |
| [analysis/product_integration](analysis/product_integration/README.md) | `product_integration` | σ-finite product measures, Tonelli, real/complex/finite-dimensional Fubini, Euclidean Borel comparison, convolution integrals/support/L1 estimates |
| [analysis/differential_equations](analysis/differential_equations/README.md) | `differential_equations` | Picard integral operators, local ODE existence/uniqueness, smooth solutions of smooth vector fields |
| [analysis/functional](analysis/functional/README.md) | `functional_analysis` | Real normed/Hilbert spaces, Arzelà–Ascoli, Riesz representation, Hahn–Banach, open mapping, compact supports, definitions of \(L^p\), weak derivatives, and Sobolev spaces |
| [analysis/fourier_schwartz](analysis/fourier_schwartz/README.md) | `fourier_schwartz` | Schwartz spaces, Fourier formulas/preservation, Gaussian transform, inversion via approximate identities |
| [analysis/fourier_l2](analysis/fourier_l2/README.md) | `fourier_l2` | Parseval, unitary L² Fourier transform, bounded multipliers, weighted norms and integer-derivative comparisons |
| [analysis/distributions](analysis/distributions/README.md) | `distributions` | Test-function topology, continuous duals, injection of locally integrable functions, distribution derivatives/support/smoothing, Sobolev comparisons and diffeomorphism pullbacks |
| [analysis/euclidean_sobolev](analysis/euclidean_sobolev/README.md) | `euclidean_sobolev` | Integer-order Sobolev spaces, weak-derivative comparisons, duality, local coordinate changes and embeddings |
| [analysis/lp_spaces](analysis/lp_spaces/README.md) | `lp_spaces` | Real Lp/L∞ Banach structures, real/complex L2, density, translations, convolution/approximate identities |
| [analysis/measure_convergence](analysis/measure_convergence/README.md) | `measure_convergence` | Monotone convergence, Fatou, dominated convergence, a.e.-quotient integration, real/complex/finite-dimensional integration and series interchange |
| [analysis/complex_hilbert](analysis/complex_hilbert/README.md) | `complex_hilbert` | Complex Riesz representation, bounded adjoints, closed-subspace projections, finite-rank factorization and compact operators |
| [analysis/fredholm_operators](analysis/fredholm_operators/README.md) | `fredholm_operators` | Compact-operator ideals, Atkinson equivalence, kernel/cokernel indices, index laws and local constancy |
| [analysis/integration](analysis/integration/README.md) | `integration` | Riemann integration, Lebesgue integration via L¹ completion |
| [analysis/scalar_compatibility](analysis/scalar_compatibility/README.md) | `scalar_compatibility` | Shared real arithmetic, distance, limit and scalar compatibility examples |

## Geometry

| Location | Package | Contents |
| --- | --- | --- |
| [geometry/smooth_partitions](geometry/smooth_partitions/README.md) | `smooth_partitions` | Flat functions, compactly supported cutoffs, locally finite smooth partitions of unity, extension by zero and locally finite sums |
| [geometry/manifolds](geometry/manifolds/README.md) | `manifolds` | Atlases, smooth maps, tangent spaces and derivatives |
| [geometry/inverse_implicit](geometry/inverse_implicit/README.md) | `inverse_implicit` | Local inverses, parameterized implicit functions, constant-rank coordinates, regular-value submanifolds and tangent kernels |
| [geometry/morse_lemma](geometry/morse_lemma/README.md) | `morse_lemma` | Symmetric-form inertia, Morse coordinates, parameterized local normal forms, isolated critical points and locally constant indices |
| [geometry/boundary_manifolds](geometry/boundary_manifolds/README.md) | `boundary_manifolds` | Half-space/orthant charts, tangent cones and invariant derivatives, boundary/face tangent bundles, neat embeddings, products/intervals/disks |
| [geometry/manifold_gluing](geometry/manifold_gluing/README.md) | `manifold_gluing` | Collars, boundary gluing, smooth structures and comparison maps |
| [geometry/compact_embeddings](geometry/compact_embeddings/README.md) | `compact_embeddings` | Compact-manifold embeddings from finite charts/cutoffs, collar-compatible neat embeddings, stabilized relative embedding families |
| [geometry/tubular_neighborhoods](geometry/tubular_neighborhoods/README.md) | `tubular_neighborhoods` | Tubular neighborhoods, collapse maps, boundary comparisons and product/stabilization identities; requirements and checks remain partly unverified |
| [geometry/vector_bundles](geometry/vector_bundles/README.md) | `vector_bundles` | General real/complex bundles, locally constant rank, bundle maps/sections/pullbacks and universality |
| [geometry/bundle_operations](geometry/bundle_operations/README.md) | `bundle_operations` | Cocycle gluing, direct sums/tensors/duals/Hom/exterior powers, realification/complexification and pullback |
| [geometry/smooth_bundles](geometry/smooth_bundles/README.md) | `smooth_bundles` | Real/complex smooth bundles and metrics, duals/tensors/exterior powers, smooth frame actions/local diffeomorphisms, representation-associated bundles, tangent/normal comparisons |
| [geometry/bundle_connections](geometry/bundle_connections/README.md) | `bundle_connections` | Real/complex bundle connections, bundle-valued forms and induced connections, metric-compatible and Levi–Civita connections |
| [geometry/chern_weil](geometry/chern_weil/README.md) | `chern_weil` | Curvature, Bianchi identity, and closed trace forms for real vector bundles |
| [geometry/bundle_complements](geometry/bundle_complements/README.md) | `bundle_complements` | Metrics/finite embeddings from finite partitions, orthogonal complements, continuous-projection images and sets of isomorphism classes |
| [geometry/bundle_extension](geometry/bundle_extension/README.md) | `bundle_extension` | Tietze, neighborhood extension of bundles/maps/isomorphisms over closed subspaces, shrinking comparisons and stabilization |
| [geometry/grassmannians](geometry/grassmannians/README.md) | `grassmannians` | Finite Grassmannians, graph coordinates, universal bundles and stabilization |
| [geometry/grassmannian_cells](geometry/grassmannian_cells/README.md) | `grassmannian_cells` | Schubert coordinates, finite CW structures, oriented coverings, standard inclusions and stable finite-stage comparisons |
| [geometry/bundle_homotopy](geometry/bundle_homotopy/README.md) | `bundle_homotopy` | Bundle homotopy comparisons, relative extension along cofibrations, sphere clutching and gauge isomorphism criteria |
| [geometry/bundle_classification](geometry/bundle_classification/README.md) | `bundle_classification` | Finite classifying maps for real/complex bundles, stabilized homotopy classification, oriented/framed bundles and naturality |
| [geometry/tangent_bundles](geometry/tangent_bundles/README.md) | `tangent_bundles` | Tangent total spaces, tangent maps, functor laws, smooth fiber operations |
| [geometry/normal_bundles](geometry/normal_bundles/README.md) | `normal_bundles` | Immersion normal bundles, local orthonormal frames, direct-sum decompositions, base change and stabilization |
| [geometry/examples/tangent_normal](geometry/examples/tangent_normal/README.md) | `tangent_normal` | Euclidean tangent bundles, coordinate inclusions, parabolas, degenerate-degree examples |
| [geometry/lie_groups](geometry/lie_groups/README.md) | `lie_groups` | Lie groups/algebras, adjoint derivatives/exponentials, Lie structures on O/SO/Pin/Spin and complex extensions |
| [geometry/euclidean_forms](geometry/euclidean_forms/README.md) | `euclidean_forms` | Local differential forms, wedge products/exterior derivatives, coordinate expressions, pullbacks |
| [geometry/differential_forms](geometry/differential_forms/README.md) | `differential_forms` | Global differential forms, gluing, pullbacks, de Rham cohomology |
| [geometry/coordinate_calculus](geometry/coordinate_calculus/README.md) | `coordinate_calculus` | Calculus, local/global forms, manifolds and cohomology compatibility examples |

## Topology

[Guide to layout and dependencies within the field](topology/README.md).

| Location | Package | Contents |
| --- | --- | --- |
| [topology/basic](topology/basic/README.md) | `topology` | Topologies/subspaces, continuous maps, compactness, separation |
| [topology/metric](topology/metric/README.md) | `metric_spaces` | Metric topologies, metrization, real line, real-valued functions, finite partitions of unity |
| [topology/clutching_linearization](topology/clutching_linearization/README.md) | `clutching_linearization` | Laurent approximation, stable companion linearization, choice-independent spectral inverse classes, naturality/direct sums/basic-product inverse identities |
| [topology/k_theory](topology/k_theory/README.md) | `topological_k_theory` | Complex-bundle Grothendieck rings, stable isomorphism criteria, contravariant pullback, rank/reduced groups, finite discrete computations |
| [topology/relative_k_theory](topology/relative_k_theory/README.md) | `relative_k_theory` | Relative-triple/reduced-group comparisons, negative-degree exact sequences, excision, Mayer–Vietoris, external products, disk/sphere pairs |
| [topology/bott_product](topology/bott_product/README.md) | `bott_product` | Bott external-product maps, inverse comparisons and naturality |
| [topology/periodic_k_theory](topology/periodic_k_theory/README.md) | `periodic_k_theory` | Relative/reduced Bott isomorphisms, integer degrees, six-term exactness/naturality, point/sphere computations, iterated Bott generators |
| [topology/compact_support_k](topology/compact_support_k/README.md) | `compact_support_k` | Compactly supported K-groups, general bundle-triple comparisons, neighborhood independence, proper pullback and extension by zero |
| [topology/k_theory_thom](topology/k_theory_thom/README.md) | `k_theory_thom` | Complex Koszul classes, Thom isomorphisms via Bott/complements, pullback/direct sums/composition, real-bundle complexification |
| [topology/constructions](topology/constructions/README.md) | `topological_constructions` | Products, quotients, coproducts, gluing, compact-open topology |
| [topology/algebra](topology/algebra/README.md) | `topological_algebra` | Topological algebra, coordinate/matrix topologies, continuity criteria |
| [topology/homotopy](topology/homotopy/README.md) | `algebraic_topology` | Homotopies, pointed quotients, mapping cones, finite CW pairs, standard-simplex coordinates |
| [topology/thom_spaces](topology/thom_spaces/README.md) | `thom_spaces` | Disk/sphere bundles, Thom quotients, metric/suspension/direct-sum comparisons, finite CW pair types and relative singular theory |
| [topology/cohomology_thom](topology/cohomology_thom/README.md) | `cohomology_thom` | Relative Thom-class products/zero sections, fiber restrictions, standard-disk generators |
| [topology/puppe_sequences](topology/puppe_sequences/README.md) | `puppe_sequences` | CW cofibrations, iterated pointed cofibers/suspension comparisons, quotient comparisons, contravariant Hom exactness |
| [topology/fundamental](topology/fundamental/README.md) | `fundamental_groups` | Fundamental groupoids/groups, amalgamated van Kampen theorem, simple connectedness |
| [topology/coverings](topology/coverings/README.md) | `covering_spaces` | Covering lifts, subgroup/conjugacy classification, universal coverings and deck transformations |
| [topology/singular/cohomology](topology/singular/cohomology/README.md) | `singular_cohomology` | Singular chains/cochains, relative/reduced theories, homotopy invariance, path components and contractible spaces |
| [topology/singular/subdivision](topology/singular/subdivision/README.md) | `singular_subdivision` | Barycentric subdivision, small chains, open-cover/subspace comparisons |
| [topology/singular/products](topology/singular/products/README.md) | `singular_products` | Cup products on singular cochains/cohomology, Leibniz rules, units/associativity/naturality |
| [topology/singular/cap](topology/singular/cap/README.md) | `singular_cap` | Cap and relative products, Kronecker evaluation and adjunction formulas |
| [topology/singular/excision](topology/singular/excision/README.md) | `singular_excision` | Excision, Mayer–Vietoris, good-pair/quotient comparisons |
| [topology/singular/eilenberg_zilber](topology/singular/eilenberg_zilber/README.md) | `singular_eilenberg_zilber` | Alexander–Whitney/shuffle chain homotopy equivalence |
| [topology/singular/symmetry](topology/singular/symmetry/README.md) | `singular_symmetry` | Cup commutation homotopies and graded commutativity |
| [topology/singular/cech](topology/singular/cech/README.md) | `singular_cech` | Cover double complexes and projective-complex comparisons |
| [topology/singular/simplicial](topology/singular/simplicial/README.md) | `singular_simplicial` | Finite simplicial realizations, affine singular chains and product comparisons |
| [topology/singular/cellular](topology/singular/cellular/README.md) | `singular_cellular` | Finite CW cellular bases/attaching degrees, arbitrary-coefficient comparisons and naturality |
| [topology/singular/cellular_algebra](topology/singular/cellular_algebra/README.md) | `singular_cellular_algebra` | Relative-chain direct sums, Hom and comparison-map lemmas |
| [topology/singular/finite_algebra](topology/singular/finite_algebra/README.md) | `singular_finite_algebra` | Finite-model coefficient comparisons, universal coefficients and Künneth |
| [topology/singular/tensor_dual](topology/singular/tensor_dual/README.md) | `singular_tensor_dual` | Tensor/Hom comparison using finite dual bases |
| [topology/singular/tensor_bridge](topology/singular/tensor_bridge/README.md) | `singular_tensor_bridge` | Integer/nonnegative tensor-complex comparisons |
| [topology/singular/low_degree](topology/singular/low_degree/README.md) | `singular_low_degree` | Path-choice chain normalization and first cohomology of products |
| [topology/spheres](topology/spheres/README.md) | `sphere_maps` | Sphere orientations, reflection and circle integer-power degrees |
| [topology/examples/cohomology](topology/examples/cohomology/README.md) | `cohomology_models` | Empty/contractible/sphere computations and relative-theory examples |
| [topology/examples/finite_models](topology/examples/finite_models/README.md) | `cohomology_examples` | Finite graphs, torus, real projective plane: groups/products/induced maps |
| [topology/examples/cap](topology/examples/cap/README.md) | `cap_models` | Point, relative cross-product and connecting-map examples |
| [topology/examples/cells](topology/examples/cells/README.md) | `cell_spaces` | Group completion, homotopy, quotient/cell, matrix, finite-space and simplex examples |

## Type checking

Use [building and checking](USAGE.md) for package and workspace commands, shared caches, resource options and reports.
Package READMEs contain a scope summary, an API table and links to source, dependencies and shared checking instructions.
Detailed constructions and historical records are in [mathematical notes](../math/package-notes/README.md); syntax and macro examples are in the [standard-library guide](std/USAGE.md).

Examples: [complexes](algebra/homological/concrete_complexes/README.md), [coordinate calculus](geometry/coordinate_calculus/README.md), [cell_spaces](topology/examples/cells/README.md), [scalar compatibility](analysis/scalar_compatibility/README.md), [small categories](category/src/SmallCategories.ref), and [limits in the terminal category](category/src/TerminalLimits.ref).

[Singular cohomology examples](topology/examples/cohomology/README.md) check representative cochains, relative connecting maps, coefficient-induced maps, path components, and empty/point/interval computations.
[Finite-model examples](topology/examples/finite_models/README.md) compute groups and cohomology products using comparison maps with spaces.
