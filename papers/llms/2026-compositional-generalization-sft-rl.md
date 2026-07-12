# From Reasoning Traces to Reusable Modules: Understanding Compositional Generalization in Language Model Reasoning

## Metadata

- Authors: Kong et al.
- Year: 2026
- Link: https://www.alphaxiv.org/abs/2606.18089
- arXiv: https://arxiv.org/abs/2606.18089
- Topic: LLM post-training, SFT + RL, compositional generalization
- Status: first read

## Problem

Why does combining **SFT** then **RL** produce stronger reasoning than either alone?
The authors frame reasoning as composition of reusable atomic modules (skills + routing).

## Core idea

1. Reasoning traces are built from discrete latent selections (atomic modules).
2. **SFT** provides compound traces containing raw module material.
3. **RL** decomposes traces and enables recombination → compositional generalization.
4. Training on **compound traces** beats isolated atomic modules alone.

## Concepts to deepen

| Concept | Priority | Note | Exercise | I understand? |
|---|---|---|---|---|
| **SFT** | high | [supervised-fine-tuning](../../notes/llms/supervised-fine-tuning.md) | [sft_mini](../../exercises/pytorch/sft_mini/) | [ ] |
| **RL post-training** | high | [rl-post-training](../../notes/llms/rl-post-training.md) | [rl_policy_gradient_cartpole](../../exercises/pytorch/rl_policy_gradient_cartpole/) | [ ] |
| **N-grams** | high | [n-grams](../../notes/llms/n-grams.md) | [ngrams_language_model](../../exercises/pytorch/ngrams_language_model/) | [ ] |
| Compositional generalization | medium | — | — | [ ] |
| Latent module selection | low | — | — | [ ] |

## Required knowledge

- [ ] Language modeling loss (cross-entropy)
- [ ] Supervised fine-tuning on (prompt, response) pairs
- [ ] Policy gradients / RL on token or sequence level
- [ ] N-gram language models as baselines
- [ ] Generalization vs memorization

## Key equations

_(Fill while reading — especially SFT loss and RL objective used in experiments.)_

### SFT objective

- Inputs: model π_θ, dataset of reasoning traces
- Optimized: cross-entropy on demonstrated tokens
- Intuition: teach the model to imitate expert traces

### RL objective

- Inputs: reward on full traces or partial correctness
- Optimized: expected reward under policy
- Intuition: discover which sub-skills matter and recombine them

## Training procedure

1. Collect or construct compositional reasoning traces
2. **SFT** phase — imitate full compound traces
3. **RL** phase — explore novel compositions with reward signal
4. Evaluate on held-out compositional configurations

## Experiments

- Controlled synthetic tasks (module composition)
- Compare: SFT only, RL only, SFT→RL, atomic-only training

## Mini reproduction

Smallest useful slice:

1. Train a tiny **n-gram** or small LM baseline on synthetic sequences
2. Implement a minimal **SFT** loop on (input, output) pairs in PyTorch
3. Add a toy **RL** step (bandit or short horizon) before scaling to full LLM

## Questions

- Where exactly do **n-grams** appear in the experimental setup?
- How is the reward defined for reasoning traces?
- What is the difference between this RL and standard RLHF/PPO pipelines?

## What I still do not understand

- Formal definition of "atomic module" in the hierarchical latent model
- Why RL decomposes but SFT alone does not
- Practical hyperparameters for SFT→RL handoff

## Related concepts to study

- [ ] [SFT](../../notes/llms/supervised-fine-tuning.md)
- [ ] [RL post-training](../../notes/llms/rl-post-training.md)
- [ ] [N-grams](../../notes/llms/n-grams.md)
- [ ] [Policy gradients](../../notes/reinforcement-learning/policy-gradients.md)
