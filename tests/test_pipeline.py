import pandas as pd

from src.data_pipeline import load_payments
from src.features import build_features


def test_payment_loader_coerces_invalid_rows(tmp_path):
    path = tmp_path / "payments.csv"
    pd.DataFrame({"Year": ["2020", "bad"], "Volume": ["10", "x"]}).to_csv(path, index=False)
    loaded = load_payments(path)
    assert len(loaded) == 1
    assert not build_features(
        pd.DataFrame({"period": pd.date_range("2020", periods=16, freq="QE"), "volume": range(16)})
    ).empty
