# `bundle_homotopy`

Bundle homotopy comparisons, relative extension along cofibrations, sphere clutching and gauge isomorphism criteria.

APIs specialize `Homotopy.Over`. Endpoint comparisons use compact Hausdorff bases; real clutching isomorphism criteria require gauges on both disks.

| Entry | Purpose |
| --- | --- |
| `Cylinder.endpointIsomorphismExists` | Compare bundle endpoints over compact-Hausdorff/interval products |
| `For.Pullbacks.Along` / `Relative` | Compare homotopic pullbacks, prove identity on fixed subsets |
| `For.Extensions` / `To` | Relative automorphism/isomorphism extension along cofibrations |
| `For.Contractible` / `Disks.Triviality` | Trivialize arbitrary bundles over contractible compact spaces/closed disks |
| `Clutching.With` / `Pullback` | Construct two-open-set transition bundles and pullback comparisons |
| `Clutching.Homotopy` / `With.Sum` / `With.Stabilize` | Send transition homotopies, block sums, stabilization to isomorphisms |
| `Disks.Hemispheres.Cover` | Actual two-disk-pushout/sphere homeomorphisms, closed-hemisphere gluing |
| `Disks.Clutched` / `Homotopy` | Boundary GL clutching and disk-restriction trivializations |
| `Disks.Clutched.Comparison.diskGaugeCriterion` | Equivalence of compatible boundary gauges on both disks and bundle isomorphisms |
| `Homotopy.Examples.Mobius` / `CircleLine` | Real sign-transition and complex unit-circle-transition lines |

[Source](src/root.ref) · [Dependencies](ref.toml) · [Checking](../../USAGE.md) · [Notes](../../../math/package-notes/geometry/bundle_homotopy.md)
