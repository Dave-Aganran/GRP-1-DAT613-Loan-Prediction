import pandas as pd
import joblib
import gradio as gr

MODEL_PATH = "model.joblib"
TRAIN_PATH = "data/loan_train.csv"
TARGET = "Loan_Status"  # change if needed

model = joblib.load(MODEL_PATH)

# Build input schema from training file columns
df = pd.read_csv(TRAIN_PATH)
if TARGET in df.columns:
    df = df.drop(columns=[TARGET])

def predict_from_inputs(*values):
    input_dict = dict(zip(df.columns, values))
    X = pd.DataFrame([input_dict])
    prediction = model.predict(X)[0]
    return str(prediction)

inputs = []
for col in df.columns:
    if pd.api.types.is_numeric_dtype(df[col]):
        inputs.append(gr.Number(label=col))
    else:
        choices = sorted(df[col].dropna().astype(str).unique().tolist())
        inputs.append(gr.Dropdown(choices=choices, label=col))

demo = gr.Interface(
    fn=predict_from_inputs,
    inputs=inputs,
    outputs=gr.Textbox(label="Prediction"),
    title="Loan Approval Prediction (Random Forest)",
    description="Enter applicant details to predict loan approval status."
)

#demo.launch()

if __name__ == "__main__":
    demo.launch()
