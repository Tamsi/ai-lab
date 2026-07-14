# Roadmap

Inspired by [AI-ML-Roadmap-from-scratch](https://github.com/aadi1011/AI-ML-Roadmap-from-scratch), but **personal**: only your resources, and every skill links to a [topic sheet](topics/) with **math + practice + build** separated.

## How to use

1. Pick a module below (order is a suggestion, not a prison)
2. Open the **topic** → follow links in order: Theory → Math → Practice → Build
3. Add notes in `notes/` · solve in `exercises/` · log in [PROGRESS.md](PROGRESS.md)

---

## Module 0 — Setup

| | Resource |
|---|---|
| Python + editor | your usual setup |
| This repo | `git clone` + `pip install numpy pytest` |

---

## Module 1 — Math for AI

| Topic | Sheet | Can implement in repo? |
|---|---|---|
| Dot product | [dot-product](topics/dot-product.md) | ✅ [exercises/dot-product](../exercises/dot-product/) |
| Matrix multiplication | [matrix-multiplication](topics/matrix-multiplication.md) | ✅ [exercises/matrix-multiplication](../exercises/matrix-multiplication/) |
| Linear algebra (vectors, transforms) | [linear-algebra](topics/linear-algebra.md) | 🔜 exercise when ready |
| Gradients & optimization | [gradient-descent](topics/gradient-descent.md) | 🔜 |
| Probability & statistics | [probability](topics/probability.md) | 🔜 |
| Discrete math / proofs | [discrete-math](topics/discrete-math.md) | notes only (MIT 6.042) |

**Your active courses:** [DL.AI Math](resources.md), [Udacity LA](resources.md), [3Blue1Brown LA](resources.md), [MIT 6.042 PDF](resources.md)

---

## Module 2 — Machine learning

| Topic | Sheet | Can implement? |
|---|---|---|
| Supervised learning | [supervised-learning](topics/supervised-learning.md) | 🔜 linear regression exercise |
| Loss functions (MSE, cross-entropy) | [loss-functions](topics/loss-functions.md) | 🔜 |
| Train / val / test | [model-evaluation](topics/model-evaluation.md) | 🔜 |

**Your active course:** [Coursera ML (Andrew Ng)](resources.md)

---

## Module 3 — Deep learning

| Topic | Sheet | Can implement? |
|---|---|---|
| Tensors & autograd | [tensors-autograd](topics/tensors-autograd.md) | 🔜 micrograd-style |
| Neural network (MLP) | [mlp](topics/mlp.md) | 🔜 |
| Backpropagation | [backpropagation](topics/backpropagation.md) | 🔜 |
| CNN | [cnn](topics/cnn.md) | 🔜 |
| RNN / sequences | [rnn](topics/rnn.md) | 🔜 |

**Your resources:** [Karpathy Zero to Hero](resources.md)

---

## Module 4 — LLMs & NLP

| Topic | Sheet | Can implement? |
|---|---|---|
| N-grams | [n-grams](topics/n-grams.md) | 🔜 |
| Tokenization (BPE) | [tokenization](topics/tokenization.md) | 🔜 |
| Attention | [attention](topics/attention.md) | 🔜 |
| **Encoder–decoder** | [encoder-decoder](topics/encoder-decoder.md) | 🔜 **example sheet** |
| Transformer | [transformer](topics/transformer.md) | 🔜 mini-GPT |
| SFT | [sft](topics/sft.md) | 🔜 |
| RL post-training | [rl-post-training](topics/rl-post-training.md) | 🔜 |

**Your resources:** [Karpathy LLM deep dive](resources.md), [CS229 LLM lecture](resources.md), [Transformers in Practice](resources.md), [papers/](papers/)

---

## Module 5 — CUDA & hardware

| Topic | Sheet | Can implement? |
|---|---|---|
| CUDA basics | [cuda](topics/cuda.md) | 🔜 (needs GPU + nvcc) |
| CPU vs GPU matmul | [gpu-matmul](topics/gpu-matmul.md) | 🔜 |

**Your resources:** [NVIDIA CUDA materials](resources.md)

---

## Module 6 — Reinforcement learning

| Topic | Sheet | Can implement? |
|---|---|---|
| MDP & policy gradients | [policy-gradients](topics/policy-gradients.md) | 🔜 tabular then CartPole |

---

## Legend

| Symbol | Meaning |
|---|---|
| ✅ | Exercise exists and tests pass |
| 🔜 | Planned — create `exercises/<name>/` when you start |
| notes only | Theory from book/paper, no code exercise yet |

## What we can realistically implement here

| Feasible now (NumPy / pure Python) | Needs PyTorch later | Needs GPU / CUDA |
|---|---|---|
| dot product, matmul, gradients | MLP, attention, tokenizer | CUDA kernels |
| linear/logistic regression | mini transformer, SFT loop | gpu matmul benchmark |
| n-grams, softmax | RNN, encoder-decoder toy | |
| tabular RL | policy gradient CartPole | |

Start small in Module 1–2, grow into Module 4 when Coursera + Karpathy foundations are in place.
