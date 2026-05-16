# WS-02: Problem Statement

> **Bab 2 — Problem Formulation & System Context**

---

## Ringkasan Materi

### Problem Formation Model

Masalah riset melewati 5 tahap transformasi. Melompat langsung dari Reality ke Variable adalah kesalahan paling umum.

```
Reality → Observed Issue (Symptom) → Diagnosed Problem (Root Cause)
→ Researchable Problem (Scoped) → Measurable Variable (Operationalized)
```

### Topic ≠ Problem ≠ Research Problem

| Level | Contoh | Status |
|-------|--------|--------|
| **Topik** | Keamanan IoT | Terlalu luas, tidak bisa diuji |
| **Problem** | MQTT tidak terenkripsi | Spesifik tapi belum riset |
| **Research Problem** | Belum ada studi membandingkan overhead TLS 1.3 vs DTLS pada MQTT di IoT RAM < 64KB | Bisa dirancang eksperimennya |

### Symptom vs Root Cause

Apa yang diamati (gejala) ≠ mengapa terjadi (akar masalah). Gunakan **5 Whys** atau **Fishbone Diagram** untuk menggali.

Contoh: "User meninggalkan checkout" (symptom) → "Waktu loading > 8 detik karena API call sequential" (root cause).

### System Thinking

Setiap masalah riset TI harus terikat pada komponen sistem: **Input → Process → Output → Outcome → Constraints → Stakeholders**.

### Problem Quality Check

Masalah riset yang layak harus memenuhi 5 kriteria:
- **Clarity** — Satu orang membaca akan paham
- **Measurability** — Ada metrik kuantitatif
- **Relevance** — Penting untuk domain
- **Testability** — Bisa gagal (falsifiable)
- **Impact** — Ada kontribusi jika terjawab

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan | Menyelesaikan masalah (*solve*) | Memahami dan membuktikan (*understand & prove*) |
| Masalah | Bug, error, fitur belum ada | Gap dalam pengetahuan |
| Scope | Selesaikan semua yang perlu | Batasi agar bisa dibuktikan |
| Output | Working system | Evidence, paper, replicable findings |

### Istilah Penting

- **Problem Statement** — Formulasi tertulis: konteks sistem + gap + dampak + justifikasi
- **System Context** — Deskripsi lengkap: input, proses, output, outcome, constraints, stakeholders
- **Problem Drift** — Masalah "bermutasi" dari pendahuluan ke metodologi karena statement awal tidak presisi
- **Solution-First Thinking** — Memulai dari solusi tanpa masalah yang jelas — berbahaya dalam riset
- **Operational Definition** — Definisi variabel yang cukup jelas agar peneliti lain bisa mengukur hal yang sama

---

## A.2 — Problem Statement Builder

```
PROBLEM STATEMENT BUILDER

Domain & Konteks
  Domain   : Analitik Finansial dan Prediksi Harga Saham
  Konteks  : Prediksi harga penutupan harian saham perbankan (BBRI) menggunakan machine learning

System Context
  Input       : Data historis harga saham BBRI (OHLCV) periode 2015-2025 dari Investing.com/Yahoo Finance
  Process     : Preprocessing (MinMax scaling, windowing), pelatihan model (LSTM vs XGBoost), prediksi time-series
  Output      : Prediksi harga penutupan harian saham BBRI dan nilai error (RMSE, MAE, MAPE, R2)
  Outcome     : Informasi prediksi yang akurat untuk mendukung pengambilan keputusan investasi
  Constraints : Volatilitas pasar yang tinggi, pengaruh berita makroekonomi yang tidak ada dalam data historis
  Stakeholders: Investor, analis keuangan, peneliti algoritma time-series

Fenomena → Problem
  Fenomena yang diamati             : Fluktuasi harga saham BBRI sering kali tidak linear dan sulit diprediksi dengan metode statistik klasik
  Gejala (symptom) yang terukur     : Error prediksi tinggi (RMSE/MAE besar) pada metode tradisional seperti regresi linear atau ARIMA saat menghadapi data saham yang volatil
  Masalah yang didiagnosis          : Model tradisional gagal menangkap pola non-linear kompleks dan dependensi jangka panjang dalam data deret waktu saham
  Masalah riset (researchable)      : Belum diketahui secara pasti apakah model deep learning (LSTM) secara konsisten menghasilkan error prediksi (MAE/RMSE) lebih rendah dibanding model ensemble yang kuat (XGBoost) pada data BBRI (2015-2025)
  Variabel yang terukur             : Jenis model (LSTM vs XGBoost) sebagai variabel independen, serta RMSE, MAE, dan R2 sebagai variabel dependen

Problem Quality Check
  [x] Clarity — Apakah satu orang membaca akan paham?
  [x] Measurability — Apakah ada metrik kuantitatif?
  [x] Relevance — Apakah penting untuk domain?
  [x] Testability — Apakah bisa gagal?
  [x] Impact — Apakah ada kontribusi jika terjawab?

Problem Statement (1 paragraf):
  Prediksi harga saham BBRI merupakan tantangan yang kompleks akibat tingginya volatilitas pasar dan pola data non-linear yang sulit dimodelkan oleh algoritma time-series klasik. Meskipun metode machine learning seperti XGBoost telah menunjukkan kinerja yang baik, model deep learning seperti Long Short-Term Memory (LSTM) secara teoritis lebih mampu menangkap pola dependensi jangka panjang. Namun, belum ada bukti konklusif mengenai mana yang lebih superior secara konsisten untuk data spesifik saham BBRI. Oleh karena itu, masalah riset yang dirumuskan adalah menguji perbandingan kinerja antara LSTM dan XGBoost pada dataset harga penutupan harian BBRI (2015-2025) untuk membuktikan model mana yang mampu memberikan tingkat error prediksi (MAE dan RMSE) lebih rendah serta goodness-of-fit (R2) yang lebih tinggi.
```

