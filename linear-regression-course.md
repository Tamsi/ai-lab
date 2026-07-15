# Linear Regression Course

### ft_linear_regression · full tutorial (formulas & steps only)

This document is a **course / tutorial** for the 42 project `ft_linear_regression`.  
It contains **no code** — only concepts, formulas, and the steps to follow.

---

# Part 0 — What you are building

You have a CSV file (`data.csv`) with cars:

| Column | Meaning | Role in ML |
|--------|---------|------------|
| `km` | mileage | **feature** \(x\) — input |
| `price` | price in € | **target** \(y\) — what you want to predict |

**Goal:** given a mileage, estimate the price of a car.

You must build **two programs**:

1. **Training** — learn parameters from the dataset  
2. **Prediction** — use those parameters to answer: “how much for this km?”

---

# Part 1 — Vocabulary (learn these words)

## 1.1 Linear regression

A method that predicts a number \(y\) using a **straight line**:

\[
\hat{y} = \theta_0 + \theta_1 \cdot x
\]

Here: predict **price** from **mileage**.

---

## 1.2 Feature and target

| Name | Symbol | In this project |
|------|--------|-----------------|
| Feature (input) | \(x\) | mileage (`km`) |
| Target (label) | \(y\) | real price |
| Prediction | \(\hat{y}\) or \(h_\theta(x)\) | estimated price |

---

## 1.3 Hypothesis

The formula your model uses to predict:

\[
h_\theta(x) = \theta_0 + \theta_1 \cdot x
\]

Also written in the subject as:

\[
\text{estimatePrice}(\text{mileage}) = \theta_0 + \theta_1 \cdot \text{mileage}
\]

---

## 1.4 Parameters: \(\theta_0\) and \(\theta_1\)

These are the **two numbers the model learns**.

| Symbol | ML name | Everyday meaning |
|--------|---------|------------------|
| \(\theta_0\) | **bias** / intercept | price when \(x = 0\) (base value) |
| \(\theta_1\) | **weight** / slope | how much price changes when km increases by 1 |

Equivalence with the classic ML writing \(y = wx + b\):

| Subject notation | Classic ML |
|------------------|------------|
| \(\theta_0\) | \(b\) (bias) |
| \(\theta_1\) | \(w\) (weight) |

**Example intuition:**

- \(\theta_0 \approx 8500\) → a car with 0 km would be worth about 8500 € on this line  
- \(\theta_1 \approx -0.02\) → each extra km lowers the price by about 0.02 €  
- Negative \(\theta_1\) is expected: more km → cheaper car

**Before training**, the subject requires:

\[
\theta_0 = 0, \quad \theta_1 = 0
\]

So at the start, every prediction is \(0\).

---

## 1.5 Error (residual)

For one car:

\[
\text{error} = h_\theta(x) - y = (\theta_0 + \theta_1 \cdot x) - y
\]

| Sign | Meaning |
|------|---------|
| error \(> 0\) | prediction too high |
| error \(< 0\) | prediction too low |
| error \(= 0\) | perfect on that example |

---

## 1.6 Squared error

\[
\text{squared error} = (h_\theta(x) - y)^2
\]

Why square?

- \(+100\) and \(-100\) count the same  
- large mistakes are penalized more than small ones  

---

## 1.7 Cost function / MSE (Mean Squared Error)

Global quality of the model on **all** \(m\) examples:

\[
J(\theta_0, \theta_1) = \frac{1}{m} \sum_{i=0}^{m-1} \bigl(h_\theta(x^{(i)}) - y^{(i)}\bigr)^2
\]

| \(J\) | Meaning |
|-------|---------|
| Large | bad model |
| Small | good model |

**Training goal:** find \(\theta_0, \theta_1\) that **minimize** \(J\).

In this project, \(m = 24\) (number of cars in `data.csv`).

---

## 1.8 Gradient descent

Algorithm that minimizes \(J\) by updating \(\theta_0\) and \(\theta_1\) little by little.

Imagine \(J\) as a valley. You are at the top. At each step you walk downhill.

```text
J(θ)
  ↑
  |  start
  |   \
  |    \___
  |        ‾‾‾ minimum  ← goal
  +──────────────→ θ
```

---

## 1.9 Learning rate (\(\alpha\))

Size of each step in gradient descent.

| \(\alpha\) too small | \(\alpha\) too large | \(\alpha\) good |
|----------------------|----------------------|-----------------|
| \(J\) barely decreases | \(\theta\) explode → `nan` | \(J\) decreases steadily |
| needs huge iterations | diverges | converges |

**Rule of thumb while debugging:**

- cost stuck → increase \(\alpha\)  
- cost becomes `nan` → decrease \(\alpha\)  

---

## 1.10 Iteration / epoch

