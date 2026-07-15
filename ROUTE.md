# Learning route — AI from scratch

For a post–high-school student with basic maths and some Python.  
**Do not start with LLM, Agentic AI, or RLHF.** They depend on everything below.

You have **Udacity** — this route uses it where it fills gaps Karpathy does not cover (CNN, RNN/LSTM, structured PyTorch projects).

---

## The order (overview)

```text
Step 1  Classical ML              Coursera Andrew Ng
Step 2  Math (parallel)           3Blue1Brown + DL.AI Math
Step 3  DL from scratch           Karpathy Zero to Hero L1–L5
Step 4  CNN & sequence models     Karpathy L6 + Udacity Deep Learning ND
Step 5  LLMs & Transformers       Karpathy L7–L8, TIP, Deep Dive
Step 6  Post-training             SFT, RLHF
Step 7  Agentic AI                Udacity nd900 — last
```

---

## What each topic covers (honest map)

| Topic | Covered? | Where |
|---|---|---|
| Loss, gradient descent, regularization | ✅ | Step 1 |
| Linear algebra, calculus, probability | ✅ | Step 2 |
| Tensors, autograd, backprop, MLP | ✅ | Step 3 (Karpathy) |
| N-grams, char-level LM | ✅ | Step 3 L2 (makemore bigrams) |
| **CNN** (conv, pooling, ResNet, transfer learning) | ✅ | **Step 4** — Udacity DL Course 2 + Karpathy L6 |
| **RNN / LSTM / GRU** | ✅ | **Step 4** — Udacity DL Course 3 |
| Seq2Seq, attention (before full transformer) | ✅ | Step 4 — Udacity DL Course 3 |
| Self-attention, GPT, BPE | ✅ | Step 5 |
| KV cache, quantization, inference | ✅ | Step 5 — TIP + Deep Dive |
| SFT, RLHF | ✅ | Step 6 |
| Agents, RAG, tool use | ✅ | Step 7 |
| GANs / diffusion | optional | Udacity DL Course 4 — skip unless curious |

**Why it felt incomplete:** Karpathy *Zero to Hero* jumps from MLP → a CNN detour (L6) → **GPT (L7)**. It never teaches classic RNN/LSTM, and L6 alone is not a full CNN course. Step 4 fixes that.

---

## Step 1 — Classical machine learning

### What you learn

The core loop of all ML:

> Given examples `(X, y)`, define a **loss**, minimize it with **gradient descent**, and avoid **overfitting** with train/validation splits and regularization.

### What you should be able to explain after

- Linear & logistic regression
- Train / validation / test splits
- Bias–variance, regularization
- Gradient descent on a loss surface
- Neural networks as stacked non-linear layers (last weeks of the course)

### Course (start here)

| # | Resource | Link |
|---|---|---|
| 1.1 | **Coursera — Machine Learning (Andrew Ng)** | https://www.coursera.org/learn/machine-learning |
| 1.2 | Weeks 1–3 — regression, classification, regularization | same course |
| 1.3 | Weeks 4–6 — neural networks, advice for ML projects | same course |
| 1.4 | Remaining weeks — SVM, trees, clustering, anomaly detection | same course |

Finish the **full course** — not only the first 3 weeks.

---

## Step 2 — Math for ML (run in parallel with Step 1)

### What you learn

Vectors, dot products, matrices, derivatives, chain rule, probability — the maths behind neural nets and attention.

### What you should be able to explain after

- Dot product = similarity / projection (attention uses this)
- Matrix × vector = one linear layer
- Chain rule = backprop

### Videos (intuition first)

