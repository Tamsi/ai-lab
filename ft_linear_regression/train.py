import csv

DATASET_PATH = "data.csv"
THETAS_PATH = "thetas.txt"
LEARNING_RATE = 0.01
ITERATIONS = 10000


def load_dataset(path):
    mileages, prices = [], []
    with open(path, newline="") as file:
        for row in csv.DictReader(file):
            mileages.append(float(row["km"]))
            prices.append(float(row["price"]))
    return mileages, prices


def normalize(mileages):
    km_min, km_max = min(mileages), max(mileages)
    scaled = [(km - km_min) / (km_max - km_min) for km in mileages]
    return scaled, km_min, km_max


def denormalized_thetas(theta0_n, theta1_n, km_min, km_max):
    theta1 = theta1_n / (km_max - km_min)
    theta0 = theta0_n - theta1 * km_min
    return theta0, theta1


def estimate_price(x, theta0, theta1):
    # h(x) = theta0 + theta1 * x
    return theta0 + theta1 * x


def error(prediction, real_price):
    # h(x) - y
    return prediction - real_price


def squared_error(prediction, real_price):
    # (h(x) - y)^2
    return error(prediction, real_price) ** 2


def mse(mileages, prices, theta0, theta1):
    # MSE = (1/m) * SUM( (h(x_i) - y_i)^2 )
    m = len(mileages)
    total = 0.0
    for i in range(m):
        prediction = estimate_price(mileages[i], theta0, theta1)
        total += squared_error(prediction, prices[i])
    return total / m


def cost(mileages, prices, theta0, theta1):
    # J(theta) = MSE
    return mse(mileages, prices, theta0, theta1)


def gradients(mileages, prices, theta0, theta1):
    # Gradients of the cost J (= MSE):
    #   dJ/d_theta0 = (1/m) * SUM(error)
    #   dJ/d_theta1 = (1/m) * SUM(error * x)
    m = len(mileages)
    sum_error = 0.0
    sum_error_x = 0.0

    for i in range(m):
        prediction = estimate_price(mileages[i], theta0, theta1)
        err = error(prediction, prices[i])
        sum_error += err
        sum_error_x += err * mileages[i]

    grad_theta0 = (1 / m) * sum_error
    grad_theta1 = (1 / m) * sum_error_x
    return grad_theta0, grad_theta1


def train(mileages, prices, learning_rate, iterations):
    theta0, theta1 = 0.0, 0.0

    print(f"cost start: {cost(mileages, prices, theta0, theta1):.2f}")

    for step in range(iterations):
        grad_theta0, grad_theta1 = gradients(mileages, prices, theta0, theta1)
        # subject formulas:
        #   tmp_theta = learning_rate * gradient
        #   theta = theta - tmp_theta
        theta0 -= learning_rate * grad_theta0
        theta1 -= learning_rate * grad_theta1
    return theta0, theta1


def save_thetas(path, theta0, theta1):
    with open(path, "w") as file:
        file.write(f"{theta0}\n{theta1}\n")


def main():
    mileages, prices = load_dataset(DATASET_PATH)
    mileages_n, km_min, km_max = normalize(mileages)

    theta0_n, theta1_n = train(mileages_n, prices, LEARNING_RATE, ITERATIONS)
    theta0, theta1 = denormalized_thetas(theta0_n, theta1_n, km_min, km_max)
    save_thetas(THETAS_PATH, theta0, theta1)

    print(f"cost end: {cost(mileages, prices, theta0, theta1):.2f}")
    print(f"theta0={theta0}")
    print(f"theta1={theta1}")


if __name__ == "__main__":
    main()
