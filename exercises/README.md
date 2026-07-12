# Exercises

## Subjects

List of things to implement. Create a folder only when you start one.

| Status | Subject | Folder | Verify |
|---|---|---|---|
| [x] | Dot product from scratch | [dot-product/](dot-product/) | `pytest exercises/dot-product` |
| [x] | Matrix multiplication (loops + NumPy bench) | [matrix-multiplication/](matrix-multiplication/) | `pytest exercises/matrix-multiplication` |
| [ ] | N-gram language model | _(create `n-grams/` when ready)_ | |
| [ ] | Softmax + cross-entropy | | |
| [ ] | Gradient descent visualization | | |
| [ ] | Scaled dot-product attention | | |
| [ ] | Minimal SFT loop | | |
| [ ] | CUDA vector add | | |

## Folder layout (when you start an exercise)

```text
exercises/<subject>/
├── solution.py       ← your code
├── test_*.py         ← tests (copy from dot-product/)
└── results.md        ← what you observed (optional)
```

Copy [dot-product/](dot-product/) as a starting point.
