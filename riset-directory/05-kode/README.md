# 05-kode

Source code implementasi — **Tahap 1** (Preprocessing), **Tahap 2** (XGBoost), **Tahap 3** (LSTM), dan **Tahap 4** (Pipeline Evaluasi).

## Struktur yang direncanakan

```
05-kode/
├── data_loader.py       # Pengunduhan dan preprocessing data saham (MinMax scaling, windowing)
├── train_xgboost.py     # Training, hyperparameter tuning, dan penyimpanan model XGBoost
├── train_lstm.py        # Pembuatan arsitektur, training epoch, dan penyimpanan model LSTM
├── evaluate.py          # Perhitungan metrik evaluasi komparatif (RMSE, MAE, R2)
└── visualization.py     # Pembuatan grafik perbandingan harga aktual vs prediksi
```

## Acuan

- Rencana implementasi preprocessing: [../09-docs/tahap-1-pengumpulan-dan-preprocessing-data.md](../09-docs/tahap-1-pengumpulan-dan-preprocessing-data.md)
- Rencana model baseline: [../09-docs/tahap-2-implementasi-baseline-xgboost.md](../09-docs/tahap-2-implementasi-baseline-xgboost.md)
- Rencana model LSTM: [../09-docs/tahap-3-implementasi-lstm.md](../09-docs/tahap-3-implementasi-lstm.md)
