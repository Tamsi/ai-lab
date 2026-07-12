# Curriculum Index

Complete map of notes, exercises, implementations, experiments, and projects.
Scaffolds are ready to fill — only **dot product** and **matrix multiplication** are implemented.

See [COURSES.md](COURSES.md) for external course links and [ROADMAP.md](ROADMAP.md) for milestones.

## Exercises

### Mathematics (`exercises/mathematics/`)

| Exercise | Milestone | Note |
|---|---|---|
| [sigma_notation](exercises/mathematics/sigma_notation/) | M1 | [sigma-notation](notes/mathematics/algebra/sigma-notation.md) |
| [derivatives](exercises/mathematics/derivatives/) | M1 | [derivatives](notes/mathematics/calculus/derivatives.md) |
| [gradients](exercises/mathematics/gradients/) | M1 | [gradients](notes/mathematics/calculus/gradients.md) |
| [probability_drills](exercises/mathematics/probability_drills/) | M1 | [probability-basics](notes/mathematics/probability/probability-basics.md) |

### NumPy (`exercises/numpy/`)

| Exercise | Status | Milestone |
|---|---|---|
| [dot_product](exercises/numpy/dot_product/) | ✅ Done | M1 |
| [matrix_multiplication](exercises/numpy/matrix_multiplication/) | ✅ Done | M1 |
| [linear_transformations](exercises/numpy/linear_transformations/) | Scaffold | M1 |
| [linear_regression](exercises/numpy/linear_regression/) | Scaffold | M1 |
| [logistic_regression](exercises/numpy/logistic_regression/) | Scaffold | M2 |
| [gradient_descent](exercises/numpy/gradient_descent/) | Scaffold | M1 |
| [softmax_cross_entropy](exercises/numpy/softmax_cross_entropy/) | Scaffold | M1 |
| [train_val_test](exercises/numpy/train_val_test/) | Scaffold | M2 |
| [pca](exercises/numpy/pca/) | Scaffold | M2 |
| [k_means](exercises/numpy/k_means/) | Scaffold | M2 |
| [regularization](exercises/numpy/regularization/) | Scaffold | M2 |

### PyTorch (`exercises/pytorch/`)

| Exercise | Milestone |
|---|---|
| [tensor_basics](exercises/pytorch/tensor_basics/) | M3 |
| [mlp_from_scratch](exercises/pytorch/mlp_from_scratch/) | M3 |
| [backprop_manual](exercises/pytorch/backprop_manual/) | M3 |
| [optimizers](exercises/pytorch/optimizers/) | M3 |
| [attention_scratch](exercises/pytorch/attention_scratch/) | M5 |
| [transformer_block](exercises/pytorch/transformer_block/) | M5 |
| [tokenizer_bpe](exercises/pytorch/tokenizer_bpe/) | M5 |

### Systems (`exercises/systems/`)

| Exercise | Milestone |
|---|---|
| [ieee754](exercises/systems/ieee754/) | M4 |
| [floating_point_accumulation](exercises/systems/floating_point_accumulation/) | M4 |
| [cache_friendly_matmul](exercises/systems/cache_friendly_matmul/) | M4 |
| [cpu_vs_gpu_baseline](exercises/systems/cpu_vs_gpu_baseline/) | M4 |

### CUDA (`exercises/cuda/`)

| Exercise | Milestone |
|---|---|
| [lab_01_vector_add](exercises/cuda/lab_01_vector_add/) | M4 |
| [lab_02_matrix_multiply_naive](exercises/cuda/lab_02_matrix_multiply_naive/) | M4 |
| [lab_03_shared_memory_tiling](exercises/cuda/lab_03_shared_memory_tiling/) | M4 |

## Notes by domain

| Domain | Index |
|---|---|
| Mathematics | [algebra](notes/mathematics/algebra/), [calculus](notes/mathematics/calculus/), [linear-algebra](notes/mathematics/linear-algebra/), [probability](notes/mathematics/probability/), [statistics](notes/mathematics/statistics/), [optimization](notes/mathematics/optimization/), [information-theory](notes/mathematics/information-theory/) |
| Computer systems | [binary/fp](notes/computer-systems/binary-and-floating-point/), [cpu](notes/computer-systems/cpu/), [memory](notes/computer-systems/memory-and-cache/), [gpu](notes/computer-systems/gpu/), [cuda](notes/computer-systems/cuda/), [distributed](notes/computer-systems/distributed-computing/) |
| ML / DL / LLM / RL | [machine-learning](notes/machine-learning/), [deep-learning](notes/deep-learning/), [llms](notes/llms/), [reinforcement-learning](notes/reinforcement-learning/), [world-models](notes/world-models/) |

## Implementations

| Module | Milestone |
|---|---|
| [linear-regression](implementations/linear-regression/) | M1 |
| [logistic-regression](implementations/logistic-regression/) | M2 |
| [pca](implementations/pca/) | M2 |
| [neural-network](implementations/neural-network/) | M3 |
| [autograd-engine](implementations/autograd-engine/) | M3 |
| [tokenizer](implementations/tokenizer/) | M5 |
| [transformer](implementations/transformer/) | M5 |
| [world-model](implementations/world-model/) | M6 |

## Experiments

| Experiment | Milestone |
|---|---|
| [gradient-descent](experiments/gradient-descent/) | M1 |
| [matrix-multiplication](experiments/matrix-multiplication/) | M1 |
| [floating-point-precision](experiments/floating-point-precision/) | M4 |
| [cpu-vs-gpu](experiments/cpu-vs-gpu/) | M4 |
| [attention-memory](experiments/attention-memory/) | M5 |
| [model-scaling](experiments/model-scaling/) | M5 |

## Portfolio projects

| Project | Milestone |
|---|---|
| [gradient-playground](projects/gradient-playground/) | M1 |
| [tiny-autograd](projects/tiny-autograd/) | M3 |
| [gpu-matmul-lab](projects/gpu-matmul-lab/) | M4 |
| [mini-transformer](projects/mini-transformer/) | M5 |
| [latent-world-model](projects/latent-world-model/) | M6 |

## Completion workflow

For each topic:

1. Study external course section → [COURSES.md](COURSES.md)
2. Write or update concept note in `notes/`
3. Implement exercise in `exercises/` (tests must pass)
4. Record observations in `results.md`
5. Log week in [PROGRESS.md](PROGRESS.md)
6. Close linked GitHub issue
