# Homological algebra examples

| Module | Constructions checked |
| --- | --- |
| `BasicComplexes` | Zero/concentrated complexes, identity cones and signs |
| `Cyclic` / `Extensions` | Ext¹/Tor₁ of \(\mathbb Z/2,\mathbb Z/4\), coefficient maps, extension classes |
| `Cyclic.ProjectiveCoefficient` | \(\operatorname{Tor}_n(\mathbb Z/2,\mathbb Z)=0\)、\(n>0\) |
| `Cyclic.DoubleTensor.Balanced` / `BalancedExact` | Both resolution comparisons, variable swaps, connecting maps |
| `ExactSequences` | \(0\to\mathbb Z\to\mathbb Z^2\to\mathbb Z\to0\) and naturality |
| `Finite` | Nondiagonal three-term integer complexes, basis changes, generators/induced maps |
| `Finite.Bounded.UniversalCoefficient` | Ext¹/Hom and tensor/Tor₁ short exact sequences and splittings |
| `Finite.Bounded.IntegerTor` / `IntegerTensor.Selected` | Total-degree-three Tor term \(\mathbb Z/2\), generator lifts/projections |
| `Finite.Bounded.IntegerTensorNaturality` | Both short-exact squares under nontrivial basis changes |
| `Field.Tensor` | Canonical external products, splitting changes, swap signs, left/right units |

[Build and check](../../../USAGE.md) from the repository root:

```sh
cargo run --manifest-path ref-type/Cargo.toml -p cli -- libs/algebra/homological/concrete_complexes --module concrete_complexes --memory-mib 15872 --diagnostics compact
```

Select examples with `--module concrete_complexes.Finite.Bounded.UniversalCoefficient` and similar options.
