# Cap-product examples

Package: `cap_models`; public modules are declared in [src/root.ref](src/root.ref).
These examples use [singular cap products](../../singular/cap/README.md).

| Source | Example |
| --- | --- |
| [Point](src/Point.ref) | The integral cap-unit law on a discrete point in arbitrary chain degree |
| [RelativeCross](src/RelativeCross.ref) | Relative degree-zero homology cross products, representatives, and projection formulas |
| [Connecting](src/Connecting.ref) | Signed compatibility with relative cochain connecting maps |

The root also declares `Line`, but this checkout contains neither `src/Line.ref` nor `src/Line/root.ref`.
Package loading and type-check success therefore remain unconfirmed; the examples above describe the source files that are present.
See [checking the libraries](../../../USAGE.md) for current check commands and evidence requirements.
