# Linear Regression Course

### ft_linear_regression · handwritten-style notes

---

## Introduction

You have a `data.csv` file with **24 cars**. For each one you know:

- its **mileage** (km)
- its **price** (€)

**Question:** how do you predict the price of a car when you only know its mileage?

This is a **linear regression** problem: find a relationship between two values. Here, a **line** linking km and price.

---

# Chapter 1 — The model: a line

## 1.1 The idea

On a graph, each car is a point:

```text
price (€)
  ↑
  |    ·
  |  ·   ·
  |·       ·
  |___________→ km
```

You look for the **line** that passes "through the middle" of those points. That line is your **model**.

## 1.2 The formula

A line is always:

```
estimated_price = θ0 + θ1 × km
```

**θ0** (theta zero) = **intercept**
→ the price when km = 0 (base value of the line)

**θ1** (theta one) = **slope**
→ how much the price changes when km increases by 1

**Example:** if θ0 = 8000 and θ1 = −0.02:

- car at 0 km → 8000 + (−0.02 × 0) = **8000 €**
- car at 100 000 km → 8000 + (−0.02 × 100000) = **6000 €**
- car at 200 000 km → 8000 + (−0.02 × 200000) = **4000 €**

A negative θ1 means: more km → lower price. That makes sense.

## 1.3 Vocabulary

| French | English | Symbol |
|--------|---------|--------|
| Variable d'entrée | Feature | x (km) |
| Variable à prédire | Target | y (price) |
| Prédiction | Prediction / Hypothesis | ŷ |
| Paramètres du modèle | Parameters / Weights | θ0 and θ1 |

The formula ŷ = θ0 + θ1·x is called the **hypothesis**: what your model **predicts**.

---

# Chapter 2 — The problem: we do not know θ0 and θ1

At the start, **you do not know** which numbers to put in the formula.

You could guess θ0 = 5000, θ1 = −0.01… but that would be random.

**Solution:** let the computer (or you, by hand) **learn** the right values by looking at the 24 cars in the dataset.

That is **training**.

Initialize:

```
θ0 = 0
θ1 = 0
```

With that, the model predicts **0 €** for every car. Wrong, but it is the starting point.

---

# Chapter 3 — Measuring error

## 3.1 Error on one car

For car i:

```
error = prediction − real_price
error = (θ0 + θ1 × km) − price
```

**Example** (θ0=0, θ1=0, car at 240 000 km, real price 3650 €):

- prediction = 0
- error = 0 − 3650 = **−3650**

**Negative error** → you **underestimated** (you said too low).

**Positive error** → you **overestimated**.

## 3.2 Error on the whole dataset: MSE

We do not look at one car only. We want a **global error** over all 24.

We use the **Mean Squared Error** (MSE):

```
J(θ0, θ1) = (1/m) × Σ (prediction_i − price_i)²
```

where **m = 24** (number of cars).

**Why square?**

- an error of +100 and −100 count the same
- big errors are penalized more than small ones

**J(θ)** is the **cost function**: one number that says if your model is good or bad.

- **large J** → bad model
- **small J** → good model

**Training goal:** find θ0 and θ1 that make **J as small as possible**.

---

# Chapter 4 — Gradient descent

## 4.1 The idea

Imagine J(θ) is a **valley**. You are at the top. You want to reach the lowest point (the minimum).

**Gradient descent** means: at each step, look at which direction the slope goes up, and **walk the other way**.

```text
J(θ)
  ↑
  |  You are here
  |    \
  |     \  ← you go down
  |      \___
  |          ‾‾‾ minimum
  +────────────→ θ
```

## 4.2 Learning rate (α)

Each step has a size: **α** (learning rate).

- α **too large** → you jump over the minimum and diverge
- α **too small** → you move too slowly
- α **well chosen** → you converge to the right θ0 and θ1

On this project, km values are large (up to 240 000), so α must be **very small** (often around 10⁻⁷ to 10⁻¹⁰).

## 4.3 Update formulas (42 subject)

**Step 1** — For each car, compute prediction and error.

**Step 2** — Sum over all 24 cars:

```
S1 = Σ (prediction_i − price_i)
S2 = Σ (prediction_i − price_i) × km_i
```

**Step 3** — Compute corrections:

```
tmp_θ0 = α × (1/m) × S1
tmp_θ1 = α × (1/m) × S2
```

**Step 4** — Update **at the same time**:

```
θ0 ← θ0 − tmp_θ0
θ1 ← θ1 − tmp_θ1
```

**Important:** compute both `tmp` values with the **old** θ0 and θ1, then replace both at once.

**Step 5** — Repeat thousands of times until θ0 and θ1 stabilize.

---

# Chapter 5 — Handwritten example (3 cars)

To simplify, use 3 cars instead of 24:

