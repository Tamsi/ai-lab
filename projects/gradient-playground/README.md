# Gradient Playground

**Status:** Planned (start week 3)

## Goal

Interactive visualization of optimization on 2D loss surfaces. Adjust learning rate,
starting point, optimizer, and iteration count — then watch the parameter trajectory.

## Concepts

- Functions and loss surfaces
- Gradients and partial derivatives
- Learning rate and convergence
- SGD, momentum, Adam (later)

## Triangle

```text
Equation:  θ_{t+1} = θ_t − η ∇L(θ_t)
Code:      theta = theta - learning_rate * gradient
Plot:      loss surface + optimization path
```

## Planned stack

- Python, NumPy, Matplotlib
- Optional: small web UI (later)

## Milestones

- [ ] Plot a 2D loss function (e.g. bowl, Rosenbrock)
- [ ] Implement gradient descent step
- [ ] Animate trajectory over iterations
- [ ] Compare learning rates side by side
- [ ] Add momentum (optional)

## Related

- Milestone 1 (optimization foundations)
- `experiments/gradient-descent/` (benchmarks and plots)
