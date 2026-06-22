# 06-output

Hasil olahan data & visualisasi — **Tahap 4** (lihat [../09-docs/tahap-4-eksperimen-dan-evaluasi.md](../09-docs/tahap-4-eksperimen-dan-evaluasi.md)).

Dihasilkan oleh `05-kode/evaluate.py` dan `05-kode/visualization.py` setelah pengujian model LSTM vs XGBoost pada data testing.

## tables/

| File | Isi |
|---|---|
| `model_comparison.csv` | Perbandingan nilai metrik RMSE, MAE, dan R2 Score untuk model XGBoost dan LSTM |
| `hyperparameter_log.csv` | Catatan parameter terbaik dari pencarian grid search / random search |

## figures/

| File | Isi |
|---|---|
| `prediction_vs_actual.png` | Grafik garis komparatif harga aktual saham BBRI vs prediksi LSTM vs prediksi XGBoost |
| `residual_analysis.png` | Plot sebaran residu/error dari masing-masing model untuk menguji bias model |
| `training_loss.png` | Grafik pergerakan loss (MSE) model LSTM pada training set vs validation set selama epoch |

## Acuan

[../09-docs/tahap-4-eksperimen-dan-evaluasi.md](../09-docs/tahap-4-eksperimen-dan-evaluasi.md)
