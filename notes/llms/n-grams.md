# N-gram Language Models

**Status:** Not started  
**Milestone:** LLMs  
**Related exercise:** [ngrams_language_model](../../exercises/pytorch/ngrams_language_model/)  
**Papers:** [2606.18089](../../papers/llms/2026-compositional-generalization-sft-rl.md)

## Intuition

An **n-gram** model predicts the next token from only the previous \(n{-}1\) tokens.
It estimates \(P(w_t \mid w_{t-n+1}, \ldots, w_{t-1})\) via counting in a corpus.
Simple, interpretable baseline before neural LMs.

## Formal definition

Maximum likelihood on counts:

\[
P(w_t \mid w_{t-n+1:t-1}) = \frac{\text{count}(w_{t-n+1:t})}{\text{count}(w_{t-n+1:t-1})}
\]

Smoothing (e.g. Laplace) avoids zero probabilities for unseen n-grams.

## Why it matters in machine learning

- Historical baseline for language modeling
- Often used in papers as a **simple comparator** to neural models
- Builds intuition for Markov assumptions and sparsity
- Mentioned in [2606.18089](../../papers/llms/2026-compositional-generalization-sft-rl.md) — verify role in experiments when reading

## Minimal implementation

```python
from collections import defaultdict

def train_bigram(tokens):
    counts = defaultdict(lambda: defaultdict(int))
    for a, b in zip(tokens, tokens[1:]):
        counts[a][b] += 1
    return counts
```

## Experiment

Train bigram/trigram on a tiny corpus; compare perplexity to a small neural LM.

## Connection to research papers

Baseline or analysis tool in compositional reasoning experiments.

## What I still do not understand

- Where exactly n-grams are used in 2606.18089 (baseline? negative control?)
- Smoothing tradeoffs at scale
- Bridge from n-grams to subword BPE tokenization
