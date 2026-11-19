# Practical 6: Linear Regression & Polynomial Regression (California Housing Dataset)

## Required Libraries
- `pandas`
- `matplotlib`
- `scikit-learn`

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
pip install pandas matplotlib scikit-learn
```

**Option B (Direct user install on Ubuntu 20.04/22.04):**
```bash
python3 -m pip install --user pandas matplotlib scikit-learn
```
*(On Ubuntu 24.04+, if not using `venv`, add `--break-system-packages`: `python3 -m pip install --break-system-packages pandas matplotlib scikit-learn`)*

### 3. Execute Practical
```bash
cd Practical_06_Linear_and_Polynomial_Regression
python3 practical_06.py
```

> **Note:** On the first run, `fetch_california_housing` downloads the dataset (~400 KB) and caches it in `~/scikit_learn_data`. The script also saves `regression_results.csv` and `regression_comparison.png` in the current directory.
