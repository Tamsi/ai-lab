"""
logreg_predict.py — predict Hogwarts houses for the test set.

Usage:
    python logreg_predict.py datasets/dataset_test.csv weights.txt

Output:
    houses.csv with header: Index,Hogwarts House
"""

import sys

from utils import load_csv, sigmoid, usage


HOUSES = ("Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin")
OUTPUT_PATH = "houses.csv"


def load_weights(path):
    """
    Reload what save_weights wrote.

    TODO 1: parse features, means, stds, thetas
    TODO 2: return (features, means, stds, thetas_dict)
    """
    # TODO: implement
    raise NotImplementedError("load_weights")


def prepare_test_features(rows, features, means, stds):
    """
    Build biased, scaled X for the test set.

    TODO 1: extract the same feature columns in the same order
    TODO 2: apply the SAME missing-value policy as training
    TODO 3: scale with train means/stds (do NOT recompute on test)
    TODO 4: add bias column
    TODO 5: also keep the Index values aligned with the rows you output
    TODO 6: return indexes, X
    """
    # TODO: implement
    raise NotImplementedError("prepare_test_features")


def predict_house(x, thetas):
    """
    One-vs-all decision:

      house = argmax_h  sigmoid(theta_h · x)

    TODO 1: for each house, compute probability
    TODO 2: return the house with the highest probability
    """
    # TODO: implement
    raise NotImplementedError("predict_house")


def write_houses(path, indexes, houses):
    """
    Exact format required by the subject:

        Index,Hogwarts House
        0,Gryffindor
        1,Hufflepuff
        ...

    TODO 1: open path for writing
    TODO 2: write header
    TODO 3: write each Index,house line
    """
    # TODO: implement
    raise NotImplementedError("write_houses")


def main():
    if len(sys.argv) != 3:
        usage("Usage: python logreg_predict.py <dataset_test.csv> <weights_file>")

    # TODO: load weights, load test CSV, prepare features,
    #       predict each house, write houses.csv
    raise NotImplementedError("logreg_predict.main pipeline")


if __name__ == "__main__":
    main()
