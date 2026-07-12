"""Dot product exercise — implement dot_product() in solution.py."""

from exercises.numpy.dot_product.solution import dot_product


def demo_geometric_cases() -> None:
    aligned = ([1.0, 0.0], [2.0, 0.0])
    opposite = ([1.0, 0.0], [-1.0, 0.0])
    orthogonal = ([1.0, 0.0], [0.0, 1.0])

    for label, (x, y) in [
        ("aligned", aligned),
        ("opposite", opposite),
        ("orthogonal", orthogonal),
    ]:
        print(f"{label}: {dot_product(x, y)}")


if __name__ == "__main__":
    demo_geometric_cases()
