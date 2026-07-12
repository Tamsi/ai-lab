# Glossary

Scientific vocabulary and notation used across this repository. Add entries as
concepts are studied — do not try to fill this upfront.

---

## Notation

| Symbol | Meaning |
|---|---|
| **x**, **y** | Vectors (column vectors unless stated otherwise) |
| **A**, **W** | Matrices |
| x · y | Dot product (inner product) of vectors x and y |
| ‖x‖ | Norm of vector x |
| Σᵢ | Summation over index i |
| θ | Model parameters |
| η | Learning rate |
| ∇L(θ) | Gradient of loss L with respect to θ |
| d_k | Key dimension in multi-head attention |

---

## Terms

### Dot product

Algebraic sum of element-wise products of two vectors. Geometrically related to
projection and the angle between vectors. Central to attention scores and linear
layers.

### Matrix multiplication

Combines linear transformations. For **C** = **AB**, entry Cᵢⱼ is the dot product
of row i of **A** with column j of **B**. Requires inner dimensions to match.

### Gradient descent

Iterative optimization: θ_{t+1} = θ_t − η ∇L(θ_t). Moves parameters in the
direction that most reduces the loss.

---

_Add new entries at the bottom as learning progresses._
