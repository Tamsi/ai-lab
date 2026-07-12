"""Matrix multiplication exercise — implement matmul() in solution.py."""

import time

import numpy as np

from exercises.numpy.matrix_multiplication.solution import matmul


def benchmark_sizes(sizes: list[int]) -> None:
    rng = np.random.default_rng(42)
    for n in sizes:
        A = rng.standard_normal((n, n)).tolist()
        B = rng.standard_normal((n, n)).tolist()

        t0 = time.perf_counter()
        _ = matmul(A, B)
        loop_s = time.perf_counter() - t0

        A_np = np.array(A)
        B_np = np.array(B)
        t0 = time.perf_counter()
        _ = A_np @ B_np
        numpy_s = time.perf_counter() - t0

        print(f"n={n:4d}  loop={loop_s:.4f}s  numpy={numpy_s:.6f}s  speedup={loop_s / numpy_s:.0f}x")


if __name__ == "__main__":
    benchmark_sizes([32, 64, 128])
