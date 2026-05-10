# WS-07: Experimental Design & Validity

> **Bab 7 — Experimental Design & Validity**

---

## Ringkasan Materi

### Correlation ≠ Causality

Kausalitas membutuhkan 3 syarat:
1. **Covariance** — X dan Y bergerak bersama
2. **Temporal precedence** — X berubah sebelum Y
3. **Elimination of alternatives** — Tidak ada faktor lain yang menjelaskan Y

Controlled experiment adalah satu-satunya metode yang bisa membuktikan kausalitas.

### Empat Jenis Validitas

| Jenis | Pertanyaan | Ancaman Umum |
|-------|-----------|-------------|
| **Internal** | Apakah hubungan IV→DV nyata? | Confounding variable, selection bias |
| **External** | Apakah bisa digeneralisasi? | Dataset terlalu spesifik |
| **Construct** | Apakah mengukur konsep yang benar? | Metrik tidak sesuai |
| **Conclusion** | Apakah kesimpulan statistik valid? | Sample size kecil, uji salah |

Internal dan external validity sering berkonflik: semakin terkontrol (internal kuat) → semakin artificial (external lemah).

### Tiga Tipe Eksperimen dalam Riset TI

| Tipe | Deskripsi | Kapan Digunakan |
|------|----------|----------------|
| **Comparison Study** | Metode A vs B pada kondisi identik | Membandingkan pendekatan berbeda |
| **Ablation Study** | Full system → lepas komponen satu per satu | Mengukur kontribusi tiap komponen |
| **Parameter Study** | Variasikan satu parameter, amati dampak | Uji sensitifitas/robustness |

### Fairness dalam Perbandingan

Perbandingan yang adil = **kondisi identik** untuk semua metode: dataset sama, preprocessing sama, tuning effort sebanding, environment sama, metrik sama.

Contoh tidak adil: Transformer (30 fitur tambahan + Bayesian optimization) vs RF (default params) → hasilnya misleading.

### Threats to Validity = Diidentifikasi Sebelum Eksperimen

Ancaman validitas harus diidentifikasi **sebelum** eksperimen dan mitigasinya dirancang sebagai bagian dari desain — bukan ditulis sebagai boilerplate setelah selesai.

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan testing | Memastikan sistem memenuhi requirement | Membuktikan hubungan kausal antar variabel |
| Baseline | Versi sebelumnya (last release) | Metode tervalidasi dari literatur |
| Kegagalan | Bug → fix → release | H₀ tidak ditolak → tetap kontribusi ilmiah |
| Sukses | 100% test pass | Evidence valid — mendukung atau menolak hipotesis |

### Istilah Penting

- **Causality** — Hubungan sebab-akibat (covariance + temporal + elimination)
- **Controlled Experiment** — Ubah satu variabel, kontrol sisanya, amati efek
- **Fairness** — Semua metode diuji pada kondisi yang benar-benar identik
- **Threats to Validity** — Faktor yang bisa melemahkan kesimpulan jika tidak dimitigasi
- **Conclusion Validity** — Validitas statistik: power, sample size, uji yang tepat

---

## Template A.7 — Desain Eksperimen Lengkap

