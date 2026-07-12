# Dot Product — Results

## Geometric cases

| Pair | x · y | Interpretation |
|---|---|---|
| [1,0] · [2,0] | 2.0 | Same direction → positive |
| [1,0] · [-1,0] | -1.0 | Opposite → negative |
| [1,0] · [0,1] | 0.0 | Perpendicular → zero |

## Observations

- The dot product encodes directional alignment, not just magnitude.
- For unit vectors, x · y equals cos(θ); this is the basis of cosine similarity.
- A linear layer output yᵢ = wᵢ · x + bᵢ is one dot product per neuron.

## Failures / surprises

_(None yet — update as you experiment.)_

## Conclusions

The dot product is the atomic operation behind matrix-vector multiply and attention
scores. Understanding these three geometric cases makes the attention formula
less mysterious.
