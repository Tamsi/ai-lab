# Tiny Autograd

**Status:** Planned (Milestone 3)

Build a minimal automatic differentiation engine:

```python
a = Value(2.0)
b = Value(3.0)
c = a * b
c.backward()
```

Target API and concepts: computation graph, chain rule, local derivatives, backpropagation.
