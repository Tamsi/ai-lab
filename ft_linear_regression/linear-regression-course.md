# Linear Regression Course

### ft_linear_regression · full tutorial (formulas & steps only)

This document is a **course / tutorial** for the 42 project `ft_linear_regression`.  
It contains **no code** — only concepts, formulas, and the steps to follow.

All formulas are written in plain text (no LaTeX).

---

# Part 0 — What you are building

You have a CSV file (`data.csv`) with cars:

| Column | Meaning | Role in ML |
|--------|---------|------------|
| `km` | mileage | **feature** `x` — input |
| `price` | price in € | **target** `y` — what you want to predict |

**Goal:** given a mileage, estimate the price of a car.

You must build **two programs**:

1. **Training** — learn parameters from the dataset
2. **Prediction** — use those parameters to answer: "how much for this km?"

---

# Part 1 — Vocabulary (learn these words)

## 1.1 Linear regression

A method that predicts a number `y` using a **straight line**:

```text
predicted_price = theta0 + theta1 * x
```

Here: predict **price** from **mileage**.

---

## 1.2 Feature and target

| Name | Symbol | In this project |
|------|--------|-----------------|
| Feature (input) | `x` | mileage (`km`) |
| Target (label) | `y` | real price |
| Prediction | `y_hat` or `h(x)` | estimated price |

---

## 1.3 Hypothesis

The formula your model uses to predict:

```text
h(x) = theta0 + theta1 * x
```

Also written in the subject as:

```text
estimatePrice(mileage) = theta0 + theta1 * mileage
```

Same thing, different notation.

---

## 1.4 Parameters: theta0 and theta1

These are the **two numbers the model learns**.

| Symbol | ML name | Everyday meaning |
|--------|---------|------------------|
| `theta0` | **bias** / intercept | price when `x = 0` (base value) |
| `theta1` | **weight** / slope | how much price changes when km increases by 1 |

Equivalence with the classic ML writing `y = w*x + b`:

| Subject notation | Classic ML |
|------------------|------------|
| `theta0` | `b` (bias) |
| `theta1` | `w` (weight) |

**Example intuition:**

- `theta0 ≈ 8500` → a car with 0 km would be worth about 8500 € on this line
- `theta1 ≈ -0.02` → each extra km lowers the price by about 0.02 €
- Negative `theta1` is expected: more km → cheaper car

**Before training**, the subject requires:

```text
theta0 = 0
theta1 = 0
```

So at the start, every prediction is `0`.

---

## 1.5 Error (residual)

For one car:

```text
error = h(x) - y
error = (theta0 + theta1 * x) - y
```

| Sign | Meaning |
|------|---------|
| error > 0 | prediction too high |
| error < 0 | prediction too low |
| error = 0 | perfect on that example |

---

## 1.6 Squared error

```text
squared_error = (h(x) - y)^2
```

Why square?

- `+100` and `-100` count the same
- large mistakes are penalized more than small ones

---

## 1.7 Cost function / MSE (Mean Squared Error)

Global quality of the model on **all** `m` examples:

```text
J(theta0, theta1) = (1/m) * SUM( (h(x_i) - y_i)^2 )
```

| J | Meaning |
|---|---------|
| Large | bad model |
| Small | good model |

**Training goal:** find `theta0` and `theta1` that **minimize** `J`.

In this project, `m = 24` (number of cars in `data.csv`).

---

## 1.8 Gradient descent

Algorithm that minimizes `J` by updating `theta0` and `theta1` little by little.

Imagine `J` as a valley. You are at the top. At each step you walk downhill.

```text
J(theta)
  ↑
  |  start
  |   \
  |    \___
  |        ‾‾‾ minimum  ← goal
  +──────────────→ theta
```

---

## 1.9 Learning rate (alpha)

Size of each step in gradient descent.

