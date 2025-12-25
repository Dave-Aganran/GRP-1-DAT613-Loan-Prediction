# DAT613 Loan Approval Prediction (Random Forest) – Group Project

This repository contains the full workflow for the DAT613 group project:
- Data preparation and EDA (with at least one visualization)
- Model training using a supervised ML model (Random Forest)
- Model evaluation using Accuracy and F1-score
- Deployment to Hugging Face Spaces using a Gradio UI
- Git & GitHub workflow documentation for collaboration

## Project Structure
```
DAT613-Loan-Prediction/
├─ data/
│  ├─ loan_train.csv
│  └─ loan_test.csv
├─ notebooks/
│  └─ 01_DAT613_Loan_Prediction.ipynb
├─ src/
│  ├─ train.py
│  ├─ predict.py
│  └─ utils.py
├─ app.py
├─ requirements.txt
└─ model.joblib (generated after training)
```

## How to Run Locally

1) Create a virtual environment and install dependencies:
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
```

2) Train the model (creates `model.joblib`):
```bash
python src/train.py
```

3) Run the Gradio app:
```bash
python app.py
```

## Hugging Face Spaces Deployment (Gradio)

1) Create a Hugging Face account.
2) Go to **Spaces → Create new Space**.
   - Space SDK: **Gradio**
   - Hardware: default (CPU)
3) Upload (or push) these files to the Space repo root:
   - `app.py`
   - `requirements.txt`
   - `model.joblib`
   - `data/loan_train.csv` (used to build the UI inputs)
4) Wait for build to complete, then test the UI.
5) Copy the Space URL and take a screenshot for the report.

## Recommended GitHub Collaboration Workflow (for your report)

- Use `main` as the stable branch, `dev` as integration.
- Each member works on a feature branch (e.g., `feature-eda`, `feature-training`, `feature-deployment`, `feature-report`).
- Use Pull Requests to merge feature branches into `dev`, then merge `dev` into `main`.
- Make frequent commits with meaningful messages (not a single “final commit”).

## Notes
- If your target column name differs from `Loan_Status`, update `TARGET` in `src/train.py` and `app.py`.
