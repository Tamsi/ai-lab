# Learning Focus

Personal priorities for this repository. Everything else is supporting material.

## Three pillars

| Pillar | Goal | Start here |
|---|---|---|
| **Math for AI** | Linear algebra, probability, optimization, information theory — only what feeds ML/LLMs | [notes/mathematics/](notes/mathematics/) · [exercises/numpy/](exercises/numpy/) |
| **CUDA** | Understand GPU execution; write and profile kernels | [notes/computer-systems/cuda/](notes/computer-systems/cuda/) · [exercises/cuda/](exercises/cuda/) |
| **How LLMs work** | Tokenization → attention → training → SFT → RL post-training → generation | [notes/llms/](notes/llms/) · [exercises/pytorch/](exercises/pytorch/) |

## Supporting tracks

| Track | Why | Notes | Exercises |
|---|---|---|---|
| **Tensors** | Language of PyTorch and GPU code | [tensors.md](notes/deep-learning/tensors.md) | [tensor_basics](exercises/pytorch/tensor_basics/) |
| **ML basics** | Regression, loss, evaluation before deep dive | [machine-learning/](notes/machine-learning/) | [exercises/numpy/](exercises/numpy/) |
| **CNN** | Convolutions, local patterns, vision baselines | [cnn.md](notes/deep-learning/cnn.md) | [cnn_conv2d](exercises/pytorch/cnn_conv2d/) |
| **RNN** | Sequential models before Transformers | [rnn.md](notes/deep-learning/rnn.md) | [rnn_sequence](exercises/pytorch/rnn_sequence/) |
| **RL** | Post-training (PPO, GRPO), agents, reward | [reinforcement-learning/](notes/reinforcement-learning/) | [policy_gradient_tabular](exercises/numpy/policy_gradient_tabular/) |

## Paper-driven learning

When you read a paper on [alphaXiv](https://www.alphaxiv.org/), add it to
[papers/READING-QUEUE.md](papers/READING-QUEUE.md) and list every concept you
want to deepen — even if you do not understand the paper yet.

Example: [2606.18089](https://www.alphaxiv.org/abs/2606.18089) → SFT, RL post-training, n-grams, compositional generalization.

See [CONCEPTS.md](CONCEPTS.md) for the master concept index linked to papers.

## Weekly minimum

1. One concept note updated
2. One exercise submitted and verified (`python scripts/submit.py <path>`)
3. One paper added or progressed in the reading queue
4. One entry in [PROGRESS.md](PROGRESS.md)