| alpha too small | alpha too large | alpha good |
|-----------------|-----------------|------------|
| J barely decreases | theta explode → `nan` | J decreases steadily |
| needs huge iterations | diverges | converges |

**Rule of thumb while debugging:**

- cost stuck → increase `alpha`
- cost becomes `nan` → decrease `alpha`

---

## 1.10 Iteration / epoch

One full pass over the dataset to compute errors and update `theta0` and `theta1`.

You typically repeat this thousands or hundreds of thousands of times.

Do **not** confuse:

| Concept | Meaning |
|---------|---------|
| `m` | number of examples (cars) |
| iterations | how many times you update theta |

---

## 1.11 Normalization (feature scaling)

Not mandatory in the subject PDF, but often **necessary in practice** because raw km values are huge (tens/hundreds of thousands).

That makes `theta1`'s gradient enormous and `theta0`'s tiny → hard to pick one learning rate.

**Min-max normalization:**

```text
x_norm = (x - x_min) / (x_max - x_min)
```

Then every mileage is in `[0, 1]`.

You train on `x_norm`, then convert theta back so prediction still uses raw km (see Part 3, Step A6).

---

# Part 2 — Formulas of the subject (mandatory)

## 2.1 Hypothesis

```text
h(x) = theta0 + theta1 * x
```

## 2.2 Gradient descent updates (simultaneous)

```text
tmp_theta0 = alpha * (1/m) * SUM( h(x_i) - y_i )
tmp_theta1 = alpha * (1/m) * SUM( (h(x_i) - y_i) * x_i )

theta0 = theta0 - tmp_theta0
theta1 = theta1 - tmp_theta1
```

**Critical rule:** compute both `tmp` values with the **old** `theta0` and `theta1`, then update both at once.

These `tmp` terms come from the derivatives (gradients) of the cost:

```text
dJ/d_theta0 = (1/m) * SUM( h - y )
dJ/d_theta1 = (1/m) * SUM( (h - y) * x )
```

---

# Part 3 — Training steps (Phase A)

Follow these steps in order.

### Step A1 — Load the dataset

- Open `data.csv`
- Read every row: mileage `x`, price `y`
- Keep `m` = number of rows

### Step A2 — (Recommended) Normalize mileages

```text
x_norm_i = (x_i - x_min) / (x_max - x_min)
```

Save `x_min` and `x_max` — you need them later.

### Step A3 — Initialize parameters

```text
theta0 = 0
theta1 = 0
```

Choose `alpha` (learning rate) and `N` (iterations).  
With normalized `x`, `alpha` like `0.1` often works.  
With raw km, `alpha` must be tiny (and convergence is harder).

### Step A4 — One training iteration

For every example `i = 0 .. m-1`:

1. Predict: `h = theta0 + theta1 * x_i`
2. Error: `e = h - y_i`
3. Accumulate:
   - `S1 += e`
   - `S2 += e * x_i`

Then:

4. `tmp_theta0 = alpha * (1/m) * S1`
5. `tmp_theta1 = alpha * (1/m) * S2`
6. Update simultaneously:
   - `theta0 = theta0 - tmp_theta0`
   - `theta1 = theta1 - tmp_theta1`

### Step A5 — Repeat Step A4

Do this `N` times.

**Watch the cost `J`:**

- start: usually very high (predictions near 0)
- middle: should decrease
- end: much lower, and values should stabilize

If `J` barely moves → `alpha` too small or not enough iterations.  
If `J` becomes `nan` → `alpha` too large.

### Step A6 — (If you normalized) Convert theta back to raw km

You trained:

```text
price = theta0_norm + theta1_norm * ((km - km_min) / (km_max - km_min))
```

Expand to get a formula on raw `km`:

```text
theta1 = theta1_norm / (km_max - km_min)
theta0 = theta0_norm - theta1 * km_min
```

Now prediction matches the subject formula:

```text
price = theta0 + theta1 * km
```

### Step A7 — Save theta0 and theta1

Store them so the prediction program can load them later.

