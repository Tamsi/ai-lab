"""
scatter_plot.py — answer:

What are the two features that are similar?

Usage:
    python scatter_plot.py datasets/dataset_train.csv
"""

import sys

import matplotlib.pyplot as plt

from utils import load_csv, numerical_features, usage


def plot_scatter(path):
    """
    TODO 1: load the train CSV
    TODO 2: explore pairs of numerical features (scatter)
    TODO 3: find the two features that look almost identical / linearly related
    TODO 4: display ONE clear scatter plot for that pair
    TODO 5: print the two feature names
    """
    # TODO: implement
    raise NotImplementedError("plot_scatter")


def main():
    if len(sys.argv) != 2:
        usage("Usage: python scatter_plot.py <dataset_train.csv>")
    plot_scatter(sys.argv[1])


if __name__ == "__main__":
    main()
