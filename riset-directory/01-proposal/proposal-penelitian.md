# Proposal Penelitian

**Judul:** Analisis Komparatif Performa Long Short-Term Memory (LSTM) dan eXtreme Gradient Boosting (XGBoost) dalam Prediksi Harga Saham BBRI (2015-2025)

---

## 1. Pendahuluan
*(Tulis Latar Belakang di sini. Bahas mengenai pentingnya prediksi harga saham, volatilitas pasar modal Indonesia, khususnya saham blue-chip BBRI, serta keterbatasan metode statistik konvensional).*

## 2. Rumusan Masalah
1. Apakah model deep learning Long Short-Term Memory (LSTM) secara konsisten menghasilkan tingkat kesalahan prediksi (RMSE dan MAE) yang lebih rendah dibandingkan model ensemble eXtreme Gradient Boosting (XGBoost) pada data saham BBRI periode 2015-2025?
2. Bagaimana perbandingan goodness-of-fit (R2 Score) antara model LSTM dan XGBoost dalam menjelaskan variansi pergerakan harga saham BBRI?

## 3. Tujuan Penelitian
1. Mengimplementasikan model LSTM dan XGBoost untuk memprediksi harga saham BBRI.
2. Mengevaluasi secara komparatif performa kedua model menggunakan metrik RMSE, MAE, dan R2 Score.
3. Menyediakan rekomendasi empiris mengenai pemilihan arsitektur machine learning yang paling optimal untuk prediksi saham lokal yang volatil.

## 4. Tinjauan Pustaka & Gap Penelitian
*(Bahas penelitian terdahulu yang menggunakan LSTM dan XGBoost untuk data time series saham, serta identifikasi gap riset terkait komparasi komprehensif pada saham spesifik berkapitalisasi besar seperti BBRI dalam rentang waktu jangka panjang).*

## 5. Metodologi Penelitian
### 5.1 Pengumpulan Data
Data historis harian saham BBRI periode 2015-2025 diperoleh dari Yahoo Finance / Investing.com.

### 5.2 Preprocessing Data
* Normalisasi data menggunakan MinMax Scaler.
* Pembuatan data sekuensial (sliding window).
* Pembagian data kronologis (80% training, 20% testing).

### 5.3 Implementasi Model
* **Model Baseline:** XGBoost Regressor dengan optimasi hyperparameter.
* **Model Eksperimental:** LSTM Neural Network dengan beberapa layer tersembunyi dan dropout layer.

### 5.4 Metrik Evaluasi
Kinerja model diukur menggunakan Root Mean Squared Error (RMSE), Mean Absolute Error (MAE), dan R-squared (R2).
