# Logistic Regression Course

### dslr · full tutorial (formulas & steps only)

This document is a **course / tutorial** for the 42 project `dslr`
(Data Science × Logistic Regression — Harry Potter and the Data Scientist).

It contains **no code** — only concepts, formulas, and the steps to follow.

---

# Part 0 — What you are building

You have two CSV files in `datasets/`:

| File | Role |
|------|------|
| `dataset_train.csv` | labeled students (house known) — used to train |
| `dataset_test.csv` | unlabeled students (house empty) — used to predict |

Each row is a Hogwarts student with courses (numerical features) and a house (target).

| Column group | Examples | Role in ML |
|--------------|----------|------------|
| Identity | `First Name`, `Last Name`, `Birthday`, `Best Hand` | usually **not** used for training |
| Features | `Arithmancy`, `Astronomy`, `Herbology`, ... | inputs \(x\) |
| Target | `Hogwarts House` | label \(y\) — one of 4 houses |

**Goal:** recreate a Sorting Hat — given course scores, predict the house.

You must build programs in this order (subject recommendation):

1. **describe** — statistics on numerical features (without cheating helpers)
2. **histogram / scatter_plot / pair_plot** — explore and choose features
3. **logreg_train** — learn weights with gradient descent (one-vs-all)
4. **logreg_predict** — write `houses.csv` for the test set

