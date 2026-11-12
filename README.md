# Payment Volume Forecaster

## Objective

Cashless-payment volume forecasts help banks, acquirers and payment-service providers plan capacity, liquidity and customer-support operations. This project reconciles hierarchical payment observations into an auditable forecasting workflow that separates recurring seasonality from structural growth and highlights channel-level performance.

## Architecture

```text
Payment-Volume-Forecaster/
├── assets/
│   └── charts/                         # Trend and forecast-error visuals
├── data/
│   └── BIS_CPMI_CASHLESS_csv_flat.csv
├── notebooks/
│   └── Payment_forecasting.ipynb
├── src/
│   ├── data_pipeline.py                # BIS payment-data ingestion
│   ├── features.py                     # Seasonal lags and rolling baselines
│   ├── train.py                        # Time-ordered model training
│   ├── predict.py                      # Forecast generation
│   └── generate_charts.py              # Monitoring charts
└── tests/
```

## Quickstart

```bash
pip install -r requirements.txt
python -c "from src.data_pipeline import load_payments; from src.features import build_features; from src.train import train; train(build_features(load_payments('data/BIS_CPMI_CASHLESS_csv_flat.csv')))"
python -m src.generate_charts
```

![Probabilistic cashless payment volume forecast](assets/charts/01_cashless_volume_trend.png)

The fan chart connects the last observed payment volume to the forecast median and separates structural growth from seasonal movement with P10–P90 and P25–P75 prediction intervals.

![Forecast horizon degradation and backtest error](assets/charts/02_model_error.png)

The horizon-error chart compares the Hierarchical Ensemble with a Naive Seasonal Baseline across MAPE and RMSE, making degradation and model-governance trade-offs visible.
