import pandas as pd
import joblib

MODEL_PATH = "model.joblib"

def load_model():
    return joblib.load(MODEL_PATH)

def predict_one(model, features: dict):
    X = pd.DataFrame([features])
    return model.predict(X)[0]

if __name__ == "__main__":
    # Example usage (edit values to match your dataset columns)
    model = load_model()
    sample = {}
    print("Prediction:", predict_one(model, sample))
