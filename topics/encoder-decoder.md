# Encoder–Decoder

**Status:** not started · **Module:** 4 — LLMs & NLP

## Goal

Understand how an encoder maps an input sequence to a representation and a decoder
generates an output sequence (translation, summarization, seq2seq before full Transformer).

---

## Where to learn

| Role | Source | Specific link |
|---|---|---|
| **Math** | DeepLearning.AI — Math for ML | [Linear Algebra Applied I](https://learn.deeplearning.ai/specializations/mathematics-for-machine-learning-and-data-science/lesson/chi9v/linear-algebra-applied-i) (vectors, matrices for neural layers) |
| **Math** | 3Blue1Brown | [Essence of linear algebra playlist](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) — esp. dot product, matrix multiply |
| **Math** | Udacity — Linear Algebra Essentials | [Course home](https://www.udacity.com/course/linear-algebra-essentials--cd0667) |
| **Theory** | MIT 6.042 (MCS) | [PDF](https://courses.csail.mit.edu/6.042/spring18/mcs.pdf) — Ch. 4 *Mathematical Data Types* (functions, relations) |
| **Theory** | Coursera — Andrew Ng ML | [Course home](https://www.coursera.org/learn/machine-learning) — supervised learning framing |
| **Practice** | Karpathy — Zero to Hero | [makemore Part 1 — building makemore](https://www.youtube.com/watch?v=VMj-3S1tku0) (sequence modeling) |
| **Practice** | Karpathy — Zero to Hero | [Let's build GPT: from scratch](https://www.youtube.com/watch?v=kCc8FmEb1nY) (modern seq model; compare to classical enc-dec) |
| **Practice** | DeepLearning.AI — Transformers in Practice | [Course home](https://learn.deeplearning.ai/courses/transformers-in-practice/) — encoder-decoder vs decoder-only |
| **Practice** | Stanford CS229 guest lecture | [Building LLMs](https://www.youtube.com/watch?v=9vM4p9NN0Ts) — architecture stack overview |
| **Paper** | Attention Is All You Need | [notes](../papers/1706.03762-attention-is-all-you-need.md) — how enc-dec evolved into Transformer |

---

## Build in this repo

| Step | What | Where |
|---|---|---|
| 1 | Prerequisites: dot product + matmul | [dot-product](../exercises/dot-product/) · [matrix-multiplication](../exercises/matrix-multiplication/) |
| 2 | Tiny seq2seq on synthetic pairs (e.g. reverse string) | `exercises/encoder-decoder/` _(create when ready)_ |
| 3 | My notes | `notes/concepts/encoder-decoder.md` _(optional)_ |

**Suggested mini-project:** two small RNNs or a single `nn.Transformer` with `batch_first=True` on `(input, target)` pairs of length ≤ 16.

---

## Checklist

- [ ] Math: comfortable with matrix × vector (linear layer)
- [ ] Theory: read MIT 6.042 functions section (skim)
- [ ] Practice: watch makemore Part 1 + one Transformers in Practice lesson on seq2seq
- [ ] Build: implement toy encoder-decoder
- [ ] Can explain: difference vs decoder-only GPT

## What I still don't get

-