```
EXPERIMENT DESIGN

Research Question : Apakah LSTM menghasilkan MAE dan RMSE lebih rendah serta R2 lebih tinggi dibanding baseline XGBoost pada dataset harga penutupan harian saham BBRI (2015-2025) dari Investing.com/Yahoo Finance?
Hypothesis        : H0: Tidak ada perbedaan signifikan MAE/RMSE dan R2 antara LSTM dan XGBoost. H1: LSTM memiliki MAE/RMSE lebih rendah dan R2 lebih tinggi dibanding XGBoost.
Tipe Eksperimen   : [x] Comparison  [ ] Ablation  [ ] Parameter

Kondisi Eksperimen:
| Kondisi | Deskripsi | IV Value | CV Settings |
|---------|-----------|----------|-------------|
| Control | XGBoost baseline | XGBoost | Dataset BBRI 2015-2025, split 80/20, window 30, MinMax, seed 42 |
| Treatment | LSTM model | LSTM | Dataset BBRI 2015-2025, split 80/20, window 30, MinMax, seed 42 |

Fairness Checklist:
  [x] Dataset identik untuk semua kondisi
  [x] Preprocessing setara
  [x] Tuning effort setara
  [x] Environment identik
  [x] Metrik evaluasi sama

Threat Analysis:
| Threat Type | Ancaman Spesifik | Mitigasi |
|-------------|-----------------|----------|
| Internal    | Data leakage akibat split time series yang salah | Gunakan split kronologis dan walk-forward validation |
| External    | Hanya satu emiten (BBRI) dan periode tertentu | Nyatakan batasan; uji tambahan pada emiten lain jika tersedia |
| Construct   | Metrik error tidak menangkap manfaat trading | Tambahkan directional accuracy sebagai metrik eksploratif |
| Conclusion  | Variansi tinggi dan non-stationary | Gunakan bootstrap pada error dan laporkan interval kepercayaan |

Statistical Plan:
  Uji statistik   : Diebold-Mariano atau Wilcoxon signed-rank pada error berpasangan
  Justifikasi      : Menguji perbedaan akurasi forecast pada pasangan error yang identik
  Alpha            : 0.05
  Effect size min  : Penurunan MAE/RMSE >= 5% atau delta R2 >= 0.02
```

---

## Latihan 1 — Desain Eksperimen

Susun desain eksperimen berdasarkan RQ, variabel, dan sistem dari WS-04 sampai WS-06.

**RQ:** Apakah LSTM menghasilkan MAE dan RMSE lebih rendah serta R2 lebih tinggi dibanding baseline XGBoost pada dataset harga penutupan harian saham BBRI (2015-2025) dari Investing.com/Yahoo Finance?
**Tipe eksperimen:** [x] Comparison / [ ] Ablation / [ ] Parameter

| Kondisi | Deskripsi | IV Value | CV Settings |
|---------|-----------|----------|-------------|
| Control | XGBoost baseline | XGBoost | Dataset BBRI 2015-2025, split 80/20, window 30, MinMax, seed 42 |
| Treatment | LSTM model | LSTM | Dataset BBRI 2015-2025, split 80/20, window 30, MinMax, seed 42 |

---

## Latihan 2 — Fairness Checklist

Evaluasi apakah desain eksperimen di Latihan 1 sudah fair.

| Kriteria | Status | Detail |
|----------|--------|--------|
| Dataset identik | Ya | Sama-sama pakai BBRI 2015-2025 |
| Preprocessing setara | Ya | MinMax, window 30, split kronologis |
| Tuning effort setara | Ya | Grid search sederhana pada kedua model |
| Environment identik | Ya | Hardware dan library versi sama |
| Metrik evaluasi sama | Ya | RMSE, MAE, R2, MAPE |

**Ada yang tidak fair?** [ ] Ya / [x] Tidak
> Jika ya, bagaimana cara memperbaikinya? N/A

---

## Latihan 3 — Threat Analysis

Identifikasi ancaman validitas untuk desain eksperimen ini.

| Threat Type | Ancaman Spesifik | Mitigasi |
|-------------|-----------------|----------|
| Internal | Data leakage karena windowing tidak kronologis | Gunakan split kronologis dan cek overlap | 
| External | Hanya satu emiten, pasar Indonesia | Tambah emiten lain atau sebut sebagai batasan | 
| Construct | Metrik error tidak mencerminkan profit | Tambahkan directional accuracy sebagai metrik eksploratif |
| Conclusion | Sample test kecil dan data volatil | Gunakan bootstrap, laporkan CI |

**Ancaman mana yang paling sulit dimitigasi?** External validity
**Mengapa?**
> Generalisasi ke emiten lain sulit tanpa data multi-saham dan periode berbeda.

---

## Refleksi

> Sebuah paper melaporkan "metode kami mengalahkan semua baseline." Apa 3 pertanyaan pertama yang harus diajukan untuk mengevaluasi klaim ini?

**Jawaban:**
1. Apakah dataset, preprocessing, dan split identik untuk semua baseline?
2. Apakah tuning effort dan budget komputasi setara untuk tiap metode?
3. Apakah metrik dan uji statistik sesuai dengan tujuan prediksi?
