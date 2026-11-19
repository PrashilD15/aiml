# Practical 7: Code Explanation & Viva Guide
## 🛍️ Customer Segmentation (K-Means & Hierarchical Clustering)

---

### 🎯 Aim of the Practical
To perform **Unsupervised Customer Segmentation** on mall shoppers based on `Age`, `Annual Income`, and `Spending Score` using **K-Means Clustering** (with the Elbow Method) and **Hierarchical Agglomerative Clustering** (with a Dendrogram).

---

### 🧩 Chunk-by-Chunk Code Breakdown

#### 🔹 Chunk 1: Feature Extraction
```python
import os
import matplotlib.pyplot as plt
import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering, KMeans

path = "/home/avcoe/Mall_Customers.csv" if os.path.exists("/home/avcoe/Mall_Customers.csv") else "datasets/Mall_Customers.csv"
df = pd.read_csv(path)
X = df.iloc[:, [2, 3, 4]].values
```
- **What it does:**
  - Loads the customer dataset.
  - `df.iloc[:, [2, 3, 4]].values` extracts columns 2, 3, and 4 (`Age`, `Annual Income (k$)`, and `Spending Score (1-100)`) as a NumPy array $X$.
  - These 3 numerical attributes define each customer's spending profile without requiring customer IDs or labels.

---

#### 🔹 Chunk 2: Elbow Method & Dendrogram
```python
wcss = [KMeans(n_clusters=k, init='k-means++', random_state=42, n_init=10).fit(X).inertia_ for k in range(1, 11)]

plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(range(1, 11), wcss, marker='o')
plt.title("Elbow Method for Optimal K")
plt.xlabel("Clusters (K)")
plt.ylabel("WCSS")

plt.subplot(1, 2, 2)
dendrogram(linkage(X, method='ward'))
plt.title("Hierarchical Clustering Dendrogram")
plt.tight_layout()
plt.show()
```
- **What it does:**
  - **Elbow Method:** Fits K-Means for $K = 1$ to $10$. For each $K$, records `.inertia_` (Within-Cluster Sum of Squares - WCSS), which measures how tightly grouped the clusters are.
  - Plots WCSS vs. $K$: The optimal number of clusters is located at the sharp "elbow" bend ($K = 5$).
  - **Dendrogram:** Uses `scipy.cluster.hierarchy.linkage(X, method='ward')` to build a hierarchical agglomerative tree and plots it using `dendrogram`.
- **Viva Examiner Tip:**
  - *Examiner:* "What does `init='k-means++'` mean?"
  - *Answer:* It smartly initializes cluster centers far apart from each other, avoiding bad local minima that happen with purely random initialization.
  - *Examiner:* "What is Ward's linkage?"
  - *Answer:* It merges the two clusters that minimize the increase in total within-cluster variance.

---

#### 🔹 Chunk 3: Model Fitting & Cluster Labeling
```python
kmeans = KMeans(n_clusters=5, init='k-means++', random_state=0, n_init=10)
df['KMeans_Cluster'] = kmeans.fit_predict(X)

hc = AgglomerativeClustering(n_clusters=5, linkage='ward')
df['Hierarchical_Cluster'] = hc.fit_predict(X)

print("--- Clustered Customer Sample (First 5 Rows) ---")
print(df[['CustomerID', 'Age', 'Annual Income (k$)', 'Spending Score (1-100)', 'KMeans_Cluster', 'Hierarchical_Cluster']].head())
```
- **What it does:**
  - Trains both **K-Means** and **Agglomerative Hierarchical Clustering** with $K = 5$.
  - `.fit_predict(X)` assigns a cluster ID (`0` to `4`) to each customer.
  - Stores cluster predictions as new columns in the DataFrame and displays the first 5 records.

---

### 🎤 Top Viva Questions & Instant Answers for Practical 7

**Q1: What are the main steps in the K-Means algorithm?**
1. Choose $K$ initial centroids randomly (or via K-Means++).
2. Assign each data point to its closest centroid using Euclidean distance.
3. Recompute the centroid of each cluster as the mean of its assigned points.
4. Repeat steps 2 and 3 until centroids stop shifting (convergence).

**Q2: What is the difference between Partitional (K-Means) and Hierarchical Clustering?**
- **Partitional (K-Means):** Flat partition of data into $K$ non-overlapping clusters; requires specifying $K$ in advance; faster ($\mathcal{O}(N)$).
- **Hierarchical:** Produces a nested tree of clusters (Dendrogram); does not require pre-specifying $K$ upfront; slower ($\mathcal{O}(N^2)$).

**Q3: How do you read a Dendrogram to find the optimal number of clusters?**
- Find the longest vertical lines that are not intercepted by any horizontal cluster merge lines. Drawing a horizontal threshold line across them reveals the natural cluster count.
