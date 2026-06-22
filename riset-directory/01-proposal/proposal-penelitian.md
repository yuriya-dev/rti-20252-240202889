# Proposal Penelitian: Analisis Komparatif Model LSTM, XGBoost, dan Hybrid Stacking dalam Prediksi Harga Saham BBRI (2015-2025)

---

## 1. Pendahuluan
Pasar modal merupakan salah satu indikator penting dari kesehatan perekonomian suatu negara. Di Indonesia, saham PT Bank Rakyat Indonesia (Persero) Tbk (BBRI) merupakan salah satu saham berkapitalisasi besar (blue-chip) yang sangat aktif diperdagangkan di Bursa Efek Indonesia (BEI) dan masuk dalam indeks LQ45. Namun, pergerakan harga saham BBRI bersifat non-linear, non-stasioner, dan volatil karena dipengaruhi oleh berbagai faktor eksternal makroekonomi, kebijakan moneter, sentimen pasar, hingga peristiwa global seperti Pandemi COVID-19.

Metode statistik konvensional seperti ARIMA sering kali gagal menangkap dinamika non-linearitas dan volatilitas tinggi pada data time series keuangan. Seiring perkembangan teknologi kecerdasan buatan, model pembelajaran mesin (machine learning) seperti XGBoost dan pembelajaran mendalam (deep learning) seperti Long Short-Term Memory (LSTM) banyak diterapkan untuk memprediksi harga saham. Model XGBoost tangguh dalam menangani data tabular terstruktur dengan fitur lag, sementara LSTM sangat baik dalam menangani ketergantungan temporal jangka panjang. Penelitian ini mengusulkan analisis komparatif performa model LSTM, XGBoost, dan Hybrid Stacking (menggabungkan keluaran LSTM dan fitur teknikal ke dalam XGBoost) untuk menentukan metode yang paling optimal dan stabil dalam memprediksi harga saham BBRI dari tahun 2015 hingga 2025.

## 2. Rumusan Masalah
1. Apakah model deep learning LSTM secara konsisten menghasilkan kesalahan prediksi (RMSE, MAE, MAPE) yang lebih rendah dibandingkan model ensemble XGBoost dan model Hybrid Stacking pada data saham BBRI?
2. Bagaimana perbandingan nilai goodness-of-fit ($R^2$ Score) ketiga model dalam menjelaskan variansi pergerakan harga saham BBRI?
3. Apakah perbedaan performa antara ketiga model tersebut signifikan secara statistik berdasarkan pengujian Wilcoxon Signed-Rank Test?

## 3. Tujuan Penelitian
1. Mengimplementasikan model LSTM, XGBoost Baseline, dan Hybrid Stacking untuk memprediksi harga saham BBRI harian.
2. Mengevaluasi secara komparatif performa ketiga model menggunakan metrik RMSE, MAE, $R^2$, dan MAPE pada data testing.
3. Menguji signifikansi perbedaan performa model secara statistik menggunakan Wilcoxon Signed-Rank Test di seluruh 10 runs terkontrol.
4. Menyediakan rekomendasi empiris yang valid mengenai pemilihan model untuk prediksi saham blue-chip di pasar modal Indonesia.

## 4. Tinjauan Pustaka & Gap Penelitian
Penelitian terdahulu menunjukkan bahwa LSTM sering kali menjadi pilihan utama untuk data time series karena kemampuannya meminimalkan masalah vanishing gradient. Namun, model deep learning membutuhkan data dalam jumlah sangat besar dan rentan terhadap overfitting jika data memiliki noise tinggi. Di sisi lain, beberapa penelitian melaporkan bahwa model berbasis pohon keputusan seperti XGBoost mampu mengungguli deep learning pada data terstruktur jika diberikan fitur lag dan indikator teknikal yang representatif. Model Hybrid Stacking menggabungkan kekuatan keduanya, namun kompleksitas komputasinya meningkat. Gap penelitian yang ingin diselesaikan adalah kurangnya pengujian reliabilitas statistik multi-run pada saham spesifik perbankan Indonesia (BBRI) dengan menyertakan structural breaks dalam jangka panjang (10 tahun).

## 5. Metodologi Penelitian

### 5.1 Pengumpulan Data
Data historis harian saham BBRI dari 2015-01-01 s.d. 2025-12-31 diperoleh dari Yahoo Finance API, mencakup harga Open, High, Low, Close, dan Volume (OHLCV).

### 5.2 Preprocessing & Feature Engineering
- **Normalisasi:** MinMax Scaling untuk menormalkan fitur ke rentang `[0, 1]`.
- **Indikator Teknikal:** Menghitung SMA_20, EMA_50, RSI_14, MACD, dan ATR_14.
- **Fitur Lag:** Membuat lag-1 s.d. lag-60 harga penutupan sebagai autoregressive features.
- **Windowing:** Menggunakan sequence window sebesar 60 hari untuk memprediksi harga penutupan hari berikutnya.
- **Splitting:** Membagi data secara kronologis (80% training set, 20% testing set).

### 5.3 Implementasi Model
- **LSTM:** Model dengan 2 layer LSTM (128 dan 64 units), dropout 0.2, dilatih menggunakan Huber loss dan optimizer Adam.
- **XGBoost:** Baseline model dengan 500 pohon, lr=0.05, dan max_depth=6.
- **Hybrid Stacking:** Menggunakan prediksi LSTM (scaled) pada Level 1 sebagai fitur tambahan bersama fitur teknikal untuk dilatih pada XGBoost Meta-Learner Level 2.

### 5.4 Evaluasi & Validasi
Kinerja diuji dengan running 10 kali menggunakan seed acak berbeda (`43` s.d. `52`). Metrik evaluasi mencakup RMSE, MAE, $R^2$, MAPE, dan Wilcoxon Signed-Rank Test untuk signifikansi perbedaan performa.
