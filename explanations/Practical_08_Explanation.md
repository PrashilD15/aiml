# Practical 8: Code Explanation & Viva Guide
## 🔬 Dimensionality Reduction using PCA with SVM

---

### 🎯 Aim of the Practical
To perform feature reduction on 30 diagnostic features of the **Wisconsin Breast Cancer Dataset (`wdbc.csv`)** using **Principal Component Analysis (PCA)** retaining 95% variance, and compare **Support Vector Machine (SVM)** accuracy before and after PCA.

---

### 🧩 Chunk-by-Chunk Code Breakdown

#### 🔹 Chunk 1: Dataset Preparation & Preprocessing
```python
import os
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

path = "/home/avcoe/wdbc.csv" if os.path.exists("/home/avcoe/wdbc.csv") else "datasets/wdbc.csv"
df = pd.read_csv(path)
if 'id' in df.columns:
    df = df.drop('id', axis=1)

X = df.drop("diagnosis", axis=1)
y = df["diagnosis"]
```
- **What it does:**
  - Drops unique `id` values (which carry zero predictive value).
  - Separates the target column (`diagnosis`: `M` = Malignant, `B` = Benign) from the 30 continuous cell measurements.

---

#### 🔹 Chunk 2: Standardization & Stratified Split
```python
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42, stratify=y)
```
- **What it does:**
  - `StandardScaler()` standardizes all 30 features ($\mu = 0, \sigma = 1$).
  - `stratify=y` guarantees that both the training and testing sets have the exact same proportion of Malignant and Benign diagnoses as the original dataset.
- **Viva Examiner Tip:**
  - *Examiner:* "Why MUST we scale data before running PCA?"
  - *Answer:* PCA seeks axes that maximize variance. If one feature has variance 10,000 and another has variance 0.1 simply due to measurement units, PCA will treat the large-unit feature as primary, distorting true relationships. Standardization gives every feature an equal baseline.

---

#### 🔹 Chunk 3: Baseline SVM Classifier (Before PCA)
```python
svm_before = SVC(kernel="rbf")
svm_before.fit(X_train, y_train)
acc_before = accuracy_score(y_test, svm_before.predict(X_test))
```
- **What it does:**
  - Trains a Support Vector Classifier with a Radial Basis Function (**RBF kernel**) on all 30 original features.
  - Records the baseline accuracy on the test set.

---

#### 🔹 Chunk 4: PCA Dimensionality Reduction
```python
pca = PCA(n_components=0.95)
X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)
```
- **What it does:**
  - `n_components=0.95` specifies that PCA should automatically select the minimal number of principal components needed to preserve **95% of the total cumulative variance**.
  - `fit_transform(X_train)` computes the covariance matrix, eigenvalues, and eigenvectors on training data and projects the data onto these principal axes.
  - `transform(X_test)` projects the test set onto the exact same learned axes.
- **Viva Examiner Tip:**
  - *Examiner:* "How many features are left after PCA with 95% variance?"
  - *Answer:* Typically only 10 to 11 principal components are needed out of the original 30 features!

---

#### 🔹 Chunk 5: SVM Classifier (After PCA) & Comparison
```python
svm_after = SVC(kernel="rbf")
svm_after.fit(X_train_pca, y_train)
acc_after = accuracy_score(y_test, svm_after.predict(X_test_pca))

print("--- PCA DIMENSIONALITY REDUCTION SUMMARY ---")
print(f"Features Before PCA : {X.shape[1]}  --> Accuracy: {acc_before * 100:.2f}%")
print(f"Features After PCA  : {X_train_pca.shape[1]}  --> Accuracy: {acc_after * 100:.2f}%")
print(f"Total Variance Kept : {pca.explained_variance_ratio_.sum() * 100:.2f}%")
```
- **What it does:**
  - Trains and evaluates SVM on the reduced dimensional representation.
  - Confirms that feature count drops by ~65% while classification accuracy remains virtually identical (or even improves due to noise reduction).

---

### 🎤 Top Viva Questions & Instant Answers for Practical 8

**Q1: What is Principal Component Analysis (PCA)?**
- An unsupervised linear transformation technique that converts correlated high-dimensional features into a smaller set of linearly uncorrelated orthogonal features called **Principal Components**.

**Q2: What is the mathematical relationship between Eigenvalues and Principal Components?**
- **Eigenvectors** define the direction of the new principal component axes.
- **Eigenvalues** define the magnitude of variance explained along each axis.

**Q3: What are the main advantages of applying PCA?**
1. Mitigates the **Curse of Dimensionality**.
2. Speeds up ML model training and inference.
3. Eliminates multicollinearity between features.
4. Enables 2D and 3D visualization of high-dimensional data.
