#!/usr/bin/env python3
"""Generate course and exercise scaffolds for AI Foundations Lab."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

NOTE_STUB = """# {title}

**Status:** Not started  
**Milestone:** {milestone}  
**Related exercise:** {exercise}

## Intuition

_(What does this concept mean geometrically or conceptually?)_

## Formal definition

_(Equations and precise statements.)_

## Why it matters in machine learning

- 

## Minimal implementation

```python
# TODO
```

## Experiment

_(What to plot, measure, or compare.)_

## Connection to research papers

_(Where does this appear in papers you read?)_

## What I still do not understand

- 

## References

{references}
"""

EXERCISE_README = """# {title}

**Status:** Not started  
**Milestone:** {milestone}

## Objective

{objective}

## Constraints

{constraints}

## Tasks

{tasks}

## Reflection

{reflection}

## Deliverables

- Concept note: `{note_path}`
- This exercise folder completed with tests passing
- Observations recorded in `results.md`
"""

EXERCISE_PY = '''"""{title} — implement in solution.py."""

from exercises.{pkg}.solution import {func}


def main() -> None:
    raise NotImplementedError("Complete this exercise in solution.py")


if __name__ == "__main__":
    main()
'''

SOLUTION_PY = '''"""{title} — your implementation goes here."""


def {func}(*args, **kwargs):
    raise NotImplementedError("Implement me")
'''

TEST_PY = '''import pytest

from exercises.{pkg}.solution import {func}

pytestmark = pytest.mark.skip(reason="Exercise scaffold — implement solution first")


def test_placeholder():
    assert {func} is not None
'''

RESULTS_MD = """# {title} — Results

## Observations

_(What did you measure or visualize?)_

## Failures / surprises

_(What broke or contradicted intuition?)_

## Conclusions

_(What you take away — include honest gaps.)_
"""

SECTION_README = """# {title}

**Milestone:** {milestone}

## Topics

{topic_list}

## External courses

{courses}

## How to study a topic

1. Read intuition section in the concept note
2. Complete the linked exercise
3. Record benchmarks or plots in `results.md`
4. Update [GLOSSARY.md](../../GLOSSARY.md) and [PROGRESS.md](../../PROGRESS.md)
"""


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        return
    path.write_text(content, encoding="utf-8")


def scaffold_note(rel: str, title: str, milestone: str, exercise: str, refs: str) -> None:
    path = ROOT / "notes" / rel
    write(
        path,
        NOTE_STUB.format(
            title=title,
            milestone=milestone,
            exercise=exercise,
            references=refs,
        ),
    )


def scaffold_exercise(
    category: str,
    slug: str,
    title: str,
    milestone: str,
    objective: str,
    constraints: str,
    tasks: list[str],
    reflection: list[str],
    note_path: str,
    func: str,
) -> None:
    pkg = f"{category}.{slug}"
    base = ROOT / "exercises" / category / slug
    tasks_md = "\n".join(f"{i}. {t}" for i, t in enumerate(tasks, 1))
    reflection_md = "\n".join(f"- {r}" for r in reflection)
    write(
        base / "README.md",
        EXERCISE_README.format(
            title=title,
            milestone=milestone,
            objective=objective,
            constraints=constraints,
            tasks=tasks_md,
            reflection=reflection_md,
            note_path=note_path,
        ),
    )
    write(base / "exercise.py", EXERCISE_PY.format(title=title, pkg=pkg, func=func))
    write(base / "solution.py", SOLUTION_PY.format(title=title, func=func))
    write(base / "test_solution.py", TEST_PY.format(pkg=pkg, func=func))
    write(base / "results.md", RESULTS_MD.format(title=title))
    write(base / "__init__.py", "")


def scaffold_section_readme(
    rel: str, title: str, milestone: str, topics: list[tuple[str, str]], courses: str
) -> None:
    topic_lines = "\n".join(f"- [{t}]({f})" for t, f in topics)
    write(
        ROOT / rel / "README.md",
        SECTION_README.format(
            title=title,
            milestone=milestone,
            topic_list=topic_lines,
            courses=courses,
        ),
    )


def scaffold_impl(slug: str, title: str, milestone: str, description: str) -> None:
    write(
        ROOT / "implementations" / slug / "README.md",
        f"# {title}\n\n**Status:** Not started  \n**Milestone:** {milestone}\n\n{description}\n",
    )


def scaffold_experiment(slug: str, title: str, milestone: str, description: str) -> None:
    write(
        ROOT / "experiments" / slug / "README.md",
        f"# {title}\n\n**Status:** Not started  \n**Milestone:** {milestone}\n\n{description}\n",
    )


def scaffold_paper(rel: str, title: str, link: str) -> None:
    write(
        ROOT / "papers" / rel,
        f"""# {title}

