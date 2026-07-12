"""Matrix multiplication — your implementation goes here."""


def matmul(A: list[list[float]], B: list[list[float]]) -> list[list[float]]:
    m, n = len(A), len(A[0])
    n_b, p = len(B), len(B[0])
    if n != n_b:
        raise ValueError(f"Incompatible shapes: ({m},{n}) x ({n_b},{p})")

    C = [[0.0] * p for _ in range(m)]
    for i in range(m):
        for j in range(p):
            total = 0.0
            for k in range(n):
                total += A[i][k] * B[k][j]
            C[i][j] = total
    return C
