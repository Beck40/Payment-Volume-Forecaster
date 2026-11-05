"""Generate payment-volume forecasts from a saved model."""
import joblib


def predict(frame, model_path="data/model.pkl"):
    bundle = joblib.load(model_path)
    return bundle["model"].predict(frame[bundle["features"]])