## Metadata

- Authors:
- Year:
- Link: {link}
- Topic:
- Status: not started

## Problem

## Core idea

## Required knowledge

- [ ]

## Questions

## Related concepts to study

- [ ]
""",
    )


def main() -> None:
    # --- COURSES.md ---
    write(
        ROOT / "COURSES.md",
        """# Course Catalog

External courses mapped to repository paths and milestones. Work through courses
in parallel with notes, exercises, and weekly [PROGRESS.md](PROGRESS.md) entries.

## Milestone 1 — Mathematical foundations

| Course | Link | Maps to |
|---|---|---|
| 3Blue1Brown — Linear Algebra | https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab | `notes/mathematics/linear-algebra/`, `exercises/numpy/` |
| 3Blue1Brown — Calculus | https://www.youtube.com/playlist?list=PLVUDmbpupCaqz8nECyVys-tFkUs--OKsY | `notes/mathematics/calculus/`, `exercises/mathematics/` |
| Khan Academy — Probability & Statistics | https://www.khanacademy.org/math/statistics-probability | `notes/mathematics/probability/`, `notes/mathematics/statistics/` |

## Milestone 2 — Machine learning from scratch

| Course | Link | Maps to |
|---|---|---|
| Andrew Ng — Machine Learning Specialization | https://www.coursera.org/specializations/machine-learning-introduction | `notes/machine-learning/`, `exercises/numpy/`, `implementations/` |
| fast.ai — Practical Deep Learning (Tabular/ML sections) | https://course.fast.ai/ | `notes/machine-learning/` |

## Milestone 3 — Neural networks

| Course | Link | Maps to |
|---|---|---|
| Michael Nielsen — Neural Networks and Deep Learning | http://neuralnetworksanddeeplearning.com/ | `notes/deep-learning/`, `projects/tiny-autograd/` |
| Dive into Deep Learning (d2l.ai) | https://d2l.ai/ | `notes/deep-learning/`, `exercises/pytorch/` |

## Milestone 4 — Computer architecture and GPU

| Course | Link | Maps to |
|---|---|---|
| An Even Easier Introduction to CUDA | https://developer.nvidia.com/blog/even-easier-introduction-cuda/ | `notes/computer-systems/cuda/` |
| CUDA Programming Guide | https://docs.nvidia.com/cuda/cuda-programming-guide/index.html | `notes/computer-systems/cuda/`, `exercises/cuda/` |
| NVIDIA CUDA Zone Exercises (PDF) | https://www.nvidia.com/content/cudazone/download/Exercise_Instructions.pdf | `exercises/cuda/` |
| CMU 15-418 / related systems lectures | https://www.cs.cmu.edu/~418/ | `notes/computer-systems/` |

## Milestone 5 — Transformers and LLMs

| Course | Link | Maps to |
|---|---|---|
| DeepLearning.AI — Transformers in Practice | https://learn.deeplearning.ai/courses/transformers-in-practice/ | `notes/llms/`, `projects/mini-transformer/` |
| Stanford CS224N (public lectures) | https://web.stanford.edu/class/cs224n/ | `notes/llms/`, `papers/transformers/` |
| Andrej Karpathy — Neural Networks: Zero to Hero | https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ | `projects/mini-transformer/`, `exercises/pytorch/` |

## Milestone 6 — Reinforcement learning and world models

| Course | Link | Maps to |
|---|---|---|
| David Silver — RL Course | https://www.youtube.com/playlist?list=PLqLZQ0b3nNYsGrqiiGVZ2qUFiFXn22pjK | `notes/reinforcement-learning/` |
| Spinning Up in Deep RL (OpenAI) | https://spinningup.openai.com/ | `notes/reinforcement-learning/`, `projects/latent-world-model/` |
| Udacity — Agentic AI | https://www.udacity.com/course/agentic-ai--nd900 | `notes/llms/`, agent tooling (applied) |

## Papers (alphaXiv)

