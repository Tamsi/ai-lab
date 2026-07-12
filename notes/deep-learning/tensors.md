# Tensors

**Status:** Not started  
**Milestone:** Deep learning  
**Related exercise:** [tensor_basics](../../exercises/pytorch/tensor_basics/)

## Intuition

A **tensor** is a multi-dimensional array. Scalars (0D), vectors (1D), matrices
(2D), and batches of images (4D: N×C×H×W) are all tensors. Deep learning
frameworks run operations on tensors in parallel on CPU or GPU.

## Formal definition

Tensor \(\mathbf{T} \in \mathbb{R}^{d_1 \times \cdots \times d_k}\).

Key ops: reshape, transpose, matmul (`@`), element-wise ops, **broadcasting**
(aligning shapes by stretching size-1 dimensions).

## Why it matters in machine learning

- Every forward pass is tensor arithmetic
- Attention: \(\text{softmax}(QK^\top / \sqrt{d}) V\) is batched tensor matmul
- CUDA kernels operate on flat memory backing tensors

## Minimal implementation

```python
import torch
x = torch.randn(4, 3)      # batch of 4 vectors
W = torch.randn(3, 2)
y = x @ W                  # shape (4, 2)
```

## Experiment

Print `.shape`, `.stride()`, and memory layout for 2D vs transposed tensor.

## What I still do not understand

- When contiguous memory matters for CUDA
- `einsum` vs explicit matmul for readability and speed
- Automatic mixed precision (fp16/bf16) effects
