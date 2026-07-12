# Recurrent Neural Networks (RNN)

**Status:** Not started  
**Milestone:** Deep learning  
**Related exercise:** [rnn_sequence](../../exercises/pytorch/rnn_sequence/)

## Intuition

An **RNN** processes sequences step by step, maintaining a **hidden state** that
carries information from past tokens. Unlike Transformers, early RNNs had limited
parallelism during training but introduced sequential memory.

## Formal definition

\[
h_t = \phi(W_{hh} h_{t-1} + W_{xh} x_t + b), \quad y_t = W_{hy} h_t
\]

LSTM/GRU variants add gating to mitigate vanishing gradients.

## Why it matters in machine learning

- Historical backbone for seq2seq before attention
- Helps understand why self-attention replaced recurrence for long contexts
- Still relevant for streaming / small embedded models

## Minimal implementation

```python
rnn = torch.nn.RNN(input_size, hidden_size, batch_first=True)
out, h_n = rnn(x_sequence)
```

## Experiment

Train char-RNN on tiny corpus; compare to Transformer on same data.

## What I still do not understand

- BPTT truncation effects
- When RNNs are still practical vs Transformers
