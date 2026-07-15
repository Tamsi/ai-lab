THETAS_PATH = "thetas.txt"


def load_thetas(path):
    with open(path) as file:
        theta0 = float(file.readline())
        theta1 = float(file.readline())
    return theta0, theta1


def estimate_price(mileage, theta0, theta1):
    return theta0 + theta1 * mileage


def main():
    theta0, theta1 = load_thetas(THETAS_PATH)
    mileage = float(input("Enter mileage: "))
    price = estimate_price(mileage, theta0, theta1)
    print(f"Estimated price: {price:.2f}")


if __name__ == "__main__":
    main()
