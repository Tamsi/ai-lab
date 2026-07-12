# Matrix Multiplication

## Intuition

Matrix multiplication composes linear transformations. If **A** transforms space
one way and **B** another, then **AB** applies **B** first, then **A** (when
acting on column vectors: **ABx** = **A(Bx)**).

Each entry of the product is a dot product: row meets column.

## Formal definition

For **A** ∈ ℝᵐˣⁿ and **B** ∈ ℝⁿˣᵖ:

**C** = **AB** ∈ ℝᵐˣᵖ

Cᵢⱼ = Σₖ Aᵢₖ Bₖⱼ

**Dimension rule:** inner dimensions must match (n = n). Outer dimensions give the
result shape (m × p).

## Geometric interpretation

- Each column of **AB** is **A** applied to the corresponding column of **B**
- Each row of **AB** is a linear combination of rows of **B**, weighted by a row of **A**
- Not commutative: **AB** ≠ **BA** in general

## Why it matters in machine learning

- **Neural network layers**: **y** = **Wx** + **b** is matrix-vector multiplication
- **Attention**: **QKᵀ** is a batch of dot products between queries and keys
- **Batch processing**: stacking inputs as rows/columns enables parallel linear transforms
- **GPUs** are optimized for large dense matrix multiplies (GEMM)

## Minimal implementation

```python
def matmul(A, B):
  m, n = len(A), len(A[0])
  n_b, p = len(B), len(B[0])
  if n != n_b:
    raise ValueError(f"Incompatible shapes: ({m},{n}) x ({n_b},{p})")
  C = [[0.0] * p for _ in range(m)]
  for i in range(m):
    for j in range(p):
      for k in range(n):
        C[i][j] += A[i][k] * B[k][j]
  return C
```

## Experiment

1. Implement triple-nested-loop matmul vs NumPy `@`
2. Time both for sizes 64, 256, 1024
3. Record speedup ratio in `exercises/numpy/matrix_multiplication/results.md`

## Connection to research papers

Every Transformer layer is dominated by matrix multiplications (projections for
Q, K, V, output, and MLP weights). Hardware throughput for GEMM largely
determines training cost.

## What I still do not understand

- Exact memory hierarchy effects (cache blocking, tiling) that make GPU matmul fast
- When to use einsum vs explicit matmul for readability and performance
