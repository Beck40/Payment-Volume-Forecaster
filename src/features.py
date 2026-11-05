"""Time-series features for payment volume forecasting."""
import pandas as pd


def build_features(frame: pd.DataFrame, lags=(1, 4, 12)) -> pd.DataFrame:
    result = frame.copy().set_index("period")
    for lag in lags:
        result[f"lag_{lag}"] = result["volume"].shift(lag)
    result["rolling_mean_4"] = result["volume"].rolling(4).mean()
    return result.dropna()

