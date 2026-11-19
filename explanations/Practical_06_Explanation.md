# Practical 6: Code Explanation & Viva Guide
## 📈 Regression Analysis (Linear vs Polynomial Regression)

---

### 🎯 Aim of the Practical
To implement and compare **Linear Regression** and **Polynomial Regression (Degree 2)** to predict house prices using the **Housing Dataset (`Housing.csv`)**, evaluating models with MSE, MAE, and $R^2$ Score.

---

### 🧩 Chunk-by-Chunk Code Breakdown

#### 🔹 Chunk 1: Categorical Encoding & Dataset Splitting
```python
import os
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

path = "/home/avcoe/Housing.csv" if os.path.exists("/home/avcoe/Housing.csv") else "datasets/Housing.csv"
df = pd.read_csv(path)

# Separate features & encode categorical columns
X = pd.get_dummies(df.drop("price", axis=1), drop_first=True)
y = df["price"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```
- **What it does:**
  - `df.drop("price", axis=1)` isolates the independent features.
  - `pd.get_dummies(..., drop_first=True)` applies **One-Hot Encoding** to categorical columns (like `mainroad`, `guestroom`, `furnishingstatus`).
  - `drop_first=True` drops the first dummy category to avoid the **dummy variable trap** (multicollinearity).
  - Splits the data into 80% train and 20% test subsets.

---

#### 🔹 Chunk 2: Linear Regression Model
```python
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)
lin_pred = linear_model.predict(X_test)
```
- **What it does:**
  - Fits a standard ordinary least squares (OLS) linear model: $\hat{y} = w_1 x_1 + w_2 x_2 + \dots + b$.
  - Generates predictions `lin_pred` for test samples.

---

#### 🔹 Chunk 3: Polynomial Regression Pipeline
```python
poly_model = Pipeline([
    ("poly", PolynomialFeatures(degree=2, include_bias=False)),
    ("scaler", StandardScaler()),
    ("reg", LinearRegression())
])
poly_model.fit(X_train, y_train)
poly_pred = poly_model.predict(X_test)
```
- **What it does:**
  - Creates a **Scikit-Learn Pipeline** that sequentially applies 3 steps:
    1. `PolynomialFeatures(degree=2, include_bias=False)`: Generates quadratic polynomial terms ($x_i^2$) and interaction terms ($x_i \cdot x_j$).
    2. `StandardScaler()`: Standardizes the expanded feature set to prevent numerical overflow and stabilize regression coefficients.
    3. `LinearRegression()`: Fits the linear regression model onto the transformed polynomial features.
- **Viva Examiner Tip:**
  - *Examiner:* "Why use `Pipeline` instead of doing steps manually?"
  - *Answer:* A pipeline encapsulates the transformation and training workflow. It guarantees that scaling parameters learned on `X_train` are properly applied to `X_test` without causing **data leakage**.

---

#### 🔹 Chunk 4: Evaluation & Model Comparison
```python
comparison = pd.DataFrame({
    "Model": ["Linear Regression", "Polynomial Regression"],
    "MSE": [mean_squared_error(y_test, lin_pred), mean_squared_error(y_test, poly_pred)],
    "MAE": [mean_absolute_error(y_test, lin_pred), mean_absolute_error(y_test, poly_pred)],
    "R2 Score": [r2_score(y_test, lin_pred), r2_score(y_test, poly_pred)]
})

print("--- MODEL COMPARISON ---")
print(comparison.to_string(index=False))
```
- **What it does:**
  - Calculates 3 key regression metrics for both models:
    - **Mean Squared Error (MSE):** $\frac{1}{n} \sum (y_i - \hat{y}_i)^2$ (penalizes large errors heavily).
    - **Mean Absolute Error (MAE):** $\frac{1}{n} \sum |y_i - \hat{y}_i|$ (average magnitude of errors).
    - **$R^2$ Score (Coefficient of Determination):** Proportion of variance in target explained by the model ($1.0$ is perfect fit).

---

### 🎤 Top Viva Questions & Instant Answers for Practical 6

**Q1: What problem occurs if you set the polynomial degree too high (e.g., degree 6 or 10)?**
- **Overfitting:** The model fits the training data too closely, capturing random noise and fluctuations, resulting in very poor performance on unseen test data.

**Q2: What is the difference between $R^2$ score and adjusted $R^2$ score?**
- $R^2$ always increases or stays the same when you add more features, even if the features are irrelevant.
- **Adjusted $R^2$** penalizes the score for adding irrelevant predictors that do not improve model quality.

**Q3: What does a negative $R^2$ score indicate?**
- A negative $R^2$ means the model performs worse than a simple horizontal line predicting the mean value of the target.
