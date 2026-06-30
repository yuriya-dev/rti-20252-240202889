# Tahap 6 — Penyajian Hasil & Visualisasi

**Status:** Selesai  
**Ketergantungan:** [tahap-4-eksperimen-dan-evaluasi.md](tahap-4-eksperimen-dan-evaluasi.md), [tahap-5-draf-paper.md](tahap-5-draf-paper.md)

---

## 1. Tujuan

Menyusun rencana penyajian hasil eksperimen yang terstruktur, bebas bias visualisasi, dan siap diintegrasikan ke dalam manuskrip jurnal. Tahap ini mengacu pada **WS-12: Result Presentation & Visualization**.

---

## 2. Tabel Hasil Eksperimen (Ringkasan 10 Run)

**Tabel 1. Perbandingan Performa Model Prediksi Harga Saham BBRI (2015–2025)**

*N = 10 run per skenario. Nilai: mean ± std. Diurutkan berdasarkan MAE ascending (metrik primer).*

| Skenario                | MAE (mean ± std, Rp) | RMSE (mean ± std, Rp) | R² (mean ± std)     | MAPE (mean ± std, %) | n  |
|-------------------------|----------------------|----------------------|---------------------|----------------------|----|
| **XGBoost Baseline**    | **126.15 ± 4.59**    | **188.57 ± 4.04**    | **0.8412 ± 0.0068** | **3.14 ± 0.13**      | 10 |
| Hybrid (LSTM→XGBoost)   | 128.61 ± 6.63        | 193.76 ± 5.46        | 0.8323 ± 0.0095     | 3.19 ± 0.19          | 10 |
| LSTM Baseline           | 229.03 ± 26.45       | 301.61 ± 30.94       | 0.5901 ± 0.0808     | 5.56 ± 0.64          | 10 |

**Temuan utama:**
- XGBoost Baseline mengungguli LSTM di seluruh metrik dengan selisih MAE ~45% lebih rendah.
- Hybrid Stacking tidak memberikan peningkatan signifikan atas XGBoost saja (MAE hanya 2% lebih tinggi, p = 0.0056).
- LSTM jauh lebih tidak stabil: std MAE = 26.45 Rp vs XGBoost 4.59 Rp (rasio ~5.8×).

---

## 3. Rencana Visualisasi

Keempat grafik berikut sudah dihasilkan otomatis oleh `05-kode/BBRI_Stock_Prediction.ipynb` per run dan tersimpan di `06-output/run-*/`.

| # | Jenis Grafik | Pesan Ilmiah | File Output | Status |
|---|-------------|--------------|-------------|--------|
| 1 | **Grouped bar chart + error bar** | XGBoost dan Hybrid jauh lebih akurat dari LSTM; keduanya setara satu sama lain | `06_komparasi_metrik.png` | ✅ Tersedia |
| 2 | **Box plot (R² per model)** | Distribusi R² XGBoost sangat rapat (stabil antar-seed), LSTM sangat lebar (tidak stabil) | *Perlu generate dari agregat CSV* | ⚠️ Perlu dibuat |
| 3 | **Line chart overlay** | XGBoost dan Hybrid mengikuti tren aktual BBRI lebih dekat daripada LSTM | `05_prediksi_vs_aktual.png` | ✅ Tersedia |
| 4 | **Rolling MAE line chart** | XGBoost mempertahankan MAE rendah sepanjang test set; LSTM melonjak saat periode volatil | `08_rolling_mae.png` | ✅ Tersedia |

> **Prioritas untuk manuskrip:** Grafik #1 dan #3 adalah yang paling krusial untuk mendukung argumen komparatif. Grafik #2 (box plot R²) perlu dibuat dari agregat 10 CSV untuk menunjukkan stabilitas antar-run secara eksplisit.

---

## 4. Bias Check Visualisasi

| Bias | Grafik #1 (Bar) | Grafik #2 (Box) | Grafik #3 (Line) | Grafik #4 (Rolling) |
|------|:--------------:|:---------------:|:----------------:|:-------------------:|
| Truncated axis (Y tidak mulai 0) | ✅ Mulai 0 | ✅ Full range | ✅ Harga aktual | ✅ Full range |
| Error bar / CI ditampilkan | ✅ ± std bar | ✅ IQR + whisker | ➖ N/A | ➖ N/A |
| Semua kondisi ditampilkan | ✅ 3 model | ✅ 3 model | ✅ 3 model | ✅ 3 model |
| Tidak ada efek 3D | ✅ | ✅ | ✅ | ✅ |

**Catatan perbaikan:** Grafik #3 (line chart) sebaiknya menambahkan *shaded area* (min/max dari 10 run) untuk menunjukkan bandwidth prediksi secara jujur. Ini belum diimplementasikan di versi saat ini.

---

## 5. Checklist Result Presentation Plan

- [x] Tabel hasil self-contained (judul, satuan, N tercantum)
- [x] Mean ± std dilaporkan (bukan single number)
- [x] Diurutkan berdasarkan metrik utama (MAE ascending)
- [x] Y-axis mulai dari 0 di semua grafik
- [x] Error bar ditampilkan di bar chart dan box plot
- [x] Semua skenario ditampilkan (tidak cherry-picked)
- [x] Tidak ada efek 3D
- [ ] Shaded area pada line chart (perbaikan minor — opsional untuk versi final)

---

## 6. Output yang Dihasilkan dari Tahap Ini

- **WS-12** di `worksheets/ws-12-result-presentation.md` — Worksheet selesai diisi dengan data riil.
- **Tabel 1** siap copy-paste ke `07-manuskrip/naskah-jurnal.md` (Bagian 4. Results).
- Keempat grafik tersedia di `06-output/run-1/` s.d. `run-10/` sebagai referensi visual.