| # | Resource | Lesson |
|---|---|---|
| 2.1 | 3Blue1Brown — Linear Algebra | [Ep.1 Vectors](https://www.youtube.com/watch?v=fNk_zzaMoSs) |
| 2.2 | 3Blue1Brown — Linear Algebra | [Ep.3 Linear transformations](https://www.youtube.com/watch?v=kYB8IZa5AuE) |
| 2.3 | 3Blue1Brown — Linear Algebra | [Ep.4 Matrix multiplication](https://www.youtube.com/watch?v=XkY2DOUCWMU) |
| 2.4 | 3Blue1Brown — Linear Algebra | [Ep.9 Dot products](https://www.youtube.com/watch?v=LyGKycYT2v0) |
| 2.5 | 3Blue1Brown — Calculus | [Ch.2 Derivative](https://www.youtube.com/watch?v=9vKqVkMQHKk) |
| 2.6 | 3Blue1Brown — Calculus | [Ch.4 Chain rule](https://www.youtube.com/watch?v=YG15m2VwSjA) |
| 2.7 | 3Blue1Brown — Deep Learning | [Gradient descent @ 06:55](https://www.youtube.com/watch?v=IHZwWFHWa-w&t=415) |

**Playlists:** [Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) · [Calculus](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr)

### Structured courses

| # | Resource | Link |
|---|---|---|
| 2.8 | DeepLearning.AI — Math for ML | https://learn.deeplearning.ai/specializations/mathematics-for-machine-learning-and-data-science |
| 2.9 | — Linear Algebra Applied I | https://learn.deeplearning.ai/specializations/mathematics-for-machine-learning-and-data-science/lesson/chi9v/linear-algebra-applied-i |
| 2.10 | — Linear Algebra Applied II | https://learn.deeplearning.ai/specializations/mathematics-for-machine-learning-and-data-science/lesson/0q26g/linear-algebra-applied-ii |
| 2.11 | — Gradients (Course 2) | same specialization |
| 2.12 | — Probability (Course 3) | same specialization |
| 2.13 | **Udacity — Linear Algebra Essentials** | https://www.udacity.com/course/linear-algebra-essentials--cd0667 |

---

## Step 3 — Deep learning from scratch (Karpathy)

### What you learn

Build autograd, backprop, and training loops **by hand**. Understand tensors and MLPs before PyTorch abstractions and before CNN/RNN.

### What you should be able to explain after

- Forward vs backward pass
- What `loss.backward()` computes
- N-grams and why neural nets beat count-based models
- How a char-level MLP predicts the next character

### Prerequisites

Step 1 underway. Step 2 videos 2.1–2.7 watched.

### Videos + labs

| # | Video | Lab |
|---|---|---|
| 3.1 | [L1 micrograd](https://www.youtube.com/watch?v=VMj-3S1tku0) | https://github.com/karpathy/micrograd |
| 3.2 | [L2 makemore bigrams](https://www.youtube.com/watch?v=PaCmpygFfXo) | https://github.com/karpathy/makemore |
| 3.3 | [L3 makemore MLP](https://www.youtube.com/watch?v=TCH_1BHY58I) | makemore repo |
| 3.4 | [L4 activations & BatchNorm](https://www.youtube.com/watch?v=P6sfmUTpUmc) | makemore repo |
| 3.5 | [L5 backprop ninja](https://www.youtube.com/watch?v=q8SA3rM6ckI) | makemore repo |

**Playlist:** https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ  
**Clone once:** `git clone https://github.com/karpathy/nn-zero-to-hero`

### Supplement

| Resource | Link |
|---|---|
| 3Blue1Brown — Backpropagation | https://www.youtube.com/watch?v=Ilg3gGewQ5U |

**Gate:** L1–L3 done before Step 4.

---

## Step 4 — CNN & sequence models (RNN → attention)

### What you learn

**CNN:** convolutions, pooling, image classification, transfer learning, object detection basics.  
**RNN:** recurrence, LSTM/GRU, sequence-to-sequence, attention — the path that existed **before** transformers and still explains why attention was invented.

### What you should be able to explain after

- Why CNNs use conv + pooling instead of flattening images
- Vanishing gradients and why LSTM gates help
- How an RNN processes a sequence step by step
- Seq2Seq + attention vs a plain RNN
- How Karpathy's L6 CNN fits into a language model

### Prerequisites

Step 3 complete (Karpathy L1–L5).

### Karpathy — CNN in context

| # | Video | Lab |
|---|---|---|
| 4.1 | [L6 full lecture](https://www.youtube.com/watch?v=t3YJ5hKiMQ0) | [notebook](https://github.com/karpathy/nn-zero-to-hero/blob/master/lectures/makemore/makemore_part5_cnn1.ipynb) |
| 4.2 | L6 — WaveNet intro @ 17:11 | same video |
| 4.3 | L6 — dilated conv @ 21:36 | same video |
| 4.4 | L6 — CNN block @ 47:44 | same video |

### Udacity — Deep Learning Nanodegree

**Home:** https://www.udacity.com/course/deep-learning--nd101  
**Repo (notebooks):** https://github.com/udacity/deep-learning-v2-pytorch

| # | Udacity module | What it covers | Skip if… |
|---|---|---|---|
| 4.5 | **Course 1** — Constructing & Training NNs | PyTorch MLPs, training loops, metrics | …you already did Karpathy L1–L5 (skim only) |
| 4.6 | **Course 2** — Convolutional Neural Networks | Conv, pooling, ResNet, transfer learning, detection, segmentation | **Do not skip** |
| 4.7 | **Course 2 project** — Landmark classifier | End-to-end CNN project | required |
| 4.8 | **Course 3** — Sequence Models & Transformers | Tokenization, embeddings, **RNN, LSTM, GRU**, Seq2Seq, attention | **Do not skip** |
| 4.9 | **Course 3** — transformer Q&A project | Bridge toward Step 5 | recommended |
| 4.10 | Course 4 — GANs & diffusion | Generative models | optional |

**Gate:** Step 5 only after Course 2 + Course 3 (RNN/LSTM section at minimum).

---

## Step 5 — LLMs & Transformers

### What you learn

Decoder-only GPT, BPE tokenization, modern transformer stacks, inference, scaling.

### What you should be able to explain after

- BPE tokenization
- Self-attention: Q, K, V
- Causal mask (decoder-only)
- Pretraining = next-token prediction
- KV cache at inference

### Prerequisites

Steps 3–4 done. You already saw attention in Udacity Course 3 — now you **build GPT from scratch**.

### Videos + labs

| # | Video | Lab |
|---|---|---|
| 5.1 | [L7 Build GPT](https://www.youtube.com/watch?v=kCc8FmEb1nY) | https://github.com/karpathy/nanoGPT |
| 5.2 | [L8 GPT tokenizer](https://www.youtube.com/watch?v=zduSFxRajkE) | https://github.com/karpathy/minbpe |
| 5.3 | DL.AI — Transformers in Practice | https://learn.deeplearning.ai/courses/transformers-in-practice/ |
| 5.4 | TIP — [Attention](https://learn.deeplearning.ai/courses/transformers-in-practice/lesson/79yzr2/attention) | Colab labs on platform |
| 5.5 | TIP — [Positional encoding](https://learn.deeplearning.ai/courses/transformers-in-practice/lesson/2fn8lb/positional-encoding) | same |
| 5.6 | TIP — [Model layers](https://learn.deeplearning.ai/courses/transformers-in-practice/lesson/y8sw6e/model-layers) | same |
| 5.7 | TIP — Module 3 (KV cache, quantization) | same course |
| 5.8 | [Karpathy — Deep Dive into LLMs](https://www.youtube.com/watch?v=7xTGNNLPyMI) | — |
| 5.9 | [Stanford CS229 — Building LLMs](https://www.youtube.com/watch?v=9vM4p9NN0Ts) | — |

**Deep Dive timestamps:** [Tokenization 07:47](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=467) · [Pretraining 41:20](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=2480) · [Inference 26:01](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=1561)

### Optional deeper track

| Resource | Link |
|---|---|
| Karpathy — build nanoGPT | https://github.com/karpathy/build-nanogpt · [video](https://www.youtube.com/watch?v=l8pRSuU81PU) |
| Hugging Face LLM Course | https://huggingface.co/learn/llm-course/en/chapter1/1 |

### Papers (after L7)

| Paper | Link |
|---|---|
| Attention Is All You Need | https://arxiv.org/abs/1706.03762 |
| 2606.18089 (SFT & RL) | https://arxiv.org/abs/2606.18089 |
| 2503.10622 | https://arxiv.org/abs/2503.10622 |

---

## Step 6 — Post-training (SFT & RLHF)

### What you learn

Alignment after pretraining: SFT, reward models, RLHF.

### Prerequisites

Step 5 complete — you must understand GPT training first.

| # | Resource | Link |
|---|---|---|
| 6.1 | Deep Dive — [SFT @ 01:01:06](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=3666) | — |
| 6.2 | Deep Dive — [RL @ 02:14:42](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=8082) | — |
| 6.3 | Deep Dive — [RLHF @ 02:48:26](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=10106) | — |
| 6.4 | Paper 2606.18089 | https://arxiv.org/abs/2606.18089 |
| 6.5 | HF LLM Course — fine-tuning (ch.10+) | https://huggingface.co/learn/llm-course/en/chapter10/1 |

---

## Step 7 — Agentic AI (last)

### What you learn

Prompting, CoT, ReAct, tools, RAG, multi-agent workflows.

### Why last

Agents assume you know how LLMs generate text, their limits, and when fine-tuning beats prompting.

### Prerequisites

Steps 5–6 done (minimum: L7 + TIP Modules 1–2).

| # | Resource | Link |
|---|---|---|
| 7.1 | **Udacity — Agentic AI**, Course 1 | https://www.udacity.com/course/agentic-ai--nd900 |
| 7.2 | Course 2 — workflows | same |
| 7.3 | Course 3 — agents + RAG | same |
| 7.4 | Course 4 — multi-agent | same |

---

## Suggested timeline (part-time, ~14–20 months)

| Months | Focus |
|---|---|
| 1–3 | Step 1 + Step 2 |
| 4–6 | Step 3 (Karpathy L1–L5) |
| 7–9 | Step 4 (CNN + RNN — Udacity DL) |
| 10–12 | Step 5 (GPT, TIP, Deep Dive) |
| 13–14 | Step 6 |
| 15–16 | Step 7 |

**Order matters more than speed.**

---

## Quick answers

| Question | Answer |
|---|---|
| Are CNN & RNN in the route? | **Yes — Step 4** (Udacity DL + Karpathy L6) |
| LLM or Agentic first? | **LLM** (Step 5) |
| Best first course? | **Coursera Andrew Ng** |
| Best first code course? | **Karpathy L1 micrograd** |
| Which Udacity courses? | **Deep Learning nd101** (Step 4) + **Agentic nd900** (Step 7) + LA optional (Step 2) |
| Skip Udacity Course 1? | **Yes**, if Karpathy L1–L5 is solid — start at Course 2 |

---

## All course homes

| Course | Link |
|---|---|
| Coursera ML | https://www.coursera.org/learn/machine-learning |
| DL.AI Math | https://learn.deeplearning.ai/specializations/mathematics-for-machine-learning-and-data-science |
| Udacity Linear Algebra | https://www.udacity.com/course/linear-algebra-essentials--cd0667 |
| Udacity Deep Learning | https://www.udacity.com/course/deep-learning--nd101 |
| Karpathy Zero to Hero | https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ |
| Transformers in Practice | https://learn.deeplearning.ai/courses/transformers-in-practice/ |
| Udacity Agentic AI | https://www.udacity.com/course/agentic-ai--nd900 |
| Hugging Face LLM Course | https://huggingface.co/learn/llm-course/en/chapter1/1 |