| Car | km | Real price |
|-----|-----|------------|
| A | 240 000 | 3 650 € |
| B | 139 800 | 3 800 € |
| C | 22 899 | 7 990 € |

**Start:** θ0 = 0, θ1 = 0, α = 0.0000001, m = 3

### Iteration 1

**Car A** (240 000 km, 3650 €)

- prediction = 0 + 0 × 240000 = **0**
- error = 0 − 3650 = **−3650**
- error × km = −3650 × 240000 = **−876 000 000**

**Car B** (139 800 km, 3800 €)

- prediction = **0**
- error = **−3800**
- error × km = **−531 240 000**

**Car C** (22 899 km, 7990 €)

- prediction = **0**
- error = **−7990**
- error × km = **−182 963 010**

**Sums:**

- S1 = (−3650) + (−3800) + (−7990) = **−15 440**
- S2 ≈ **−1 590 203 010**

**Corrections:**

- tmp_θ0 = 0.0000001 × (1/3) × (−15440) ≈ **−0.000515**
- tmp_θ1 = 0.0000001 × (1/3) × (−1.59×10⁹) ≈ **−53**

**New θ:**

- θ0 = 0 − (−0.000515) = **0.000515**
- θ1 = 0 − (−53) = **53**

After 1 iteration, the model still predicts badly, but θ has **started** to move.

### Iteration 2

Restart with θ0 ≈ 0.0005 and θ1 ≈ 53.

**Car A:**

- prediction = 0.0005 + 53 × 240000 = **12 720 000** ← huge!
- error = 12 720 000 − 3650 = **+12 716 350**

θ1 = 53 is far too large. That is why α must be very small and you need many iterations.

After tens of thousands of iterations with a good α, you should get something like:

- **θ0 ≈ 8 000**
- **θ1 ≈ −0.02**

Then predictions become consistent.

---

# Chapter 6 — The two project phases

## Phase A — Training (once)

```text
1. Open data.csv
2. Set θ0 = 0, θ1 = 0
3. Repeat N times (e.g. 100 000):
      - for each car: prediction, error
      - compute S1 and S2
      - update θ0 and θ1
4. Save final θ0 and θ1 (to a file)
```

**Input:** the 24 cars  
**Output:** learned θ0 and θ1

## Phase B — Prediction (as often as you want)

```text
1. Load θ0 and θ1 (from phase A)
2. Ask the user for a mileage
3. Compute: price = θ0 + θ1 × km
4. Display the result
```

**Example** with θ0 = 8000, θ1 = −0.02, km = 150 000:

```
price = 8000 + (−0.02 × 150000) = 8000 − 3000 = 5000 €
```

**Input:** one km + saved θ  
**Output:** one estimated price

---

# Chapter 7 — Overview diagram

```text
┌─────────────────────────────────────────────────────────┐
│                    YOUR PROJECT                         │
├─────────────────────────────────────────────────────────┤
│                                                         │
│   data.csv (24 cars)                                    │
│        │                                                │
│        ▼                                                │
│   ┌─────────────┐                                       │
│   │  TRAINING   │  ← Gradient descent                   │
│   │  (Phase A)  │  ← Minimize MSE                       │
│   └──────┬──────┘                                       │
│          │                                              │
│          ▼                                              │
│      θ0, θ1  (learned parameters)                      │
│          │                                              │
│          ▼                                              │
│   ┌─────────────┐                                       │
│   │ PREDICTION  │  ← Formula: θ0 + θ1 × km              │
│   │  (Phase B)  │                                       │
│   └──────┬──────┘                                       │
│          │                                              │
│          ▼                                              │
│      Estimated price (€)                                │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

# Chapter 8 — Cheat sheet

| Concept | Formula | Role |
|---------|---------|------|
| **Hypothesis** | ŷ = θ0 + θ1·x | Predict price |
| **Error** | ŷ − y | Gap on 1 car |
| **MSE** | (1/m)·Σ(ŷ−y)² | Global gap |
| **Gradient θ0** | (1/m)·Σ(ŷ−y) | How to adjust θ0 |
| **Gradient θ1** | (1/m)·Σ(ŷ−y)·x | How to adjust θ1 |
| **Update** | θ := θ − α·gradient | One descent step |

---

# What to remember

1. **Linear regression** = find a line: price = θ0 + θ1×km.
2. **θ0 and θ1** are unknown at first; training finds them.
3. **MSE** measures model quality; we minimize it.
4. **Gradient descent** adjusts θ0 and θ1 little by little, iteration after iteration.
5. **Learning rate** = step size; not too big, not too small.
6. **Phase A** (train) before **Phase B** (predict): learn once, predict many times.

---

*Related files in this repo: `train.py`, `predict.py`, `data.csv`*