### Step A8 — Sanity checks

Good signs:

- `theta1 < 0` (more km → lower price)
- `theta0` in the thousands (rough base price)
- final `J` much smaller than starting `J`
- predictions look realistic (e.g. 150 000 km → around a few thousand €)

---

# Part 4 — Prediction steps (Phase B)

No cost. No gradient. Only the hypothesis.

### Step B1 — Load trained `theta0`, `theta1`

### Step B2 — Ask the user for a mileage

### Step B3 — Apply the hypothesis

```text
estimated_price = theta0 + theta1 * mileage
```

### Step B4 — Display the result

That is the whole mandatory prediction program.

---

# Part 5 — End-to-end map

```text
data.csv
   |
   v
[optional] normalize km -> x in [0, 1]
   |
   v
initialize theta0=0, theta1=0
   |
   v
repeat N times:
   for each car:
      prediction = theta0 + theta1 * x
      error = prediction - price
   update theta0, theta1 with gradient descent
   |
   v
[optional] denormalize theta -> formula on raw km
   |
   v
save theta0, theta1
   |
   v
PREDICT: price = theta0 + theta1 * user_km
```

---

# Part 6 — Bonus ideas (subject)

Only evaluated if the mandatory part is perfect.

1. **Plot the data** — scatter of km vs price
2. **Plot the regression line** — same graph, line `y = theta0 + theta1 * x`
3. **Precision program** — measure how good the model is, for example:

```text
MSE  = J(theta0, theta1)
RMSE = sqrt(MSE)
MAE  = (1/m) * SUM( |h(x_i) - y_i| )

R2   = 1 - ( SUM( (y_i - h(x_i))^2 ) / SUM( (y_i - mean(y))^2 ) )
```

---

# Part 7 — What the peer review checks

- no library that does the regression for you (e.g. `numpy.polyfit` is cheating)
- correct hypothesis: `h(x) = theta0 + theta1 * x`
- correct training formulas from the subject
- simultaneous update of `theta0` and `theta1`
- theta start at 0 before training

---

# Part 8 — Cheat sheet

| Concept | Formula / fact |
|---------|----------------|
| Hypothesis | `h = theta0 + theta1 * x` |
| Bias | `theta0` |
| Weight | `theta1` |
| Error | `h - y` |
| Squared error | `(h - y)^2` |
| Cost / MSE | `J = (1/m) * SUM((h - y)^2)` |
| Grad theta0 | `(1/m) * SUM(h - y)` |
| Grad theta1 | `(1/m) * SUM((h - y) * x)` |
| Update | `theta = theta - alpha * grad` |
| Learning rate | step size `alpha` |
| Normalize | `x_norm = (x - x_min) / (x_max - x_min)` |
| Denormalize theta | `theta1 = theta1_norm / (x_max - x_min)` then `theta0 = theta0_norm - theta1 * x_min` |
| Predict | `theta0 + theta1 * km` |

---

# Part 9 — Common mistakes

1. Updating `theta0` then using the **new** `theta0` to update `theta1` (must be simultaneous)
2. Confusing `m` (examples) with number of iterations
3. Learning rate too small → cost flat; too large → `nan`
4. Predicting before training (or with theta = 0)
5. Training on normalized `x` but forgetting to denormalize theta before predicting raw km
6. Expecting `theta1 > 0` — on this dataset it should be negative

---

# What to remember in one page

1. **Linear regression** = fit a line `price ≈ theta0 + theta1 * km`
2. **`theta0`** = bias, **`theta1`** = weight
3. **MSE / cost `J`** measures how wrong the line is
4. **Gradient descent** reduces `J` by updating theta each iteration
5. **Learning rate** controls step size
6. **Normalize** km if raw values prevent convergence, then convert theta back
7. **Train once**, then **predict** as many times as you want

---

*Related project files: `data.csv`, `subject.pdf`, `train.py`, `predict.py`*
