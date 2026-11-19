# ============================================================
# Practical 9: Model Optimization, Ensemble Learning & GridSearchCV
# ============================================================

# 1. Import required libraries
import pandas as pd
import numpy as np

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import (
    train_test_split,
    cross_val_score,
    GridSearchCV,
    StratifiedKFold
)

from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)

# 2. Load Dataset
data = load_breast_cancer()

X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target, name="target")

print("Dataset Shape:", X.shape)
print("\nFirst 5 rows:")
print(X.head())

print("\nClass Names:")
print(data.target_names)

# 3. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining data:", X_train.shape)
print("Testing data:", X_test.shape)

# 4. Define Models

# SVM with StandardScaler
svm_model = Pipeline([
    ("scaler", StandardScaler()),
    ("model", SVC(kernel="rbf", C=1.0, gamma="scale"))
])

# Random Forest
rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# AdaBoost
ada_model = AdaBoostClassifier(
    n_estimators=50,
    learning_rate=1.0,
    random_state=42
)

models = {
    "SVM": svm_model,
    "Random Forest": rf_model,
    "AdaBoost": ada_model
}

# 5. Train Models and Evaluate BEFORE Optimization
results_before = []

print("\n" + "=" * 60)
print("PERFORMANCE BEFORE HYPERPARAMETER TUNING")
print("=" * 60)

for name, model in models.items():

    # Train
    model.fit(X_train, y_train)

    # Prediction
    y_pred = model.predict(X_test)

    # Metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    results_before.append({
        "Model": name,
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall,
        "F1 Score": f1
    })

    print("\n", name)
    print("-" * 40)
    print("Accuracy :", round(accuracy, 4))
    print("Precision:", round(precision, 4))
    print("Recall   :", round(recall, 4))
    print("F1 Score :", round(f1, 4))

# 6. Cross Validation
print("\n" + "=" * 60)
print("5-FOLD CROSS VALIDATION")
print("=" * 60)

cv = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

cv_results = []

for name, model in models.items():

    scores = cross_val_score(
        model,
        X,
        y,
        cv=cv,
        scoring="accuracy"
    )

    cv_results.append({
        "Model": name,
        "Mean CV Accuracy": scores.mean(),
        "Std": scores.std()
    })

    print("\n", name)
    print("Fold Scores:", np.round(scores, 4))
    print("Mean Accuracy:", round(scores.mean(), 4))
    print("Standard Deviation:", round(scores.std(), 4))

# 7. Hyperparameter Tuning using Grid Search
print("\n" + "=" * 60)
print("GRID SEARCH HYPERPARAMETER TUNING")
print("=" * 60)

# SVM Parameter Grid
svm_pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", SVC())
])

svm_params = {
    "model__C": [0.1, 1, 10, 100],
    "model__gamma": ["scale", 0.01, 0.001],
    "model__kernel": ["rbf", "linear"]
}

svm_grid = GridSearchCV(
    svm_pipeline,
    svm_params,
    cv=5,
    scoring="accuracy",
    n_jobs=-1
)

svm_grid.fit(X_train, y_train)

print("\nBest SVM Parameters:")
print(svm_grid.best_params_)
print("Best SVM CV Score:", round(svm_grid.best_score_, 4))

# Random Forest Parameter Grid
rf_params = {
    "n_estimators": [50, 100, 200],
    "max_depth": [None, 5, 10, 20],
    "min_samples_split": [2, 5],
    "min_samples_leaf": [1, 2]
}

rf_grid = GridSearchCV(
    RandomForestClassifier(random_state=42),
    rf_params,
    cv=5,
    scoring="accuracy",
    n_jobs=-1
)

rf_grid.fit(X_train, y_train)

print("\nBest Random Forest Parameters:")
print(rf_grid.best_params_)
print("Best Random Forest CV Score:", round(rf_grid.best_score_, 4))

# AdaBoost Parameter Grid
ada_params = {
    "n_estimators": [50, 100, 200],
    "learning_rate": [0.01, 0.1, 0.5, 1.0]
}

ada_grid = GridSearchCV(
    AdaBoostClassifier(random_state=42),
    ada_params,
    cv=5,
    scoring="accuracy",
    n_jobs=-1
)

ada_grid.fit(X_train, y_train)

print("\nBest AdaBoost Parameters:")
print(ada_grid.best_params_)
print("Best AdaBoost CV Score:", round(ada_grid.best_score_, 4))

# 8. Evaluate Optimized Models
optimized_models = {
    "SVM": svm_grid.best_estimator_,
    "Random Forest": rf_grid.best_estimator_,
    "AdaBoost": ada_grid.best_estimator_
}

results_after = []

print("\n" + "=" * 60)
print("PERFORMANCE AFTER HYPERPARAMETER TUNING")
print("=" * 60)

for name, model in optimized_models.items():

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    results_after.append({
        "Model": name,
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall,
        "F1 Score": f1
    })

    print("\n", name)
    print("-" * 40)
    print("Accuracy :", round(accuracy, 4))
    print("Precision:", round(precision, 4))
    print("Recall   :", round(recall, 4))
    print("F1 Score :", round(f1, 4))

    print("\nClassification Report:")
    print(classification_report(
        y_test,
        y_pred,
        target_names=data.target_names
    ))

    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

# 9. Compare BEFORE and AFTER Optimization
before_df = pd.DataFrame(results_before)
after_df = pd.DataFrame(results_after)

print("\n" + "=" * 60)
print("COMPARISON: BEFORE vs AFTER OPTIMIZATION")
print("=" * 60)

comparison = before_df.copy()
comparison["Accuracy After"] = after_df["Accuracy"]
comparison["Precision After"] = after_df["Precision"]
comparison["Recall After"] = after_df["Recall"]
comparison["F1 Score After"] = after_df["F1 Score"]

print("\n")
print(comparison.to_string(index=False))

# 10. Calculate Improvement
print("\n" + "=" * 60)
print("IMPROVEMENT AFTER OPTIMIZATION")
print("=" * 60)

for i in range(len(before_df)):
    model_name = before_df.loc[i, "Model"]
    acc_before = before_df.loc[i, "Accuracy"]
    acc_after = after_df.loc[i, "Accuracy"]
    improvement = (acc_after - acc_before) * 100

    print(
        f"{model_name}: "
        f"{acc_before:.4f} -> {acc_after:.4f} "
        f"({improvement:+.2f}%)"
    )

# 11. Final Model Comparison
final_comparison = pd.DataFrame({
    "Model": before_df["Model"],
    "Before Accuracy": before_df["Accuracy"],
    "After Accuracy": after_df["Accuracy"],
    "Before Precision": before_df["Precision"],
    "After Precision": after_df["Precision"],
    "Before Recall": before_df["Recall"],
    "After Recall": after_df["Recall"],
    "Before F1": before_df["F1 Score"],
    "After F1": after_df["F1 Score"]
})

print("\nFinal Comparison Table:")
print(final_comparison.round(4).to_string(index=False))

# 12. Find Best Model
best_index = after_df["Accuracy"].idxmax()
best_model = after_df.loc[best_index, "Model"]
best_accuracy = after_df.loc[best_index, "Accuracy"]

print("\n" + "=" * 60)
print("BEST MODEL")
print("=" * 60)
print("Best Model:", best_model)
print("Test Accuracy:", round(best_accuracy, 4))
