# AI Foundations Lab

A public learning laboratory focused on **math for AI**, **CUDA**, and **how LLMs work**
— with supporting tracks in ML, RL, CNNs, RNNs, and tensors.

**Start here:** [FOCUS.md](FOCUS.md) · [EXERCISES.md](exercises/EXERCISES.md) · [papers/READING-QUEUE.md](papers/READING-QUEUE.md)

## Learning pillars

| Pillar | What you build |
|---|---|
| **Math for AI** | Linear algebra, probability, optimization, softmax/cross-entropy |
| **CUDA** | Kernels, memory, GPU matmul |
| **LLMs** | N-grams → tokenization → attention → Transformer → SFT → RL post-training |

## Supporting tracks

Tensors · ML basics · CNN · RNN · Reinforcement learning

Full concept map: [CONCEPTS.md](CONCEPTS.md)

## Paper-driven learning

Read papers on [alphaXiv](https://www.alphaxiv.org/), list concepts to deepen, link to notes and exercises.

Example: [2606.18089](https://www.alphaxiv.org/abs/2606.18089) → SFT, RL, n-grams → [paper sheet](papers/llms/2026-compositional-generalization-sft-rl.md)

## Submit exercises

```bash
pip install numpy pytest matplotlib
python scripts/submit.py numpy/dot_product
```

See [exercises/SUBMISSION.md](exercises/SUBMISSION.md).

## Learning principle

Every concept: **Intuition → Math → Code → Experiment**

```text
   Equation  ↔  Code  ↔  Visualization
```

## Main projects

| Project | Goal | Status |
|---|---|---|
| [Gradient Playground](projects/gradient-playground/) | Visualize optimization | Planned |
| [Mini Transformer](projects/mini-transformer/) | Small language model | Planned |
| [GPU Matmul Lab](projects/gpu-matmul-lab/) | CPU vs GPU matmul | Planned |
| [Tiny Autograd](projects/tiny-autograd/) | Autograd engine | Planned |

## Repository map

| Directory | Purpose |
|---|---|
| `notes/` | Concept notes |
| `exercises/` | Exercises + [submission registry](exercises/submissions/registry.json) |
| `papers/` | [Reading queue](papers/READING-QUEUE.md) + paper sheets |
| `projects/` | Portfolio projects |
| `scripts/submit.py` | Verify exercise submissions |

## References

### Mathematics and ML

- [3Blue1Brown — Linear Algebra](https://www.youtube.com/watch?v=fNk_zzaMoSs&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)
- [3Blue1Brown — Calculus](https://www.youtube.com/watch?v=NosYmlLLFB4&list=PLVUDmbpupCaqz8nECyVys-tFkUs--OKsY)
- [DeepLearning.AI — Transformers in Practice](https://learn.deeplearning.ai/courses/transformers-in-practice/)
- [Karpathy — Neural Networks: Zero to Hero](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ)

### CUDA

- [An Even Easier Introduction to CUDA](https://developer.nvidia.com/blog/even-easier-introduction-cuda/)
- [CUDA Programming Guide](https://docs.nvidia.com/cuda/cuda-programming-guide/index.html)
- [CUDA Zone Exercises (PDF)](https://www.nvidia.com/content/cudazone/download/Exercise_Instructions.pdf)

## Documents

- [FOCUS.md](FOCUS.md) — your priorities
- [CONCEPTS.md](CONCEPTS.md) — notions to learn
- [EXERCISES.md](exercises/EXERCISES.md) — exercise catalog + verify commands
- [COURSES.md](COURSES.md) — external courses
- [PROGRESS.md](PROGRESS.md) — weekly log
