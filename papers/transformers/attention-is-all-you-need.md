# Attention Is All You Need

## Metadata

- Authors: Vaswani et al.
- Year: 2017
- Link: https://arxiv.org/abs/1706.03762
- Topic: Transformers, sequence modeling
- Status: first read

## Problem

Sequence transduction models (e.g. machine translation) relied heavily on
recurrent or convolutional encoders-decoders. The authors ask whether recurrence
is necessary, or whether attention alone can model dependencies.

## Core idea

_(To be completed after reading — week 2 target.)_

1. Replace recurrence with multi-head self-attention.
2. ...
3. ...

## Required knowledge

- [x] Dot products
- [x] Matrix multiplication
- [ ] Softmax
- [ ] Positional encoding
- [ ] Cross-entropy loss
- [ ] Layer normalization

## Architecture

_(Introduction and Figure 1 only for now.)_

- Encoder-decoder stack
- Multi-head attention blocks
- Position-wise feed-forward networks
- Residual connections and layer normalization

## Key equations

### Scaled dot-product attention

**Attention(Q, K, V)** = softmax(QKᵀ / √d_k) V

- **Q**, **K**, **V**: query, key, value matrices
- d_k: dimension of keys (scaling factor in denominator)

_I still need to understand why √d_k stabilizes variance of dot products._

## Training procedure

_Not studied yet._

## Hardware and computational considerations

_Not studied yet._

## Experiments

- WMT 2014 English-German and English-French translation
- BLEU score as primary metric

## Mini reproduction

Smallest useful slice: implement scaled dot-product attention on random Q, K, V
tensors and visualize attention weights for a toy sequence.

## Questions

- Why does scaling by √d_k matter for gradient stability?
- How do positional encodings interact with permutation invariance of attention?

## Related concepts to study

- [ ] Softmax and cross-entropy
- [ ] Embeddings
- [ ] Causal masking for decoders

## References

- [3Blue1Brown — Linear Algebra](https://www.youtube.com/watch?v=fNk_zzaMoSs&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)
- [DeepLearning.AI — Transformers in Practice](https://learn.deeplearning.ai/courses/transformers-in-practice/)
