# 🧠 Artificial Intelligence & Machine Learning (AIML) Lab Practicals

[![Python 3](https://img.shields.io/badge/Python-3.x-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Linux](https://img.shields.io/badge/OS-Linux%20%7C%20Ubuntu-E95420?logo=ubuntu&logoColor=white)](https://ubuntu.com/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![GitHub](https://img.shields.io/badge/Repo-PrashilD15%2Faiml-black?logo=github)](https://github.com/PrashilD15/aiml)

---

## 📁 Repository Structure (Practical Folders)

Each practical is organized into its own folder with its Python script and a practical-specific `README.md`:

| Practical | Folder & Script | Dataset | Libraries Needed |
| :---: | :--- | :---: | :--- |
| **01** | [`Practical_01_Intelligent_Agent/practical_01.py`](Practical_01_Intelligent_Agent/practical_01.py) | Interactive Input | Built-in (`datetime`) — **No pip needed** |
| **02** | [`Practical_02_BFS_and_DFS_Route_Planning/practical_02.py`](Practical_02_BFS_and_DFS_Route_Planning/practical_02.py) | Built-in Graph | Built-in (`collections`, `time`) — **No pip needed** |
| **03** | [`Practical_03_Rule_Based_Expert_System/practical_03.py`](Practical_03_Rule_Based_Expert_System/practical_03.py) | Built-in Rules | Built-in — **No pip needed** |
| **04** | [`Practical_04_Data_Preprocessing_and_EDA/practical_04.py`](Practical_04_Data_Preprocessing_and_EDA/practical_04.py) | `heart.csv` | `pandas`, `matplotlib`, `seaborn`, `numpy`, `scikit-learn` |
| **05** | [`Practical_05_Classification_Logistic_Regression_and_KNN/practical_05.py`](Practical_05_Classification_Logistic_Regression_and_KNN/practical_05.py) | `heart.csv` | `pandas`, `matplotlib`, `scikit-learn` |
| **06** | [`Practical_06_Linear_and_Polynomial_Regression/practical_06.py`](Practical_06_Linear_and_Polynomial_Regression/practical_06.py) | California Housing (`sklearn`) | `pandas`, `matplotlib`, `scikit-learn` |
| **07** | [`Practical_07_Clustering_KMeans_and_Hierarchical/practical_07.py`](Practical_07_Clustering_KMeans_and_Hierarchical/practical_07.py) | `Mall_Customers.csv` | `pandas`, `matplotlib`, `scikit-learn`, `scipy` |
| **08** | [`Practical_08_PCA_Dimensionality_Reduction/practical_08.py`](Practical_08_PCA_Dimensionality_Reduction/practical_08.py) | Breast Cancer (`sklearn`) | `numpy`, `matplotlib`, `scikit-learn` |
| **09** | [`Practical_09_Hyperparameter_Tuning_and_Ensemble_Models/practical_09.py`](Practical_09_Hyperparameter_Tuning_and_Ensemble_Models/practical_09.py) | Breast Cancer (`sklearn`) | `pandas`, `numpy`, `scikit-learn` |

> **Dataset Path Auto-Detection:** CSV-based practicals (4, 5, 7) automatically search for the dataset in:
> 1. Current practical folder (`./<file>.csv`)
> 2. Repository `datasets/` folder (`../datasets/<file>.csv`)
> 3. Lab PC path (`/home/avcoe/<file>.csv`)
>
> So they will run cleanly on both college Ubuntu lab PCs and personal laptops without `FileNotFoundError`.

---

## 🐧 Ubuntu Linux Setup (For College Lab Computers)

### Step 1: Clone the Repository
```bash
git clone https://github.com/PrashilD15/aiml.git
cd aiml
```

### Step 2: What if `pip` is NOT installed in Python?
If running `python3 -m pip --version` gives `No module named pip`, install `pip` (and `venv` + `tk` for matplotlib plots) via `apt`:
```bash
sudo apt update && sudo apt install -y python3-pip python3-venv python3-tk
```

### Step 3: Install All Libraries at Once (Recommended)
Using a virtual environment works on **every Ubuntu version** (including Ubuntu 24.04 where system `pip install` is blocked by PEP 668):
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

*(Alternative without `venv`: on Ubuntu 20.04/22.04 run `python3 -m pip install --user -r requirements.txt`; on Ubuntu 24.04+ run `python3 -m pip install --break-system-packages -r requirements.txt`.)*

---

## 🚀 Practical-Wise Linux Execution & `pip` Install Commands

### Practical 1: Intelligent Agents (Chatbot, Recommendation Assistant, Smart Home Controller)
No external libraries needed.
```bash
cd Practical_01_Intelligent_Agent
python3 practical_01.py
```

### Practical 2: Route Planning using BFS and DFS
No external libraries needed.
```bash
cd Practical_02_BFS_and_DFS_Route_Planning
python3 practical_02.py
```

### Practical 3: Rule-Based Expert System (Forward & Backward Chaining)
No external libraries needed.
```bash
cd Practical_03_Rule_Based_Expert_System
python3 practical_03.py
```

### Practical 4: Data Preprocessing and EDA (`heart.csv`)
```bash
# Install libraries (if not already installed)
python3 -m pip install --user pandas matplotlib seaborn numpy scikit-learn

# Run
cd Practical_04_Data_Preprocessing_and_EDA
python3 practical_04.py
```

### Practical 5: Classification using Logistic Regression & KNN (`heart.csv`)
```bash
# Install libraries (if not already installed)
python3 -m pip install --user pandas matplotlib scikit-learn

# Run
cd Practical_05_Classification_Logistic_Regression_and_KNN
python3 practical_05.py
```

### Practical 6: Linear Regression & Polynomial Regression (California Housing)
```bash
# Install libraries (if not already installed)
python3 -m pip install --user pandas matplotlib scikit-learn

# Run
cd Practical_06_Linear_and_Polynomial_Regression
python3 practical_06.py
```

### Practical 7: Clustering Techniques (K-Means & Hierarchical Clustering)
```bash
# Install libraries (if not already installed)
python3 -m pip install --user pandas matplotlib scikit-learn scipy

# Run
cd Practical_07_Clustering_KMeans_and_Hierarchical
python3 practical_07.py
```

### Practical 8: Dimensionality Reduction using PCA
```bash
# Install libraries (if not already installed)
python3 -m pip install --user numpy matplotlib scikit-learn

# Run
cd Practical_08_PCA_Dimensionality_Reduction
python3 practical_08.py
```

### Practical 9: Hyperparameter Tuning & Ensemble Models (SVM, Random Forest, AdaBoost)
```bash
# Install libraries (if not already installed)
python3 -m pip install --user pandas numpy scikit-learn

# Run
cd Practical_09_Hyperparameter_Tuning_and_Ensemble_Models
python3 practical_09.py
```

> **Tip for Ubuntu 24.04+:** If `python3 -m pip install --user ...` says `error: externally-managed-environment`, either activate the `venv` (`source venv/bin/activate` and run `pip install ...`) or add `--break-system-packages` to the `pip install` command.
