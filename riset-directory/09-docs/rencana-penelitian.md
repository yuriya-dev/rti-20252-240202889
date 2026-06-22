# Rencana Penelitian: Prediksi Harga Saham BBRI Menggunakan LSTM vs XGBoost

## 1. Ringkasan

| Item | Keterangan |
|---|---|
| Judul | Analisis Komparatif Performa Long Short-Term Memory (LSTM), eXtreme Gradient Boosting (XGBoost), dan Hybrid Stacking dalam Prediksi Harga Saham BBRI (2015-2025) |
| Target Publikasi | Jurnal Riset Teknologi Informasi / Jurnal Ilmiah Sinta 2/3 |
| Stack | Python, TensorFlow/Keras, XGBoost, Pandas, NumPy, Scikit-learn, Yahoo Finance API |
| Masalah | Fluktuasi harga saham BBRI tidak linear, volatil, dan dipengaruhi oleh structural breaks (seperti pandemi COVID-19) sehingga sulit dimodelkan secara akurat oleh model deep learning murni tanpa overfitting. |
| Solusi | Komparasi model deep learning (LSTM), ensemble learning (XGBoost), dan arsitektur Hybrid Stacking untuk meminimalkan error prediksi (RMSE, MAE, R², MAPE) secara konsisten di seluruh 10 run terkontrol. |
| Setup Lingkungan | [setup-eksperimen.md](setup-eksperimen.md) |

## 2. Alur Kerja (Roadmap)

Seluruh tahapan penelitian telah berhasil diselesaikan dengan baik:

- [x] **Tahap 1** — [Pengumpulan & Preprocessing Data Saham BBRI](tahap-1-pengumpulan-dan-preprocessing-data.md) — *Selesai*
- [x] **Tahap 2** — [Implementasi Baseline XGBoost](tahap-2-implementasi-baseline-xgboost.md) — *Selesai*
- [x] **Tahap 3** — [Implementasi Model LSTM](tahap-3-implementasi-lstm.md) — *Selesai*
- [x] **Tahap 4** — [Eksperimen & Evaluasi Kinerja](tahap-4-eksperimen-dan-evaluasi.md) — *Selesai*
- [x] **Tahap 5** — [Draf Paper Jurnal](tahap-5-draf-paper.md) — *Selesai*

---

## 3. Catatan

Eksperimen ini dijalankan secara terotomatisasi sebanyak 10 kali menggunakan seed acak dinamis (`43` s.d. `52`) untuk menjamin reliabilitas statistik. Seluruh metrik, visualisasi plot, dan model biner disimpan secara terstruktur di folder [`06-output/`](../06-output/).
