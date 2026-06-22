# 06-output

Hasil olahan data, model biner, dan visualisasi dari pengujian model LSTM, XGBoost, dan Hybrid Stacking saham BBRI.

## Struktur Direktori

Dihasilkan secara otomatis oleh `05-kode/run_all_experiments.py` per seed acak (Run 1 s.d. Run 10).

```text
06-output/
├── README.md
├── run-1/
│   ├── 01_eda_bbri.png
│   ├── ...
│   ├── 08_rolling_mae.png
│   ├── BBRI_Stock_Prediction_executed.ipynb
│   ├── hasil_metrik_komparasi.csv
│   ├── hasil_uji_statistik.csv
│   ├── hasil_prediksi_lengkap.csv
│   ├── lstm_best_model.keras
│   ├── model_lstm_bbri.keras
│   ├── model_xgboost_baseline_bbri.pkl
│   ├── model_xgboost_hybrid_bbri.pkl
│   ├── scaler_X_bbri.pkl
│   └── scaler_y_bbri.pkl
└── run-2/ s.d. run-10/ (memiliki struktur file yang identik)
```

## Daftar File Output Per Run

Setiap folder `run-X` berisi **18 file** hasil eksekusi:

### 1. Visualisasi (`01_*.png` s.d. `08_*.png`)
- `01_eda_bbri.png`: Eksplorasi data historis harga penutupan, return harian, dan volume BBRI.
- `02_technical_indicators.png`: Visualisasi indikator Bollinger Bands, MACD, RSI, dan ATR.
- `03_lstm_training.png`: Grafik riwayat loss training vs validation untuk model LSTM.
- `04_xgb_feature_importance.png`: Peringkat kontribusi fitur teknikal dan fitur lag pada model XGBoost.
- `05_prediksi_vs_aktual.png`: Komparasi visual pergerakan harga aktual vs prediksi ketiga model pada test set.
- `06_komparasi_metrik.png`: Diagram batang perbandingan metrik MAE, RMSE, R², dan MAPE untuk ketiga model.
- `07_analisis_residual.png`: Histogram distribusi residual error dan scatter plot aktual vs prediksi.
- `08_rolling_mae.png`: Visualisasi ketahanan model sepanjang waktu menggunakan MAE rolling window 60 hari.

### 2. Tabel Hasil Eksperimen (.csv)
- `hasil_metrik_komparasi.csv`: Nilai MAE, RMSE, R², dan MAPE untuk LSTM, XGBoost, dan Hybrid.
- `hasil_uji_statistik.csv`: Hasil uji Wilcoxon Signed-Rank Test untuk pembuktian signifikansi statistik (p-value).
- `hasil_prediksi_lengkap.csv`: Log data harian test set berisi harga aktual, hasil prediksi, dan residual error masing-masing model.

### 3. Model Biner (.keras, .pkl)
- `model_lstm_bbri.keras` & `lstm_best_model.keras`: Bobot model neural network LSTM.
- `model_xgboost_baseline_bbri.pkl`: Model machine learning XGBoost Baseline.
- `model_xgboost_hybrid_bbri.pkl`: Model XGBoost Meta-Learner Hybrid Stacking.
- `scaler_X_bbri.pkl` & `scaler_y_bbri.pkl`: Scaler fitur input dan target untuk preprocessing.

### 4. Salinan Eksperimen (.ipynb)
- `BBRI_Stock_Prediction_executed.ipynb`: Notebook Jupyter lengkap dengan grafik dan stdout hasil eksekusi run terkait.
