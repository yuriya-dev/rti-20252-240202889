# Naskah Jurnal Penelitian

**Judul:** Analisis Komparatif Performa Model Long Short-Term Memory (LSTM), eXtreme Gradient Boosting (XGBoost), dan Hybrid Stacking dalam Prediksi Harga Saham BBRI (2015-2025)

**Penulis:** Wahyu Tri Cahya  
**Afiliasi:** Program Studi Informatika, Fakultas Teknik  
**Email:** wahyutricahya@student.university.ac.id  

---

## Abstrak
Prediksi harga saham harian merupakan topik penting namun menantang dalam riset keuangan karena sifat data pasar saham yang volatil, non-linear, dan rentan terhadap noise. Penelitian ini menyajikan analisis komparatif performa model deep learning Long Short-Term Memory (LSTM) Baseline, model machine learning eXtreme Gradient Boosting (XGBoost) Baseline, serta model Hybrid Stacking dua tingkat (LSTM → XGBoost) dalam memprediksi harga penutupan harian saham PT Bank Rakyat Indonesia (Persero) Tbk (BBRI) dari periode 1 Januari 2015 hingga 31 Desember 2025. Untuk memastikan kestabilan hasil dan menghindari keberuntungan statistik, pengujian dilakukan sebanyak 10 kali run terkontrol dengan 10 random seed berbeda. Hasil evaluasi menunjukkan bahwa XGBoost Baseline secara konsisten menghasilkan tingkat error terendah dengan rata-rata MAE sebesar 126.1506 ± 4.5945 Rp, RMSE sebesar 188.5673 ± 4.0398 Rp, $R^2$ Score sebesar 0.8412 ± 0.0068, dan MAPE sebesar 3.1385% ± 0.1263%. Model Hybrid Stacking menunjukkan performa yang kompetitif namun tidak mampu mengungguli baseline XGBoost ($R^2$ = 0.8323 ± 0.0095), sementara model LSTM Baseline menghasilkan kinerja terendah ($R^2$ = 0.5901 ± 0.0808). Pengujian statistik menggunakan Wilcoxon Signed-Rank Test pada residual error mengonfirmasi bahwa perbedaan performa di antara ketiga model tersebut adalah signifikan secara statistik (p-value < 0.05). Hasil ini mengindikasikan bahwa model ensemble pohon keputusan (XGBoost) yang dikombinasikan dengan indikator teknikal dan fitur lag autoregressive yang tepat lebih tangguh dan stabil dibanding model deep learning murni untuk prediksi saham dengan volatilitas tinggi.

**Kata Kunci:** Prediksi Saham, BBRI, LSTM, XGBoost, Hybrid Stacking, Wilcoxon Test.

## Abstract
Daily stock price prediction is a critical but challenging topic in financial research due to the volatile, non-linear, and noisy nature of stock market data. This study presents a comparative analysis of a deep learning model, Long Short-Term Memory (LSTM) Baseline, a machine learning model, eXtreme Gradient Boosting (XGBoost) Baseline, and a two-level Hybrid Stacking model (LSTM → XGBoost) in predicting the daily closing price of PT Bank Rakyat Indonesia (Persero) Tbk (BBRI) shares from January 1, 2015, to December 31, 2025. To ensure results stability and avoid statistical fluke, the experiments were run 10 times under controlled environments with 10 different random seeds. The evaluation results demonstrate that the XGBoost Baseline consistently produces the lowest error rates with an average MAE of 126.1506 ± 4.5945 IDR, RMSE of 188.5673 ± 4.0398 IDR, $R^2$ Score of 0.8412 ± 0.0068, and MAPE of 3.1385% ± 0.1263%. The Hybrid Stacking model shows competitive performance but fails to outperform the XGBoost baseline ($R^2$ = 0.8323 ± 0.0095), while the LSTM Baseline yields the lowest performance ($R^2$ = 0.5901 ± 0.0808). Statistical testing using the Wilcoxon Signed-Rank Test on residual errors confirms that the performance differences among the three models are statistically significant (p-value < 0.05). These findings suggest that decision tree-based ensemble models (XGBoost) combined with proper technical indicators and autoregressive lag features are more robust and stable than pure deep learning models for high-volatility stock prediction.

