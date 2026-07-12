# CUDA

Notes and references for GPU programming with NVIDIA CUDA. Part of
[Milestone 4: Computer architecture and GPU](../../../ROADMAP.md#milestone-4-computer-architecture-and-gpu).

## Recommended reading order

1. [An Even Easier Introduction to CUDA](https://developer.nvidia.com/blog/even-easier-introduction-cuda/) — gentle entry point: kernels, threads, blocks, `cudaMalloc` / `cudaMemcpy`
2. [CUDA Programming Guide](https://docs.nvidia.com/cuda/cuda-programming-guide/index.html) — canonical reference (memory model, execution model, streams, cooperative groups)
3. Official lab exercises — see [exercises/cuda/](../../../exercises/cuda/)

## What to capture in concept notes

Each note in this folder should follow the repo template:

- Intuition (CPU vs GPU, SIMT, warps)
- Formal definition (launch config, memory spaces)
- Minimal implementation (host + device code snippet)
- Experiment (timing, occupancy, or correctness check)
- What I still do not understand

## Planned topics

- [ ] Thread hierarchy (grid → block → thread)
- [ ] Global, shared, and constant memory
- [ ] Memory coalescing and bank conflicts
- [ ] Streams and overlap (H2D / compute / D2H)
- [ ] Profiling with Nsight

## Related

- `notes/computer-systems/gpu/` — architecture before programming
- `projects/gpu-matmul-lab/` — capstone: compare CPU vs GPU matmul
- `exercises/cuda/` — hands-on NVIDIA-style exercises
