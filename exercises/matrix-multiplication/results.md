# Matrix Multiplication — Results

## Benchmarks

Run `python -m exercises.numpy.matrix_multiplication.exercise` and paste timings here.

| Size (n×n) | Loop (s) | NumPy (s) | Speedup |
|---|---|---|---|
| 32 | _run locally_ | _run locally_ | _run locally_ |
| 64 | | | |
| 128 | | | |

## Observations

- Loop implementation is O(n³) — same asymptotic complexity as optimized GEMM, but
  constant factors differ enormously (Python interpreter vs BLAS/CUDA).
- Each output entry is a dot product between a row and a column.
- Neural network layers are batched matrix multiplies; GPU throughput on GEMM
  dominates training time for large models.

## Failures / surprises

_(Update after running benchmarks on your machine.)_

## Conclusions

Understanding loop matmul makes the dimension rules and attention projections
concrete. NumPy (and later GPU kernels) exist because this operation is the
computational backbone of deep learning.
