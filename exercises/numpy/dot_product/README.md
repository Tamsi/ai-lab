# Dot Product from Scratch

## Objective

Implement the dot product without NumPy, then compare with NumPy and explore
geometric cases (aligned, opposite, orthogonal vectors).

## Constraints

- Pure Python for the core `dot_product` function
- NumPy allowed only for verification and optional benchmarks
- No `numpy.dot` inside your implementation

## Tasks

1. Implement `dot_product(x, y)` with explicit summation
2. Verify against NumPy for random vectors
3. Compute dot products for aligned, opposite, and orthogonal pairs
4. Relate results to cos(θ) using the geometric formula
5. Record observations in `results.md`

## Reflection

- What happens when vectors have different lengths?
- How does normalization relate to cosine similarity?
- Where does the dot product appear in a single linear layer?
