# WS-04: Research Question & Hypothesis

> **Bab 4 — Research Question, Contribution & Hypothesis**

---

## Ringkasan Materi

### RQ Bukan Pertanyaan Biasa

Research Question yang baik secara implisit mengandung cetak biru eksperimen: subjek, baseline, metrik, domain, dataset.

| Kualitas | Contoh |
|----------|--------|
| **Buruk** | "Bagaimana pengaruh deep learning terhadap deteksi malware?" |
| **Baik** | "Apakah CNN menghasilkan F1-Score lebih tinggi dari RF pada CIC-MalMem-2022?" |

Perbedaan: RQ yang baik menyebutkan **metode spesifik**, **metrik terukur**, **baseline**, dan **dataset**.

### Tiga Jenis RQ

| Jenis | Pola | Kebutuhan |
|-------|------|-----------|
| **Comparison** | A vs B → mana lebih baik? | ≥ 2 metode, metrik sama |
| **Improvement** | A' vs A → modifikasi lebih baik? | Pre/post, bukti perbaikan |
| **Exploratory** | Faktor X₁...Xₙ → pengaruh terhadap Y? | Multi-variabel, korelasi/regresi |

### Contribution Statement

Tiga jenis kontribusi: **Improvement** (metode terbukti lebih baik), **Comparison** (perbandingan sistematis yang belum ada), **Novel Approach** (pendekatan baru). Kontribusi harus terhubung langsung dengan gap — kontribusi tanpa gap = klaim tanpa justifikasi.

### Hypothesis H₀ / H₁

- **H₀** (Null) = Tidak ada perbedaan signifikan — asumsi default, harus dibuktikan salah
- **H₁** (Alternative) = Ada perbedaan signifikan — diterima hanya jika H₀ ditolak
- Harus **falsifiable**, mengandung **metrik terukur**, dirumuskan **SEBELUM eksperimen**

### Rantai Operasionalisasi

```
RQ → Variable → Metric → Data → Analysis
```

Jika rantai ini tidak lengkap, RQ belum mature. Bi-directional: RQ yang tidak bisa jadi hipotesis testable harus direvisi mundur.

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan pertanyaan | Apa yang harus dibangun? | Apa yang harus dibuktikan? |
| Bentuk jawaban | Sistem yang berfungsi | Bukti empiris terukur |
| Sukses diukur oleh | User satisfaction, uptime | Signifikansi statistik, effect size |
| Jika gagal | Debug dan perbaiki | Laporkan, analisis mengapa |

### Istilah Penting

- **Research Question (RQ)** — Pertanyaan spesifik: variabel terukur + metrik + konteks
- **Contribution Statement** — Apa yang diketahui setelah riset selesai yang sebelumnya belum ada
- **H₀ / H₁** — Null vs Alternative Hypothesis
- **Falsifiability** — Kondisi hipotesis ditolak harus bisa didefinisikan sebelum eksperimen
- **Operationalization** — Proses mewujudkan konsep abstrak menjadi variabel terukur

---

## A.4 — RQ-Contribution-Hypothesis


RQ-CONTRIBUTION-HYPOTHESIS

RQ-CONTRIBUTION-HYPOTHESIS

Gap Statement  : Belum ada bukti empiris komparatif spesifik pada karakteristik volatilitas pasar modal Indonesia (saham BBRI) yang membandingkan performa LSTM dan XGBoost secara adil.

Research Question:
  Tipe         : [x] Comparison  [ ] Improvement  [ ] Exploratory
  Formulasi    : Apakah LSTM menghasilkan MAE dan RMSE lebih rendah serta R2 lebih tinggi dibanding baseline XGBoost pada dataset harga penutupan harian saham BBRI (2015-2025) dari Investing.com/Yahoo Finance?
  Variabel IV  : Jenis model (LSTM vs XGBoost)
  Variabel DV  : Akurasi prediksi harga saham
  Metrik       : RMSE, MAE (utama), R2, dan MAPE (pendukung)
  Dataset      : Dataset harga penutupan harian saham BBRI periode 2015-2025 dari Yahoo Finance / Investing.com (fitur: Open, High, Low, Close, Volume).
  Baseline     : XGBoost Regression

Quality Check RQ:
  [x] Variabel spesifik
  [x] Metrik jelas
  [x] Baseline ada
  [x] Konteks disebutkan
  [x] Memerlukan eksperimen (bukan hanya survei literatur)

Contribution Statement:
  Apa yang baru diketahui : Menyediakan bukti komparatif tentang keunggulan LSTM vs XGBoost khusus pada data runtun waktu saham BBRI dengan rentang waktu yang sangat panjang (10 tahun).
  Jenis kontribusi        : [ ] Improvement  [x] Comparison  [ ] Novel approach
  Gap yang diisi          : Mengisi Context+Performance gap dengan melakukan benchmarking komparatif pada saham blue-chip Indonesia untuk merekomendasikan arsitektur prediksi yang andal.

