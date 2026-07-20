# Day 6 — Write the Tests

Last time (Day 4) you were handed a function and wrote tests for it. This time you've got a
small module — your job is to find the cases worth testing, not just read tracebacks.

## Setup

1. Fork this repo (top right → **Fork**)
2. Clone your fork
3. `cd` into this folder: `day6-testing/`
4. `pip install pytest` if you don't already have it

## What's here

- `store_analytics.py` — the module under test. Read every docstring closely — that's the
  spec. It tells you exactly what counts as correct, including how each function should
  handle bad input.
- `test_store_analytics.py` — your starter file. `pytest` and the module are already
  imported, and one test is already written to show you the pattern.
- `sample_orders.csv` — a small sample data file, used for testing `load_orders_from_csv`.

## Your task

Add your own tests to `test_store_analytics.py`, below the example. Aim for **8-10 tests**
covering genuinely different cases — not eight variations on the same idea. Want the
stretch goal? Push for **15**, and think about *why* a case is worth testing, not just how
many you can write.

Most of your tests should be unit tests (one function, checked in isolation). Trying a test
that exercises more than one function working together? That's an integration test — one or
two of those is a nice stretch, not a requirement.

## Before you submit

Run your tests:

```
pytest -v
```

Make sure everything passes before you commit.

## Submit

Commit and push to your fork, then drop your fork URL in [submission sheet] by [deadline].
