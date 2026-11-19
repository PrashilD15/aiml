# 🧠 Artificial Intelligence & Machine Learning (AIML) Lab Practicals

[![Python 3](https://img.shields.io/badge/Python-3.x-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Linux](https://img.shields.io/badge/OS-Linux%20%7C%20Ubuntu-E95420?logo=ubuntu&logoColor=white)](https://ubuntu.com/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub](https://img.shields.io/badge/Repo-PrashilD15%2Faiml-black?logo=github)](https://github.com/PrashilD15/aiml)

> **Quick Jump / थेट नेव्हिगेशन:**
> - [📘 Part 1: Complete English Guide (Linux Terminal Commands & Viva Q&A)](#-part-1-complete-english-guide)
> - [📙 भाग २: संपूर्ण मराठी मार्गदर्शिका (लिनक्स कमांड्स व व्हायव्हा प्रश्नोत्तरे)](#-भाग-२-संपूर्ण-मराठी-मार्गदर्शिका)
> - [📚 Chunk-by-Chunk Code Explanations Folder (`explanations/`)](explanations/)

---

# 📘 PART 1: COMPLETE ENGLISH GUIDE

## 1. System Overview & Dual Compatibility
This repository contains complete implementations of **AIML Laboratory Practicals (1 to 9)**.

The codebase is built Linux-first and includes automatic path detection:
- **College Lab PCs (Linux / Ubuntu):** Automatically reads datasets from `/home/avcoe/` where laboratory datasets reside.
- **Personal Laptops / PCs (Linux, Windows, macOS):** Automatically falls back to the local `datasets/` directory included in this repository.

---

## 2. Linux Terminal Commands (Setup & Execution)

### Step 1: Open Terminal & Clone Repository
Open your Linux terminal (`Ctrl + Alt + T` on Ubuntu):
```bash
git clone https://github.com/PrashilD15/aiml.git
cd aiml
```

### Step 2: Install Dependencies via `pip3`
Install required packages using Linux Python 3 package manager:
```bash
python3 -m pip install -r requirements.txt
```
*(Or install packages directly:)*
```bash
python3 -m pip install pandas scikit-learn matplotlib seaborn numpy scipy
```

### Step 3: Run Any Practical
Execute scripts using Linux `python3`:

```bash
# Practical 1: Model-Based Reflex Agent (Smart Home HVAC System)
python3 Practical_01_Smart_Home_Agent.py

# Practical 2: Route Planning using BFS & DFS
python3 Practical_02_Route_Planning_BFS_and_DFS.py

# Practical 3: Rule-Based Expert System (Forward & Backward Chaining)
python3 Practical_03_Rule_Based_Expert_System.py

# Practical 4: Data Preprocessing, EDA & Train-Test Split
python3 Practical_04_Data_Preprocessing_and_EDA.py

# Practical 5: Classification using Logistic Regression & KNN
python3 Practical_05_Classification_Logistic_and_KNN.py

# Practical 6: Regression Analysis (Linear vs Polynomial)
python3 Practical_06_Regression_Linear_and_Polynomial.py

# Practical 7: Customer Segmentation Clustering (K-Means & Hierarchical)
python3 Practical_07_Customer_Segmentation_KMeans_and_Hierarchical.py

# Practical 8: Dimensionality Reduction using PCA with SVM
python3 Practical_08_Dimensionality_Reduction_PCA_and_SVM.py

# Practical 9: Model Optimization, Ensemble Learning & GridSearchCV
python3 Practical_09_Ensemble_Learning_and_Hyperparameter_Tuning.py
```

---

## 3. Practicals Index & Implementation Details

| Practical | Actual Script Name | Dataset | Core Algorithm / Technique | 📖 Chunk Explanation & Viva Guide |
| :---: | :--- | :---: | :--- | :--- |
| **01** | [`Practical_01_Smart_Home_Agent.py`](Practical_01_Smart_Home_Agent.py) | Sensor Inputs | Model-Based Reflex Agent | [📘 Read Explanation](explanations/Practical_01_Explanation.md) |
| **02** | [`Practical_02_Route_Planning_BFS_and_DFS.py`](Practical_02_Route_Planning_BFS_and_DFS.py) | Built-in Graph | Breadth-First & Depth-First Search | [📘 Read Explanation](explanations/Practical_02_Explanation.md) |
| **03** | [`Practical_03_Rule_Based_Expert_System.py`](Practical_03_Rule_Based_Expert_System.py) | Medical Rules | Forward & Backward Chaining | [📘 Read Explanation](explanations/Practical_03_Explanation.md) |
| **04** | [`Practical_04_Data_Preprocessing_and_EDA.py`](Practical_04_Data_Preprocessing_and_EDA.py) | `heart.csv` | Missing value, Outlier, Split | [📘 Read Explanation](explanations/Practical_04_Explanation.md) |
| **05** | [`Practical_05_Classification_Logistic_and_KNN.py`](Practical_05_Classification_Logistic_and_KNN.py) | `Admission_Predict.csv` | Logistic Regression & KNN | [📘 Read Explanation](explanations/Practical_05_Explanation.md) |
| **06** | [`Practical_06_Regression_Linear_and_Polynomial.py`](Practical_06_Regression_Linear_and_Polynomial.py) | `Housing.csv` | Linear vs Polynomial ($Degree=2$) | [📘 Read Explanation](explanations/Practical_06_Explanation.md) |
| **07** | [`Practical_07_Customer_Segmentation_KMeans_and_Hierarchical.py`](Practical_07_Customer_Segmentation_KMeans_and_Hierarchical.py) | `Mall_Customers.csv` | K-Means (Elbow) & Dendrogram | [📘 Read Explanation](explanations/Practical_07_Explanation.md) |
| **08** | [`Practical_08_Dimensionality_Reduction_PCA_and_SVM.py`](Practical_08_Dimensionality_Reduction_PCA_and_SVM.py) | `wdbc.csv` | PCA & Support Vector Machine | [📘 Read Explanation](explanations/Practical_08_Explanation.md) |
| **09** | [`Practical_09_Ensemble_Learning_and_Hyperparameter_Tuning.py`](Practical_09_Ensemble_Learning_and_Hyperparameter_Tuning.py) | `breast_cancer.csv` | Random Forest, AdaBoost & GridSearch | [📘 Read Explanation](explanations/Practical_09_Explanation.md) |

---

## 4. Comprehensive Oral / Viva Voce Questions & Answers (English)

### 🔹 Practical 1: Model-Based Reflex Agent (Smart Home HVAC System)
- **Q1: What type of agent architecture is implemented in Practical 1?**
  - **Answer:** A **Model-Based Reflex Agent**. Unlike a simple reflex agent, it maintains an **internal state** (history of recent temperature readings) to understand how the environment changes over time.
- **Q2: What is the PEAS description for this Smart Home Agent?**
  - **Answer:**
    - **Performance Measure:** Comfort (maintaining target temperature) and energy savings (turning off devices when no motion is detected).
    - **Environment:** Room / indoor home environment.
    - **Actuators:** AC (Cooling), Heater (Heating), and Fan.
    - **Sensors:** Thermometer (temperature sensor) and PIR Motion Detector.
- **Q3: What is the difference between a Simple Reflex Agent and a Model-Based Reflex Agent?**
  - **Answer:** A Simple Reflex Agent acts solely on the current percept (condition-action rules) without memory. A Model-Based Reflex Agent maintains internal state memory to handle partially observable environments and monitor trends.

### 🔹 Practical 2: Route Planning using BFS and DFS
- **Q1: What is the fundamental difference between BFS and DFS?**
  - **Answer:** BFS explores nodes level by level using a FIFO Queue and guarantees finding the shortest path on unweighted graphs. DFS explores deep along a single branch before backtracking using a LIFO Stack.
- **Q2: Does BFS always find the optimal path?**
  - **Answer:** Yes, for unweighted graphs (where each move has an identical edge cost of 1). For weighted graphs, algorithms like Dijkstra or A* are necessary.
- **Q3: What are the space and time complexities?**
  - **Answer:**
    - Time complexity for both is $\mathcal{O}(V + E)$ where $V$ is vertices and $E$ is edges.
    - Space complexity: BFS requires $\mathcal{O}(V)$ because an entire tree breadth is held in memory; DFS requires $\mathcal{O}(d)$ where $d$ is maximum depth.

### 🔹 Practical 3: Expert System & Chaining
- **Q1: Explain the difference between Forward Chaining and Backward Chaining.**
  - **Answer:**
    - **Forward Chaining (Data-Driven):** Starts with known atomic facts (e.g., `Fever`, `Cough`) and fires matching rules from the knowledge base until deriving new conclusions. Ideal for monitoring, diagnosis, and reactive planning.
    - **Backward Chaining (Goal-Driven):** Starts with a candidate goal (e.g., `Medicine`) and recursively searches backward for rules whose premises are validated by current facts. Ideal for debugging and hypothesis verification.
- **Q2: What is an Inference Engine?**
  - **Answer:** The computational brain of an expert system that applies logical deduction rules to facts stored within the knowledge base to reach conclusions.

### 🔹 Practical 4: Data Preprocessing & EDA
- **Q1: Why is data preprocessing required before feeding data to ML algorithms?**
  - **Answer:** Real-world datasets contain missing values, invalid types, extreme outliers, duplicate rows, and unscaled columns. Garbage data results in biased, inaccurate models ("garbage in, garbage out"). Preprocessing ensures model robustness and rapid numerical convergence.
- **Q2: When should missing values be filled with Median instead of Mean?**
  - **Answer:** Use **Mean** when data follows a symmetric, normal distribution without extreme values. Use **Median** when data is skewed or has large outliers, as median is a non-parametric statistic unaffected by extreme outliers.
- **Q3: Why do we split data into Train and Test sets?**
  - **Answer:** To evaluate the generalization performance of the model on unseen test data and detect whether the model is overfitting to training data.

### 🔹 Practical 5: Classification (Logistic Regression & KNN)
- **Q1: Is Logistic Regression a regression or a classification technique?**
  - **Answer:** It is a **classification algorithm**. While it fits a linear boundary, it maps continuous predictions through the sigmoid function $\sigma(z) = \frac{1}{1 + e^{-z}}$ to yield a probability score between 0 and 1, which is categorized into discrete classes.
- **Q2: Why is Feature Scaling (StandardScaler) essential for KNN?**
  - **Answer:** K-Nearest Neighbors classifies instances based on Euclidean distance: $d(p, q) = \sqrt{\sum (p_i - q_i)^2}$. If one feature is measured in thousands and another in decimals, the larger feature will dominate the distance metric. `StandardScaler` normalizes each feature to have mean $\mu = 0$ and standard deviation $\sigma = 1$.
- **Q3: What are Precision, Recall, and F1-Score?**
  - **Answer:**
    - $\text{Precision} = \frac{TP}{TP + FP}$ (Exactness: of all predicted positives, how many were truly positive?)
    - $\text{Recall} = \frac{TP}{TP + FN}$ (Completeness: of all actual positives, how many did we identify?)
    - $\text{F1-Score} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$ (Harmonic mean balancing precision and recall).

### 🔹 Practical 6: Regression Analysis (Linear vs Polynomial)
- **Q1: Why choose Polynomial Regression over simple Linear Regression?**
  - **Answer:** Linear Regression models straight-line relationships ($y = mx + c$). If the underlying relationship is non-linear or curved, Linear Regression underfits. Polynomial Regression introduces higher-degree terms ($x^2, x^3$) to map non-linear trends.
- **Q2: What is the $R^2$ Score (Coefficient of Determination)?**
  - **Answer:** $R^2 = 1 - \frac{SS_{\text{res}}}{SS_{\text{tot}}}$. It quantifies the proportion of variance in the dependent variable explained by independent features. An $R^2$ of 1.0 indicates a perfect fit.

### 🔹 Practical 7: Customer Segmentation Clustering (K-Means & Hierarchical)
- **Q1: What is Unsupervised Learning?**
  - **Answer:** Machine learning where the model is provided with unlabeled inputs without predefined target outcomes. The model discovers natural clusters, patterns, and groupings within the data.
- **Q2: How does the Elbow Method determine optimal $K$ in K-Means?**
  - **Answer:** It computes Within-Cluster Sum of Squares (WCSS / inertia) for various values of $K$. As $K$ increases, WCSS decreases. The point where the rate of decrease forms an acute bend (like an elbow) represents the optimal balance of compact clusters without overfitting.
- **Q3: What is a Dendrogram?**
  - **Answer:** A tree diagram representing hierarchical clustering steps. The vertical axis denotes distance/dissimilarity between clusters; horizontal cuts define cluster groups.

### 🔹 Practical 8: Dimensionality Reduction (PCA & SVM)
- **Q1: What is the "Curse of Dimensionality"?**
  - **Answer:** As feature dimensions grow large, data points become sparse in high-dimensional space. Models require exponentially more data to generalize, computational latency spikes, and distance metrics degrade.
- **Q2: How does Principal Component Analysis (PCA) work?**
  - **Answer:** PCA standardizes the data, calculates the covariance matrix, determines its eigenvectors (principal axes) and eigenvalues (variance magnitude), and rotates/projects the dataset onto orthogonal axes that maximize explained variance.

### 🔹 Practical 9: Ensemble Learning & Hyperparameter Tuning
- **Q1: What is Ensemble Learning? What is the difference between Bagging and Boosting?**
  - **Answer:** Combining multiple individual models (weak learners) to construct a stronger, more accurate predictor.
    - **Bagging (e.g., Random Forest):** Trains multiple models in parallel on random bootstrap subsets of data and averages predictions to reduce variance (overfitting).
    - **Boosting (e.g., AdaBoost):** Trains models sequentially; each subsequent learner places higher sample weights on mistakes made by earlier learners to reduce bias.
- **Q2: What is GridSearchCV and why is K-Fold Cross-Validation used?**
  - **Answer:** `GridSearchCV` searches across all specified combinations of hyperparameters for an estimator. $K$-fold cross-validation divides data into $K$ subsets, training on $K-1$ and validating on the remaining 1, ensuring parameters perform robustly on unseen data.

---
---

# 📙 भाग २: संपूर्ण मराठी मार्गदर्शिका

## १. प्रणाली परिचय आणि लिनक्स सुसंगतता
या रिपॉझिटरीमध्ये **AIML लॅब प्रॅक्टिकल्स (१ ते ९)** चे संपूर्ण आणि अचूक पायथन कोड दिलेले आहेत.

हा कोड **लिनक्स आणि कॉलेज कॉम्प्युटरसाठी** विशेष अनुकूल केला आहे:
- **कॉलेज लॅब लिनक्स पीसी (Ubuntu/Debian):** कॉलेज लॅबमधील संगणकावर डेटासेट्स आधीपासूनच `/home/avcoe/` मध्ये असतात. हा कोड कोणत्याही बदलांशिवाय थेट तिथे चालतो.
- **घरचा लॅपटॉप / कॉम्प्युटर:** जर तुम्ही लॅपटॉपवर कोड चालवत असाल, तर तो या रिपॉझिटरीमधील `datasets/` फोल्डरमधून सर्व डेटासेट्स आपोआप लोड करतो.

---

## २. लिनक्स टर्मिनल कमांड्स (सेटअप व एक्झिक्युशन)

### पायरी १: लिनक्स टर्मिनल उघडा आणि प्रोजेक्ट क्लोन करा
लिनक्स टर्मिनल उघडा (शॉर्टकट: `Ctrl + Alt + T`):
```bash
git clone https://github.com/PrashilD15/aiml.git
cd aiml
```

### पायरी २: `python3-pip` द्वारे लायब्ररी इन्स्टॉल करा
लिनक्समध्ये `python3` वापरून सर्व लायब्ररी इन्स्टॉल करा:
```bash
python3 -m pip install -r requirements.txt
```
*(किंवा मॅन्युअली इन्स्टॉल करा:)*
```bash
python3 -m pip install pandas scikit-learn matplotlib seaborn numpy scipy
```

### पायरी ३: प्रॅक्टिकल रन करा
लिनक्स टर्मिनलमध्ये `python3` वापरून खालीलप्रमाणे प्रॅक्टिकल्स चालवा:

```bash
# प्रॅक्टिकल १: मॉडेल-बेस्ड स्मार्ट होम एजंट
python3 Practical_01_Smart_Home_Agent.py

# प्रॅक्टिकल २: रूट प्लॅनिंग (BFS आणि DFS)
python3 Practical_02_Route_Planning_BFS_and_DFS.py

# प्रॅक्टिकल ३: एक्सपर्ट सिस्टीम (फॉरवर्ड आणि बॅकवर्ड चेनिंग)
python3 Practical_03_Rule_Based_Expert_System.py

# प्रॅक्टिकल ४: डेटा प्रीप्रोसेसिंग आणि ट्रेन-टेस्ट स्प्लिट
python3 Practical_04_Data_Preprocessing_and_EDA.py

# प्रॅक्टिकल ५: क्लासिफिकेशन (Logistic Regression आणि KNN)
python3 Practical_05_Classification_Logistic_and_KNN.py

# प्रॅक्टिकल ६: रिग्रेशन ॲनालिसिस (लिनिअर आणि पॉलिइनॉमिअल)
python3 Practical_06_Regression_Linear_and_Polynomial.py

# प्रॅक्टिकल ७: कस्टमर सेगमेंटेशन क्लस्टरिंग (के-मीन्स आणि डेंड्रोग्राम)
python3 Practical_07_Customer_Segmentation_KMeans_and_Hierarchical.py

# प्रॅक्टिकल ८: डायमेंशनॅलिटी रिडक्शन (PCA सह SVM)
python3 Practical_08_Dimensionality_Reduction_PCA_and_SVM.py

# प्रॅक्टिकल ९: मॉडेल ऑप्टिमायझेशन, एन्सेम्बल लर्निंग आणि GridSearchCV
python3 Practical_09_Ensemble_Learning_and_Hyperparameter_Tuning.py
```

---

## ३. सर्व प्रॅक्टिकल्सची सविस्तर माहिती

| प्रॅक्टिकल | फाईलचे प्रत्यक्ष पूर्ण नाव | डेटासेट | वापरलेला अल्गोरिदम / तंत्रज्ञान | 📖 सविस्तर स्पष्टीकरण लिंक |
| :---: | :--- | :---: | :--- | :--- |
| **०१** | [`Practical_01_Smart_Home_Agent.py`](Practical_01_Smart_Home_Agent.py) | सेन्सर्स इनपुट | मॉडेल-बेस्ड रिफ्लेक्स एजंट | [📘 स्पष्टीकरण वाचा](explanations/Practical_01_Explanation.md) |
| **०२** | [`Practical_02_Route_Planning_BFS_and_DFS.py`](Practical_02_Route_Planning_BFS_and_DFS.py) | आलेखाचा डेटा | Breadth-First व Depth-First Search | [📘 स्पष्टीकरण वाचा](explanations/Practical_02_Explanation.md) |
| **०३** | [`Practical_03_Rule_Based_Expert_System.py`](Practical_03_Rule_Based_Expert_System.py) | वैद्यकीय नियम | फॉरवर्ड व बॅकवर्ड चेनिंग | [📘 स्पष्टीकरण वाचा](explanations/Practical_03_Explanation.md) |
| **०४** | [`Practical_04_Data_Preprocessing_and_EDA.py`](Practical_04_Data_Preprocessing_and_EDA.py) | `heart.csv` | डेटा क्लीनिंग, मिसिंग व्हॅल्यू भरणे | [📘 स्पष्टीकरण वाचा](explanations/Practical_04_Explanation.md) |
| **०५** | [`Practical_05_Classification_Logistic_and_KNN.py`](Practical_05_Classification_Logistic_and_KNN.py) | `Admission_Predict.csv` | लॉजिस्टीक रिग्रेशन व KNN | [📘 स्पष्टीकरण वाचा](explanations/Practical_05_Explanation.md) |
| **०६** | [`Practical_06_Regression_Linear_and_Polynomial.py`](Practical_06_Regression_Linear_and_Polynomial.py) | `Housing.csv` | लिनिअर विरुद्ध पॉलिइनॉमिअल (Degree 2) | [📘 स्पष्टीकरण वाचा](explanations/Practical_06_Explanation.md) |
| **०७** | [`Practical_07_Customer_Segmentation_KMeans_and_Hierarchical.py`](Practical_07_Customer_Segmentation_KMeans_and_Hierarchical.py) | `Mall_Customers.csv` | के-मीन्स (एल्बो पद्धत) व डेंड्रोग्राम | [📘 स्पष्टीकरण वाचा](explanations/Practical_07_Explanation.md) |
| **०८** | [`Practical_08_Dimensionality_Reduction_PCA_and_SVM.py`](Practical_08_Dimensionality_Reduction_PCA_and_SVM.py) | `wdbc.csv` | PCA व सपोर्ट व्हेक्टर मशीन | [📘 स्पष्टीकरण वाचा](explanations/Practical_08_Explanation.md) |
| **०९** | [`Practical_09_Ensemble_Learning_and_Hyperparameter_Tuning.py`](Practical_09_Ensemble_Learning_and_Hyperparameter_Tuning.py) | `breast_cancer.csv` | रँडम फॉरेस्ट, ॲडाबूस्ट व GridSearch | [📘 स्पष्टीकरण वाचा](explanations/Practical_09_Explanation.md) |

---

## ४. तोंडी परीक्षा (Oral / Viva Voce) प्रश्न आणि उत्तरे (मराठी)

### 🔹 प्रॅक्टिकल १: मॉडेल-बेस्ड स्मार्ट होम एजंट
- **प्रश्न १: प्रॅक्टिकल १ मध्ये कोणत्या प्रकारचा AI एजंट वापरला आहे?**
  - **उत्तर:** **मॉडेल-बेस्ड रिफ्लेक्स एजंट (Model-Based Reflex Agent)**. हा एजंट फक्त सध्याच्या परिस्थितीवर अवलंबून न राहता मागील तापमानाचा इतिहास (Internal State/Memory) लक्षात ठेवतो.
- **प्रश्न २: या एजंटचे PEAS (Performance, Environment, Actuators, Sensors) काय आहे?**
  - **उत्तर:**
    - **Performance:** खोलीचे तापमान योग्य राखणे आणि वीज बचत करणे.
    - **Environment:** खोली / घर.
    - **Actuators:** AC (थंडावा), हीटर (उबदारपणा) आणि फॅन.
    - **Sensors:** तापमान सेन्सर (थर्मोमीटर) आणि मोशन सेन्सर (PIR).
- **प्रश्न ३: सिम्पल रिफ्लेक्स आणि मॉडेल-बेस्ड रिफ्लेक्स एजंटमधील फरक काय?**
  - **उत्तर:** सिम्पल रिफ्लेक्स एजंटला भूतकाळाची आठवण नसते (फक्त IF-THEN नियम); मॉडेल-बेस्ड एजंट अंतर्गत मेमरी (Internal State) ठेवून निर्णय घेतो.

### 🔹 प्रॅक्टिकल २: BFS आणि DFS रूट प्लॅनिंग
- **प्रश्न १: BFS आणि DFS मधील मुख्य फरक काय आहे?**
  - **उत्तर:** BFS मध्ये रांगेचा (Queue - FIFO) वापर करून लेव्हलनुसार शोध घेतला जातो, ज्यामुळे सर्वात लहान मार्ग मिळतो. DFS मध्ये स्टॅकचा (Stack - LIFO) वापर करून एकाच शाखेत खोलवर जाऊन शेवटपर्यंत शोध घेतला जातो.
- **प्रश्न २: BFS नेहमी सर्वात कमी अंतराचा मार्ग देतो का?**
  - **उत्तर:** होय, पण फक्त अनवेटेड (Unweighted) आलेखासाठी. जर कडांना वजन (Weights) असेल, तर डायक्स्ट्रा किंवा A* अल्गोरिदम वापरावा लागतो.
- **प्रश्न ३: BFS आणि DFS ची मेमरी कपॅसिटी कशी असते?**
  - **उत्तर:** BFS ला जास्त मेमरी लागते कारण एका लेव्हलचे सर्व नोड्स Queue मध्ये साठवावे लागतात ($\mathcal{O}(V)$). DFS ला कमी मेमरी लागते ($\mathcal{O}(d)$).

### 🔹 प्रॅक्टिकल ३: एक्सपर्ट सिस्टीम आणि चेनिंग
- **प्रश्न १: फॉरवर्ड चेनिंग आणि बॅकवर्ड चेनिंग मधील फरक सांगा.**
  - **उत्तर:**
    - **फॉरवर्ड चेनिंग (डेटा-ड्रिव्हन):** आधीपासून माहीत असलेल्या तथ्यांवरून/माहितीवरून सुरुवात करून निष्कर्षापर्यंत जाते.
    - **बॅकवर्ड चेनिंग (गोल-ड्रिव्हन):** अंतिम निष्कर्षापासून सुरुवात करून तो सिद्ध करण्यासाठी मागील माहिती शोधते.
- **प्रश्न २: एक्सपर्ट सिस्टीमचे मुख्य भाग कोणते?**
  - **उत्तर:** १. नॉलेज बेस (नियम व माहिती), २. इन्फरन्स इंजिन (निर्णय घेणारा मेंदू), ३. युजर इंटरफेस.

### 🔹 प्रॅक्टिकल ४: डेटा प्रीप्रोसेसिंग आणि EDA
- **प्रश्न १: डेटा प्रीप्रोसेसिंग का गरजेचे आहे?**
  - **उत्तर:** कच्च्या डेटामध्ये अनेक त्रुटी, गहाळ माहिती आणि विसंगती असतात. जर चुकीचा डेटा मॉडेलला दिला, तर मॉडेल चुकीचे अंदाज बांधते (Garbage in, Garbage out). म्हणूनच डेटा साफ करणे आवश्यक आहे.
- **प्रश्न २: मिसिंग व्हॅल्यू भरताना Mean ऐवजी Median कधी वापरावा?**
  - **उत्तर:** जेव्हा डेटामध्ये टोकाचे आकडे (Outliers) असतात, तेव्हा **Median (मध्यक)** वापरावा, कारण आउटलायर्सचा मीडियनवर परिणाम होत नाही.
- **प्रश्न ३: डेटा ट्रेन आणि टेस्ट सेटमध्ये का विभागतात?**
  - **उत्तर:** मॉडेल नवीन डेटामधून अचूक अंदाज बांधू शकते का (Generalization) हे तपासण्यासाठी आणि मॉडेल ओव्हरफिट होत नाही ना हे पाहण्यासाठी.

### 🔹 प्रॅक्टिकल ५: वर्गीकरण (लॉजिस्टीक रिग्रेशन आणि KNN)
- **प्रश्न १: लॉजिस्टीक रिग्रेशन हा रिग्रेशन अल्गोरिदम आहे की क्लासिफिकेशन?**
  - **उत्तर:** नावात रिग्रेशन असले तरी हा **क्लासिफिकेशन (वर्गीकरण)** अल्गोरिदम आहे. तो सिग्मॉइड फंक्शनद्वारे संभाव्यता (Probability) मोजून ० किंवा १ मध्ये वर्गीकरण करतो.
- **प्रश्न २: KNN साठी डेटा स्केलिंग (StandardScaler) का आवश्यक आहे?**
  - **उत्तर:** KNN बिंदूंमधील अंतर (Euclidean Distance) मोजतो. जर एका कॉलमची व्हॅल्यू खूप मोठी आणि दुसऱ्याची लहान असेल, तर मोठा कॉलम अंतरावर जास्त प्रभाव टाकतो. सर्व कॉलम्सना समान महत्त्व देण्यासाठी स्केलिंग आवश्यक आहे.
- **प्रश्न ३: प्रिसिजन, रिकॉल आणि F1-स्कोअर म्हणजे काय?**
  - **उत्तर:**
    - **प्रिसिजन (Precision):** मॉडेलने पॉझिटिव्ह ठरवलेल्यांपैकी किती खरोखर पॉझिटिव्ह आहेत.
    - **रिकॉल (Recall):** खरोखर असलेल्या पॉझिटिव्हपैकी मॉडेलने किती बरोबर ओळखले.
    - **F1-स्कोअर:** प्रिसिजन आणि रिकॉलचा सुवर्णमध्य (Harmonic Mean).

### 🔹 प्रॅक्टिकल ६: रिग्रेशन ॲनालिसिस
- **प्रश्न १: लिनिअर रिग्रेशनऐवजी पॉलिइनॉमिअल रिग्रेशन का वापरतात?**
  - **उत्तर:** लिनिअर रिग्रेशन फक्त सरळ रेषेतील संबंध दाखवू शकते. जर डेटा वक्राकार (Curved/Non-linear) असेल, तर पॉलिइनॉमिअल रिग्रेशन उच्च घातांक ($x^2, x^3$) जोडून अचूक अंदाज देतो.
- **प्रश्न २: $R^2$ स्कोअर काय दर्शवतो?**
  - **उत्तर:** मॉडेलने डेटाचा किती टक्के फरक अचूक ओळखला आहे ते $R^2$ स्कोअर सांगतो. १.० म्हणजे १००% अचूक मॉडेल.

### 🔹 प्रॅक्टिकल ७: कस्टमर सेगमेंटेशन क्लस्टरिंग (के-मीन्स आणि हायराक्रिकल)
- **प्रश्न १: अनसुपरव्हाइझ्ड लर्निंग म्हणजे काय?**
  - **उत्तर:** ज्या डेटामध्ये पूर्वीपासून लेबल्स किंवा उत्तरे दिलेली नसतात, त्यातील नमुने किंवा गट (Clusters) शोधणे म्हणजे अनसुपरव्हाइझ्ड लर्निंग.
- **प्रश्न २: K-Means मध्ये योग्य $K$ कसा निवडतात?**
  - **उत्तर:** **एल्बो पद्धतीद्वारे (Elbow Method)**. वेगवेगळ्या $K$ व्हॅल्यूजसाठी त्रुटींचा (WCSS) आलेख काढला जातो. ज्या ठिकाणी आलेखाचा उतार कोपऱ्यासारखा (Elbow) वाकतो, तो सर्वोत्तम $K$ असतो.
- **प्रश्न ३: डेंड्रोग्राम (Dendrogram) म्हणजे काय?**
  - **उत्तर:** हायराक्रिकल क्लस्टरिंगमधील झाडासारखा आलेख, जो दाखवतो की बिंदू किंवा क्लस्टर्स एकमेकांशी किती अंतरावर एकत्र जोडले गेले आहेत.

### 🔹 प्रॅक्टिकल ८: डायमेंशनॅलिटी रिडक्शन (PCA आणि SVM)
- **प्रश्न १: कर्स ऑफ डायमेंशनॅलिटी (Curse of Dimensionality) म्हणजे काय?**
  - **उत्तर:** जेव्हा कॉलम्सची (वैशिष्ट्यांची) संख्या खूप वाढते, तेव्हा डेटा विरळ होतो, मॉडेल स्लो होते, जास्त मेमरी लागते आणि अचूकता कमी होते. या समस्येला कर्स ऑफ डायमेंशनॅलिटी म्हणतात.
- **प्रश्न २: PCA कसे काम करते?**
  - **उत्तर:** PCA मूळ डेटाचे कोव्हेरियन्स आणि आयगेन-व्हॅल्यूज काढून डेटा अशा अक्षांवर प्रोजेक्ट करतो जिथे जास्तीत जास्त माहिती (Variance) टिकून राहील आणि कॉलमची संख्या कमी होईल.

### 🔹 प्रॅक्टिकल ९: मॉडेल ऑप्टिमायझेशन, एन्सेम्बल लर्निंग आणि ट्युनिंग
- **प्रश्न १: बॅगिंग (Bagging) आणि बूस्टिंग (Boosting) मध्ये काय फरक आहे?**
  - **उत्तर:**
    - **बॅगिंग (उदा. Random Forest):** अनेक डिसिजन ट्री मॉडेल्स स्वतंत्रपणे आणि समांतर चालवले जातात आणि बहुमताने निर्णय घेतला जातो (Overfitting कमी होते).
    - **बूस्टिंग (उदा. AdaBoost):** मॉडेल्स एकामागून एक चालवले जातात आणि पुढील मॉडेल मागील मॉडेलच्या चुका सुधारण्यावर भर देते (Bias कमी होतो).
- **प्रश्न २: GridSearchCV काय करते?**
  - **उत्तर:** ग्रिड सर्च दिलेल्या सर्व पॅरामीटर्सच्या सर्व संभाव्य जोड्या तपासून आणि ५-Fold क्रॉस-व्हॅलिडेशन करून सर्वोत्तम अचूकता देणारी जोडी शोधून काढते.

---

## 📁 फोल्डर रचना (Directory Layout)

```
aiml/
│
├── Practical_01_Smart_Home_Agent.py
├── Practical_02_Route_Planning_BFS_and_DFS.py
├── Practical_03_Rule_Based_Expert_System.py
├── Practical_04_Data_Preprocessing_and_EDA.py
├── Practical_05_Classification_Logistic_and_KNN.py
├── Practical_06_Regression_Linear_and_Polynomial.py
├── Practical_07_Customer_Segmentation_KMeans_and_Hierarchical.py
├── Practical_08_Dimensionality_Reduction_PCA_and_SVM.py
├── Practical_09_Ensemble_Learning_and_Hyperparameter_Tuning.py
│
├── explanations/                                   # प्रॅक्टिकलनुसार कोडचे तुकडे व स्पष्टीकरण
│   ├── README.md
│   ├── Practical_01_Explanation.md
│   ├── Practical_02_Explanation.md
│   ├── Practical_03_Explanation.md
│   ├── Practical_04_Explanation.md
│   ├── Practical_05_Explanation.md
│   ├── Practical_06_Explanation.md
│   ├── Practical_07_Explanation.md
│   ├── Practical_08_Explanation.md
│   └── Practical_09_Explanation.md
│
├── datasets/                                       # लॅपटॉपसाठी डेटासेट्स
│   ├── heart.csv
│   ├── Admission_Predict.csv
│   ├── Housing.csv
│   ├── Mall_Customers.csv
│   ├── wdbc.csv
│   └── breast_cancer.csv
│
├── requirements.txt                                # लायब्ररी आवश्यकता
├── .gitignore
└── README.md                                       # इंग्रजी व मराठी मार्गदर्शिका
```

---

## 👨‍💻 Author
- **Prashil Dalvi** ([@PrashilD15](https://github.com/PrashilD15))
- Amrutvahini College of Engineering, Sangamner (AVCOE)
