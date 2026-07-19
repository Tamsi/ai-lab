"""
pair_plot.py — scatter-plot matrix to choose features for logistic regression.

Question:
From this visualization, which features are you going to use for your logistic regression?

Usage:
    python pair_plot.py datasets/dataset_train.csv
"""

import sys

import matplotlib.pyplot as plt

from utils import load_csv, numerical_features, usage


def plot_pair(path):
    """
    TODO 1: load the train CSV
    TODO 2: select numerical features (maybe drop obvious useless ones first)
    TODO 3: build a pair plot / scatter matrix
            (rows/cols = features; optional: color points by house)
    TODO 4: from the plot, choose the features you will keep for training
    TODO 5: print your selected feature list
    TODO 6: show or save the figure
    """
    # TODO: implement
    raise NotImplementedError("plot_pair")


def main():
    if len(sys.argv) != 2:
        usage("Usage: python pair_plot.py <dataset_train.csv>")
    plot_pair(sys.argv[1])


if __name__ == "__main__":
    main()
