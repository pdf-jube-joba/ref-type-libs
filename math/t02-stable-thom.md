# T02 Stable homotopy classes and Thom spectra

## Requirements

- Primary implementation: `stable_thom_spaces`.
- Construct pointed-sphere homotopy classes, suspension maps, and stable homotopy groups as their direct limits.
- Construct MO, MSO, and the framed sphere spectrum from finite-Grassmannian universal Thom spaces and structure maps.
- Prove finite-stage presentations, stabilization, direct-sum products, and signs; expose APIs for downstream finite-stage representatives.

## Dependencies

- [B06 Bundle classifying maps and stabilization](b06-bundle-classification.md)
- [C02 Disk bundles, sphere bundles, and Thom spaces](c02-thom-spaces.md)
- [K02 CW cofibrations and Puppe sequences](../libs/topology/puppe_sequences/README.md)
- [B08 Grassmannian cell decompositions](b08-grassmannian-cells.md)

## Implementation

[stable_thom_spaces](../libs/topology/stable_thom_spaces/README.md) provides the pointed-sphere class sets, their suspension maps, the sequential direct limit with its universal property, and the common-stage homotopy criterion for representatives. The sphere spectrum supplies concrete structure maps. The finite real and oriented Grassmannian Thom spaces use the tautological projection bundle. The finite unoriented rank structure map adds a line and descends from the suspension cylinder to the target Thom quotient.

The abelian group laws on the stable class sets, finite ambient factorization, the compatibility of rank structure maps with ambient stabilization, the oriented rank structure maps, and direct-sum products and signs remain open.
