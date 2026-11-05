"""Load and standardise BIS cashless payment observations."""
from pathlib import Path
import pandas as pd


def load_payments(path: str | Path) -> pd.DataFrame:
    frame = pd.read_csv(path)
    frame.columns = [str(c).strip().lower().replace(" ", "_") for c in frame.columns]
    date = next((c for c in frame.columns if "year" in c or "date" in c), frame.columns[0])
    frame["period"] = pd.to_datetime(frame[date].astype(str), errors="coerce")
    value = next((c for c in frame.columns if "volume" in c or "number" in c or "value" in c), frame.columns[-1])
    frame["volume"] = pd.to_numeric(frame[value], errors="coerce")
    return frame.dropna(subset=["period", "volume"]).sort_values("period")

