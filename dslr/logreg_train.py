"""
logreg_train.py — train one-vs-all logistic regression with gradient descent.

Usage:
    python logreg_train.py datasets/dataset_train.csv

Output:
    a weights file (choose a format) that logreg_predict.py can reload.
"""

import math
import sys

from utils import load_csv, sigmoid, usage


HOUSES = ("Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin")
WEIGHTS_PATH = "weights.txt"

# After pair_plot exploration, put your chosen features here.
SELECTED_FEATURES = [
    # TODO: fill with course names, e.g. "Astronomy", "Herbology", ...
]

LEARNING_RATE = 0.1
ITERATIONS = 1000


def prepare_dataset(rows):
    """
    Build X (list of feature vectors) and house labels (list of house names).

    TODO 1: keep only rows usable for training (handle missing values)
    TODO 2: extract SELECTED_FEATURES in a fixed order
    TODO 3: return raw feature rows + houses
    """
    # TODO: implement
    raise NotImplementedError("prepare_dataset")


def fit_scaler(X):
    """
    Compute per-feature mean and std on training X (no bias column yet).

    TODO 1: for each feature column, compute mean and std (reuse utils)
    TODO 2: return (means, stds)
    """
    # TODO: implement
    raise NotImplementedError("fit_scaler")


def transform(X, means, stds):
    """
    x_scaled = (x - mean) / std

    TODO 1: scale each feature
    TODO 2: avoid division by zero if std == 0
    TODO 3: return scaled X
    """
    # TODO: implement
    raise NotImplementedError("transform")


def add_bias(X):
    """
    Prepend 1.0 to every row.

    TODO 1: return [[1.0, *row] for row in X]
    """
    # TODO: implement
    raise NotImplementedError("add_bias")


def binary_labels(houses, positive_house):
    """
    TODO 1: return [1.0 if h == positive_house else 0.0 for h in houses]
    """
    # TODO: implement
    raise NotImplementedError("binary_labels")


def predict_proba(x, theta):
    """
    h_theta(x) = sigmoid(theta · x)

    TODO 1: compute dot product theta · x
    TODO 2: return sigmoid(z)
    """
    # TODO: implement
    raise NotImplementedError("predict_proba")


def cost(X, y, theta):
    """
    J(theta) = - (1/m) * SUM(
        y * log(h) + (1 - y) * log(1 - h)
    )

    TODO 1: for each example, compute h = predict_proba(x, theta)
    TODO 2: accumulate the log-loss terms (watch log(0) — use a tiny epsilon)
    TODO 3: return J
    """
    # TODO: implement
    raise NotImplementedError("cost")


def gradients(X, y, theta):
    """
    dJ/d_theta_j = (1/m) * SUM( (h_i - y_i) * x_i_j )

    TODO 1: init grad vector of zeros (same length as theta)
    TODO 2: for each example, err = h - y ; add err * x_j to grad_j
    TODO 3: divide by m ; return grad
    """
    # TODO: implement
    raise NotImplementedError("gradients")


def train_binary(X, y, learning_rate, iterations):
    """
    Batch gradient descent for one binary logistic model.

    TODO 1: init theta to zeros
    TODO 2: loop iterations:
              - compute grad
              - simultaneously: theta_j -= learning_rate * grad_j
    TODO 3: optionally print cost at start / end
    TODO 4: return theta
    """
    # TODO: implement
    raise NotImplementedError("train_binary")


def train_one_vs_all(X, houses, learning_rate, iterations):
    """
    TODO 1: for each house in HOUSES:
              - build binary y
              - train_binary
              - store theta
    TODO 2: return dict house -> theta
    """
    # TODO: implement
    raise NotImplementedError("train_one_vs_all")


def save_weights(path, features, means, stds, thetas):
    """
    Save everything predict needs: features, scalers, thetas.

    Format is your choice (plain text, CSV, JSON...) — keep it simple.

    TODO 1: write selected feature names
    TODO 2: write means and stds
    TODO 3: write each house theta vector
    """
    # TODO: implement
    raise NotImplementedError("save_weights")


def main():
    if len(sys.argv) != 2:
        usage("Usage: python logreg_train.py <dataset_train.csv>")

    if not SELECTED_FEATURES:
        usage(
            "Fill SELECTED_FEATURES in logreg_train.py after running pair_plot.py",
            code=1,
        )

    rows = load_csv(sys.argv[1])

    # TODO: wire the full pipeline:
    #   prepare_dataset -> fit_scaler -> transform -> add_bias
    #   -> train_one_vs_all -> save_weights
    raise NotImplementedError("logreg_train.main pipeline")


if __name__ == "__main__":
    main()
