from pathlib import Path

def project_root() -> Path:
    # Adjust if needed
    return Path(__file__).resolve().parents[1]
