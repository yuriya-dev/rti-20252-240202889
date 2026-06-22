# WS-09: Implementation & Environment

> **Bab 9 — Implementasi Riset & Kontrol Lingkungan**

---

## Ringkasan Materi

### Implementasi Riset ≠ Coding Biasa

Tujuan implementasi riset bukan membuat software yang berfungsi, melainkan membangun **instrumen pengukuran yang konsisten**. Setiap modul harus di-mapping ke variabel (dari Bab 6), parameter harus config-driven, dan logging aktif dari hari pertama.

### Reproducible Implementation Model

```
Design → Implementation → Environment Setup → Execution Consistency → Reproducibility → Trustworthy Result
```

Setiap transisi memiliki syarat:
- Design → Implementation: kode sesuai mapping variabel-ke-komponen
- Implementation → Environment: versi, dependency, seed, path, OS eksplisit
- Environment → Consistency: seed terkunci, urutan deterministik
- Consistency → Reproducibility: dokumentasi lengkap
- Reproducibility → Trust: siapa pun ikuti dokumentasi → hasil sama/serupa

### Repeatability vs Reproducibility

| Level | Peneliti | Environment | Hasil |
|-------|---------|-------------|-------|
| **Repeatability** | Sama | Sama | Sama persis |
| **Reproducibility** | Berbeda | Berbeda (ikuti docs) | Sama/serupa |

Capai **repeatability** dulu, baru **reproducibility**.

### Engineering vs Research Perspective

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan | Sistem berfungsi untuk user | Instrumen pengukuran konsisten |
| Dependency | Update ke terbaru | Lock di versi spesifik |
| Testing | Unit, integration, E2E | Repeatability test (run ulang → sama?) |
| Dokumentasi | User guide, API docs | Environment spec, execution steps, expected output |
| Config | Default masuk akal | Setiap parameter eksplisit & adjustable |

### Jebakan Kognitif

1. Menunda environment setup → bug sulit dilacak
2. Tidak pakai version control → hasil tidak bisa direkonstruksi
3. Menolak Docker/container → "di laptop saya bisa" saat review
4. 3× hasil sama ≠ repeatable (bisa cache/state tersimpan)

### Istilah Penting

- **Environment Specification** — Deskripsi lengkap: hardware, OS, runtime, library + versi, config, seed
- **Dependency** — Komponen eksternal yang harus di-lock versinya
- **Config-driven** — Parameter dieksternalisasi ke file konfigurasi, bukan hardcode

---

## Template A.9 — Dokumentasi Setup Eksperimen

```
EXPERIMENT SETUP DOCUMENTATION

Hardware:
  CPU     : Apple M2 (8 Cores)
  RAM     : 16 GB
  GPU     : Apple M2 (Integrated)
  Storage : SSD

Software:
  OS        : macOS 26.5.1
  Runtime   : Python 3.9.6
  Framework : TensorFlow 2.20.0, Keras 3.10.0, XGBoost 2.1.4

Dependencies:
| Library | Version | Sumber | Hash/Checksum |
|---------|---------|--------|---------------|
| tensorflow | 2.20.0 | PyPI | - |
| xgboost | 2.1.4 | PyPI | - |
| scikit-learn | 1.6.1 | PyPI | - |
| pandas | 2.3.3 | PyPI | - |
| numpy | 2.0.2 | PyPI | - |
| yfinance | 0.2.66 | PyPI | - |

Konfigurasi:
  Config file     : riset-directory/05-kode/config.json
  Random seed     : 42
  Hyperparameters : LSTM (units: 50/100, dropout: 0.2, learning_rate: 0.001); XGBoost (max_depth: 3/5/7, learning_rate: 0.05, n_estimators: 100/500)

Reproducibility Check:
  [x] Dependency terdokumentasi (requirements.txt / lock file)
  [x] Seed ditetapkan di semua level (Python, NumPy, framework)
  [x] Config di version control
  [x] README instruksi reproduksi lengkap
```

---

## Latihan 1 — Environment Specification

Dokumentasikan environment untuk eksperimen Anda (boleh environment saat ini atau yang direncanakan).

| Komponen | Spesifikasi |
|----------|------------|
| CPU | Apple M2 (8 Cores) |
| RAM | 16 GB |
| GPU | Apple M2 Integrated |
| OS | macOS 26.5.1 |
| Runtime | Python 3.9.6 |
| Framework | TensorFlow 2.20.0, Keras 3.10.0, XGBoost 2.1.4 |
| Random Seed | 42 |

