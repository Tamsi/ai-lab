# Exercise Submission

## Workflow

1. **Pick** an exercise from [EXERCISES.md](EXERCISES.md)
2. **Read** the linked concept note in `notes/`
3. **Implement** in `solution.py` (do not edit `test_solution.py` unless adding tests you need)
4. **Remove** `pytest.mark.skip` from `test_solution.py` when ready to verify
5. **Run locally:**
   ```bash
   python scripts/submit.py <category>/<exercise>
   # example:
   python scripts/submit.py numpy/dot_product
   ```
6. **Record observations** in `results.md`
7. **Update** [CONCEPTS.md](../CONCEPTS.md) and [PROGRESS.md](../PROGRESS.md)

## What verification does

`scripts/submit.py`:

1. Runs `pytest` on `test_solution.py` for that exercise
2. Prints pass/fail output
3. Appends result to [submissions/registry.json](submissions/registry.json)

```json
{
  "submissions": [
    {
      "exercise": "numpy/dot_product",
      "status": "passed",
      "timestamp": "2026-07-12T21:00:00+00:00"
    }
  ]
}
```

## Folder structure

```text
exercises/<category>/<name>/
├── README.md           # objectives, constraints, reflection
├── exercise.py         # optional demo / benchmark runner
├── solution.py         # YOUR implementation
├── test_solution.py    # automated verification (pytest)
└── results.md          # what you observed
```

## CUDA exercises

CUDA labs may use `.cu` files + Makefile instead of pure Python. Keep
`test_solution.py` as a host-side correctness check (e.g. compare CPU reference).

## Rules

- **Public repo:** your own implementations only (no university graded solutions)
- Tests must pass without network access
- Honest `results.md` — failures are valuable data
