import csv
import sys

import matplotlib

if "--show" in sys.argv:
    # Interactive window
    pass
else:
    matplotlib.use("Agg")

import matplotlib.pyplot as plt

DATASET_PATH = "data.csv"
THETAS_PATH = "thetas.txt"


def load_dataset(path):
    mileages, prices = [], []
    with open(path, newline="") as file:
        for row in csv.DictReader(file):
            mileages.append(float(row["km"]))
            prices.append(float(row["price"]))
    return mileages, prices


def load_thetas(path):
    with open(path) as file:
        theta0 = float(file.readline())
        theta1 = float(file.readline())
    return theta0, theta1


def estimate_price(mileage, theta0, theta1):
    return theta0 + theta1 * mileage


def main():
    mileages, prices = load_dataset(DATASET_PATH)
    theta0, theta1 = load_thetas(THETAS_PATH)

    x_line = [min(mileages), max(mileages)]
    y_line = [estimate_price(x, theta0, theta1) for x in x_line]

    plt.figure(figsize=(8, 5))
    plt.scatter(mileages, prices, label="data", color="steelblue")
    plt.plot(x_line, y_line, color="crimson", label="regression line")
    plt.xlabel("km")
    plt.ylabel("price")
    plt.title(f"price = {theta0:.2f} + ({theta1:.6f} * km)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("regression.png", dpi=150)
    print("Saved regression.png")

    if "--show" in sys.argv:
        plt.show()


if __name__ == "__main__":
    main()
