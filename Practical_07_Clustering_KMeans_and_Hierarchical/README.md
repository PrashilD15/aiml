# Practical 7: Clustering Techniques (K-Means & Hierarchical Clustering)

## Required Libraries
- `pandas`
- `matplotlib`
- `scikit-learn`
- `scipy`

## Ubuntu Linux Setup & Execution

### 1. If `pip` is NOT installed on Ubuntu
```bash
sudo apt update && sudo apt install -y python3-pip python3-venv python3-tk
```

### 2. Install Required Libraries using `pip`
**Option A (Recommended — works on all Ubuntu versions including 24.04):**
```bash
python3 -m venv venv
source venv/bin/activate
pip install pandas matplotlib scikit-learn scipy
```

**Option B (Direct user install on Ubuntu 20.04/22.04):**
```bash
python3 -m pip install --user pandas matplotlib scikit-learn scipy
```
*(On Ubuntu 24.04+, if not using `venv`, add `--break-system-packages`: `python3 -m pip install --break-system-packages pandas matplotlib scikit-learn scipy`)*

### 3. Execute Practical
```bash
cd Practical_07_Clustering_KMeans_and_Hierarchical
python3 practical_07.py
```
