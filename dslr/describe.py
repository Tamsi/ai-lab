"""
describe.py — display Count / Mean / Std / Min / 25% / 50% / 75% / Max
for every numerical feature of a dataset.

Usage:
    python describe.py datasets/dataset_train.csv

Forbidden: pandas.DataFrame.describe, numpy mean/std/percentile helpers, etc.
Implement stats in utils.py and call them here.
"""

import sys

from utils import (
    column_values,
    count,
    load_csv,
    maximum,
    mean,
    minimum,
    numerical_features,
    percentile,
    std,
    usage,
)


def describe(path):
    """
    TODO 1: load CSV with load_csv
    TODO 2: get numerical feature names
    TODO 3: for each feature, collect values and compute the 8 stats
    TODO 4: print a table (features as columns, stats as rows) similar to subject
    """
    # TODO: implement
    raise NotImplementedError("describe")


def main():
    if len(sys.argv) != 2:
        usage("Usage: python describe.py <dataset.csv>")
    describe(sys.argv[1])


if __name__ == "__main__":
    main()
