# WS-05: Variabel & Metrik

> **Bab 5 — Metric, Measurement & Data**

---

## Ringkasan Materi

### Measurement Alignment Model

Setiap pengukuran yang valid harus bisa ditelusuri melalui rantai ini tanpa lompatan logis:

```
Problem → Concept → Variable → Metric → Data → Result
```

### Operationalization = Keputusan Desain

Menerjemahkan konsep abstrak menjadi variabel terukur bukan proses mekanis. "Code quality" yang diukur via SonarQube code smells membawa asumsi implisit. Setiap operasionalisasi harus didokumentasikan dan dijustifikasi.

### Empat Tipe Data (NOIR)

| Tipe | Ciri | Contoh | Operasi Valid |
|------|------|--------|---------------|
| **Nominal** | Kategori, tanpa urutan | Jenis algoritma (RF, SVM, CNN) | Modus, chi-square |
| **Ordinal** | Urutan, interval tidak sama | Skala Likert (1-5) | Median, Spearman |
| **Interval** | Jarak bermakna, tanpa nol absolut | Suhu Celsius | Mean, Pearson, t-test |
| **Ratio** | Jarak bermakna + nol absolut | Waktu eksekusi (ms) | Semua operasi |

Tipe data menentukan uji statistik yang valid. Kebanyakan metrik performa TI = ratio; persepsi pengguna = ordinal.

### Kriteria Pemilihan Metrik

- **Representative** — Mewakili konsep yang diteliti
- **Sensitive** — Cukup peka menangkap perbedaan bermakna (hindari ceiling effect)
- **Feasible** — Bisa dikumpulkan dalam batasan waktu dan biaya

### Pre-registration

Metrik harus ditentukan **sebelum** eksperimen. Memilih metrik setelah melihat data = **p-hacking**. Metrik tambahan yang ditemukan kemudian dilaporkan sebagai *exploratory*, bukan *confirmatory*.

### Primary vs Secondary Metric

- **Primary Metric** — Langsung terikat ke hipotesis, menentukan kesimpulan
- **Secondary Metric** — Pendukung, dilaporkan di samping primary; statusnya suplementer

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Pemilihan metrik | Berdasarkan kebiasaan/tool yang ada | Berdasarkan construct validity |
| Anomali | Dihapus untuk laporan bersih | Diinvestigasi — bisa jadi temuan |
| Kapan dipilih | Setelah sistem jadi (monitoring) | Sebelum eksperimen (by design) |

### Istilah Penting

- **Operationalization** — Transformasi konsep abstrak menjadi variabel terukur
- **Construct Validity** — Sejauh mana pengukuran benar-benar mengukur konsep yang dimaksud
- **Measurement Scale** — Klasifikasi data (NOIR) yang menentukan analisis valid
- **Multi-metric Evaluation** — Menggunakan beberapa metrik untuk menangkap konsep kompleks

---

## Template A.5 — Definisi Variabel, Metrik & Justifikasi

```
VARIABLE & METRIC DEFINITION

Research Question: Apakah LSTM menghasilkan MAE dan RMSE lebih rendah serta R2 lebih tinggi dibanding baseline XGBoost pada dataset harga penutupan harian saham BBRI (2015-2025) dari Investing.com/Yahoo Finance?

| Variabel | Tipe | Konsep | Metrik | Skala | Satuan | Cara Mengukur | Justifikasi |
|----------|------|--------|--------|-------|--------|---------------|-------------|
| Jenis model (LSTM vs XGBoost) | IV   | Metode prediksi time series | Kategori model | Nominal | - | Set `model_type` di config eksperimen | RQ perbandingan dua model; sejalan dengan studi komparatif di paper/ws-03 (Alkayes & Sugihartono 2025; Aprilia et al. 2026). |
| Akurasi prediksi harga saham | DV   | Error prediksi dan goodness-of-fit | RMSE, MAE (primary), R2 dan MAPE (secondary) | Ratio | Rupiah, %, unitless | Hitung error antara y_pred dan y_true pada test set | Metrik ini umum di literatur prediksi saham (Alkayes & Sugihartono 2025; Rosyd et al. 2024; Aprilia et al. 2026). |
| Dataset dan konfigurasi tetap | CV   | Kondisi eksperimen konstan | Split ratio, window size, scaler, seed | Nominal/Ratio | - | Dicatat di config/log dan diverifikasi ulang | Mengisolasi pengaruh model, mencegah bias perbandingan. |

Alignment Check:
  RQ → Concept → Variable → Metric → Data → Result
  [x] Setiap langkah terdokumentasi
  [x] Tidak ada "lompatan logis"
  [x] Metrik mengukur apa yang dimaksud (construct validity)
```

