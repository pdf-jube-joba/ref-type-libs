# G01 Smooth bump functions and partitions of unity

## Requirements

- Primary implementation: `smooth_partitions`.
- Construct smooth cutoffs for Euclidean compact sets and open neighborhoods; prove support and all-order derivative properties.
- Construct locally finite cover refinements and smooth partitions of unity on second-countable manifolds; expose finite compact versions.
- Expose support-conditional extension by zero for functions/sections on open sets and smoothness of locally finite sums.

## Dependencies

None.

## Implementation

- [x] Implemented in `smooth_partitions`.
- [x] Constructed flat functions from exponentials; proved all-order partial derivatives and boundary vanishing.
- [x] Proved Euclidean compact-set/open-neighborhood cutoffs, value one on open neighborhoods, compact support, and support inclusion.
- [x] Selected countable subcovers from local bumps on second-countable Hausdorff manifolds; constructed smooth partitions with locally finite supports and open refinements.
- [x] Published the finite version for compact manifolds.
- [x] Published support-conditional extension by zero for functions and sections in local fiber coordinates.
- [x] Published smoothness of locally finite sums on Euclidean spaces and manifolds.
- [x] Added real-line cutoff/partition examples and finite partitions on zero-dimensional compact manifolds.

See [smooth_partitions](../../libs/geometry/smooth_partitions/README.md) for the public API and proof structure.

Standard checks at implementation commit `51799530317db36f73adc63a2d9b2aa743378414` passed all 1,883 target/dependency modules and all 10,233 repository modules.
Full check: 9,538 newly checked, 695 reused, 0 save failures or corrupt reads; source agreement confirmed.
Final `periodic_k_theory` recovered one worker under a 10 GiB virtual-memory limit, resumed from a checkpoint, and passed.