| Paper | Link | Sheet |
|---|---|---|
| Attention Is All You Need | https://arxiv.org/abs/1706.03762 | `papers/transformers/attention-is-all-you-need.md` |
| Your reference | https://www.alphaxiv.org/abs/2503.10622 | `papers/` (add sheet when reading) |

## Suggested weekly mix (~8 h)

| Hours | Activity |
|---|---|
| 2 | Video course or reading |
| 2 | Math exercises (`exercises/mathematics/`) |
| 2 | Implementation (`exercises/numpy/`, `pytorch/`, `cuda/`) |
| 1 | Paper sheet |
| 1 | `PROGRESS.md` + glossary |
""",
    )

  # --- CURRICULUM.md index ---
    write(
        ROOT / "CURRICULUM.md",
        """# Curriculum Index

Complete map of notes, exercises, implementations, and experiments.
**Legend:** ✅ done · 📝 scaffold · ⬜ placeholder

See [COURSES.md](COURSES.md) for external course links.

## Exercises by track

| Track | Folder | Count |
|---|---|---|
| Mathematics | [exercises/mathematics/](exercises/mathematics/) | pen-and-paper + SymPy |
| NumPy / ML | [exercises/numpy/](exercises/numpy/) | core ML from scratch |
| PyTorch | [exercises/pytorch/](exercises/pytorch/) | deep learning |
| Systems | [exercises/systems/](exercises/systems/) | hardware and precision |
| CUDA | [exercises/cuda/](exercises/cuda/) | GPU kernels |

## Milestone checklist