One full pass over the dataset to compute errors and update \(\theta_0, \theta_1\).

You typically repeat this thousands or hundreds of thousands of times.

Do **not** confuse:

| Concept | Meaning |
|---------|---------|
| \(m\) | number of examples (cars) |
| iterations | how many times you update \(\theta\) |

---

## 1.11 Normalization (feature scaling)

Not mandatory in the subject PDF, but often **necessary in practice** because raw km values are huge (tens/hundreds of thousands).

That makes \(\theta_1\)'s gradient enormous and \(\theta_0\)'s tiny → hard to pick one learning rate.

**Min-max normalization:**

\[
x_{\text{norm}} = \frac{x - x_{\min}}{x_{\max} - x_{\min}}
\]

Then every mileage is in \([0, 1]\).

You train on \(x_{\text{norm}}\), then convert \(\theta\) back so prediction still uses raw km (see Part 4).

---

# Part 2 — Formulas of the subject (mandatory)

## 2.1 Hypothesis

\[
h_\theta(x) = \theta_0 + \theta_1 \cdot x
\]

## 2.2 Gradient descent updates (simultaneous)

\[
\text{tmp\_}\theta_0 = \alpha \cdot \frac{1}{m} \sum_{i=0}^{m-1} \bigl(h_\theta(x^{(i)}) - y^{(i)}\bigr)
\]

\[
\text{tmp\_}\theta_1 = \alpha \cdot \frac{1}{m} \sum_{i=0}^{m-1} \bigl(h_\theta(x^{(i)}) - y^{(i)}\bigr) \cdot x^{(i)}
\]

\[
\theta_0 := \theta_0 - \text{tmp\_}\theta_0
\]

\[
\theta_1 := \theta_1 - \text{tmp\_}\theta_1
\]

**Critical rule:** compute both `tmp` values with the **old** \(\theta_0, \theta_1\), then update both at once.

These `tmp` terms come from the derivatives (gradients) of the cost:

\[
\frac{\partial J}{\partial \theta_0} = \frac{1}{m} \sum (h - y)
\]

\[
\frac{\partial J}{\partial \theta_1} = \frac{1}{m} \sum (h - y) \cdot x
\]

---

# Part 3 — Training steps (Phase A)

Follow these steps in order.

### Step A1 — Load the dataset

- Open `data.csv`
- Read every row: mileage \(x\), price \(y\)
- Keep \(m =\) number of rows

### Step A2 — (Recommended) Normalize mileages

\[
x_{\text{norm}}^{(i)} = \frac{x^{(i)} - x_{\min}}{x_{\max} - x_{\min}}
\]

Save \(x_{\min}\) and \(x_{\max}\) — you need them later.

### Step A3 — Initialize parameters

\[
\theta_0 = 0, \quad \theta_1 = 0
\]

Choose \(\alpha\) (learning rate) and \(N\) (iterations).  
With normalized \(x\), \(\alpha\) like \(0.1\) often works.  
With raw km, \(\alpha\) must be tiny (and convergence is harder).

### Step A4 — One training iteration

For every example \(i = 0 \ldots m-1\):

1. Predict: \(h = \theta_0 + \theta_1 \cdot x^{(i)}\)  
2. Error: \(e = h - y^{(i)}\)  
3. Accumulate:
   - \(S_1 += e\)
   - \(S_2 += e \cdot x^{(i)}\)

Then:

4. \(\text{tmp\_}\theta_0 = \alpha \cdot (1/m) \cdot S_1\)  
5. \(\text{tmp\_}\theta_1 = \alpha \cdot (1/m) \cdot S_2\)  
6. Update simultaneously:
   - \(\theta_0 \leftarrow \theta_0 - \text{tmp\_}\theta_0\)
   - \(\theta_1 \leftarrow \theta_1 - \text{tmp\_}\theta_1\)

### Step A5 — Repeat Step A4

Do this \(N\) times.

**Watch the cost \(J\):**

- start: usually very high (predictions near 0)  
- middle: should decrease  
- end: much lower, and values should stabilize  

If \(J\) barely moves → \(\alpha\) too small or not enough iterations.  
If \(J\) becomes `nan` → \(\alpha\) too large.

### Step A6 — (If you normalized) Convert \(\theta\) back to raw km

You trained:

\[
\text{price} = \theta_{0_{\text{norm}}} + \theta_{1_{\text{norm}}} \cdot \frac{km - km_{\min}}{km_{\max} - km_{\min}}
\]

Expand to get a formula on raw `km`:

\[
\theta_1 = \frac{\theta_{1_{\text{norm}}}}{km_{\max} - km_{\min}}
\]

\[
\theta_0 = \theta_{0_{\text{norm}}} - \theta_1 \cdot km_{\min}
\]