Hypothesis Pair:
  H₀ : Tidak ada perbedaan signifikan nilai MAE/RMSE dan R2 antara prediksi LSTM dan baseline XGBoost pada data saham BBRI.
  H₁ : LSTM memiliki MAE/RMSE yang secara signifikan lebih rendah dan R2 yang lebih tinggi dibandingkan baseline XGBoost pada data saham BBRI.
  Threshold              : Signifikansi statistik α = 0.05 untuk uji Diebold-Mariano atau Wilcoxon signed-rank test pada pasangan error prediksi. Penurunan error (MAE/RMSE) setidaknya 5% dari baseline.
  Justifikasi threshold  : α=0.05 adalah standar statistik; penurunan 5% error dipandang relevan secara praktis untuk memengaruhi margin profitabilitas trading.

---

## Latihan 1 — Dari Gap ke RQ

**Gap dari WS-03:** Belum ada komparasi yang adil dan spesifik untuk model LSTM vs XGBoost pada data saham lokal berkapitalisasi besar seperti BBRI (Context + Performance gap).

**RQ versi pertama (tulis bebas):**
> Manakah yang lebih baik antara deep learning dan machine learning untuk prediksi harga saham BBRI?

**Evaluasi RQ:**

| Komponen | Ada? | Isi |
|----------|------|-----|
| Metode spesifik | Ya | LSTM vs XGBoost |
| Metrik terukur | Ya | MAE, RMSE, R2 |
| Baseline | Ya | XGBoost |
| Dataset/konteks | Ya | Harga penutupan harian BBRI (2015-2025) |

**Tipe RQ:** [x] Comparison / [ ] Improvement / [ ] Exploratory

**RQ versi revisi (setelah evaluasi):**
> Apakah LSTM menghasilkan MAE dan RMSE lebih rendah serta R2 lebih tinggi dibanding baseline XGBoost pada dataset harga penutupan harian saham BBRI (2015-2025) dari Investing.com/Yahoo Finance?

---

## Latihan 2 — Hypothesis Pair

Rumuskan pasangan hipotesis dari RQ di Latihan 1.

| Komponen | Isi |
|----------|-----|
| H₀ | Tidak ada perbedaan signifikan MAE/RMSE dan R2 antara prediksi LSTM dan XGBoost pada dataset BBRI |
| H₁ | LSTM menghasilkan MAE/RMSE secara signifikan lebih rendah dan R2 lebih tinggi dibandingkan XGBoost |
| Metrik | MAE, RMSE, R2, p-value uji Diebold-Mariano/Wilcoxon (α=0.05) |
| Threshold | α=0.05; penurunan MAE/RMSE >= 5% atau delta R2 >= 0.02 |
| Justifikasi threshold | α=0.05 adalah batas standar kepercayaan 95%; margin 5% penurunan error cukup relevan untuk skenario trading finansial. |

**Apakah hipotesis ini falsifiable?** [x] Ya / [ ] Tidak
> Bagaimana cara membuktikannya salah? Jika setelah diuji statistik, p-value > 0.05 atau LSTM justru memiliki RMSE/MAE yang lebih besar dari XGBoost, maka H₁ ditolak.

---

## Latihan 3 — Rantai Operasionalisasi

Lengkapi rantai dari RQ hingga metode analisis.

| Tahap | Isi |
|-------|-----|
| RQ | Apakah LSTM menghasilkan MAE dan RMSE lebih rendah serta R2 lebih tinggi dibanding baseline XGBoost pada dataset BBRI? |
| Variable (IV) | Jenis model: `LSTM` vs `XGBoost` |
| Variable (DV) | Akurasi prediksi harga saham |
| Metric | RMSE, MAE, R2, MAPE, p-value uji statistik |
| Data source | Dataset harga penutupan harian saham BBRI periode 2015-2025 dari Yahoo Finance / Investing.com. |
| Analysis method | Preprocessing (MinMax scaling, windowing sequence), pembagian data (time-series split 80/20), training model, prediksi test set, evaluasi error per pasangan prediksi aktual, uji statistik Diebold-Mariano/Wilcoxon. |

**Apakah rantai lengkap?** [x] Ya / [ ] Tidak
> Jika tidak, tahap mana yang perlu direvisi? — N/A

---

## Refleksi

**Judul:** Prediksi Harga Saham BBRI Menggunakan LSTM vs XGBoost
**RQ yang diekstrak:** Apakah LSTM menghasilkan MAE dan RMSE lebih rendah serta R2 lebih tinggi dibanding baseline XGBoost pada dataset harga penutupan harian saham BBRI (2015-2025)?
**Komponen yang hilang:** Evaluasi perbandingan ini sering kali mengabaikan sentimen makroekonomi eksternal, yang seharusnya bisa menjadi saran untuk penelitian selanjutnya.