Use GitHub [milestones](https://github.com/Tamsi/ai-lab/milestones) and [issues](https://github.com/Tamsi/ai-lab/issues) to track completion.

Each exercise produces: note + code + test + `results.md` + PROGRESS entry.
""",
    )

    M1 = "Milestone 1: Mathematical foundations"
    M2 = "Milestone 2: Machine learning from scratch"
    M3 = "Milestone 3: Neural networks"
    M4 = "Milestone 4: Computer architecture and GPU"
    M5 = "Milestone 5: Transformers and LLMs"
    M6 = "Milestone 6: RL and world models"

    # --- Notes: mathematics ---
    math_la = [
        ("Dot product", "linear-algebra/dot-product.md"),
        ("Matrix multiplication", "linear-algebra/matrix-multiplication.md"),
        ("Linear transformations", "linear-algebra/linear-transformations.md"),
        ("Norms and distances", "linear-algebra/norms-and-distances.md"),
        ("Eigenvalues and eigenvectors", "linear-algebra/eigenvalues.md"),
        ("Orthogonality and projections", "linear-algebra/orthogonal-projections.md"),
    ]
    scaffold_section_readme(
        "notes/mathematics/linear-algebra",
        "Linear Algebra",
        M1,
        math_la,
        "- [3Blue1Brown — Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)",
    )
    for title, fname in math_la[2:]:
        scaffold_note(
            f"mathematics/linear-algebra/{fname}",
            title,
            M1,
            f"exercises/numpy/{fname.replace('.md', '').replace('-', '_')}/",
            "- 3Blue1Brown Linear Algebra",
        )

    math_calc = [
        ("Derivatives", "calculus/derivatives.md"),
        ("Chain rule", "calculus/chain-rule.md"),
        ("Gradients", "calculus/gradients.md"),
        ("Taylor approximation", "calculus/taylor-series.md"),
    ]
    scaffold_section_readme(
        "notes/mathematics/calculus",
        "Calculus",
        M1,
        math_calc,
        "- [3Blue1Brown — Calculus](https://www.youtube.com/playlist?list=PLVUDmbpupCaqz8nECyVys-tFkUs--OKsY)",
    )
    for title, fname in math_calc:
        scaffold_note(f"mathematics/{fname}", title, M1, "exercises/mathematics/", "- 3Blue1Brown Calculus")

    math_prob = [
        ("Probability basics", "probability/probability-basics.md"),
        ("Expectation and variance", "probability/expectation-variance.md"),
        ("Common distributions", "probability/distributions.md"),
        ("Maximum likelihood", "probability/maximum-likelihood.md"),
    ]
    scaffold_section_readme(
        "notes/mathematics/probability",
        "Probability",
        M1,
        math_prob,
        "- [Khan Academy — Probability](https://www.khanacademy.org/math/statistics-probability/probability-library)",
    )
    for title, fname in math_prob:
        scaffold_note(f"mathematics/{fname}", title, M1, "exercises/mathematics/", "- Khan Academy")

    math_stats = [
        ("Estimators and bias", "statistics/estimators.md"),
        ("Confidence intervals", "statistics/confidence-intervals.md"),
        ("Hypothesis testing", "statistics/hypothesis-testing.md"),
    ]
    scaffold_section_readme(
        "notes/mathematics/statistics",
        "Statistics",
        M1,
        math_stats,
        "- Khan Academy Statistics",
    )
    for title, fname in math_stats:
        scaffold_note(f"mathematics/{fname}", title, M1, "exercises/mathematics/", "- Khan Academy")

    math_opt = [
        ("Gradient descent", "optimization/gradient-descent.md"),
        ("Convexity", "optimization/convexity.md"),
        ("Lagrange multipliers", "optimization/lagrange-multipliers.md"),
        ("Adam and momentum", "optimization/adaptive-methods.md"),
    ]
    scaffold_section_readme(
        "notes/mathematics/optimization",
        "Optimization",
        M1,
        math_opt,
        "- d2l.ai optimization chapters",
    )
    for title, fname in math_opt:
        scaffold_note(f"mathematics/{fname}", title, M1, "exercises/numpy/gradient_descent/", "- d2l.ai")

    math_alg = [
        ("Functions and logarithms", "algebra/functions-and-logarithms.md"),
        ("Sigma notation", "algebra/sigma-notation.md"),
    ]
    scaffold_section_readme(
        "notes/mathematics/algebra",
        "Algebra",
        M1,
        math_alg,
        "- 3Blue1Brown / Khan Algebra",
    )
    for title, fname in math_alg:
        scaffold_note(f"mathematics/{fname}", title, M1, "exercises/mathematics/", "- Khan Academy")

    math_it = [
        ("Entropy", "information-theory/entropy.md"),
        ("KL divergence", "information-theory/kl-divergence.md"),
        ("Cross-entropy", "information-theory/cross-entropy.md"),
    ]
    scaffold_section_readme(
        "notes/mathematics/information-theory",
        "Information Theory",
        M5,
        math_it,
        "- Cover & Thomas (reference); ML blogs",
    )
    for title, fname in math_it:
        scaffold_note(f"mathematics/{fname}", title, M5, "exercises/numpy/softmax_cross_entropy/", "- CS224N")

    # --- Notes: computer systems ---
    cs_topics = {
        "binary-and-floating-point": [
            ("IEEE 754 representation", "ieee754.md"),
            ("Floating-point error", "rounding-error.md"),
        ],
        "cpu": [("CPU execution model", "execution-model.md"), ("Pipelining", "pipelining.md")],
        "memory-and-cache": [
            ("Memory hierarchy", "memory-hierarchy.md"),
            ("Cache locality", "cache-locality.md"),
        ],
        "gpu": [("GPU architecture", "gpu-architecture.md"), ("SIMT execution", "simt.md")],
        "distributed-computing": [
            ("Data parallelism", "data-parallelism.md"),
            ("All-reduce", "all-reduce.md"),
        ],
    }
    for folder, topics in cs_topics.items():
        rel_topics = [(t, f"{folder}/{f}") for t, f in topics]
        scaffold_section_readme(
            f"notes/computer-systems/{folder}",
            folder.replace("-", " ").title(),
            M4,
            rel_topics,
            "- CUDA Programming Guide; CMU 15-418",
        )
        for title, fname in topics:
            scaffold_note(
                f"computer-systems/{folder}/{fname}",
                title,
                M4,
                f"exercises/systems/",
                "- CUDA / systems courses",
            )

    # --- Notes: ML domains ---
    domain_notes = {
        "machine-learning": (M2, [
            ("Bias-variance tradeoff", "bias-variance.md"),
            ("Train-validation-test", "data-splits.md"),
            ("Regularization", "regularization.md"),
            ("Evaluation metrics", "evaluation-metrics.md"),
        ]),
        "deep-learning": (M3, [
            ("Neurons and layers", "neurons-and-layers.md"),
            ("Backpropagation", "backpropagation.md"),
            ("Activation functions", "activation-functions.md"),
            ("Initialization", "weight-initialization.md"),
            ("Normalization", "normalization.md"),
        ]),
        "llms": (M5, [
            ("Tokenization", "tokenization.md"),
            ("Embeddings", "embeddings.md"),
            ("Attention", "attention.md"),
            ("Transformer architecture", "transformer.md"),
            ("Autoregressive training", "autoregressive-training.md"),
        ]),
        "reinforcement-learning": (M6, [
            ("Markov decision processes", "mdp.md"),
            ("Bellman equations", "bellman.md"),
            ("Policy gradients", "policy-gradients.md"),
            ("Actor-critic", "actor-critic.md"),
        ]),
        "world-models": (M6, [
            ("Latent dynamics", "latent-dynamics.md"),
            ("Model-based RL", "model-based-rl.md"),
            ("Imagination and planning", "imagination.md"),
        ]),
    }
    for domain, (milestone, topics) in domain_notes.items():
        rel_topics = [(t, f"{t.lower().replace(' ', '-').replace('/', '-')}.md") for t, _ in [(t, t) for t, _ in topics]]
        # fix topic file names
        fixed = []
        for title, fname in topics:
            fixed.append((title, fname))
        scaffold_section_readme(
            f"notes/{domain}",
            domain.replace("-", " ").title(),
            milestone,
            fixed,
            f"- See [COURSES.md](../../COURSES.md)",
        )
        for title, fname in topics:
            scaffold_note(f"{domain}/{fname}", title, milestone, f"exercises/", "- See COURSES.md")

    # --- exercises/mathematics ---
    write(ROOT / "exercises/mathematics/README.md", "# Mathematics Exercises\n\nPen-and-paper and SymPy exercises. See subfolders.\n")
    math_exercises = [
        ("sigma_notation", "Sigma notation drills", M1, "Practice summation notation", ["Paper only or SymPy"], ["Rewrite sums", "Expand examples"], ["When is notation ambiguous?"], "notes/mathematics/algebra/sigma-notation.md", "expand_sigma"),
        ("derivatives", "Derivatives of common functions", M1, "Compute derivatives by hand and verify with SymPy", ["SymPy allowed"], ["Polynomials", "Log/exp", "Chain rule examples"], ["Where do non-differentiable points matter in ML?"], "notes/mathematics/calculus/derivatives.md", "derivative"),
        ("gradients", "Multivariate gradients", M1, "Compute gradients of scalar fields", ["SymPy allowed"], ["Quadratic form", "Rosenbrock", "Log-likelihood"], ["Connection to gradient descent?"], "notes/mathematics/calculus/gradients.md", "gradient"),
        ("probability_drills", "Probability exercises", M1, "Bayes rule and expectation", ["Paper or SymPy"], ["Conditional probability", "Law of total probability"], ["Common confusion in ML papers?"], "notes/mathematics/probability/probability-basics.md", "bayes"),
    ]
    for args in math_exercises:
        scaffold_exercise("mathematics", *args)

    # --- exercises/numpy (new ones) ---
    write(ROOT / "exercises/numpy/README.md", "# NumPy Exercises\n\nMachine learning building blocks from scratch.\n")
    numpy_exercises = [
        ("linear_transformations", "Linear transformations", M1, "Apply matrices to basis vectors and visualize", ["NumPy + Matplotlib"], ["2D rotation", "Shear", "Composition"], ["How does this relate to neural layers?"], "notes/mathematics/linear-algebra/linear-transformations.md", "apply_transform"),
        ("linear_regression", "Linear regression from scratch", M1, "Implement OLS and gradient descent", ["NumPy only", "No sklearn for core"], ["MSE", "Analytical solution", "GD"], ["Effect of learning rate?"], "implementations/linear-regression/", "predict_linear"),
        ("logistic_regression", "Logistic regression from scratch", M2, "Binary classification with sigmoid", ["NumPy only"], ["Sigmoid", "Cross-entropy", "GD"], ["Decision boundary shape?"], "implementations/logistic-regression/", "predict_logistic"),
        ("gradient_descent", "Gradient descent on 2D surfaces", M1, "Implement GD on quadratic and Rosenbrock", ["NumPy + Matplotlib"], ["Plot trajectory", "Compare learning rates"], ["When does GD fail?"], "notes/mathematics/optimization/gradient-descent.md", "gradient_descent_step"),
        ("softmax_cross_entropy", "Softmax and cross-entropy", M1, "Stable softmax and CE loss", ["NumPy only"], ["Softmax", "CE", "Numerical stability"], ["Why log-sum-exp trick?"], "notes/mathematics/information-theory/cross-entropy.md", "cross_entropy"),
        ("train_val_test", "Train-validation-test splits", M2, "Implement splits and leakage checks", ["NumPy only"], ["Random split", "Stratified split"], ["What leaks validation into training?"], "notes/machine-learning/data-splits.md", "train_val_test_split"),
        ("pca", "PCA from scratch", M2, "Eigendecomposition on covariance", ["NumPy only"], ["Center data", "Covariance", "Project"], ["Link to SVD?"], "implementations/pca/", "pca_transform"),
        ("k_means", "K-means clustering", M2, "Lloyd's algorithm", ["NumPy only"], ["Assign", "Update", "Convergence"], ["Sensitivity to initialization?"], "notes/machine-learning/", "k_means_step"),
        ("regularization", "L2 regularization", M2, "Ridge regression effect", ["NumPy only"], ["Add penalty", "Compare coefficients"], ["Bias-variance tradeoff?"], "notes/machine-learning/regularization.md", "ridge_loss"),
    ]
    for args in numpy_exercises:
        scaffold_exercise("numpy", *args)

    # --- exercises/pytorch ---
    write(ROOT / "exercises/pytorch/README.md", "# PyTorch Exercises\n\nDeep learning implementations.\n")
    torch_exercises = [
        ("tensor_basics", "Tensor basics", M3, "Shapes, broadcasting, device moves", ["PyTorch"], ["Create tensors", "Broadcast rules", "GPU if available"], ["When does broadcasting hide bugs?"], "notes/deep-learning/", "tensor_ops"),
        ("mlp_from_scratch", "MLP from scratch", M3, "Multi-layer perceptron with manual forward", ["PyTorch"], ["Linear layers", "ReLU", "Forward pass"], ["Parameter count?"], "notes/deep-learning/neurons-and-layers.md", "mlp_forward"),
        ("backprop_manual", "Manual backprop check", M3, "Compare manual grads to autograd", ["PyTorch"], ["Tiny network", "assert close"], ["Which ops are tricky?"], "notes/deep-learning/backpropagation.md", "manual_backward"),
        ("optimizers", "Optimizer comparison", M3, "SGD vs momentum vs Adam on same loss", ["PyTorch + Matplotlib"], ["Run all", "Plot loss"], ["When does Adam help?"], "notes/mathematics/optimization/adaptive-methods.md", "train_one_epoch"),
        ("attention_scratch", "Scaled dot-product attention", M5, "Implement attention block", ["PyTorch"], ["QKV", "Mask", "Output"], ["Memory complexity?"], "notes/llms/attention.md", "scaled_dot_product_attention"),
        ("transformer_block", "Transformer block", M5, "One encoder block", ["PyTorch"], ["MHA", "FFN", "LayerNorm"], ["Parameter breakdown?"], "notes/llms/transformer.md", "transformer_block"),
        ("tokenizer_bpe", "BPE tokenizer", M5, "Train tiny BPE on corpus", ["Python"], ["Merge rules", "Encode/decode"], ["OOV handling?"], "notes/llms/tokenization.md", "bpe_encode"),
    ]
    for args in torch_exercises:
        scaffold_exercise("pytorch", *args)

    # --- exercises/systems ---
    write(ROOT / "exercises/systems/README.md", "# Systems Exercises\n\nHardware, memory, and precision.\n")
    systems_exercises = [
        ("ieee754", "IEEE 754 representation", M4, "Inspect float bit patterns", ["Python struct module"], ["Print bits", "Compare epsilons"], ["When does ML break?"], "notes/computer-systems/binary-and-floating-point/ieee754.md", "float_bits"),
        ("floating_point_accumulation", "Floating-point accumulation error", M4, "Sum many small values", ["NumPy"], ["Compare orders"], ["Real-world impact?"], "notes/computer-systems/binary-and-floating-point/rounding-error.md", "unstable_sum"),
        ("cache_friendly_matmul", "Cache-friendly access patterns", M4, "Loop order effects", ["NumPy or pure Python"], ["ijk vs ikj"], ["Why does order matter?"], "notes/computer-systems/memory-and-cache/cache-locality.md", "matmul_order"),
        ("cpu_vs_gpu_baseline", "CPU vs GPU baseline", M4, "Same op on CPU and GPU", ["PyTorch optional"], ["Time matmul", "Record hardware"], ["Transfer overhead?"], "experiments/cpu-vs-gpu/", "benchmark_matmul"),
    ]
    for args in systems_exercises:
        scaffold_exercise("systems", *args)

    # --- exercises/cuda labs ---
    cuda_labs = [
        ("lab_01_vector_add", "CUDA Lab 1 — Vector addition", M4, "First kernel: element-wise add", ["CUDA C++", "nvcc"], ["Allocate", "Launch", "Verify"], ["Block size effects?"], "notes/computer-systems/cuda/", "vector_add"),
        ("lab_02_matrix_multiply_naive", "CUDA Lab 2 — Naive matmul", M4, "Global memory matmul kernel", ["CUDA C++"], ["Naive kernel", "Correctness"], ["vs cuBLAS?"], "notes/computer-systems/cuda/", "matmul_naive"),
        ("lab_03_shared_memory_tiling", "CUDA Lab 3 — Tiled matmul", M4, "Shared memory tile optimization", ["CUDA C++"], ["Tiled kernel", "Benchmark"], ["Occupancy?"], "notes/computer-systems/cuda/", "matmul_tiled"),
    ]
    for args in cuda_labs:
        scaffold_exercise("cuda", *args)

    # --- implementations ---
    impls = [
        ("linear-regression", "Linear Regression", M1, "From-scratch linear regression with GD and closed form."),
        ("logistic-regression", "Logistic Regression", M2, "Binary classifier with sigmoid and cross-entropy."),
        ("pca", "PCA", M2, "Principal component analysis via covariance eigendecomposition."),
        ("neural-network", "Neural Network", M3, "MLP with manual or autograd backprop."),
        ("autograd-engine", "Autograd Engine", M3, "Minimal computation graph and backward pass."),
        ("tokenizer", "Tokenizer", M5, "BPE or character-level tokenizer."),
        ("transformer", "Transformer", M5, "Small decoder-only transformer."),
        ("world-model", "World Model", M6, "Latent dynamics model for 2D environment."),
    ]
    for slug, title, milestone, desc in impls:
        scaffold_impl(slug, title, milestone, desc)

    # --- experiments ---
    experiments = [
        ("gradient-descent", "Gradient Descent Visualization", M1, "Loss surfaces and optimization trajectories."),
        ("floating-point-precision", "Floating-Point Precision", M4, "fp16/bf32/fp64 comparison on reductions."),
        ("cpu-vs-gpu", "CPU vs GPU", M4, "Throughput and latency across backends."),
        ("matrix-multiplication", "Matrix Multiplication Benchmark", M1, "Scaling with matrix size."),
        ("attention-memory", "Attention Memory", M5, "Memory vs sequence length for attention."),
        ("model-scaling", "Model Scaling", M5, "Params, FLOPs, and memory vs model size."),
    ]
    for slug, title, milestone, desc in experiments:
        scaffold_experiment(slug, title, milestone, desc)

    # --- papers ---
    paper_stubs = [
        ("transformers/attention-is-all-you-need.md", None, None),  # exists
        ("optimization/adam.md", "Adam: A Method for Stochastic Optimization", "https://arxiv.org/abs/1412.6980"),
        ("llms/llama.md", "LLaMA: Open and Efficient Foundation Language Models", "https://arxiv.org/abs/2302.13971"),
        ("reinforcement-learning/dqn.md", "Playing Atari with Deep Reinforcement Learning", "https://arxiv.org/abs/1312.5602"),
        ("reinforcement-learning/ppo.md", "Proximal Policy Optimization Algorithms", "https://arxiv.org/abs/1707.06347"),
        ("world-models/dreamerv3.md", "DreamerV3", "https://arxiv.org/abs/2301.04104"),
        ("world-models/alphaxiv-2503.md", "Paper 2503.10622", "https://www.alphaxiv.org/abs/2503.10622"),
    ]
    for item in paper_stubs:
        if item[1] is None:
            continue
        rel, title, link = item
        scaffold_paper(rel, title, link)

    # package inits
    for cat in ["mathematics", "pytorch", "systems", "cuda"]:
        write(ROOT / "exercises" / cat / "__init__.py", "")

    print("Curriculum scaffolds generated.")


if __name__ == "__main__":
    main()