---

## Latihan 1 — Dari Topik ke Masalah Riset

Pilih satu topik di bidang TI yang diminati. Transformasikan melalui 5 tahap Problem Formation Model.

**Topik awal:** Prediksi harga saham BBRI menggunakan machine learning (LSTM vs XGBoost)

| Tahap | Hasil |
|-------|-------|
| Reality | Investor membutuhkan prediksi harga saham yang akurat untuk pengambilan keputusan, namun pergerakan harga BBRI sangat fluktuatif. |
| Observed Issue (Symptom) | Prediksi sering meleset jauh dari harga aktual saat menggunakan metode analisis teknikal atau statistik tradisional. |
| Diagnosed Problem (Root Cause) | Metode tradisional tidak mampu memodelkan pola non-linear dan hubungan sekuensial jangka panjang pada data deret waktu finansial. |
| Researchable Problem | Belum diketahui secara pasti sejauh mana penurunan error (RMSE/MAE) yang bisa dicapai jika menggunakan LSTM dibandingkan baseline model populer XGBoost pada saham BBRI (2015-2025). |
| Measurable Variable | Jenis model (LSTM vs XGBoost) dan error prediksi (RMSE, MAE, R2). |

**Apakah terjebak solution-first thinking?** [ ] Ya / [x] Tidak
> Jika ya, kembali ke tahap mana? -

---

## Latihan 2 — System Context Decomposition

Gambarkan konteks sistem dari masalah riset di Latihan 1.

| Komponen | Deskripsi |
|----------|----------|
| Input | Data sekunder harga historis BBRI (Open, High, Low, Close, Volume) 2015-2025 dari Yahoo Finance. |
| Process | Pembersihan data, normalisasi (MinMax), pembentukan sequence (windowing), training LSTM/XGBoost, dan komparasi hasil. |
| Output | Nilai prediksi harga saham dan perhitungan metrik evaluasi (RMSE, MAE, R2). |
| Outcome | Evaluasi model terbaik yang dapat direkomendasikan sebagai sistem peringatan/prediksi pendukung investasi. |
| Constraints | Volatilitas tinggi, kondisi pasar makro (inflasi, krisis) tidak dimodelkan, batasan komputasi training LSTM. |
| Stakeholders | Investor ritel/institusi, analis pasar modal, peneliti time-series forecasting. |

**Komponen mana yang paling relevan dengan masalah riset?** Process dan Output

---

## Latihan 3 — Problem Quality Check

Evaluasi problem statement yang sudah dibuat menggunakan 5 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Clarity | 5 | Masalah dinyatakan dengan jelas dengan komparasi dua metode spesifik pada dataset spesifik. |
| Measurability | 5 | Variabel terukur menggunakan metrik standar regresi (RMSE, MAE, R2). |
| Relevance | 5 | Prediksi harga saham bank terbesar di Indonesia sangat relevan untuk komunitas keuangan dan riset AI. |
| Testability | 5 | Eksperimen mudah direplikasi dengan membagi train/test set secara kronologis dan menghitung error. |
| Impact | 4 | Berkontribusi memberikan bukti empiris perbandingan arsitektur time-series modern pada kasus pasar lokal. |

**Skor total:** 24 / 25

**Problem statement versi final (1 paragraf):**
> Prediksi harga saham BBRI di pasar modal Indonesia masih menantang karena dinamika fluktuasinya yang kompleks dan non-linear, sehingga sering kali model tradisional menghasilkan error prediksi yang besar. Problem riset yang diajukan adalah menguji keunggulan Long Short-Term Memory (LSTM) dalam menangkap dependensi data waktu jangka panjang dibandingkan dengan baseline kuat eXtreme Gradient Boosting (XGBoost). Melalui eksperimen menggunakan data historis harian periode 2015-2025, penelitian ini akan membuktikan metode manakah yang secara konsisten memberikan nilai MAE dan RMSE yang lebih rendah, serta R2 yang lebih tinggi, sehingga dapat menjadi rekomendasi ilmiah bagi pengembangan sistem prediksi pasar modal lokal.

---

## Refleksi

> Bandingkan "masalah" yang biasa ditemui saat coding (bug, error) dengan masalah riset. Apa perbedaan fundamental dalam cara mendefinisikan dan mendekati keduanya?

**Jawaban:**
> Masalah saat coding biasanya bersifat deterministik: ada perilaku yang diharapkan, ada gejala error, lalu diperbaiki sampai sistem kembali benar. Fokusnya adalah penyelesaian cepat terhadap penyebab teknis yang spesifik.
> Masalah riset bersifat epistemik: yang dicari adalah gap pengetahuan yang belum terjawab, sehingga perlu definisi variabel, batasan konteks, hipotesis yang bisa diuji, dan bukti yang dapat direplikasi. Jadi, pendekatannya bukan hanya “memperbaiki”, tetapi “membuktikan” dengan metode yang terukur.
