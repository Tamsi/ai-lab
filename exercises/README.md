# Exercises

Subjects to implement. Full list with resources → [topics/](../topics/).

| Status | Subject | Topic sheet | Folder |
|---|---|---|---|
| [x] | Dot product | [dot-product](../topics/dot-product.md) | [dot-product/](dot-product/) |
| [x] | Matrix multiplication | [matrix-multiplication](../topics/matrix-multiplication.md) | [matrix-multiplication/](matrix-multiplication/) |
| [ ] | Gradient descent | [gradient-descent](../topics/gradient-descent.md) | _(create folder)_ |
| [ ] | Linear regression | [supervised-learning](../topics/supervised-learning.md) | _(create folder)_ |
| [ ] | N-grams | [n-grams](../topics/n-grams.md) | _(create folder)_ |
| [ ] | Attention | [attention](../topics/attention.md) | _(create folder)_ |
| [ ] | Encoder–decoder | [encoder-decoder](../topics/encoder-decoder.md) | _(create folder)_ |
| [ ] | Mini SFT | [sft](../topics/sft.md) | _(create folder)_ |

## Folder layout

```text
exercises/<subject>/
├── solution.py
├── test_*.py
└── results.md      # optional
```

Copy [dot-product/](dot-product/) when starting a new one.

```bash
pytest exercises/<subject>
```
