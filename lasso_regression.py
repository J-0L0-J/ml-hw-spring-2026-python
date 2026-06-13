"""
Lasso Regression Solution
Spring 2026 Kaggle Regression Challenge

Model comparison results (CV R²):
  Ridge      alpha=1   : 0.0310
  Lasso      alpha=5   : 0.0316  ← best
  ElasticNet alpha=0.01: 0.0310
  Huber      eps=5.0   : 0.0261
  BayesianRidge        : 0.0303

Why Lasso wins on this dataset:
  - Many of the 15 features have near-zero correlation with the target
  - Lasso performs automatic feature selection by shrinking weak
    feature coefficients exactly to zero
  - Ridge shrinks coefficients but never fully removes them
  - Lasso's L1 penalty is better suited when only a few features
    truly matter
"""

import os
import pandas as pd
import numpy as np
from sklearn.linear_model import Lasso
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import KFold
from sklearn.metrics import r2_score

# 1. Load data
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

train_df = pd.read_csv(os.path.join(BASE_DIR, "spring2026_kaggle_linear_regression_challenge_train.csv"))
test_df  = pd.read_csv(os.path.join(BASE_DIR, "spring2026_kaggle_linear_regression_challenge_test.csv"))

feature_cols = [f"x{i}" for i in range(15)]

X_train_raw = train_df[feature_cols].values
y_train     = train_df["target"].values
X_test_raw  = test_df[feature_cols].values
test_ids    = test_df["Id"].values

# 2. Impute missing values
imputer = SimpleImputer(strategy="mean")
X_train = imputer.fit_transform(X_train_raw)
X_test  = imputer.transform(X_test_raw)

print(f"Original training rows : {len(y_train)}")

# 3. Data cleaning — remove extreme outlier rows
OUTLIER_THRESHOLD = 5000
clean_mask = np.abs(y_train) <= OUTLIER_THRESHOLD

X_train_clean = X_train[clean_mask]
y_train_clean = y_train[clean_mask]

print(f"Rows after cleaning    : {clean_mask.sum()}  "
      f"(removed {(~clean_mask).sum()} rows where |target| > {OUTLIER_THRESHOLD})")

# 4. Cross-validate to select best Lasso alpha
kf = KFold(n_splits=5, shuffle=True, random_state=42)

best_alpha = None
best_cv_r2 = -np.inf

print("\nCross-validation R² — Lasso:")
for alpha in [0.1, 0.5, 1, 1.5, 2, 3, 5, 10]:
    r2s = []
    for tr_idx, val_idx in kf.split(X_train):
        tr_clean = tr_idx[np.abs(y_train[tr_idx]) <= OUTLIER_THRESHOLD]

        scaler = StandardScaler()
        Xtr  = scaler.fit_transform(X_train[tr_clean])
        Xval = scaler.transform(X_train[val_idx])

        model = Lasso(alpha=alpha, max_iter=5000)
        model.fit(Xtr, y_train[tr_clean])
        r2s.append(r2_score(y_train[val_idx], model.predict(Xval)))

    mean_r2 = np.mean(r2s)
    std_r2  = np.std(r2s)
    print(f"  alpha={alpha:>5}  CV R² = {mean_r2:.4f}  (±{std_r2:.4f})")

    if mean_r2 > best_cv_r2:
        best_cv_r2 = mean_r2
        best_alpha = alpha

print(f"\nBest alpha: {best_alpha}  →  best CV R² = {best_cv_r2:.4f}")

# 5. Show which features Lasso kept vs zeroed out
scaler_final   = StandardScaler()
X_clean_scaled = scaler_final.fit_transform(X_train_clean)
X_test_scaled  = scaler_final.transform(X_test)

final_model = Lasso(alpha=best_alpha, max_iter=5000)
final_model.fit(X_clean_scaled, y_train_clean)

print("\nFeature coefficients (Lasso feature selection):")
for i, coef in enumerate(final_model.coef_):
    status = "kept" if coef != 0 else "zeroed out"
    print(f"  x{i:<2}  coef = {coef:>10.4f}   {status}")

kept = np.sum(final_model.coef_ != 0)
print(f"\n  {kept}/15 features kept, {15 - kept} zeroed out by Lasso")

# 6. Evaluate on training data
train_r2 = r2_score(y_train_clean, final_model.predict(X_clean_scaled))
print(f"\nTrain R² on cleaned data: {train_r2:.4f}")

# 7. Predict & save submission
predictions = final_model.predict(X_test_scaled)

submission = pd.DataFrame({"Id": test_ids, "target": predictions})
submission.to_csv(os.path.join(BASE_DIR, "submission_lasso.csv"), index=False)

print(f"\nSubmission saved → submission_lasso.csv  ({len(submission)} rows)")
print(submission.head(10).to_string(index=False))
