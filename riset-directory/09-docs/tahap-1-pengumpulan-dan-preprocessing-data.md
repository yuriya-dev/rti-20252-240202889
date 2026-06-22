# Tahap 1 — Pengumpulan & Preprocessing Data Saham BBRI

**Status:** Selesai

---

## 1. Sumber Data & Parameter
* **Emiten:** PT Bank Rakyat Indonesia (Persero) Tbk (BBRI.JK)
* **Periode:** 2015-01-01 s.d. 2025-12-31
* **Penyedia Data:** Yahoo Finance API (diunduh via library `yfinance`)
* **Fitur Utama:** Open, High, Low, Close, Adj Close, Volume (OHLCV)
* **Jumlah Data:** 2,726 hari perdagangan (baris data)

## 2. Implementasi Preprocessing & Feature Engineering
1. **Handling Missing Values:** Pengecekan menunjukkan data bersih tanpa missing values.
2. **Feature Engineering (Indikator Teknikal):**
   - **Simple Moving Average (SMA_20):** Tren jangka pendek.
   - **Exponential Moving Average (EMA_50):** Tren jangka menengah.
   - **Relative Strength Index (RSI_14):** Indikator momentum jenuh beli/jenuh jual.
   - **Moving Average Convergence Divergence (MACD, Signal, Hist):** Indikator tren dan momentum.
   - **Average True Range (ATR_14):** Indikator volatilitas harga.
   - **Lag Features (Lag_Close_t-1 s.d. Lag_Close_t-60):** 60 hari harga penutupan historis sebagai autoregressive features.
3. **Data Scaling:** Menggunakan `MinMaxScaler` dari Scikit-learn untuk menormalkan semua fitur ke skala `[0, 1]` demi stabilitas pelatihan LSTM.
4. **Data Windowing:** Pembuatan sequence input (window size = 60 hari data historis) untuk memprediksi harga penutupan hari berikutnya ($t+1$).
5. **Data Splitting:** Pembagian dataset secara kronologis:
   - **80% Training Set:** Data dari Januari 2015 hingga Oktober 2023.
   - **20% Testing Set:** Data dari Oktober 2023 hingga Desember 2025.
   - Pembagian dilakukan secara non-shuffled untuk mempertahankan struktur temporal (time-series).

## 3. Hasil & Output yang Dihasilkan
- Berkas dataset saham mentah dan bersih: [`riset-directory/04-data/BBRI.JK_2020-01-01_2025-12-31.csv`](../04-data/BBRI.JK_2020-01-01_2025-12-31.csv) dan [`riset-directory/04-data/bbri_clean.csv`](../04-data/bbri_clean.csv).
- Data scale parameter (`scaler_X_bbri.pkl` dan `scaler_y_bbri.pkl`) tersimpan untuk reverse transform prediksi ke nilai rupiah asli.
- Visualisasi Eksplorasi Data (EDA) dan Indikator Teknikal berhasil di-plot dan disimpan di folder output masing-masing run.
