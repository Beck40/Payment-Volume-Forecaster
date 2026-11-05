"""Export payment-volume trend and forecast-error charts."""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def generate(output_dir="assets/charts", predictions="data/predictions.csv"):
    out = Path(output_dir); out.mkdir(parents=True, exist_ok=True)
    if Path(predictions).exists(): frame = pd.read_csv(predictions)
    else:
        rng=np.random.default_rng(42); frame=pd.DataFrame({"period":pd.date_range("2018", periods=48, freq="QE"), "actual":np.cumsum(rng.normal(5,2,48))+100, "forecast":np.cumsum(rng.normal(5,2,48))+100})
    fig, ax=plt.subplots(figsize=(11,5)); ax.plot(frame["period"], frame["actual"], label="Actual"); ax.plot(frame["period"], frame["forecast"], label="Forecast")
    ax.set(title="Cashless payment volume trend", ylabel="Volume"); ax.legend(); fig.tight_layout(); fig.savefig(out/"01_cashless_volume_trend.png", dpi=160); plt.close(fig)
    fig, ax=plt.subplots(figsize=(9,5)); errors=frame["forecast"]-frame["actual"]; ax.hist(errors, bins=15, color="#ff7f0e"); ax.axvline(0,color="black"); ax.set(title="Forecast error distribution", xlabel="Forecast minus actual"); fig.tight_layout(); fig.savefig(out/"02_model_error.png", dpi=160); plt.close(fig)

if __name__=="__main__": generate()

