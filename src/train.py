"""Train a transparent baseline payment-volume forecaster."""
from pathlib import Path
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error


def train(frame, output="data/model.pkl"):
    x = frame.drop(columns="volume"); y = frame["volume"]
    split = int(len(frame) * .8); model = RandomForestRegressor(n_estimators=250, random_state=42, n_jobs=-1)
    model.fit(x.iloc[:split], y.iloc[:split])
    print(f"holdout MAE: {mean_absolute_error(y.iloc[split:], model.predict(x.iloc[split:])):.2f}")
    Path(output).parent.mkdir(parents=True, exist_ok=True); joblib.dump({"model": model, "features": list(x.columns)}, output)
    return model

