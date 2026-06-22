# Tahap 4 — Eksperimen & Evaluasi Kinerja

**Status:** Selesai
**Ketergantungan:** [tahap-2-implementasi-baseline-xgboost.md](tahap-2-implementasi-baseline-xgboost.md), [tahap-3-implementasi-lstm.md](tahap-3-implementasi-lstm.md)

---

## 1. Desain Eksperimen
Eksperimen dilakukan untuk membandingkan performa prediksi model LSTM Baseline, XGBoost Baseline, dan Hybrid Stacking (LSTM → XGBoost) pada data testing (20% data akhir secara kronologis).

## 2. Rencana Eksekusi (Execution Plan) & Log Data
Untuk membuktikan kestabilan model dan menghindari keberuntungan statistik (statistical fluke) akibat inisialisasi bobot acak, setiap run mengevaluasi seluruh model dengan seed acak yang bervariasi (`42 + run_id`).

### Execution Plan & Status
Eksperimen telah dijalankan sebanyak 10 kali (Run 1 s.d. Run 10) dengan status akhir sebagai berikut:

| Run # | Skenario | Seed | Parameter | Status | Output Folder |
|-------|----------|------|-----------|--------|---------------|
| 1     | LSTM vs XGB vs Hybrid | 43 | window=60, epoch=100, batch=32, n_est=500 | Completed | `06-output/run-1` |
| 2     | LSTM vs XGB vs Hybrid | 44 | window=60, epoch=100, batch=32, n_est=500 | Completed | `06-output/run-2` |
| 3     | LSTM vs XGB vs Hybrid | 45 | window=60, epoch=100, batch=32, n_est=500 | Completed | `06-output/run-3` |
| 4     | LSTM vs XGB vs Hybrid | 46 | window=60, epoch=100, batch=32, n_est=500 | Completed | `06-output/run-4` |
| 5     | LSTM vs XGB vs Hybrid | 47 | window=60, epoch=100, batch=32, n_est=500 | Completed | `06-output/run-5` |
| 6     | LSTM vs XGB vs Hybrid | 48 | window=60, epoch=100, batch=32, n_est=500 | Completed | `06-output/run-6` |
| 7     | LSTM vs XGB vs Hybrid | 49 | window=60, epoch=100, batch=32, n_est=500 | Completed | `06-output/run-7` |
| 8     | LSTM vs XGB vs Hybrid | 50 | window=60, epoch=100, batch=32, n_est=500 | Completed | `06-output/run-8` |
| 9     | LSTM vs XGB vs Hybrid | 51 | window=60, epoch=100, batch=32, n_est=500 | Completed | `06-output/run-9` |
| 10    | LSTM vs XGB vs Hybrid | 52 | window=60, epoch=100, batch=32, n_est=500 | Completed | `06-output/run-10` |

### Rekapitulasi Statistik Kinerja (Hasil 10 Run)
Berikut adalah rekapitulasi rata-rata (mean) dan standar deviasi (std) metrik dari seluruh run:

| Model | MAE (Rp) | RMSE (Rp) | R² Score | MAPE (%) |
|-------|----------|-----------|----------|----------|
| **LSTM Baseline** | 229.0273 ± 26.4501 | 301.6060 ± 30.9412 | 0.5901 ± 0.0808 | 5.5588 ± 0.6445 |
| **XGBoost Baseline** | **126.1506 ± 4.5945** | **188.5673 ± 4.0398** | **0.8412 ± 0.0068** | **3.1385 ± 0.1263** |
| **Hybrid Stacking** | 128.6106 ± 6.6277 | 193.7625 ± 5.4648 | 0.8323 ± 0.0095 | 3.1868 ± 0.1862 |

### Hasil Uji Signifikansi Statistik (Wilcoxon Signed-Rank Test)
Uji signifikansi dilakukan pada residu kuadrat (squared error) model pada tingkat kepercayaan $\alpha = 0.05$:
- **LSTM vs XGBoost:** SIGNIFIKAN ✅ (p-value $\approx 3.65 \times 10^{-53}$)
- **Hybrid vs LSTM:** SIGNIFIKAN ✅ (p-value $\approx 2.77 \times 10^{-49}$)
- **Hybrid vs XGBoost:** SIGNIFIKAN ✅ (p-value $\approx 0.0056$)

*Kesimpulan:* XGBoost secara konsisten dan signifikan mengungguli model LSTM dan Hybrid Stacking pada dataset BBRI.

## 3. Metrik Evaluasi Regresi
Model diuji menggunakan empat metrik regresi kuantitatif:
1. **Root Mean Squared Error (RMSE)**
2. **Mean Absolute Error (MAE)**
3. **R-squared (R² Score)**
4. **Mean Absolute Percentage Error (MAPE)**

## 4. Visualisasi Hasil Per Run
Di dalam setiap folder `06-output/run-X`, grafik visualisasi yang disimpan meliputi:
- `05_prediksi_vs_aktual.png`: Garis komparatif pergerakan harga BBRI aktual vs prediksi.
- `06_komparasi_metrik.png`: Diagram batang perbandingan metrik evaluasi.
- `07_analisis_residual.png`: Plot distribusi residual error.
- `08_rolling_mae.png`: Rolling MAE 60 hari untuk melihat ketahanan performa model terhadap waktu.

## 5. Output yang Dihasilkan
- Script runner di `riset-directory/05-kode/run_all_experiments.py` dan notebook di `riset-directory/05-kode/BBRI_Stock_Prediction.ipynb`.
- Berkas log metrik CSV, signifikansi, dan model biner (.keras & .pkl) di `riset-directory/06-output/run-1/` s.d. `run-10/`.
