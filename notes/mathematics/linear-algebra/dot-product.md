# Dot Product

## Intuition

The dot product measures how much one vector "points in the direction of" another.
When two vectors align, the dot product is large and positive. When they point in
opposite directions, it is large and negative. When they are perpendicular
(orthogonal), it is zero.

Think of it as: *how much of **b** lies along **a*** (up to scaling).

## Formal definition

For two vectors **x** = (x₁, …, xₙ) and **y** = (y₁, …, yₙ):

**x · y** = Σᵢ xᵢ yᵢ

## Geometric interpretation

**x · y** = ‖x‖ ‖y‖ cos(θ)

where θ is the angle between the vectors and ‖·‖ denotes the Euclidean norm.

Consequences:

- **x · y** = 0 when vectors are orthogonal (θ = 90°)
- **x · x** = ‖x‖² (squared length)
- Projection of **y** onto **x**: ( (**x · y**) / ‖x‖² ) **x**

## Why it matters in machine learning

- **Similarity** between embedding vectors
- **Attention scores** in Transformers: queries and keys are compared via dot products
- **Linear layers**: matrix-vector multiply is a stack of dot products
- **Cosine similarity**: dot product normalized by vector lengths

## Minimal implementation

```python
def dot_product(x, y):
  if len(x) != len(y):
    raise ValueError("Vectors must have the same length")
  return sum(a * b for a, b in zip(x, y))
```

## Experiment

Compare dot products for:

1. **x** = [1, 0], **y** = [1, 0] → same direction → positive maximum (for unit vectors)
2. **x** = [1, 0], **y** = [-1, 0] → opposite → negative
3. **x** = [1, 0], **y** = [0, 1] → perpendicular → zero

See `exercises/numpy/dot_product/` for runnable code and benchmarks.

## Connection to research papers

The Transformer attention mechanism computes dot products between query and key
vectors to produce attention scores before the softmax.

## What I still do not understand

- Why large dimensions increase attention score variance (need more probability theory)
- Why attention divides scores by √d_k before softmax (numerical stability vs. gradient flow)
