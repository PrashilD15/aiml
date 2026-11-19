# Practical 4: Code Explanation & Viva Guide
## 📊 Data Preprocessing, EDA and Train-Test Split

---

### 🎯 Aim of the Practical
To perform **Exploratory Data Analysis (EDA)**, handle missing values and duplicate rows, compute statistical summaries, visualize feature distributions, and split data into training and testing sets on the **Heart Disease Dataset (`heart.csv`)**.

---

### 🧩 Chunk-by-Chunk Code Breakdown

#### 🔹 Chunk 1: Dynamic Dataset Loading
```python
import os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split

path = "/home/avcoe/heart.csv" if os.path.exists("/home/avcoe/heart.csv") else "datasets/heart.csv"
df = pd.read_csv(path)
```
- **What it does:**
  - Imports Pandas, Matplotlib, Seaborn, and Scikit-Learn.
  - Dynamically checks if the college lab path (`/home/avcoe/heart.csv`) exists; otherwise, falls back to the bundled local `datasets/heart.csv` file.

---

#### 🔹 Chunk 2: Data Overview & Preprocessing
```python
print("Dataset Shape:", df.shape)
print("\nMissing Values Before Handling:\n", df.isnull().sum())

# Fill missing Age with median & drop duplicate records
if 'age' in df.columns:
    df['age'] = df['age'].fillna(df['age'].median())
df = df.drop_duplicates()
print("\nShape after removing duplicates:", df.shape)
```
- **What it does:**
  - `df.shape` returns `(rows, columns)`.
  - `df.isnull().sum()` counts missing/NaN values per column.
  - `df['age'].fillna(df['age'].median())` imputes missing age values using the **Median**.
  - `df.drop_duplicates()` removes repeated duplicate rows from the dataset.
- **Viva Examiner Tip:**
  - *Examiner:* "Why fill with Median instead of Mean?"
  - *Answer:* The median is robust against extreme outliers and skewed distributions. The mean is easily distorted by unusually high or low values.

---

#### 🔹 Chunk 3: Statistical Analysis
```python
print("\n--- Summary Statistics ---")
print("Mean:\n", df.mean(numeric_only=True))
print("\nCorrelation:\n", df.corr(numeric_only=True))
```
- **What it does:**
  - Calculates the column-wise mean for all numeric features.
  - Computes the Pearson correlation matrix to measure linear dependencies between variables (values range from $-1.0$ to $+1.0$).
- **Viva Examiner Tip:**
  - *Examiner:* "What does `numeric_only=True` mean?"
  - *Answer:* It prevents Pandas from attempting mathematical operations on non-numeric or string columns, avoiding future `TypeError` warnings.

---

#### 🔹 Chunk 4: Data Visualization (Histogram & Boxplot)
```python
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.hist(df['age'], bins=15, edgecolor='black')
plt.title("Age Distribution")

plt.subplot(1, 2, 2)
sns.boxplot(x=df['chol'])
plt.title("Cholesterol Boxplot")
plt.tight_layout()
plt.show()
```
- **What it does:**
  - Creates a figure with 2 subplots side-by-side.
  - Left subplot: A **Histogram** of patient ages divided into 15 bins to display frequency distribution.
  - Right subplot: A **Boxplot** of serum cholesterol (`chol`) to identify the median, quartiles (Q1, Q3), and visual outliers (points beyond the whiskers).
- **Viva Examiner Tip:**
  - *Examiner:* "How does a boxplot define an outlier?"
  - *Answer:* Any point beyond $Q1 - 1.5 \times \text{IQR}$ or $Q3 + 1.5 \times \text{IQR}$, where $\text{IQR} = Q3 - Q1$ (Interquartile Range).

---

#### 🔹 Chunk 5: Train-Test Split (80:20)
```python
X = df.drop('target', axis=1)
y = df['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("\n--- Split Shapes ---")
print(f"X_train: {X_train.shape}, X_test: {X_test.shape}")
print(f"y_train: {y_train.shape}, y_test: {y_test.shape}")
```
- **What it does:**
  - Separates independent features ($X$) from the dependent target label ($y$).
  - `train_test_split(...)` splits the dataset into 80% training data and 20% unseen test data.
  - `random_state=42` sets the random seed for reproducible splits across different runs.

---

### 🎤 Top Viva Questions & Instant Answers for Practical 4

**Q1: Why is train-test split necessary?**
- To evaluate the machine learning model on unseen data. Testing on the same data used for training leads to biased evaluations and cannot detect **overfitting**.

**Q2: What is the difference between normalization and standardization?**
- **Normalization (Min-Max Scaling):** Rescales data to a fixed range, typically $[0, 1]$.
- **Standardization (Z-score Scaling):** Rescales data to have a mean $\mu = 0$ and standard deviation $\sigma = 1$.

**Q3: How do you identify correlation between features?**
- By examining the correlation matrix values: $+1$ indicates perfect positive correlation, $0$ indicates no linear correlation, and $-1$ indicates perfect negative correlation.
