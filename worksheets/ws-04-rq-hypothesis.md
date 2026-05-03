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

Gap Statement  : Belum ada kerangka evaluasi model ML yang simultan menilai akurasi, fairness, dan privasi untuk keputusan rekrutmen/turnover pada konteks HR organisasi di Indonesia.

Research Question:
  Tipe         : [x] Comparison  [ ] Improvement  [ ] Exploratory
  Formulasi    : Apakah metode `fairness-aware Random Forest` (RF-fair) menghasilkan F1-Score yang setidaknya setara dan tingkat ketidakadilan demografis (Demographic Parity Difference) lebih rendah dibanding `Random Forest` standar pada dataset HR Indonesia untuk tugas prediksi turnover?
  Variabel IV  : Jenis model (RF-standar vs RF-fair)
  Variabel DV  : 1) F1-Score (weighted) 2) Fairness gap (Demographic Parity Difference, Equal Opportunity Difference)
  Metrik       : F1-Score (utama), Demographic Parity Difference (DPD), Equal Opportunity Difference (EOD), dan ukuran privasi (laporan penggunaan fitur sensitif / differential privacy budget jika diterapkan)
  Dataset      : Dataset HR perusahaan Indonesia yang representatif (fitur demografis: usia, jenis kelamin, etnis jika tersedia; fitur pekerjaan: jabatan, lamanya bekerja, kinerja; outcome: turnover dalam 12 bulan). Jika belum tersedia, bangun dengan pengumpulan data anonim multi-organisasi atau gunakan data sintetis terkalibrasi.
  Baseline     : Random Forest + feature engineering (RF-standar)

Quality Check RQ:
  [x] Variabel spesifik
  [x] Metrik jelas
  [x] Baseline ada
  [x] Konteks disebutkan
  [x] Memerlukan eksperimen (bukan hanya survei literatur)

Contribution Statement:
  Apa yang baru diketahui : Menyediakan bukti empiris apakah pendekatan `fairness-aware` dapat mempertahankan atau meningkatkan akurasi sambil mengurangi ketidakadilan demografis pada dataset HR Indonesia; menyediakan kerangka evaluasi yang menggabungkan akurasi, fairness, dan pelaporan privasi.
  Jenis kontribusi        : [x] Improvement  [x] Comparison  [ ] Novel approach
  Gap yang diisi          : Mengisi Method+Context gap dengan menambahkan evaluasi fairness/privacy ke eksperimen prediksi turnover di konteks HR Indonesia.

Hypothesis Pair:
  H₀ : Tidak ada perbedaan signifikan pada F1-Score antara RF-fair dan RF-standar, dan RF-fair tidak menunjukkan pengurangan signifikan pada Demographic Parity Difference.
  H₁ : RF-fair memiliki F1-Score yang tidak lebih rendah (non-inferior) dan menunjukkan pengurangan signifikan pada Demographic Parity Difference dibanding RF-standar.
  Threshold              : Signifikansi statistik α = 0.05 untuk uji perbedaan F1 (paired bootstrap atau McNemar/paired t-test pada metrik yang sesuai); fairness target: DPD < 0.10 (10 percentage points) atau pengurangan DPD yang signifikan secara statistik.
  Justifikasi threshold  : α=0.05 adalah standar statistik; DPD < 0.10 sering dijadikan ambang praktis untuk membatasi bias sementara bukti domain-specific dapat menyesuaikan ambang ini.

---

## Latihan 1 — Dari Gap ke RQ

**Gap dari WS-03:** Belum ada kerangka evaluasi yang menggabungkan akurasi, fairness, dan privasi pada konteks HR Indonesia (Method + Context gap).

**RQ versi pertama (tulis bebas):**
> Apakah model yang dirancang untuk mengurangi bias demografis dapat mempertahankan akurasi prediksi turnover pada dataset HR Indonesia?

**Evaluasi RQ:**

