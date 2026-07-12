# alphaXiv Reading Queue

Papers to read with **concepts to deepen** — the goal is not full comprehension on
first pass, but to know precisely what to study next.

**Workflow**

1. Add a row below with link and concepts
2. Create or open the paper sheet in `papers/<topic>/`
3. Add concepts to [CONCEPTS.md](../CONCEPTS.md) if missing
4. Create GitHub issue per concept or per paper (optional)
5. Update status as you progress: `queued` → `first read` → `concepts mapped` → `understood` → `reproduced`

---

## Queue

| arXiv | Title | Concepts to deepen | Sheet | Status |
|---|---|---|---|---|
| [2606.18089](https://www.alphaxiv.org/abs/2606.18089) | From Reasoning Traces to Reusable Modules (SFT + RL) | **SFT**, **RL post-training**, **n-grams**, compositional generalization, latent module selection | [sheet](llms/2026-compositional-generalization-sft-rl.md) | first read |
| [1706.03762](https://www.alphaxiv.org/abs/1706.03762) | Attention Is All You Need | attention, positional encoding, encoder-decoder | [sheet](transformers/attention-is-all-you-need.md) | first read |
| [2503.10622](https://www.alphaxiv.org/abs/2503.10622) | _(add title when reading)_ | _(list gaps after skim)_ | [sheet](world-models/alphaxiv-2503.md) | queued |

---

## Concept index from papers

Reverse lookup: which papers mention a concept you want to learn?

| Concept | Papers |
|---|---|
| SFT | [2606.18089](llms/2026-compositional-generalization-sft-rl.md) |
| RL post-training | [2606.18089](llms/2026-compositional-generalization-sft-rl.md) |
| N-grams | [2606.18089](llms/2026-compositional-generalization-sft-rl.md) |
| Attention | [1706.03762](transformers/attention-is-all-you-need.md) |
| Compositional generalization | [2606.18089](llms/2026-compositional-generalization-sft-rl.md) |

---

## Template (copy for new papers)

```markdown
| [XXXX.XXXXX](https://www.alphaxiv.org/abs/XXXX.XXXXX) | Title | concept1, concept2 | [sheet](topic/slug.md) | queued |
```
