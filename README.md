# AI Foundations Lab

A public learning laboratory dedicated to understanding modern artificial
intelligence from mathematics to hardware.

The goal is not only to use machine learning libraries, but to understand:

- the mathematics behind machine learning;
- how neural networks learn;
- how Transformers and LLMs work;
- how hardware constraints shape model architectures;
- how reinforcement learning and world models operate;
- how to read and reproduce AI research papers.

## Learning principle

Every important concept should be explored through four layers:

1. **Intuition** — what does it mean geometrically or conceptually?
2. **Mathematics** — formal definitions and derivations
3. **Implementation** — code from scratch (or minimal dependencies)
4. **Experimentation** — plots, benchmarks, and observed behavior

Each layer connects through a simple triangle:

```text
   Equation
      ↕
    Code
      ↕
Visualization
```

## Current focus

- [x] Repository structure and learning workflow
- [ ] Mathematical foundations
- [ ] Linear algebra
- [ ] Probability and statistics
- [ ] Computer architecture
- [ ] Machine learning from scratch
- [ ] Deep learning
- [ ] Transformers and LLMs
- [ ] GPU programming
- [ ] Reinforcement learning
- [ ] World models

## Main projects

| Project | Goal | Status |
|---|---|---|
| [Gradient Playground](projects/gradient-playground/) | Visualize optimization algorithms | Planned |
| [Tiny Autograd](projects/tiny-autograd/) | Implement automatic differentiation | Planned |
| [Mini Transformer](projects/mini-transformer/) | Build a small language model | Planned |
| [GPU Matmul Lab](projects/gpu-matmul-lab/) | Compare CPU and GPU matrix operations | Planned |
| [Latent World Model](projects/latent-world-model/) | Predict environment dynamics | Planned |

## Repository map

| Directory | Purpose |
|---|---|
| `notes/` | Concept notes (intuition → math → ML relevance) |
| `exercises/` | Hands-on exercises with tests and reflection |
| `implementations/` | Standalone algorithm implementations |
| `experiments/` | Benchmarks and visual explorations |
| `papers/` | Paper reading sheets |
| `projects/` | Progressive portfolio projects |
| `assets/` | Diagrams and plots |
| `tests/` | Shared test utilities |

## Weekly rhythm (~8 h/week)

| Activity | Time |
|---|---|
| Course or reading | 2 h |
| Math exercises | 2 h |
| Implementation | 2 h |
| Paper (alphaXiv) | 1 h |
| Documentation and review | 1 h |

**Minimum weekly output:** one concept note, one implemented exercise, one plot or benchmark, one entry in [PROGRESS.md](PROGRESS.md).

## References

- [3Blue1Brown — Linear Algebra](https://www.youtube.com/watch?v=fNk_zzaMoSs&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)
- [3Blue1Brown — Calculus](https://www.youtube.com/watch?v=NosYmlLLFB4&list=PLVUDmbpupCaqz8nECyVys-tFkUs--OKsY)
- [DeepLearning.AI — Transformers in Practice](https://learn.deeplearning.ai/courses/transformers-in-practice/)
- [Udacity — Agentic AI](https://www.udacity.com/course/agentic-ai--nd900)

## Related documents

- [ROADMAP.md](ROADMAP.md) — milestones and learning path
- [PROGRESS.md](PROGRESS.md) — weekly progress log
- [GLOSSARY.md](GLOSSARY.md) — vocabulary and notation
