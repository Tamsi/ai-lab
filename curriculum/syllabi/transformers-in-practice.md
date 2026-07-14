# DeepLearning.AI — Transformers in Practice

**Home:** https://learn.deeplearning.ai/courses/transformers-in-practice/

3 modules · short lessons with labs · **after** Karpathy L2–L3

---

## Module 1 — Transformer behavior

| Lesson | Topic | Done |
|---|---|---|
| Autoregressive text generation | next-token loop | [ ] |
| Tokenization in practice | vocab, special tokens | [ ] |
| Embeddings | lookup tables | [ ] |
| Visualization: decoder-only transformers | GPT-style stack | [ ] |

---

## Module 2 — Attention and internals

| Lesson | Link | Topic | Done |
|---|---|---|---|
| Attention | [lesson/79yzr2/attention](https://learn.deeplearning.ai/courses/transformers-in-practice/lesson/79yzr2/attention) | Q, K, V, softmax | [ ] |
| Positional encoding | [lesson/2fn8lb/positional-encoding](https://learn.deeplearning.ai/courses/transformers-in-practice/lesson/2fn8lb/positional-encoding) | sin/cos, RoPE intro | [ ] |
| Model layers | [lesson/y8sw6e/model-layers](https://learn.deeplearning.ai/courses/transformers-in-practice/lesson/y8sw6e/model-layers) | MHA, FFN, residuals | [ ] |
| Visualization: encoder-decoder | decoder-only vs enc-dec | [ ] |

**Maps to:** [CH.6](../../CHAPTERS.md), [CH.6](../../CHAPTERS.md)

---

## Module 3 — Scaling and deployment

| Lesson | Topic | Done |
|---|---|---|
| KV cache | inference memory | [ ] |
| Flash attention | speed | [ ] |
| Quantization | INT8/4-bit | [ ] |
| Multi-GPU / serving | production | [ ] |

**Maps to:** CUDA module (see [nvidia-cuda.md](nvidia-cuda.md))

---

## Study order

1. Module 1 while doing Karpathy L7  
2. Module 2 in parallel with L7–L8  
3. Module 3 after Deep Dive inference section
