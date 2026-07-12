# Supervised Fine-Tuning (SFT)

**Status:** Not started  
**Milestone:** LLMs  
**Related exercise:** [sft_mini](../../exercises/pytorch/sft_mini/)  
**Papers:** [2606.18089](../../papers/llms/2026-compositional-generalization-sft-rl.md)

## Intuition

SFT teaches a pretrained language model to **imitate** desired outputs on labeled
(prompt, response) pairs. It is the first step in most LLM alignment pipelines:
the model learns format, style, and task behavior before optional RL refinement.

## Formal definition

Given dataset \(\mathcal{D} = \{(x^{(i)}, y^{(i)})\}\), minimize negative log-likelihood:

\[
\mathcal{L}_{\text{SFT}}(\theta) = - \sum_{(x,y) \in \mathcal{D}} \sum_{t} \log \pi_\theta(y_t \mid x, y_{<t})
\]

Only target tokens \(y\) contribute to the loss (prompt tokens are usually masked).

## Why it matters in machine learning

- Default way to specialize a base LLM to instructions or reasoning traces
- In [2606.18089](../../papers/llms/2026-compositional-generalization-sft-rl.md): SFT supplies **compound traces** containing atomic skills
- Pairs naturally with RL when imitation alone does not generalize

## Minimal implementation

```python
# Cross-entropy on response tokens only; prompt masked with -100 in PyTorch
loss = F.cross_entropy(logits.view(-1, vocab), targets.view(-1), ignore_index=-100)
```

## Experiment

Fine-tune a tiny GPT on 100 (question, short answer) pairs; compare samples before/after.

## Connection to research papers

SFT + RL asymmetry in compositional reasoning — SFT provides materials, RL recomposes.

## What I still do not understand

- Optimal data mix (quality vs quantity) for reasoning SFT
- When SFT hurts exploration before RL
- How to mask variable-length chat templates correctly
