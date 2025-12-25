import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score, f1_score, classification_report
from sklearn.ensemble import RandomForestClassifier
import joblib

TARGET = "Loan_Status"  # change if your target column differs

def build_pipeline(X: pd.DataFrame) -> Pipeline:
    num_cols = X.select_dtypes(include=["int64", "float64"]).columns.tolist()
    cat_cols = X.select_dtypes(include=["object", "category", "bool"]).columns.tolist()

    numeric_pipe = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="median")),
    ])

    categorical_pipe = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore")),
    ])

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_pipe, num_cols),
            ("cat", categorical_pipe, cat_cols),
        ]
    )

    model = RandomForestClassifier(
        n_estimators=300,
        random_state=42,
        class_weight="balanced"
    )

    return Pipeline(steps=[("preprocessor", preprocessor), ("model", model)])

def main():
    df = pd.read_csv("data/loan_train.csv").drop_duplicates()

    # Guard: ensure target exists and is not missing
    if TARGET not in df.columns:
        raise ValueError(f"Target column '{TARGET}' not found. Available columns: {list(df.columns)}")

    df = df.dropna(subset=[TARGET])

    X = df.drop(columns=[TARGET])
    y = df[TARGET]

    X_train, X_val, y_train, y_val = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    pipe = build_pipeline(X_train)
    pipe.fit(X_train, y_train)

    preds = pipe.predict(X_val)
    acc = accuracy_score(y_val, preds)
    f1 = f1_score(y_val, preds, average="weighted")

    print("Accuracy:", round(acc, 4))
    print("F1 (weighted):", round(f1, 4))
    print("\nClassification Report:\n", classification_report(y_val, preds))

    joblib.dump(pipe, "model.joblib")
    print("\nSaved model to model.joblib")

if __name__ == "__main__":
    main()