Now prediction matches the subject formula:

\[
\text{price} = \theta_0 + \theta_1 \cdot km
\]

### Step A7 — Save \(\theta_0\) and \(\theta_1\)

Store them so the prediction program can load them later.

### Step A8 — Sanity checks

Good signs:

- \(\theta_1 < 0\) (more km → lower price)  
- \(\theta_0\) in the thousands (rough base price)  
- final \(J\) much smaller than starting \(J\)  
- predictions look realistic (e.g. 150 000 km → around a few thousand €)

---

# Part 4 — Prediction steps (Phase B)

No cost. No gradient. Only the hypothesis.

### Step B1 — Load trained \(\theta_0, \theta_1\)

### Step B2 — Ask the user for a mileage

### Step B3 — Apply the hypothesis

\[
\text{estimated price} = \theta_0 + \theta_1 \cdot \text{mileage}
\]

### Step B4 — Display the result

That is the whole mandatory prediction program.

---

# Part 5 — End-to-end map

```text
data.csv
   │
   ▼
[optional] normalize km → x in [0, 1]
   │
   ▼
initialize θ0=0, θ1=0
   │
   ▼
repeat N times:
   for each car:
      prediction = θ0 + θ1·x
      error = prediction - price
   update θ0, θ1 with gradient descent
   │
   ▼
[optional] denormalize θ → formula on raw km
   │
   ▼
save θ0, θ1
   │
   ▼
PREDICT: price = θ0 + θ1 · user_km
```

---

# Part 6 — Bonus ideas (subject)

Only evaluated if the mandatory part is perfect.

1. **Plot the data** — scatter of km vs price  
2. **Plot the regression line** — same graph, line \(y = \theta_0 + \theta_1 x\)  
3. **Precision program** — measure how good the model is, for example:

\[
\text{MSE} = J(\theta_0, \theta_1)
\]

\[
\text{RMSE} = \sqrt{\text{MSE}}
\]

\[
\text{MAE} = \frac{1}{m}\sum |h(x_i) - y_i|
\]

\[
R^2 = 1 - \frac{\sum (y_i - h(x_i))^2}{\sum (y_i - \bar{y})^2}
\]

---

# Part 7 — What the peer review checks

- no library that does the regression for you (e.g. `numpy.polyfit` is cheating)  
- correct hypothesis \(h(x) = \theta_0 + \theta_1 x\)  
- correct training formulas from the subject  
- simultaneous update of \(\theta_0\) and \(\theta_1\)  
- \(\theta\) start at 0 before training  

---

# Part 8 — Cheat sheet

| Concept | Formula / fact |
|---------|----------------|
| Hypothesis | \(h=\theta_0+\theta_1 x\) |
| Bias | \(\theta_0\) |
| Weight | \(\theta_1\) |
| Error | \(h-y\) |
| Squared error | \((h-y)^2\) |
| Cost / MSE | \(J=\frac{1}{m}\sum(h-y)^2\) |
| Grad \(\theta_0\) | \(\frac{1}{m}\sum(h-y)\) |
| Grad \(\theta_1\) | \(\frac{1}{m}\sum(h-y)x\) |
| Update | \(\theta \leftarrow \theta - \alpha\cdot\text{grad}\) |
| Learning rate | step size \(\alpha\) |
| Normalize | \(x'=(x-x_{\min})/(x_{\max}-x_{\min})\) |
| Denormalize \(\theta\) | \(\theta_1=\theta_{1n}/\Delta\), \(\theta_0=\theta_{0n}-\theta_1 x_{\min}\) |
| Predict | \(\theta_0+\theta_1\cdot km\) |

---

# Part 9 — Common mistakes

1. Updating \(\theta_0\) then using the **new** \(\theta_0\) to update \(\theta_1\) (must be simultaneous)  
2. Confusing \(m\) (examples) with number of iterations  
3. Learning rate too small → cost flat; too large → `nan`  
4. Predicting before training (or with \(\theta=0\))  
5. Training on normalized \(x\) but forgetting to denormalize \(\theta\) before predicting raw km  
6. Expecting \(\theta_1 > 0\) — on this dataset it should be negative  

---

# What to remember in one page

1. **Linear regression** = fit a line price ≈ \(\theta_0 + \theta_1\cdot km\)  
2. **\(\theta_0\)** = bias, **\(\theta_1\)** = weight  
3. **MSE / cost \(J\)** measures how wrong the line is  
4. **Gradient descent** reduces \(J\) by updating \(\theta\) each iteration  
5. **Learning rate** controls step size  
6. **Normalize** km if raw values prevent convergence, then convert \(\theta\) back  
7. **Train once**, then **predict** as many times as you want  

---

*Related project files: `data.csv`, `subject.pdf`, `train.py`, `predict.py`*
