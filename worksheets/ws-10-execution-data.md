# WS-10: Experiment Execution & Data Collection

> **Bab 10 — Eksekusi Eksperimen & Pengumpulan Data**

---

## Ringkasan Materi

### Experiment Execution Pipeline

```
Design → Execution Plan → Controlled Execution → Data Collection → Data Logging → Dataset for Analysis
```

### Multiple Run = Non-Negotiable

Single run **tidak pernah cukup** untuk klaim ilmiah. Minimum 5-10 run per skenario dengan seed berbeda. Multiple run menghasilkan:
- Mean, std, confidence interval
- Distribusi hasil → uji statistik
- Variabilitas → error bar di grafik

### Execution Plan

Setiap eksperimen harus memiliki plan sebelum eksekusi:
- Daftar skenario
- Jumlah run per skenario
- Random seed per run (pre-determined!)
- Urutan eksekusi (randomisasi/counterbalancing)
- Pre-execution checklist

### Data Logging Komprehensif

Setiap run menghasilkan log terstruktur:
1. **Identitas** — Run ID, timestamp, skenario
2. **Konfigurasi** — Semua parameter, seed, code version
3. **Hasil** — Semua metrik, output detail
4. **Metadata** — Waktu eksekusi, resource usage, warning/error

Format: CSV/JSON/database — **bukan stdout yang di-copy-paste**.

### Engineering vs Research Execution

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Run | Sekali (deploy) | Multiple (min 5-10, seed berbeda) |
| Logging | Error log, access log | Semua parameter, metrik, metadata |
| Anomali | Bug → fix → redeploy | Investigasi → dokumentasi → analisis |
| Urutan | Tidak penting | Bisa bias — perlu randomisasi |

### Anomali = Dokumentasi, Bukan Hapus

Run gagal/anomali tidak boleh dihapus tanpa dokumentasi. Bisa jadi:
- **Bug** → fix & re-run (dokumentasikan!)
- **Batas kemampuan metode** → DNF = temuan
- **Data yang bias** jika hanya simpan run "berhasil"

### Jebakan Kognitif

1. "Satu angka cukup" → tanpa distribusi, tidak bisa diuji
2. "Seed tidak penting" → bahkan algoritma deterministik bisa dipengaruhi library stokastik
3. "Run gagal langsung hapus" → kehilangan temuan potensial
4. "Semua run harus hari ini" → thermal throttling, fatigue

---

## Template A.10 — Execution Plan & Data Log

```
EXECUTION PLAN (LSTM vs XGBoost vs Hybrid Stacking)

| Run # | Skenario | Seed | Parameter | Status | Waktu | Output Folder |
|-------|----------|------|-----------|--------|-------|---------------|
| 1     | LSTM vs XGB vs Hybrid | 43 | window=60, epochs=100, batch=32 | Completed | ~30s | 06-output/run-1 |
| 2     | LSTM vs XGB vs Hybrid | 44 | window=60, epochs=100, batch=32 | Completed | ~30s | 06-output/run-2 |
| 3     | LSTM vs XGB vs Hybrid | 45 | window=60, epochs=100, batch=32 | Completed | ~30s | 06-output/run-3 |
| 4     | LSTM vs XGB vs Hybrid | 46 | window=60, epochs=100, batch=32 | Completed | ~30s | 06-output/run-4 |
| 5     | LSTM vs XGB vs Hybrid | 47 | window=60, epochs=100, batch=32 | Completed | ~30s | 06-output/run-5 |
| 6     | LSTM vs XGB vs Hybrid | 48 | window=60, epochs=100, batch=32 | Completed | ~30s | 06-output/run-6 |
| 7     | LSTM vs XGB vs Hybrid | 49 | window=60, epochs=100, batch=32 | Completed | ~30s | 06-output/run-7 |
| 8     | LSTM vs XGB vs Hybrid | 50 | window=60, epochs=100, batch=32 | Completed | ~30s | 06-output/run-8 |
| 9     | LSTM vs XGB vs Hybrid | 51 | window=60, epochs=100, batch=32 | Completed | ~30s | 06-output/run-9 |
| 10    | LSTM vs XGB vs Hybrid | 52 | window=60, epochs=100, batch=32 | Completed | ~30s | 06-output/run-10 |

Jumlah runs per skenario : 10
Total runs               : 10 (masing-masing mengevaluasi 3 model)

DATA LOG (Hasil Rata-rata Seluruh Run):
  Skenario 1 - LSTM Baseline:
    MAE : 229.0273 ± 26.4501 Rp
    RMSE: 301.6060 ± 30.9412 Rp
    R²  : 0.5901 ± 0.0808
    MAPE: 5.5588% ± 0.6445%
  Skenario 2 - XGBoost Baseline:
    MAE : 126.1506 ± 4.5945 Rp
    RMSE: 188.5673 ± 4.0398 Rp
    R²  : 0.8412 ± 0.0068
    MAPE: 3.1385% ± 0.1263%
  Skenario 3 - Hybrid LSTM→XGBoost Stacking:
    MAE : 128.6106 ± 6.6277 Rp
    RMSE: 193.7625 ± 5.4648 Rp
    R²  : 0.8323 ± 0.0095
    MAPE: 3.1868% ± 0.1862%
```

---

## Latihan 1 — Execution Plan

Berikut adalah execution plan riil yang telah kita jalankan untuk membandingkan performa model LSTM, XGBoost, dan Hybrid Stacking pada testing set saham BBRI.