**Dependencies (minimal 5):**

| Library | Version | Alasan Dibutuhkan |
|---------|---------|-------------------|
| tensorflow | 2.20.0 | Pembuatan dan pelatihan model deep learning LSTM |
| xgboost | 2.1.4 | Pembuatan dan pelatihan model baseline XGBoost |
| scikit-learn | 1.6.1 | Pembagian dataset, pencarian hyperparameter, dan perhitungan metrik evaluasi (RMSE, MAE, R2) |
| pandas | 2.3.3 | Manipulasi dan analisis data runtun waktu (time-series) harga saham |
| numpy | 2.0.2 | Operasi aljabar linier dan transformasi array / matriks data |
| yfinance | 0.2.66 | Mengunduh data historis harga saham BBRI (OHLCV) secara otomatis |

---

## Latihan 2 — Repeatability Test Plan

Rancang tes repeatability sederhana: jalankan kode yang sama 3× di environment yang sama.

| Run | Seed | Metrik Utama | Hasil Sama? |
|-----|------|-------------|-------------|
| 1 | 42 | RMSE (regresi) | — |
| 2 | 42 | RMSE (regresi) | [x] Ya / [ ] Tidak |
| 3 | 42 | RMSE (regresi) | [x] Ya / [ ] Tidak |

**Jika hasil berbeda, kemungkinan penyebab:**
> Keberadaan sifat non-deterministik pada operasi GPU/CPU di TensorFlow/Keras jika variabel lingkungan `TF_DETERMINISTIC_OPS=1` tidak disetel, atau terjadi perbedaan inisialisasi bobot acak jika seed tidak dikunci pada level Python, NumPy, dan TensorFlow secara bersamaan.

**Checklist kontrol yang sudah diterapkan:**
- [x] Random seed di-set di semua level (Python, NumPy, TensorFlow)
- [x] Tidak ada background process yang mengganggu
- [x] Cache dibersihkan antar-run
- [x] Config file yang sama untuk semua run

---

## Latihan 3 — README Eksperimen

Tulis README minimum untuk eksperimen Anda (6 komponen wajib).

```
# Judul Eksperimen: Prediksi Harga Saham BBRI Menggunakan LSTM vs XGBoost

## 1. Environment
- CPU: Apple M2 (8 Cores)
- RAM: 16 GB
- OS: macOS 26.5.1
- Runtime: Python 3.9.6
- Framework: TensorFlow 2.20.0, XGBoost 2.1.4

## 2. Installation
Langkah instalasi:
```bash
pip install tensorflow==2.20.0 xgboost==2.1.4 scikit-learn==1.6.1 pandas==2.3.3 numpy==2.0.2 yfinance==0.2.66 matplotlib==3.9.4
```

## 3. Data
- Sumber: Yahoo Finance API (BBRI.JK)
- Format: CSV (OHLCV)
- Ukuran: ~2.500 baris (data harian dari tahun 2015 s.d. 2025)

## 4. Execution
Jalankan pipeline pengujian:
```bash
python 05-kode/evaluate.py
```

## 5. Configuration
File konfigurasi: `05-kode/config.json`
Parameter kunci:
- Random Seed: 42
- Window Size: 30 hari
- Split Ratio: 80% train, 20% test

## 6. Expected Output
1. Output metrik evaluasi (RMSE, MAE, R2) dalam terminal atau file CSV:
   - Model XGBoost: RMSE ~200, MAE ~150, R2 ~0.90
   - Model LSTM: RMSE ~150, MAE ~120, R2 ~0.93
2. Gambar grafik perbandingan harga aktual vs prediksi di `06-output/figures/prediction_vs_actual.png`.
```

---

## Refleksi

> Apakah eksperimen Anda saat ini bisa direproduksi oleh orang lain tanpa bantuan Anda? Komponen apa yang masih hilang?

**Level saat ini:** [x] Repeatability / [ ] Reproducibility / [ ] Belum keduanya
**Komponen yang belum terdokumentasi:**
> File requirements.txt yang diekspor secara formal dan tersimpan di version control, serta konfigurasi environment khusus untuk memastikan determinisme pada Mac Silicon (M2 GPU/Metal acceleration).