**Keywords:** Stock Prediction, BBRI, LSTM, XGBoost, Hybrid Stacking, Wilcoxon Test.

---

## 1. Pendahuluan
Pasar modal Indonesia berkembang pesat seiring dengan meningkatnya kesadaran investasi masyarakat. Salah satu instrumen investasi yang paling populer adalah saham BBRI, saham perbankan BUMN yang berkapitalisasi besar. Pergerakan harga saham BBRI merupakan time series finansial yang dipengaruhi oleh berbagai dinamika perekonomian lokal maupun global. Prediksi harga saham yang akurat sangat bermanfaat bagi investor dan institusi keuangan untuk mengurangi risiko kerugian investasi.

Namun, data time series harga saham memiliki karakteristik volatilitas dan noise yang tinggi serta hubungan non-linearitas yang rumit. Metode statistik parametrik konvensional seperti ARIMA sering kali tidak mampu memodelkan pergeseran tren non-linear ini secara akurat. Oleh karena itu, para peneliti mulai menerapkan teknik machine learning dan deep learning. Dalam literatur, sering diasumsikan bahwa model deep learning yang canggih seperti LSTM atau model Hybrid Stacking yang kompleks secara otomatis akan mengungguli model machine learning konvensional berbasis data tabular. Tujuan penelitian ini adalah menguji dan membandingkan performa model LSTM Baseline, XGBoost Baseline, dan Hybrid Stacking secara empiris dan statistik menggunakan uji signifikansi Wilcoxon di seluruh 10 runs terkontrol.

## 2. Tinjauan Pustaka
- **Long Short-Term Memory (LSTM):** Arsitektur deep learning recurrent neural network (RNN) yang dirancang khusus untuk menyimpan informasi historis jangka panjang dengan meminimalkan masalah *vanishing gradient*. LSTM memproses sequence data secara temporal.
- **eXtreme Gradient Boosting (XGBoost):** Algoritma ensemble learning berbasis pohon keputusan yang dioptimalkan dengan gradient boosting. XGBoost sangat tangguh untuk data tabular terstruktur dengan konvergensi yang cepat dan regularisasi internal untuk mencegah overfitting.
- **Hybrid Stacking:** Metode penggabungan beberapa model (ensemble) di mana prediksi dari satu model dasar (Level 1) dimasukkan sebagai fitur tambahan bersama data asli untuk dilatih pada model tingkat berikutnya (Level 2).
- **Wilcoxon Signed-Rank Test:** Uji statistik non-parametrik yang digunakan untuk membandingkan dua kelompok data berpasangan (residu kuadrat model) untuk menguji apakah ada perbedaan signifikan secara statistik di antara mereka.

## 3. Metodologi Penelitian
- **Dataset:** Data harga penutupan harian BBRI (2.726 baris) dari 1 Januari 2015 s.d. 31 Desember 2025 diunduh menggunakan library `yfinance`.
- **Fitur Input:**
  - Fitur lag autoregressive: 60 hari harga penutupan historis (`Lag_Close_t-1` s.d. `Lag_Close_t-60`).
  - Indikator teknikal: SMA_20, EMA_50, RSI_14, MACD, dan ATR_14.
- **Preprocessing:** MinMax scaling pada seluruh data dan split kronologis (80% training set, 20% testing set).
- **Arsitektur Model:**
  - **LSTM:** Input tensor 3D `[batch, 60, 11]`, layer LSTM 1 (128 units), Dropout (0.2), layer LSTM 2 (64 units), Dropout (0.2), Dense Output Layer (1 unit). Huber loss, Adam optimizer ($\eta = 0.001$), EarlyStopping (patience=15).
  - **XGBoost:** Estimators=500, learning_rate=0.05, max_depth=6, subsample=0.8, colsample_bytree=0.8.
  - **Hybrid Stacking:** LSTM level 1 menghasilkan prediksi scaled target, dilanjutkan XGBoost level 2 (estimators=600, lr=0.03, max_depth=5) dilatih dengan fitur input asli ditambah prediksi LSTM tersebut.