Peer evaluation requires **at least 98% accuracy** on the test set
(compared with the official labels via scikit-learn's accuracy score).

---

# Part 1 — Vocabulary

## 1.1 Classification vs regression

| Task | Output | Example |
|------|--------|---------|
| Regression | a number | car price |
| Classification | a category / class | Hogwarts house |

`ft_linear_regression` predicted a price.  
`dslr` predicts one of: `Gryffindor`, `Hufflepuff`, `Ravenclaw`, `Slytherin`.

---

## 1.2 Feature and target

| Name | Symbol | In this project |
|------|--------|-----------------|
| Feature vector | \(x\) | selected course scores for one student |
| Target / label | \(y\) | house (encoded as 0/1 for each binary model) |
| Prediction | \(h(x)\) or \(\hat{y}\) | probability (then house after one-vs-all) |

\(x\) is a vector: one number per selected feature, plus often a bias term \(x_0 = 1\).

---

## 1.3 Multi-class problem

Four houses → four classes.

You do **not** train one magical 4-way formula in the mandatory part.
You train **four binary classifiers** (one-vs-all / one-vs-rest):

| Classifier | Positive class (\(y = 1\)) | Negative class (\(y = 0\)) |
|------------|--------------------------|--------------------------|
| Model G | Gryffindor | all other houses |
| Model H | Hufflepuff | all other houses |
| Model R | Ravenclaw | all other houses |
| Model S | Slytherin | all other houses |

At prediction time: run all four models, pick the house with the **highest probability**.

---

## 1.4 Logistic regression (binary)

Almost like linear regression, but the output is squeezed into \((0, 1)\) = a probability.

Linear score (same idea as before):


\[
z = \theta \cdot x = \theta_0 x_0 + \theta_1 x_1 + \cdots + \theta_n x_n
\]


(with \(x_0 = 1\) for the bias)

Sigmoid (logistic function):


\[
g(z) = \frac{1}{1 + e^{-z}}
\]


Hypothesis:


\[
h_\theta(x) = g(\theta \cdot x) = \frac{1}{1 + e^{-\theta \cdot x}}
\]


| \(h(x)\) | Meaning |
|--------|---------|
| close to 1 | model believes "positive class" |
| close to 0 | model believes "negative class" |
| 0.5 | undecided |

---

## 1.5 Why not use linear regression for classification?

A straight line can predict values outside \([0, 1]\), and treating houses as numbers
(`Gryffindor=0`, `Slytherin=3`...) invents a fake order between classes.

Sigmoid + one-vs-all avoids both problems.

---

## 1.6 Cost function (binary cross-entropy / log loss)

For one binary logistic model, with \(m\) examples:


\[
J(\theta) = -\frac{1}{m} \sum_{i=1}^{m} \left[
  y^{(i)} \log\!\left(h_\theta(x^{(i)})\right)
  + \left(1 - y^{(i)}\right) \log\!\left(1 - h_\theta(x^{(i)})\right)
\right]
\]


Intuition:

- if \(y = 1\), you want \(h\) close to 1 → penalize small \(\log(h)\)
- if \(y = 0\), you want \(h\) close to 0 → penalize small \(\log(1 - h)\)

**Training goal:** find \(\theta\) that **minimizes** \(J\).

---

## 1.7 Gradient of the cost

Partial derivative (same shape as linear regression's gradient, but \(h\) is sigmoid):


\[
\frac{\partial J}{\partial \theta_j}
= \frac{1}{m} \sum_{i=1}^{m}
\left(h_\theta(x^{(i)}) - y^{(i)}\right) x_j^{(i)}
\]


For the whole vector:


\[
\nabla J(\theta) = \frac{1}{m}\, X^\top (h - y)
\]


(conceptually — you can implement it with loops; no numpy required)

---

## 1.8 Gradient descent

**Goal:** find \(\theta\) that minimizes \(J(\theta)\).

| Symbol in this step | Reminder |
|---------------------|----------|
| \(m\) | number of training students for this binary model |
| \(\theta_j\) | weight you are updating |
| \(\alpha\) | learning rate — how big each step is |
| \(\dfrac{\partial J}{\partial \theta_j}\) | direction and steepness of cost change for \(\theta_j\) |

Start from \(\theta = 0\) (or small values), then for each iteration:


\[
\theta_j \leftarrow \theta_j - \alpha \frac{\partial J}{\partial \theta_j}
\]


for every \(j\), using gradients computed from the **old** \(\theta\) (simultaneous update).

| \(\alpha\) too small | \(\alpha\) too large | \(\alpha\) good |
|--------------------|--------------------|---------------|
| \(J\) barely decreases | \(J\) explodes / `nan` | \(J\) decreases, then stabilizes |

---

## 1.9 Feature scaling

Course scores have very different ranges (e.g. Charms around -200, Herbology around ±10).
Without scaling, gradient descent is hard to tune.

**Standardization (recommended):**


\[
x_{\text{scaled}} = \frac{x - \mu}{\sigma}
\]


Compute \(\mu\) and \(\sigma\) on the **training** set only.
Reuse the same \(\mu\) and \(\sigma\) when predicting the test set.

**Min-max** is also possible:


\[
x_{\text{scaled}} = \frac{x - x_{\min}}{x_{\max} - x_{\min}}
\]


---

## 1.10 Missing values

The Hogwarts CSV has empty cells for some scores.

Typical simple strategies (pick one and stay consistent):

- drop the row if a used feature is missing (during training)
- replace missing values by the feature mean (train mean; reuse at predict time)

Document your choice — peers will ask.

---

## 1.11 Symbol reference — what each value means

Every symbol used in this project, in one place.

### Data and examples

| Symbol | Name | Meaning in `dslr` |
|--------|------|-------------------|
| \(i\) | example index | student number in the dataset, from \(1\) to \(m\) (or \(0\) to \(m-1\) in code — stay consistent) |
| \(m\) | number of training examples | total rows used to train **one** binary model (after dropping rows with missing selected features) |
| \(n\) | number of features | count of **selected** course columns (numerical features you kept after plots) |
| \(x^{(i)}\) | feature vector | all inputs for student \(i\): \([x_0^{(i)}, x_1^{(i)}, \ldots, x_n^{(i)}]\) |
| \(x_0^{(i)}\) | bias input | always \(1\) (artificial column so the model can learn an offset) |
| \(x_j^{(i)}\) | feature \(j\) of example \(i\) | scaled score of course \(j\) for student \(i\) (\(j \geq 1\)) |
| \(y^{(i)}\) | label | for one binary model: \(1\) = positive house, \(0\) = all other houses |
| \(X\) | design matrix | all training rows stacked: shape \(m \times (n+1)\) (includes bias column) |

### Model parameters

| Symbol | Name | Meaning |
|--------|------|---------|
| \(\theta\) | weight vector | what you learn; same length as \(x\) → \([\theta_0, \theta_1, \ldots, \theta_n]\) |
| \(\theta_j\) | weight for feature \(j\) | how much feature \(j\) pushes the linear score up or down |
| \(\theta_0\) | bias weight | intercept: shifts the decision boundary when all scaled features are \(0\) |
| \(\theta_G, \theta_H, \theta_R, \theta_S\) | house-specific weights | one full \(\theta\) vector per house (one-vs-all) |

### Predictions and outputs

| Symbol | Name | Meaning |
|--------|------|---------|
| \(z\) | linear score | \(\theta \cdot x\) before sigmoid (can be any real number) |
| \(g(z)\) | sigmoid | squashes \(z\) into \((0, 1)\) |
| \(h_\theta(x^{(i)})\) or \(h^{(i)}\) | hypothesis / probability | model's estimated \(P(y=1 \mid x^{(i)})\) for the current binary model |
| \(\hat{y}\) | predicted class | final house after argmax over the four binary probabilities |
| \(p_G, p_H, p_R, p_S\) | house probabilities | output of each binary model on one student |

### Cost and optimization

| Symbol | Name | Meaning |
|--------|------|---------|
| \(J(\theta)\) | cost / loss | average log-loss over the \(m\) examples; **lower is better** |
| \(\dfrac{\partial J}{\partial \theta_j}\) | partial gradient | how \(J\) changes when you nudge \(\theta_j\) |
| \(\nabla J(\theta)\) | gradient vector | all partial derivatives stacked — direction of steepest **increase** of \(J\) |
| \(\alpha\) | learning rate | step size for gradient descent (hyperparameter you tune) |
| \(N\) | number of iterations | how many times you repeat compute-gradient → update |

### Scaling (train statistics)

| Symbol | Name | Meaning |
|--------|------|---------|
| \(\mu_j\) | mean of feature \(j\) | computed on **train only**; used to center feature \(j\) |
| \(\sigma_j\) | std of feature \(j\) | computed on **train only**; used to scale feature \(j\) |
| \(x_{\min}, x_{\max}\) | min / max | alternative to \(\mu, \sigma\) if you use min-max scaling |

### Statistics (`describe`)

| Symbol | Name | Meaning |
|--------|------|---------|
| \(v_i\) | one observed value | one valid number in a column (missing cells skipped) |
| \(n\) (in Part 2) | count | number of valid values for that feature |
| Q1 / median / Q3 | percentiles | 25th / 50th / 75th percentile of sorted values |

### One-vs-all encoding

| House model | \(y^{(i)} = 1\) when… | \(y^{(i)} = 0\) when… |
|-------------|----------------------|----------------------|
| Gryffindor | student is Gryffindor | any other house |
| Hufflepuff | student is Hufflepuff | any other house |
| Ravenclaw | student is Ravenclaw | any other house |
| Slytherin | student is Slytherin | any other house |

---

# Part 2 — Data analysis (`describe`)

## 2.1 What to display

For **every numerical feature**, print a table like:

```text
Count, Mean, Std, Min, 25%, 50%, 75%, Max
```

You must compute these **yourself**. Forbidden to use ready-made:
`count`, `mean`, `std`, `min`, `max`, `percentile`, `describe`, etc.

## 2.2 Formulas

Assume a list of \(n\) valid numbers \(v_1, \ldots, v_n\) (skip missing cells for that feature).


\[
\begin{align*}
\text{Count} &= n \\
\text{Mean } \mu &= \frac{1}{n} \sum_{i=1}^{n} v_i \\
\text{Variance (population) } \sigma^2 &= \frac{1}{n} \sum_{i=1}^{n} (v_i - \mu)^2 \\
\text{Variance (sample) } s^2 &= \frac{1}{n-1} \sum_{i=1}^{n} (v_i - \mu)^2 \\
\text{Std} &= \sqrt{\text{Variance}} \\
\text{Min} &= \min_i v_i \\
\text{Max} &= \max_i v_i
\end{align*}
\]


Pick population or sample variance and justify your choice.

Percentile \(p\) (example method — any clear method is fine if you can explain it):

1. Sort the values ascending
2. Position \(\text{idx} = \dfrac{p}{100}\,(n - 1)\)
3. Interpolate between the two nearest sorted values if \(\text{idx}\) is not integer

Common percentiles: `25%` (Q1), `50%` (median), `75%` (Q3).

## 2.3 Steps

1. Load `dataset_train.csv`
2. Detect which columns are numerical
3. For each numerical column, collect non-empty values
4. Compute Count / Mean / Std / Min / 25% / 50% / 75% / Max
5. Print a readable table (columns = features, rows = stats)

---

# Part 3 — Visualization

Visualization answers questions. There is not always a single correct plot,
but you must be able to justify your choice.

## 3.1 Histogram — `histogram.py`

**Question:** Which Hogwarts course has a **homogeneous** score distribution
between all four houses?

Meaning: the four house histograms largely overlap — the course does **not**
separate houses well. Such a feature is often a weak predictor (candidate to drop).

Steps:

1. Load train set with houses
2. For each numerical course, plot score distribution **per house** (overlay or facets)
3. Find the course where houses look most similar
4. Be ready to name that course and show the figure

## 3.2 Scatter plot — `scatter_plot.py`

**Question:** What are the two features that are **similar**?

Meaning: two features that are (almost) linearly related — redundant information.
A classic pair in this dataset is strongly correlated (one is nearly the negative of the other).

Steps:

1. Compare numerical features pairwise (scatter)
2. Spot the pair that forms an almost perfect line
3. Show that scatter plot and name the two features

Why it matters: keeping both features adds little new signal and can hurt training.

## 3.3 Pair plot — `pair_plot.py`

A **pair plot** = grid of scatter plots for every feature vs every other feature
(diagonals often show histograms/distributions).

**Question:** From this visualization, which features will you use for logistic regression?

Steps:

1. Build a pair plot on numerical features (optionally color points by house)
2. Prefer features where houses form **visible clusters / separations**
3. Drop homogeneous / redundant / noisy features
4. Write down your selected feature list — training must use the same list

---

# Part 4 — Logistic regression formulas (mandatory)

## 4.1 Sigmoid


\[
g(z) = \frac{1}{1 + e^{-z}}
\]


Numerically, clamp \(z\) if needed to avoid overflow in \(e^{-z}\).

## 4.2 Hypothesis


\[
h_\theta(x) = g(\theta \cdot x)
\]


## 4.3 Cost


\[
J(\theta) = -\frac{1}{m} \sum_{i=1}^{m} \left[
  y^{(i)} \log(h^{(i)}) + \left(1 - y^{(i)}\right) \log\!\left(1 - h^{(i)}\right)
\right]
\]


Optional: add a tiny epsilon inside \(\log\) to avoid \(\log(0)\).

## 4.4 Gradient


\[
\frac{\partial J}{\partial \theta_j}
= \frac{1}{m} \sum_{i=1}^{m}
\left(h^{(i)} - y^{(i)}\right) x_j^{(i)}
\]


## 4.5 Update


\[
\theta_j \leftarrow \theta_j - \alpha \frac{\partial J}{\partial \theta_j}
\]


Mandatory technique: **gradient descent** (batch GD is fine).

Bonuses (only if mandatory is perfect): SGD, mini-batch, other optimizers.

---

# Part 5 — Training steps (`logreg_train`)

> **Concrete numbers:** see **Part 11** for a full step-by-step walkthrough with a mini dataset.

### Step T1 — Load `dataset_train.csv`

Keep houses and numerical features you selected.

### Step T2 — Clean

- handle missing values
- keep only selected features
- encode houses for one-vs-all later

### Step T3 — Scale features

Compute mean/std (or min/max) on train features. Transform \(X\).

### Step T4 — Add bias column


\[
x_0 = 1 \quad \text{for every student}
\]


So each row of \(X\) is \([1,\ x_{1,\text{scaled}},\ x_{2,\text{scaled}},\ \ldots]\).

### Step T5 — Train four binary models

For each house \(H\) in {Gryffindor, Hufflepuff, Ravenclaw, Slytherin}:

1. Build labels: \(y^{(i)} = 1\) if student house is \(H\), else \(0\)
2. Initialize \(\theta = 0\) (length = number of columns in \(X\))
3. Repeat \(N\) iterations:
   - compute \(h^{(i)} = g(\theta \cdot x^{(i)})\) for all \(i\)
   - compute gradients
   - update \(\theta\)
4. Store the final \(\theta\) for house \(H\)

### Step T6 — Save weights

Write a file (format of your choice) containing:

- the list of selected features
- scaling parameters (mean/std or min/max)
- the four theta vectors (and house names)

`logreg_predict` must be able to reload everything it needs.

### Step T7 — Sanity checks

- cost \(J\) for each binary model should decrease over iterations
- on the training set, most students should be assigned to their true house
  (argmax of the four probabilities)
- if accuracy is poor: revisit feature selection, scaling, `alpha`, iterations, missing values

---

# Part 6 — Prediction steps (`logreg_predict`)

### Step P1 — Load weights file + `dataset_test.csv`

### Step P2 — Prepare test features

- same feature columns, same order
- same missing-value policy
- **same** scaling parameters as training (do not recompute mean/std on test)

### Step P3 — For each student


\[
\begin{align*}
p_G &= g(\theta_G \cdot x) \\
p_H &= g(\theta_H \cdot x) \\
p_R &= g(\theta_R \cdot x) \\
p_S &= g(\theta_S \cdot x) \\
\hat{y} &= \arg\max\{p_G,\ p_H,\ p_R,\ p_S\}
\end{align*}
\]


### Step P4 — Write `houses.csv`

Exact format:

```text
Index,Hogwarts House
0,Gryffindor
1,Hufflepuff
...
```

`Index` must match the test dataset `Index` column.

---

# Part 7 — End-to-end map

```text
dataset_train.csv
       |
       v
 describe  -> understand ranges / missing / outliers
       |
       v
 histogram / scatter / pair_plot
       |
       v
 select features + cleaning + scaling
       |
       v
 for each house:
    y = 1 if house else 0
    gradient descent on logistic cost
       |
       v
 save weights (+ feature list + scalers)
       |
       v
dataset_test.csv + weights
       |
       v
 one-vs-all probabilities -> argmax house
       |
       v
 houses.csv   (goal: accuracy >= 98%)
```

---

# Part 8 — What the peer review checks

- no function that does describe / mean / std / percentile for you
- no ML library that trains logistic regression for you
- you can explain sigmoid, cost, gradient, one-vs-all
- `logreg_train` uses gradient descent
- `logreg_predict` outputs valid `houses.csv`
- accuracy on test ≥ 98%
- you can justify feature choices from the plots

---

# Part 9 — Cheat sheet

| Concept | Formula / fact |
|---------|----------------|
| Sigmoid | \(g(z) = \dfrac{1}{1 + e^{-z}}\) |
| Hypothesis | \(h_\theta(x) = g(\theta \cdot x)\) |
| Cost | \(J(\theta) = -\dfrac{1}{m}\sum\!\left[y\log h + (1-y)\log(1-h)\right]\) |
| Gradient \(j\) | \(\dfrac{\partial J}{\partial \theta_j} = \dfrac{1}{m}\sum (h - y)\, x_j\) |
| Update | \(\theta \leftarrow \theta - \alpha\, \nabla J\) |
| One-vs-all | one binary model per house |
| Predict | house \(= \arg\max\) of the 4 probabilities |
| Scale | \(\dfrac{x - \mu}{\sigma}\) (fit on train only) |
| Success | accuracy ≥ 0.98 on test |

---

# Part 10 — Common mistakes

1. Using test-set statistics to scale features (data leakage)
2. Different feature order between train and predict
3. Forgetting the bias term \(x_0 = 1\)
4. Updating theta components with mixed old/new values
5. Keeping redundant features (the highly correlated pair) without thinking
6. Comparing probabilities incorrectly (must take argmax across houses)
7. Wrong `houses.csv` header / missing Index
8. Calling pandas/numpy helpers that compute describe stats for you

---

# Part 11 — Worked example (full pipeline, step by step)

This section walks through **the entire mandatory workflow** on a tiny fake dataset.
Numbers are rounded for readability — your real `dataset_train.csv` has ~1600 students and many features.

## 11.0 Toy setup

**Selected features** (after your real plots): `Astronomy`, `Herbology`  
**Binary model trained first**: Gryffindor vs the rest (one-vs-all)  
**Missing-value rule**: drop a row if a selected feature is empty  
**Scaling**: standardization \((x - \mu) / \sigma\) on train only  
**Hyperparameters**: \(\alpha = 0.1\), \(N = 2\) iterations (toy only — use more on real data)

### Mini training set (4 students)

| \(i\) | Hogwarts House | Astronomy (raw) | Herbology (raw) |
|------|----------------|-----------------|-----------------|
| 0 | Gryffindor | 600 | -5 |
| 1 | Gryffindor | 500 | -6 |
| 2 | Ravenclaw | -400 | 8 |
| 3 | Slytherin | -500 | 7 |

Here \(m = 4\) and \(n = 2\) (two course features, plus bias \(x_0 = 1\) added later).

---

## 11.1 `describe` — understand one feature

Take **Astronomy** only. Valid values: \(600, 500, -400, -500\).

\[
\mu_{\text{Astronomy}} = \frac{600 + 500 + (-400) + (-500)}{4} = 50
\]

\[
\sigma_{\text{Astronomy}} = \sqrt{\frac{1}{4}\sum_{i}(x_i - 50)^2} \approx 529
\]

Same idea for every numerical column → table with Count, Mean, Std, Min, 25%, 50%, 75%, Max.

**What you learn:** Astronomy spans a wide range → scaling will matter for gradient descent.

---

## 11.2 Plots — why these two features (summary)

On the real dataset you would:

1. **Histogram**: drop courses where all four houses overlap too much.
2. **Scatter**: drop one of two almost-identical features.
3. **Pair plot**: keep features where houses separate visually.

For this toy example we **pretend** Astronomy + Herbology passed those checks.

---

## 11.3 Scale features (train statistics)

### Astronomy

\[
\mu_1 = 50,\quad \sigma_1 \approx 529
\]

\[
x_{1,\text{scaled}}^{(i)} = \frac{x_{1,\text{raw}}^{(i)} - 50}{529}
\]

| \(i\) | raw | scaled \(x_1\) |
|------|-----|----------------|
| 0 | 600 | \(\approx 1.04\) |
| 1 | 500 | \(\approx 0.85\) |
| 2 | -400 | \(\approx -0.85\) |
| 3 | -500 | \(\approx -1.04\) |

### Herbology

\[
\mu_2 = \frac{-5 + (-6) + 8 + 7}{4} = 1,\quad \sigma_2 \approx 6.52
\]

| \(i\) | raw | scaled \(x_2\) |
|------|-----|----------------|
| 0 | -5 | \(\approx -0.92\) |
| 1 | -6 | \(\approx -1.07\) |
| 2 | 8 | \(\approx 1.07\) |
| 3 | 7 | \(\approx 0.92\) |

**Save** \(\mu_1, \sigma_1, \mu_2, \sigma_2\) — you will reuse them at predict time on the test set.

---

## 11.4 Add bias → build matrix \(X\)

Set \(x_0^{(i)} = 1\) for every student.

\[
x^{(i)} = \begin{bmatrix} 1 \\ x_{1,\text{scaled}}^{(i)} \\ x_{2,\text{scaled}}^{(i)} \end{bmatrix},
\quad
\theta = \begin{bmatrix} \theta_0 \\ \theta_1 \\ \theta_2 \end{bmatrix}
\]

Example for student 0:

\[
x^{(0)} \approx \begin{bmatrix} 1 \\ 1.04 \\ -0.92 \end{bmatrix}
\]

---

## 11.5 One-vs-all labels (Gryffindor model)

| \(i\) | true house | \(y^{(i)}\) for Gryffindor model |
|------|------------|----------------------------------|
| 0 | Gryffindor | \(1\) |
| 1 | Gryffindor | \(1\) |
| 2 | Ravenclaw | \(0\) |
| 3 | Slytherin | \(0\) |

You will repeat training with different \(y\) for Hufflepuff, Ravenclaw, Slytherin.

---

## 11.6 Initialize and iteration 1

**Start:** \(\theta = [0,\ 0,\ 0]\)

For each student \(i\), compute \(z^{(i)} = \theta \cdot x^{(i)} = 0\) → \(h^{(i)} = g(0) = 0.5\).

### Gradients (\(\alpha\) not applied yet)

\[
\frac{\partial J}{\partial \theta_j} = \frac{1}{m}\sum_{i=1}^{m}\left(h^{(i)} - y^{(i)}\right) x_j^{(i)}
\]

With \(h^{(i)} = 0.5\) for all \(i\):

\[
\frac{\partial J}{\partial \theta_0} = \frac{1}{4}\bigl[(0.5-1) + (0.5-1) + (0.5-0) + (0.5-0)\bigr] = 0
\]

\[
\frac{\partial J}{\partial \theta_1} \approx \frac{1}{4}\bigl[(0.5-1)(1.04) + (0.5-1)(0.85) + (0.5-0)(-0.85) + (0.5-0)(-1.04)\bigr] \approx -0.11
\]

\[
\frac{\partial J}{\partial \theta_2} \approx \frac{1}{4}\bigl[(0.5-1)(-0.92) + \cdots \bigr] \approx +0.12
\]

### Update (\(\alpha = 0.1\))

\[
\theta_j \leftarrow \theta_j - \alpha \frac{\partial J}{\partial \theta_j}
\]

\[
\theta \approx [0,\ +0.011,\ -0.012]
\]

**Rule:** compute all gradients with the **old** \(\theta\), then update all \(\theta_j\) together.

---

## 11.7 Iteration 2 (same loop)

1. Recompute \(z^{(i)} = \theta \cdot x^{(i)}\) for all \(i\).
2. Recompute \(h^{(i)} = g(z^{(i)})\).
3. Recompute \(\partial J / \partial \theta_j\).
4. Update \(\theta\) again.

On real data you repeat this \(N\) times (hundreds or thousands) until \(J\) stabilizes.

**Check:** \(J\) should **decrease** each iteration for a well-chosen \(\alpha\).

---

## 11.8 Train the three other binary models

Same \(X\), same scaling, same \(\alpha\) and \(N\), but different labels:

| Model | \(y^{(i)} = 1\) if house is… |
|-------|------------------------------|
| \(\theta_H\) | Hufflepuff |
| \(\theta_R\) | Ravenclaw |
| \(\theta_S\) | Slytherin |

You end up with **four** weight vectors: \(\theta_G, \theta_H, \theta_R, \theta_S\).

---

## 11.9 Save weights (`logreg_train` output)

Your weights file must let `logreg_predict` rebuild the exact pipeline. Minimum content:

```text
features: Astronomy, Herbology
mu_Astronomy: 50
sigma_Astronomy: 529
mu_Herbology: 1
sigma_Herbology: 6.52
theta_Gryffindor: [..., ..., ...]
theta_Hufflepuff: [..., ..., ...]
theta_Ravenclaw: [..., ..., ...]
theta_Slytherin: [..., ..., ...]
```

Format is yours (JSON, CSV, custom text) as long as predict can parse it.

---

## 11.10 Predict one test student (`logreg_predict`)

**New student** (from `dataset_test.csv`):

| Index | Astronomy (raw) | Herbology (raw) |
|-------|-----------------|-----------------|
| 42 | 550 | -5 |

### Step A — scale with **train** \(\mu, \sigma\) (never recompute on test)

\[
x_1 \approx \frac{550 - 50}{529} \approx 0.94,\quad
x_2 \approx \frac{-5 - 1}{6.52} \approx -0.92
\]

\[
x = \begin{bmatrix} 1 \\ 0.94 \\ -0.92 \end{bmatrix}
\]

### Step B — four probabilities

\[
p_G = g(\theta_G \cdot x),\quad
p_H = g(\theta_H \cdot x),\quad
p_R = g(\theta_R \cdot x),\quad
p_S = g(\theta_S \cdot x)
\]

Suppose after full training you get:

| house | probability |
|-------|-------------|
| Gryffindor | 0.72 |
| Hufflepuff | 0.08 |
| Ravenclaw | 0.11 |
| Slytherin | 0.09 |

### Step C — argmax

\[
\hat{y} = \arg\max\{p_G, p_H, p_R, p_S\} = \text{Gryffindor}
\]

---

## 11.11 Write `houses.csv`

One row per test student:

```text
Index,Hogwarts House
42,Gryffindor
```

Repeat for every row in `dataset_test.csv`. `Index` must match the test file exactly.

---

## 11.12 Full pipeline checklist (real project)

| Step | Program | What happens |
|------|---------|--------------|
| 1 | `describe.py` | stats on every numerical feature |
| 2 | `histogram.py` | find homogeneous course |
| 3 | `scatter_plot.py` | find redundant pair |
| 4 | `pair_plot.py` | choose feature list |
| 5 | `logreg_train.py` | clean → scale → 4× gradient descent → save weights |
| 6 | `logreg_predict.py` | load weights → scale test → 4 probs → argmax → `houses.csv` |
| 7 | evaluation | accuracy ≥ 98% on test labels |

---

# What to remember in one page

1. Explore with **describe + plots**, then **select features**
2. **Logistic regression** = linear score + **sigmoid** → probability
3. **One-vs-all** = one binary model per house
4. Minimize **log loss** with **gradient descent**
5. **Scale** features; reuse train scalers at predict time
6. Predict with **argmax** of the four probabilities → `houses.csv`
7. Target: **≥ 98%** accuracy on the test set

---

*Related project files: `subject.pdf`, `datasets/`, `utils.py`, `describe.py`,
`histogram.py`, `scatter_plot.py`, `pair_plot.py`, `logreg_train.py`, `logreg_predict.py`*
