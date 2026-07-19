"""
histogram.py — answer:

Which Hogwarts course has a homogeneous score distribution between all four houses?

Usage:
    python histogram.py datasets/dataset_train.csv
"""

import sys

import matplotlib.pyplot as plt

from utils import load_csv, numerical_features, usage


HOUSES = ("Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin")


def plot_histograms(path):
    """
    TODO 1: load the train CSV
    TODO 2: for each numerical course feature:
              - split scores by Hogwarts House
              - plot overlapping histograms (one color per house)
    TODO 3: visually identify the most homogeneous course
    TODO 4: print the course name you believe answers the subject question
    TODO 5: show or save the figure(s)
    """
    # TODO: implement
    raise NotImplementedError("plot_histograms")


def main():
    if len(sys.argv) != 2:
        usage("Usage: python histogram.py <dataset_train.csv>")
    plot_histograms(sys.argv[1])


if __name__ == "__main__":
    main()