## 4. Hasil dan Pembahasan
Hasil evaluasi kinerja rata-rata dari 10 run yang dieksekusi secara independen dirangkum pada Tabel 1:

### Tabel 1. Hasil Evaluasi Kinerja Rata-rata Model (10 Run)

| Model | MAE (Rp) | RMSE (Rp) | $R^2$ Score | MAPE (%) |
|-------|----------|-----------|-------------|----------|
| **LSTM Baseline** | 229.0273 ± 26.4501 | 301.6060 ± 30.9412 | 0.5901 ± 0.0808 | 5.5588 ± 0.6445 |
| **XGBoost Baseline** | **126.1506 ± 4.5945** | **188.5673 ± 4.0398** | **0.8412 ± 0.0068** | **3.1385 ± 0.1263** |
| **Hybrid Stacking** | 128.6106 ± 6.6277 | 193.7625 ± 5.4648 | 0.8323 ± 0.0095 | 3.1868 ± 0.1862 |

Berdasarkan Tabel 1, **XGBoost Baseline** menunjukkan tingkat kesalahan terendah (MAE = 126.15 Rp, RMSE = 188.56 Rp) dan goodness-of-fit tertinggi ($R^2$ = 0.8412). Hal ini membantah asumsi awal bahwa deep learning (LSTM) selalu mengungguli machine learning konvensional pada data runtun waktu keuangan. Performa LSTM yang rendah ($R^2$ = 0.5901) disebabkan karena model deep learning rentan mengalami kesulitan generalisasi terhadap structural breaks tajam (seperti masa krisis ekonomi global/nasional selama rentang 10 tahun). Model Hybrid Stacking menunjukkan kinerja yang sangat baik namun tidak mampu melampaui XGBoost baseline, karena besarnya residual error LSTM Level 1 justru menambahkan derau (noise) baru yang mengaburkan performa meta-learner Level 2.

### Tabel 2. Hasil Wilcoxon Signed-Rank Test (Tingkat Kepercayaan 95%)

| Komparasi Model | Nilai Statistik | p-value | Kesimpulan |
|-----------------|-----------------|---------|------------|
| **LSTM vs XGBoost** | 16559.0 | $3.65 \times 10^{-53}$ | SIGNIFIKAN ✅ |
| **Hybrid vs LSTM** | 18661.0 | $2.77 \times 10^{-49}$ | SIGNIFIKAN ✅ |
| **Hybrid vs XGBoost** | 61294.0 | $0.0056$ | SIGNIFIKAN ✅ |

Uji Wilcoxon Signed-Rank Test pada Tabel 2 membuktikan bahwa perbedaan performa di antara ketiga model tersebut adalah signifikan secara statistik (p-value < 0.05).

## 5. Kesimpulan
Penelitian ini berhasil membandingkan performa LSTM Baseline, XGBoost Baseline, dan Hybrid Stacking dalam memprediksi harga saham BBRI periode 2015-2025 secara valid dan teruji melalui 10 run eksperimen. Hasil membuktikan bahwa model ensemble berbasis pohon keputusan (XGBoost) secara signifikan mengungguli model LSTM dan Hybrid Stacking. Untuk penelitian selanjutnya, disarankan menerapkan pemodelan berbasis Attention Mechanism (Transformer) dan memperhitungkan analisis sentimen media keuangan guna mengantisipasi structural breaks secara dinamis.

## Daftar Pustaka
1. Hochreiter, S., & Schmidhuber, J. (1997). Long short-term memory. *Neural computation*, 9(8), 1735-1780.
2. Chen, T., & Guestrin, C. (2016). Xgboost: A scalable tree boosting system. *Proceedings of the 22nd ACM SIGKDD*, 785-794.
3. Wolpert, D. H. (1992). Stacked generalization. *Neural networks*, 5(2), 241-259.
