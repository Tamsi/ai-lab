# Tests

Shared test utilities and smoke tests for the repository.

Exercise-specific tests live next to each exercise (e.g. `exercises/numpy/dot-product/test_solution.py`).

## Run all tests

```bash
pip install numpy pytest matplotlib
pytest
```

Run a single exercise demo:

```bash
python -m exercises.numpy.dot_product.exercise
python -m exercises.numpy.matrix_multiplication.exercise
```
