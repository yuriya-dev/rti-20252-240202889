# Tahap 4 — Eksperimen & Evaluasi Kinerja

**Status:** Belum Mulai
**Ketergantungan:** [tahap-2-implementasi-baseline-xgboost.md](tahap-2-implementasi-baseline-xgboost.md), [tahap-3-implementasi-lstm.md](tahap-3-implementasi-lstm.md)

---

## 1. Desain Eksperimen
Eksperimen dilakukan untuk membandingkan prediksi model LSTM dan model baseline XGBoost pada testing set (20% data akhir yang dipisahkan kronologis).

## 2. Metrik Evaluasi Regresi
Perbandingan model diukur menggunakan tiga metrik kuantitatif utama:
1. **Root Mean Squared Error (RMSE):** Mengukur sensitivitas terhadap error besar.
   $$RMSE = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2}$$
2. **Mean Absolute Error (MAE):** Mengukur deviasi absolut rata-rata prediksi.
   $$MAE = \frac{1}{n}\sum_{i=1}^{n}|y_i - \hat{y}_i|$$
3. **R-squared (R2 Score):** Mengukur goodness-of-fit atau seberapa besar variansi data aktual dapat dijelaskan oleh model.
   $$R^2 = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}$$

## 3. Visualisasi Hasil
Dihasilkan grafik komparatif:
* Grafik garis membandingkan harga aktual (BBRI) vs hasil prediksi model XGBoost vs hasil prediksi model LSTM pada testing set.
* Plot sebaran (scatter plot) error prediksi masing-masing model.

## 4. Hasil & Output yang Diharapkan
* Script pipeline evaluasi otomatis di `riset-directory/05-kode/analysis/`.
* File statistik CSV berisi perbandingan metrik performa di `riset-directory/06-output/tables/`.
* File visualisasi grafik prediksi berformat PNG di `riset-directory/06-output/figures/`.