| Komponen | Ada? | Isi |
|----------|------|-----|
| Metode spesifik | Ya | `RF-fair` vs `RF-standar` |
| Metrik terukur | Ya | F1-Score, DPD, EOD |
| Baseline | Ya | RF-standar |
| Dataset/konteks | Ya | Dataset HR perusahaan Indonesia |

**Tipe RQ:** [x] Comparison / [ ] Improvement / [ ] Exploratory

**RQ versi revisi (setelah evaluasi):**
> Apakah `fairness-aware Random Forest` menghasilkan F1-Score setidaknya setara dan Demographic Parity Difference lebih kecil dibanding `Random Forest` standar pada dataset HR perusahaan Indonesia untuk prediksi turnover dalam 12 bulan?

---

## Latihan 2 — Hypothesis Pair

Rumuskan pasangan hipotesis dari RQ di Latihan 1.

| Komponen | Isi |
|----------|-----|
| H₀ | Tidak ada perbedaan signifikan pada F1-Score antara RF-fair dan RF-standar, dan RF-fair tidak mengurangi DPD secara signifikan |
| H₁ | RF-fair memiliki F1-Score non-inferior (margin non-inferiority 0.02) dan mengurangi DPD secara signifikan dibanding RF-standar |
| Metrik | F1-weighted, Demographic Parity Difference (DPD), p-value (α=0.05) |
| Threshold | α=0.05 untuk uji statistik; margin non-inferiority F1 = 0.02; fairness practical target: DPD < 0.10 |
| Justifikasi threshold | α=0.05 adalah standar; margin F1 0.02 kecil namun praktis; DPD < 0.10 adalah ambang praktis untuk pembatasan bias sementara diskusi domain-specific diperlukan |

**Apakah hipotesis ini falsifiable?** [x] Ya / [ ] Tidak
> Bagaimana cara membuktikannya salah? Dengan eksperimen komparatif: jika RF-fair menunjukkan F1 lebih rendah dari margin non-inferiority atau tidak menurunkan DPD (tidak signifikan), H₁ ditolak.

---

## Latihan 3 — Rantai Operasionalisasi

Lengkapi rantai dari RQ hingga metode analisis.

| Tahap | Isi |
|-------|-----|
| RQ | Apakah RF-fair menghasilkan F1-Score setidaknya setara dan DPD lebih rendah dibanding RF-standar pada tugas prediksi turnover? |
| Variable (IV) | Jenis model: `RF-standar` vs `RF-fair` |
| Variable (DV) | F1-Score (weighted), Demographic Parity Difference (DPD), Equal Opportunity Difference (EOD) |
| Metric | F1-weighted (utama), DPD, EOD, p-value uji statistik, effect size (Cohen's d) |
| Data source | Dataset HR perusahaan Indonesia (fitur demografis + pekerjaan + outcome turnover 12 bulan). Jika tidak tersedia: kumpulkan multi-organisasi anonim atau buat dataset sintetis terkalibrasi. |
| Analysis method | Preprocessing (imputasi, balancing/stratified sampling), cross-validation berulang (stratified k-fold), per-fold per-model metrik, paired statistical test (bootstrap paired difference untuk F1), uji signifikan untuk DPD (bootstrap CI), analisis trade-off accuracy-fairness. Laporkan privasi/fitur sensitif; evaluasi opsi differential privacy jika relevan. |

**Apakah rantai lengkap?** [x] Ya / [ ] Tidak
> Jika tidak, tahap mana yang perlu direvisi? — N/A

---

## Refleksi

**Judul:** Implementasi ML untuk rekrutmen & prediksi turnover (kumpulan studi di WS-03)
**RQ yang diekstrak:** Apakah model yang mengintegrasikan fairness dapat mempertahankan akurasi sekaligus mengurangi bias demografis pada prediksi turnover di konteks HR Indonesia?
**Komponen yang hilang:** Dataset HR Indonesia yang representatif; evaluasi fairness dan privasi.