| Run # | Skenario | Seed | Parameter Kunci | Status |
|-------|----------|------|----------------|--------|
| 1 | LSTM vs XGBoost vs Hybrid | 43 | window=60, epoch=100, batch=32, n_est=500 | Completed |
| 2 | LSTM vs XGBoost vs Hybrid | 44 | window=60, epoch=100, batch=32, n_est=500 | Completed |
| 3 | LSTM vs XGBoost vs Hybrid | 45 | window=60, epoch=100, batch=32, n_est=500 | Completed |
| 4 | LSTM vs XGBoost vs Hybrid | 46 | window=60, epoch=100, batch=32, n_est=500 | Completed |
| 5 | LSTM vs XGBoost vs Hybrid | 47 | window=60, epoch=100, batch=32, n_est=500 | Completed |
| 6 | LSTM vs XGBoost vs Hybrid | 48 | window=60, epoch=100, batch=32, n_est=500 | Completed |
| 7 | LSTM vs XGBoost vs Hybrid | 49 | window=60, epoch=100, batch=32, n_est=500 | Completed |
| 8 | LSTM vs XGBoost vs Hybrid | 50 | window=60, epoch=100, batch=32, n_est=500 | Completed |
| 9 | LSTM vs XGBoost vs Hybrid | 51 | window=60, epoch=100, batch=32, n_est=500 | Completed |
| 10 | LSTM vs XGBoost vs Hybrid | 52 | window=60, epoch=100, batch=32, n_est=500 | Completed |

**Total skenario:** 3 (LSTM, XGBoost, Hybrid Stacking)
**Run per skenario:** 10
**Total run keseluruhan:** 10 (masing-masing run membandingkan ketiga skenario)

---

## Latihan 2 — Data Log Terstruktur

Desain format data log untuk eksperimen Anda. Tentukan field apa saja yang akan dicatat.

**Identitas:**
| Field | Contoh |
|-------|--------|
| Run ID | run-xgb-001 |
| Timestamp | 2026-06-22T22:45:00 |
| Scenario Name | XGBoost Baseline |

**Konfigurasi:**
| Field | Contoh |
|-------|--------|
| Seed | 42 |
| Code version | commit 54b8a3b |
| Dataset Path | riset-directory/04-data/bbri_clean.csv |
| Hyperparameters | {'max_depth': 5, 'n_estimators': 500} |

**Hasil:**
| Metrik | Tipe Data | Range Valid |
|--------|----------|-------------|
| RMSE | float | 0.0 - inf |
| MAE | float | 0.0 - inf |
| R2 Score | float | -inf - 1.0 |

**Format output:** [x] CSV / [x] JSON / [ ] Database / [ ] Lainnya: ____

---

## Latihan 3 — Anomaly Protocol

Rencanakan bagaimana menangani anomali. Untuk setiap jenis, tentukan langkah yang diambil.

| Jenis Anomali | Contoh | Tindakan |
|---------------|--------|----------|
| Run gagal (crash) | OOM saat melatih LSTM dengan batch_size besar | Dokumentasikan run crash, turunkan batch_size (misal dari 256 ke 32), ulangi eksekusi, catat konsumsi memori tambahan. |
| Hasil ekstrem | Nilai R2 negatif atau RMSE sangat tinggi karena model divergen | Cek normalisasi fitur (apakah data uji ter-scale dengan MinMax yang sama dengan data latih), investigasi learning rate (turunkan learning rate), catat perbaikan. |
| Waktu eksekusi anomali | Pelatihan satu epoch LSTM memakan waktu >10 menit (biasanya ~10 detik) karena CPU throttling | Periksa background process di OS, dinginkan CPU, jalankan ulang run tersebut, dokumentasikan waktu run lambat. |
| Inkonsistensi dengan run lain | Metrik performa berbeda jauh antar seed (misal run 1 R2=0.92, run 2 R2=0.45) | Investigasi kestabilan inisialisasi bobot LSTM, tingkatkan ukuran data latih atau tambahkan regularisasi (Dropout), jalankan ulang dengan parameter teregulasi. |

**Prinsip:** Detect → Investigate → Document → Decide

---

## Refleksi

> Pernahkah Anda melaporkan hasil riset/tugas dari single run? Apa risikonya? Bagaimana multiple run mengubah kepercayaan terhadap hasil?

**Pengalaman sebelumnya:**
> Sering kali dalam tugas kuliah atau eksperimen awal, kami hanya menjalankan kode sekali (single run) dan langsung melaporkan hasil akurasinya. Risiko dari pendekatan ini adalah hasil tersebut bisa jadi merupakan "keberuntungan statistik" (statistical fluke) karena inisialisasi bobot acak atau pembagian data tertentu yang menguntungkan model secara kebetulan. Kami tidak mengetahui variansi performa dan rentabilitas model jika diterapkan pada data yang berbeda atau dengan inisialisasi yang berbeda.

**Yang akan dilakukan berbeda:**
> Dalam riset ini, kami telah menjalankan setiap skenario (LSTM, XGBoost, dan Hybrid Stacking) sebanyak 10 kali menggunakan 10 random seed yang berbeda (yaitu 43 s.d. 52). Kami menghitung rata-rata (mean) dan standar deviasi (standard deviation) dari RMSE, MAE, R², dan MAPE. Hal ini memberikan estimasi interval kepercayaan yang kuat dan membuktikan bahwa keunggulan performa model XGBoost Baseline atas LSTM dan Hybrid benar-benar signifikan secara statistik (p-value < 0.05 pada Wilcoxon Signed-Rank Test) untuk data BBRI, membantah asumsi awal bahwa model deep learning atau hybrid selalu lebih baik.
