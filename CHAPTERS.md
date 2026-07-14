# AI from scratch — chapters

Personal curriculum. Each chapter lists **exact videos and courses** to follow in order.  
Mark progress: `[ ]` todo · `[~]` in progress · `[x]` done

**Detailed syllabi:** [curriculum/syllabi/](curriculum/syllabi/)

---

## Chapter 0 — Orientation

**Goal:** know what you're learning and in what order.

| # | What | Link |
|---|---|---|
| 0.1 | Read this file top to bottom | — |
| 0.2 | Bookmark all course homes | [resources.md](resources.md) |

**Order:** Chapters 1 → 2 → 3 can overlap. Chapter 4 needs Ch. 1–3. Ch. 5 needs Ch. 4. Ch. 6–8 after Ch. 5.

---

## Chapter 1 — Linear algebra for ML

**Goal:** vectors, dot product, matrices, linear maps — the language of neural nets.

| # | Resource | Lesson | Done |
|---|---|---|---|
| 1.1 | 3Blue1Brown LA | [Ep.1 — Vectors](https://www.youtube.com/watch?v=fNk_zzaMoSs) | [ ] |
| 1.2 | 3Blue1Brown LA | [Ep.2 — Span and basis](https://www.youtube.com/watch?v=k7RM-ot2NWY) | [ ] |
| 1.3 | 3Blue1Brown LA | [Ep.3 — Linear transformations](https://www.youtube.com/watch?v=kYB8IZa5AuE) | [ ] |
| 1.4 | 3Blue1Brown LA | [Ep.4 — Matrix multiplication](https://www.youtube.com/watch?v=XkY2DOUCWMU) | [ ] |
| 1.5 | 3Blue1Brown LA | [Ep.9 — Dot products and duality](https://www.youtube.com/watch?v=LyGKycYT2v0) | [ ] |
| 1.6 | DL.AI Math — Course 1 | [Linear Algebra Applied I](https://learn.deeplearning.ai/specializations/mathematics-for-machine-learning-and-data-science/lesson/chi9v/linear-algebra-applied-i) | [~] |
| 1.7 | DL.AI Math — Course 1 | [Linear Algebra Applied II](https://learn.deeplearning.ai/specializations/mathematics-for-machine-learning-and-data-science/lesson/0q26g/linear-algebra-applied-ii) | [ ] |
| 1.8 | DL.AI Math — Course 1 | [Week 3 — Vectors and linear transformations](https://learn.deeplearning.ai/specializations/mathematics-for-machine-learning-and-data-science/) | [ ] |
| 1.9 | Udacity LA | [Lessons 1–4 — Vectors → linear maps](https://www.udacity.com/course/linear-algebra-essentials--cd0667) | [ ] |
| 1.10 | Udacity LA | [Lessons 5–7 — Matmul → neural networks](https://www.udacity.com/course/linear-algebra-essentials--cd0667) | [ ] |

**Playlist:** [3Blue1Brown — Essence of Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)  
**Syllabus:** [curriculum/syllabi/dl-ai-math.md](curriculum/syllabi/dl-ai-math.md) · [3blue1brown-la.md](curriculum/syllabi/3blue1brown-la.md) · [udacity-linear-algebra.md](curriculum/syllabi/udacity-linear-algebra.md)

---

## Chapter 2 — Calculus, gradients & probability

**Goal:** derivatives, gradient descent, probability — what "learning" optimizes.

### 2A — Calculus & gradients

| # | Resource | Lesson | Done |
|---|---|---|---|
| 2.1 | 3Blue1Brown Calc | [Ch.1 — Essence of calculus](https://www.youtube.com/watch?v=WUvTyaaNkzM) | [ ] |
| 2.2 | 3Blue1Brown Calc | [Ch.2 — Paradox of the derivative](https://www.youtube.com/watch?v=9vKqVkMQHKk) | [ ] |
| 2.3 | 3Blue1Brown Calc | [Ch.4 — Chain rule](https://www.youtube.com/watch?v=YG15m2VwSjA) | [ ] |
| 2.4 | 3Blue1Brown DL | [**Gradient descent @ 06:55**](https://www.youtube.com/watch?v=IHZwWFHWa-w&t=415) | [ ] |
| 2.5 | 3Blue1Brown DL | [Gradient vectors @ 11:18](https://www.youtube.com/watch?v=IHZwWFHWa-w&t=678) | [ ] |
| 2.6 | DL.AI Math — Course 2 | [Week 2 — Gradients and gradient descent](https://learn.deeplearning.ai/specializations/mathematics-for-machine-learning-and-data-science/) | [ ] |

**Playlist:** [Essence of Calculus](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr)

### 2B — Probability & statistics

| # | Resource | Lesson | Done |
|---|---|---|---|
| 2.7 | DL.AI Math — Course 3 | [Full course — 4 weeks](https://learn.deeplearning.ai/specializations/mathematics-for-machine-learning-and-data-science/) | [ ] |
| 2.8 | MIT 6.042 (PDF) | [Part IV — Probability (Ch.16+)](https://courses.csail.mit.edu/6.042/spring18/mcs.pdf) | [ ] |

**Syllabus:** [3blue1brown-calculus.md](curriculum/syllabi/3blue1brown-calculus.md) · [dl-ai-math.md](curriculum/syllabi/dl-ai-math.md)

---

## Chapter 3 — Classical machine learning

**Goal:** supervised learning, loss, regularization — before deep nets.

| # | Resource | Lesson | Done |
|---|---|---|---|
| 3.1 | Coursera ML | [Week 1 — Linear regression + gradient descent](https://www.coursera.org/learn/machine-learning) | [ ] |
| 3.2 | Coursera ML | [Week 2 — Multivariate regression](https://www.coursera.org/learn/machine-learning) | [ ] |
| 3.3 | Coursera ML | [Week 3 — Logistic regression + regularization](https://www.coursera.org/learn/machine-learning) | [~] |
| 3.4 | 3Blue1Brown LA | [Ep.14 — Eigenvectors](https://www.youtube.com/watch?v=PFDu9oVAE-g) (PCA intuition) | [ ] |

**Syllabus:** [coursera-ml.md](curriculum/syllabi/coursera-ml.md)

---

## Chapter 4 — Deep learning foundations

**Goal:** autograd, backprop, MLP, training loop.

| # | Resource | Lesson | Done |
|---|---|---|---|
| 4.1 | Karpathy Z2H | [L1 — micrograd](https://www.youtube.com/watch?v=VMj-3S1tku0) | [ ] |
| 4.2 | Karpathy Z2H | [L2 — makemore bigrams](https://www.youtube.com/watch?v=PaCmpygFfXo) | [ ] |
| 4.3 | Karpathy Z2H | [L3 — makemore MLP](https://www.youtube.com/watch?v=TCH_1BHY58I) | [ ] |
| 4.4 | Karpathy Z2H | [L4 — activations & BatchNorm](https://www.youtube.com/watch?v=P6sfmUTpUmc) | [ ] |
| 4.5 | Karpathy Z2H | [L5 — backprop ninja](https://www.youtube.com/watch?v=q8SA3rM6ckI) | [ ] |
| 4.6 | 3Blue1Brown DL | [Backpropagation Ch.3](https://www.youtube.com/watch?v=Ilg3gGewQ5U) | [ ] |

**Playlist:** [Karpathy — Zero to Hero](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ)  
**Syllabus:** [karpathy-zero-to-hero.md](curriculum/syllabi/karpathy-zero-to-hero.md)

---

## Chapter 5 — CNN & sequences

**Goal:** convolutions and sequence models before Transformers.

| # | Resource | Lesson | Done |
|---|---|---|---|
| 5.1 | Karpathy Z2H | [L6 — WaveNet @ 17:11 architecture](https://www.youtube.com/watch?v=t3YJ5hKiMQ0&t=1031) | [ ] |
| 5.2 | Karpathy Z2H | [L6 — build hierarchy @ 21:36](https://www.youtube.com/watch?v=t3YJ5hKiMQ0&t=1296) | [ ] |
| 5.3 | Karpathy Z2H | [L6 — CNN explained @ 47:44](https://www.youtube.com/watch?v=t3YJ5hKiMQ0&t=2864) | [ ] |
| 5.4 | Karpathy Z2H | [L6 — full video](https://www.youtube.com/watch?v=t3YJ5hKiMQ0) | [ ] |

---

## Chapter 6 — LLMs & Transformers

**Goal:** tokenization, attention, GPT, pretraining, post-training.

| # | Resource | Lesson | Done |
|---|---|---|---|
| 6.1 | Karpathy Z2H | [L7 — Let's build GPT](https://www.youtube.com/watch?v=kCc8FmEb1nY) | [ ] |
| 6.2 | Karpathy Z2H | [L8 — GPT tokenizer](https://www.youtube.com/watch?v=zduSFxRajkE) | [ ] |
| 6.3 | DL.AI TIP | [Module 1 — Autoregressive generation](https://learn.deeplearning.ai/courses/transformers-in-practice/) | [ ] |
| 6.4 | DL.AI TIP | [Module 2 — Attention](https://learn.deeplearning.ai/courses/transformers-in-practice/lesson/79yzr2/attention) | [ ] |
| 6.5 | DL.AI TIP | [Positional encoding](https://learn.deeplearning.ai/courses/transformers-in-practice/lesson/2fn8lb/positional-encoding) | [ ] |
| 6.6 | DL.AI TIP | [Model layers](https://learn.deeplearning.ai/courses/transformers-in-practice/lesson/y8sw6e/model-layers) | [ ] |
| 6.7 | Karpathy Deep Dive | [Tokenization @ 07:47](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=467) | [ ] |
| 6.8 | Karpathy Deep Dive | [Pretraining @ 41:20](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=2480) | [ ] |
| 6.9 | Karpathy Deep Dive | [SFT @ 01:01:06](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=3666) | [ ] |
| 6.10 | Karpathy Deep Dive | [RL @ 02:14:42](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=8082) | [ ] |
| 6.11 | Karpathy Deep Dive | [RLHF @ 02:48:26](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=10106) | [ ] |
| 6.12 | Stanford CS229 | [Building LLMs guest lecture](https://www.youtube.com/watch?v=9vM4p9NN0Ts) | [ ] |
| 6.13 | DL.AI TIP | [Module 3 — KV cache, quantization](https://learn.deeplearning.ai/courses/transformers-in-practice/) | [ ] |
| 6.14 | Paper | [Attention Is All You Need (1706.03762)](https://arxiv.org/abs/1706.03762) | [ ] |
| 6.15 | Paper | [2606.18089 — SFT & RL](https://arxiv.org/abs/2606.18089) | [ ] |
| 6.16 | Paper | [2503.10622](https://arxiv.org/abs/2503.10622) | [ ] |

**Syllabus:** [transformers-in-practice.md](curriculum/syllabi/transformers-in-practice.md) · [karpathy-llm-deep-dive.md](curriculum/syllabi/karpathy-llm-deep-dive.md) · [stanford-cs229-llm.md](curriculum/syllabi/stanford-cs229-llm.md)

---

## Chapter 7 — CUDA & GPU

**Goal:** why GPUs matter for ML.

| # | Resource | Lesson | Done |
|---|---|---|---|
| 7.1 | NVIDIA | [Even Easier Introduction to CUDA](https://developer.nvidia.com/blog/even-easier-introduction-cuda/) | [ ] |
| 7.2 | NVIDIA | [CUDA Programming Guide](https://docs.nvidia.com/cuda/cuda-programming-guide/index.html) | [ ] |
| 7.3 | NVIDIA | [CUDA exercises PDF](https://www.nvidia.com/content/cudazone/download/Exercise_Instructions.pdf) | [ ] |

**Syllabus:** [nvidia-cuda.md](curriculum/syllabi/nvidia-cuda.md)

---

## Chapter 8 — Agentic AI

**Goal:** LLMs as components in applications (agents, RAG, tools).

| # | Resource | Lesson | Done |
|---|---|---|---|
| 8.1 | Udacity nd900 | [Course 1 — Prompting, CoT, ReAct](https://www.udacity.com/course/agentic-ai--nd900) | [ ] |
| 8.2 | Udacity nd900 | [Course 2 — Agentic workflows](https://www.udacity.com/course/agentic-ai--nd900) | [ ] |
| 8.3 | Udacity nd900 | [Course 3 — Agents + RAG](https://www.udacity.com/course/agentic-ai--nd900) | [ ] |
| 8.4 | Udacity nd900 | [Course 4 — Multi-agent systems](https://www.udacity.com/course/agentic-ai--nd900) | [ ] |

**Syllabus:** [udacity-agentic-ai.md](curriculum/syllabi/udacity-agentic-ai.md)

---

## Chapter 9 — Discrete math (parallel, optional)

**Goal:** proof literacy for reading papers. **Not blocking** — read alongside Ch. 1–3.

| # | Resource | Lesson | Done |
|---|---|---|---|
| 9.1 | MIT 6.042 | [Part I — Proofs (Ch.1–3)](https://courses.csail.mit.edu/6.042/spring18/mcs.pdf) | [ ] |
| 9.2 | MIT 6.042 | [Part II — Structures (Ch.4–8)](https://courses.csail.mit.edu/6.042/spring18/mcs.pdf) | [ ] |

**Syllabus:** [mit-6042.md](curriculum/syllabi/mit-6042.md)

---

## Suggested timeline (post-bac, ~12–18 months part-time)

```text
Months 1–3   Ch.1 + Ch.2A        (math, in parallel)
Months 3–4   Ch.2B + Ch.3        (proba + Coursera ML)
Months 5–7   Ch.4 + Ch.5         (Karpathy Z2H)
Months 8–10  Ch.6                (LLMs)
Months 11–12 Ch.7 + Ch.8         (CUDA + agents)
Throughout   Ch.9                (MIT 6.042, optional)
```

---

## Quick reference — course homes

| Course | Link |
|---|---|
| DL.AI Math | https://learn.deeplearning.ai/specializations/mathematics-for-machine-learning-and-data-science |
| Udacity Linear Algebra | https://www.udacity.com/course/linear-algebra-essentials--cd0667 |
| Coursera ML (Andrew Ng) | https://www.coursera.org/learn/machine-learning |
| 3Blue1Brown LA | https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab |
| 3Blue1Brown Calculus | https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr |
| Karpathy Zero to Hero | https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ |
| Karpathy Deep Dive LLM | https://www.youtube.com/watch?v=7xTGNNLPyMI |
| Transformers in Practice | https://learn.deeplearning.ai/courses/transformers-in-practice/ |
| Udacity Agentic AI | https://www.udacity.com/course/agentic-ai--nd900 |
| MIT 6.042 PDF | https://courses.csail.mit.edu/6.042/spring18/mcs.pdf |
