# Matrix Multiplication from Scratch

## Objective

Implement matrix multiplication with Python loops, then benchmark against NumPy
for increasing matrix sizes.

## Constraints

- Triple-nested loops for the reference implementation
- NumPy allowed for verification and timing
- No `np.matmul` / `@` inside your loop implementation

## Tasks

1. Implement `matmul(A, B)` with explicit loops
2. Verify against NumPy for random matrices
3. Benchmark sizes 64, 256, and 1024 (if feasible on your machine)
4. Record timings and speedup in `results.md`
5. Write a short note on why GPUs accelerate this operation

## Reflection

- What is the computational complexity O(?)?
- Why does Python loop performance collapse at large n?
- How does this connect to neural network forward passes?