---

## Latihan 1 — Operationalization Chain

Gunakan RQ dari WS-04. Definisikan variabel dan metriknya.

**RQ:** Apakah LSTM menghasilkan MAE dan RMSE lebih rendah serta R2 lebih tinggi dibanding baseline XGBoost pada dataset harga penutupan harian saham BBRI (2015-2025) dari Investing.com/Yahoo Finance?

| Variabel | Tipe | Konsep Abstrak | Metrik Konkret | Skala (NOIR) | Satuan |
|----------|------|---------------|----------------|-------------|--------|
| Jenis model | IV | Algoritma prediksi time series | LSTM vs XGBoost | Nominal | - |
| Akurasi prediksi harga saham | DV | Error prediksi | RMSE, MAE, R2, MAPE | Ratio | Rupiah, %, unitless |
| Konfigurasi eksperimen | CV | Kondisi tetap | Split 80/20, window 30, MinMax, seed 42 | Nominal/Ratio | - |

**Apakah ada lompatan logis dalam rantai?** [ ] Ya / [x] Tidak
> Jika ya, di mana? N/A

---

## Latihan 2 — Evaluasi Metrik

Evaluasi metrik DV yang dipilih di Latihan 1 menggunakan 3 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Representative | 5 — RMSE dan MAE langsung mengukur error prediksi harga | |
| Sensitive | 4 — peka terhadap perbedaan model pada error | |
| Feasible | 5 — perhitungan sederhana dari y_true vs y_pred | |

**Apakah perlu secondary metric?** [x] Ya / [ ] Tidak
> Jika ya, apa dan mengapa? R2 untuk goodness-of-fit dan MAPE untuk interpretasi error relatif.

**Contoh kasus ceiling effect untuk metrik ini:**
> Jika harga saham stabil dan variasi kecil, RMSE/MAE menjadi sangat kecil untuk kedua model sehingga perbedaan nyaris tidak terlihat.

---

## Latihan 3 — Data Quality Check

Bayangkan data yang akan dikumpulkan dari eksperimen. Evaluasi 4 dimensi kualitas data.

| Dimensi | Pertanyaan | Jawaban | Strategi Mitigasi |
|---------|-----------|---------|------------------|
| Completeness | *Apakah semua data point terkumpul?* | Ada missing value pada hari libur atau data tidak tercatat | Gunakan kalender perdagangan, isi missing dengan forward fill atau drop jika perlu, catat jumlah missing | |
| Consistency | *Apakah ada kontradiksi internal?* | Potensi duplikasi tanggal atau urutan tidak kronologis | Sort by date, hapus duplikasi, verifikasi satuan mata uang | |
| Validity | *Apakah benar-benar mengukur yang dimaksud?* | Outlier karena stock split atau anomali harga | Lakukan penyesuaian corporate action, cek outlier ekstrem | |
| Representativeness | *Apakah sampel mewakili populasi target?* | Hanya satu emiten (BBRI) dan satu periode | Nyatakan batasan; jika memungkinkan tambah emiten lain sebagai studi lanjutan | |

---

## Refleksi

> Mengapa memilih metrik setelah melihat data dianggap p-hacking? Apa bedanya dengan eksplorasi data yang sah?

**Jawaban:**
> Memilih metrik setelah melihat data meningkatkan risiko p-hacking karena metrik dipilih agar hasil terlihat signifikan.
> Eksplorasi data sah jika dilaporkan sebagai exploratory dan tidak digunakan untuk mengonfirmasi hipotesis utama yang sudah dipre-registrasi.
