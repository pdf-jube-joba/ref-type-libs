# `module_theory`

Modules over rings, free modules, direct sums, tensor products, exact sequences.

| Entry | Purpose |
| --- | --- |
| `module_theory.Module.Over` | Carriers/module structures, abelian homomorphism groups, submodules/kernels/images/quotients |
| `module_theory.Module.Over.FirstIsomorphism` | Kernel-quotient/image isomorphisms |
| `module_theory.Module.Over.Presentation` / `Free` | Formal-sum/relation modules, unique generator extensions, free-module projectivity |
| `module_theory.Module.Over.Free.Reindex.Injection.Retraction` | Left inverses along generator injections, free isomorphisms from bijections |
| `module_theory.Module.Over.Free.Subset.Projection` / `QuotientBasis` | Projections onto specified generators; quotients by their images identified with free modules on remaining generators |
| `module_theory.Module.Over.Free.Reindex.QuotientBasis` | Quotients by generator-map images and free modules on generators outside the image |
| `module_theory.Module.Over.Free.Coefficients` / `Finite` | Coefficient maps, finite-generator expansions, finite-support-function isomorphisms |
| `module_theory.Module.Over.Free.Induction` / `Subset` | Induction by module operations, spans of generator subsets, linear-image criteria |
| `module_theory.Module.Over.FiniteCoordinates` | Finite coordinates, standard expansions/free-set isomorphisms, head/tail decomposition, zero extension and zero-head-submodule isomorphisms |
| `module_theory.Module.Over.KernelTransport` | Kernel/cokernel isomorphisms under commuting base changes, quotient-class computations |
| `module_theory.Module.Over.Alternating` | Finite alternating sums, homomorphism compatibility, double-sum cancellation for face identities |
| `module_theory.Module.Over.Product` / `DirectSum` | Arbitrary products/sums, finite-support isomorphisms, component inclusions, sum universality/projectivity, `Generated.induction` via generators/operations |
| `module_theory.Module.Over.FinitelySupported` | Finite-support submodules of arbitrary module-family products |
| `module_theory.Module.Over.Biproduct` | Binary sums/products, projections/inclusions, pairing/copairing universality |
| `module_theory.Module.Over.ShortExact` / `ShortExactComparison` | Short exact sequences, splitting direct-sum isomorphisms, commuting-diagram comparisons |
| `module_theory.Module.Over.ExactFiveComparison` | Middle-map injectivity/surjectivity/isomorphisms in five-term exact diagrams |
| `module_theory.Module.Over.IsomorphismSquare` | Constructing inverses of remaining square edges from three isomorphic edges |
| `module_theory.Module.Over.Pushout.On` | Pushouts of two homomorphisms and unique maps from compatible maps |
| `module_theory.Module.Over.ShortExact.Pushout.On` | Short exact sequences pushed out along left coefficient maps |
| `module_theory.Module.Over.CanonicalFree` / `FreeResolution` | Free-on-elements surjections, iterated kernels, projective terms and adjacent-differential exactness |

[Source](src/root.ref) · [Dependencies](ref.toml) · [Checking](../../USAGE.md)
