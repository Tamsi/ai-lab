# CUDA Exercises

Hands-on GPU programming exercises. Start with the official NVIDIA lab sequence, then
add original exercises tied to this repo's notes and projects.

## Primary source

- [CUDA Zone — Exercise Instructions (PDF)](https://www.nvidia.com/content/cudazone/download/Exercise_Instructions.pdf)

Work through the PDF labs in order. For each lab, create a subfolder when you
implement it locally:

```text
exercises/cuda/<lab-name>/
├── README.md          # objectives, constraints, reflection
├── kernel.cu          # or .cu + host driver
├── Makefile / CMake   # build instructions
├── test_*.py          # optional correctness checks from host
└── results.md         # timings, failures, conclusions
```

## Supporting references

- [An Even Easier Introduction to CUDA](https://developer.nvidia.com/blog/even-easier-introduction-cuda/)
- [CUDA Programming Guide](https://docs.nvidia.com/cuda/cuda-programming-guide/index.html)

## Constraints (repo convention)

- Document build flags (`nvcc`, architecture sm_XX) in each lab README
- Record GPU model and driver version in `results.md`
- Prefer small, verifiable kernels before optimizing
- Commit `results.md` insights; large binaries and build artifacts stay out of git

## Milestone link

These exercises support **Milestone 4** and feed into
[GPU Matmul Lab](../../projects/gpu-matmul-lab/).

## Status

| Lab | Status |
|---|---|
| NVIDIA official sequence (PDF) | Not started |
| [lab_01_vector_add](lab_01_vector_add/) | Scaffold |
| [lab_02_matrix_multiply_naive](lab_02_matrix_multiply_naive/) | Scaffold |
| [lab_03_shared_memory_tiling](lab_03_shared_memory_tiling/) | Scaffold |
