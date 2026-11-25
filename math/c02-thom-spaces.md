# C02 Disk bundles, sphere bundles, and Thom spaces

## Requirements

- Primary implementation: `thom_spaces`.
- Construct disk/sphere bundles and their Thom quotient for real and complex metric bundles.
- Prove metric-independent comparisons, suspension presentations of trivial bundles, and direct-sum/iterated-Thom comparisons.
- Construct finite CW types of bundle pairs over finite CW bases, cofibrations, and connections to relative singular theory.

## Dependencies

- [Bundle metrics, complements, and isomorphism classes](../libs/geometry/bundle_complements/README.md)
- [K02 CW cofibrations and Puppe sequences](../libs/topology/puppe_sequences/README.md)
- [B04 Bundle homotopy invariance and clutching](../libs/geometry/bundle_homotopy/README.md)

## ImplementationStatus

Implemented: [thom_spaces](../libs/topology/thom_spaces/README.md).
Constructed real/complex metric disk and sphere bundles, pointed Thom quotients, homeomorphisms between arbitrary continuous metrics, and direct-sum/iterated-Thom comparisons.
Trivial bundles are homeomorphic to disk-suspension models of real dimensions \(n\)/\(2n\), also compared with arbitrary natural-degree iterated existing suspensions.

Over finite CW bases, constructed pair homotopy equivalences from actual bundle pairs to finite CW complexes/subcomplexes using B04 cell trivializations.
Real/complex entry: `FiniteBase.pairFiniteType`; `PairModel` exposes finite models and both subspace-preserving homotopies.
Also proved cellular approximation of attaching maps, pair comparisons for arbitrary cell attachments, and finite CW structures on subcomplexes with induced topology.
Connected sphere-boundary cofibrations, Puppe comparisons, relative singular theory of actual disk/sphere pairs after excising the added point, and relative finite-CW-model comparisons.
Check real/complex examples including rank zero and empty bases.
