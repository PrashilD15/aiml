# Practical 5: Code Explanation & Viva Guide
## 🎯 Classification using Logistic Regression & K-Nearest Neighbors (KNN)

---

### 🎯 Aim of the Practical
To build, evaluate, and compare two supervised classification algorithms—**Logistic Regression** and **K-Nearest Neighbors (KNN)**—on the **Graduate Admission Dataset (`Admission_Predict.csv`)**.

---

### 🧩 Chunk-by-Chunk Code Breakdown

#### 🔹 Chunk 1: Dataset Loading & Target Binarization
```python
import os
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

path = "/home/avcoe/Admission_Predict.csv" if os.path.exists("/home/avcoe/Admission_Predict.csv") else "datasets/Admission_Predict.csv"
df = pd.read_csv(path)

if 'target' not in df.columns:
    chance_col = 'Chance of Admit ' if 'Chance of Admit ' in df.columns else 'Chance of Admit'
    df['target'] = (df[chance_col] >= 0.7).astype(int)

features = [c for c in ['GRE Score', 'TOEFL Score', 'University Rating', 'SOP', 'LOR ', 'CGPA', 'Research'] if c in df.columns]
X = df[features]
y = df['target']
```
- **What it does:**
  - Loads the dataset.
  - Converts continuous admission probability into a binary classification target: if chance $\ge 0.70$, then $1$ (Admitted), else $0$ (Not Admitted).
  - Selects relevant feature columns (`GRE`, `TOEFL`, `CGPA`, etc.) as input matrix $X$ and `target` as vector $y$.

---

#### 🔹 Chunk 2: Feature Standardization & Split
```python
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
```
- **What it does:**
  - `StandardScaler()` scales features using the Z-score formula: $z = \frac{x - \mu}{\sigma}$.
  - `fit_transform(X)` computes the mean and variance and standardizes all columns so that $\mu = 0$ and $\sigma = 1$.
  - Splits into 80% training and 20% testing sets.
- **Viva Examiner Tip:**
  - *Examiner:* "Why is standardization essential for KNN?"
  - *Answer:* KNN calculates Euclidean distance between data points. Without scaling, a feature with large numbers (like GRE Score: 290–340) would overwhelmingly dominate features with smaller scales (like CGPA: 7–10 or SOP: 1–5).

---

#### 🔹 Chunk 3: Logistic Regression Classifier
```python
lr = LogisticRegression()
lr.fit(X_train, y_train)
lr_pred = lr.predict(X_test)
print(f"Logistic Regression Accuracy: {accuracy_score(y_test, lr_pred) * 100:.2f}%")
print("Confusion Matrix:\n", confusion_matrix(y_test, lr_pred))
```
- **What it does:**
  - Initializes and fits the `LogisticRegression` model on the training data.
  - Predicts target classes on the test set (`lr.predict(X_test)`).
  - Calculates accuracy percentage and prints the Confusion Matrix.
- **Viva Examiner Tip:**
  - *Examiner:* "How does Logistic Regression classify data?"
  - *Answer:* It calculates $z = w^T x + b$ and passes it through the **Sigmoid (Logistic) Function**: $\sigma(z) = \frac{1}{1 + e^{-z}}$. If $\sigma(z) \ge 0.5$, it predicts Class 1; otherwise, Class 0.

---

#### 🔹 Chunk 4: K-Nearest Neighbors (KNN) Classifier
```python
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
knn_pred = knn.predict(X_test)
print(f"\nKNN Accuracy: {accuracy_score(y_test, knn_pred) * 100:.2f}%")
print("KNN Classification Report:\n", classification_report(y_test, knn_pred))
```
- **What it does:**
  - Initializes `KNeighborsClassifier` with $K = 5$ neighbors.
  - For each test point, it finds the 5 closest training points by Euclidean distance and takes a majority vote.
  - Outputs accuracy and the full `classification_report` containing Precision, Recall, and F1-Score for each class.

---

### 🎤 Top Viva Questions & Instant Answers for Practical 5

**Q1: What are the components of a Confusion Matrix?**
- **True Positive (TP):** Actually Positive, correctly predicted Positive.
- **True Negative (TN):** Actually Negative, correctly predicted Negative.
- **False Positive (FP):** Actually Negative, incorrectly predicted Positive (Type I error).
- **False Negative (FN):** Actually Positive, incorrectly predicted Negative (Type II error).

**Q2: What is the formula for Precision and Recall?**
- $\text{Precision} = \frac{TP}{TP + FP}$ (Focuses on avoiding False Positives).
- $\text{Recall} = \frac{TP}{TP + FN}$ (Focuses on avoiding False Negatives).

**Q3: Is KNN a parametric or non-parametric algorithm? Why is it called a "lazy learner"?**
- KNN is **non-parametric** (makes no assumptions about underlying data distributions).
- It is a **lazy learner** because it does not learn an explicit model or weights during training; it simply stores the training instances and does all computation at query time.
