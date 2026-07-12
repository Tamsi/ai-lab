# Exercise Catalog

All exercises with **verification** via automated tests. Implement in `solution.py`,
then submit:

```bash
python scripts/submit.py numpy/dot_product
python scripts/submit.py pytorch/tensor_basics
```

Passed submissions are logged in [submissions/registry.json](submissions/registry.json).

See [SUBMISSION.md](SUBMISSION.md) for the full workflow.

---

## Math for AI

| ID | Exercise | Verify | Note |
|---|---|---|---|
| M1 | [dot_product](numpy/dot_product/) | `python scripts/submit.py numpy/dot_product` | [dot-product](../notes/mathematics/linear-algebra/dot-product.md) |
| M2 | [matrix_multiplication](numpy/matrix_multiplication/) | `python scripts/submit.py numpy/matrix_multiplication` | [matrix-multiplication](../notes/mathematics/linear-algebra/matrix-multiplication.md) |
| M3 | [gradient_descent](numpy/gradient_descent/) | `python scripts/submit.py numpy/gradient_descent` | [gradient-descent](../notes/mathematics/optimization/gradient-descent.md) |
| M4 | [softmax_cross_entropy](numpy/softmax_cross_entropy/) | `python scripts/submit.py numpy/softmax_cross_entropy` | [cross-entropy](../notes/mathematics/information-theory/cross-entropy.md) |
| M5 | [linear_regression](numpy/linear_regression/) | `python scripts/submit.py numpy/linear_regression` | ML basics |
| M6 | [derivatives](mathematics/derivatives/) | `python scripts/submit.py mathematics/derivatives` | [derivatives](../notes/mathematics/calculus/derivatives.md) |
| M7 | [gradients](mathematics/gradients/) | `python scripts/submit.py mathematics/gradients` | [gradients](../notes/mathematics/calculus/gradients.md) |

## Tensors & deep learning building blocks

| ID | Exercise | Verify | Note |
|---|---|---|---|
| T1 | [tensor_basics](pytorch/tensor_basics/) | `python scripts/submit.py pytorch/tensor_basics` | [tensors](../notes/deep-learning/tensors.md) |
| T2 | [mlp_from_scratch](pytorch/mlp_from_scratch/) | `python scripts/submit.py pytorch/mlp_from_scratch` | [neurons](../notes/deep-learning/neurons-and-layers.md) |
| T3 | [cnn_conv2d](pytorch/cnn_conv2d/) | `python scripts/submit.py pytorch/cnn_conv2d` | [cnn](../notes/deep-learning/cnn.md) |
| T4 | [rnn_sequence](pytorch/rnn_sequence/) | `python scripts/submit.py pytorch/rnn_sequence` | [rnn](../notes/deep-learning/rnn.md) |

## LLMs

| ID | Exercise | Verify | Note |
|---|---|---|---|
| L1 | [ngrams_language_model](pytorch/ngrams_language_model/) | `python scripts/submit.py pytorch/ngrams_language_model` | [n-grams](../notes/llms/n-grams.md) |
| L2 | [tokenizer_bpe](pytorch/tokenizer_bpe/) | `python scripts/submit.py pytorch/tokenizer_bpe` | [tokenization](../notes/llms/tokenization.md) |
| L3 | [attention_scratch](pytorch/attention_scratch/) | `python scripts/submit.py pytorch/attention_scratch` | [attention](../notes/llms/attention.md) |
| L4 | [transformer_block](pytorch/transformer_block/) | `python scripts/submit.py pytorch/transformer_block` | [transformer](../notes/llms/transformer.md) |
| L5 | [sft_mini](pytorch/sft_mini/) | `python scripts/submit.py pytorch/sft_mini` | [SFT](../notes/llms/supervised-fine-tuning.md) |

## Reinforcement learning

| ID | Exercise | Verify | Note |
|---|---|---|---|
| R1 | [policy_gradient_tabular](numpy/policy_gradient_tabular/) | `python scripts/submit.py numpy/policy_gradient_tabular` | [policy-gradients](../notes/reinforcement-learning/policy-gradients.md) |
| R2 | [rl_policy_gradient_cartpole](pytorch/rl_policy_gradient_cartpole/) | `python scripts/submit.py pytorch/rl_policy_gradient_cartpole` | [rl-post-training](../notes/llms/rl-post-training.md) |

## CUDA

| ID | Exercise | Verify | Note |
|---|---|---|---|
| C1 | [lab_01_vector_add](cuda/lab_01_vector_add/) | `python scripts/submit.py cuda/lab_01_vector_add` | [cuda notes](../notes/computer-systems/cuda/) |
| C2 | [lab_02_matrix_multiply_naive](cuda/lab_02_matrix_multiply_naive/) | `python scripts/submit.py cuda/lab_02_matrix_multiply_naive` | GPU matmul |
| C3 | [lab_03_shared_memory_tiling](cuda/lab_03_shared_memory_tiling/) | `python scripts/submit.py cuda/lab_03_shared_memory_tiling` | Tiling |

---

## Submission status

Check [submissions/registry.json](submissions/registry.json) for your verified exercises.

| Exercise | Last result | Timestamp |
|---|---|---|
| _(run submit.py to populate)_ | | |

_Full legacy index: [../CURRICULUM.md](../CURRICULUM.md)_
