# Practical 9: Code Explanation & Viva Guide
## 🌲 Ensemble Learning & Hyperparameter Tuning (GridSearchCV)

---

### 🎯 Aim of the Practical
To optimize and compare single classifiers (**SVM**) against ensemble learning classifiers (**Random Forest** and **AdaBoost**) using **GridSearchCV** with 5-fold cross-validation on the **Breast Cancer Dataset (`breast_cancer.csv`)**.

---

### 🧩 Chunk-by-Chunk Code Breakdown

#### 🔹 Chunk 1: Dataset Loading & Stratified Split
```python
import os
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.svm import SVC

path = "/home/avcoe/breast_cancer.csv" if os.path.exists("/home/avcoe/breast_cancer.csv") else "datasets/breast_cancer.csv"
if os.path.exists(path):
    df = pd.read_csv(path)
    X, y = df.drop(columns=["target"]), df["target"]
else:
    raw = load_breast_cancer(as_frame=True)
    X, y = raw.data, raw.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
```
- **What it does:**
  - Loads data either from CSV (`breast_cancer.csv`) or directly falls back to Scikit-Learn's built-in `load_breast_cancer` dataset.
  - Splits into 80% train and 20% test partitions using `stratify=y` to preserve target class balance.

---

#### 🔹 Chunk 2: Models and Parameter Grids
```python
models = {
    "SVM": (SVC(), {"C": [0.1, 1, 10], "kernel": ["linear", "rbf"]}),
    "Random Forest": (RandomForestClassifier(random_state=42), {"n_estimators": [50, 100]}),
    "AdaBoost": (AdaBoostClassifier(random_state=42), {"n_estimators": [50, 100], "learning_rate": [0.5, 1.0]})
}
```
- **What it does:**
  - Defines a Python dictionary mapping each algorithm name to a tuple: `(estimator, parameter_grid)`.
  - **SVM Parameters:** Tests regularization parameter `C` ($0.1, 1, 10$) and kernel types (`linear` vs `rbf`).
  - **Random Forest Parameters:** Tests number of trees `n_estimators` ($50$ vs $100$).
  - **AdaBoost Parameters:** Tests number of weak estimators and `learning_rate` ($0.5$ vs $1.0$).

---

#### 🔹 Chunk 3: Training, Tuning & Evaluation Loop
```python
print("--- MODEL OPTIMIZATION & HYPERPARAMETER TUNING ---")
for name, (model, params) in models.items():
    # Before Tuning
    model.fit(X_train, y_train)
    acc_before = accuracy_score(y_test, model.predict(X_test))

    # After Tuning with 5-Fold Cross Validation
    grid = GridSearchCV(model, params, cv=5, scoring="accuracy")
    grid.fit(X_train, y_train)
    acc_after = accuracy_score(y_test, grid.best_estimator_.predict(X_test))

    print(f"\n{name}:")
    print(f"  Accuracy Before: {acc_before * 100:.2f}% | After Tuning: {acc_after * 100:.2f}%")
    print(f"  Best Parameters: {grid.best_params_}")
```
- **What it does:**
  - **Before Tuning:** Fits default model parameters and measures baseline test accuracy.
  - **GridSearchCV:**
    - `cv=5`: Splits `X_train` into 5 folds. Trains on 4 folds, tests on the 5th, and rotates 5 times.
    - Evaluates every combination in `params` to find the combination yielding the highest mean cross-validation accuracy.
    - `grid.best_estimator_`: The retrained model holding the best hyperparameter configuration.
    - `grid.best_params_`: Displays the winning parameter values.

---

### 🎤 Top Viva Questions & Instant Answers for Practical 9

**Q1: What is the difference between Parameters and Hyperparameters?**
- **Parameters:** Learned automatically by the model from training data (e.g., weights $w$, bias $b$, tree split points).
- **Hyperparameters:** Configured manually by the user *before* training starts (e.g., learning rate, $C$, number of trees $n\_estimators$).

**Q2: What is the difference between Bagging and Boosting?**
- **Bagging (e.g., Random Forest):**
  - Base learners (Decision Trees) are trained **independently and in parallel** on bootstrap subsets.
  - Reduces **variance** (prevents overfitting).
- **Boosting (e.g., AdaBoost):**
  - Base learners are trained **sequentially**.
  - Subsequent trees assign higher weights to samples misclassified by earlier trees.
  - Reduces **bias**.

**Q3: How does GridSearchCV differ from RandomizedSearchCV?**
- `GridSearchCV` exhaustively tests **every single combination** of parameter values.
- `RandomizedSearchCV` randomly samples a fixed number of parameter combinations from probability distributions, running much faster on large parameter spaces.
