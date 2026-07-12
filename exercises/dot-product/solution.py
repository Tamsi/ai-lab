"""Dot product — your implementation goes here."""


def dot_product(x: list[float], y: list[float]) -> float:
    if len(x) != len(y):
        raise ValueError("Vectors must have the same length")
    return sum(a * b for a, b in zip(x, y))
