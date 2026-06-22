# Dokumentasi Setup Eksperimen & Lingkungan Kerja

Dokumen ini mencatat spesifikasi hardware, software, dependensi, dan konfigurasi lingkungan kerja yang digunakan untuk menjalankan eksperimen perbandingan model LSTM dan XGBoost.

## 1. Spesifikasi Lingkungan (Environment Specification)

### Hardware
* **CPU:** Apple M2 (8 Cores)
* **RAM:** 16 GB
* **GPU:** Apple M2 (Integrated)
* **Storage:** Solid State Drive (SSD)

### Software
* **OS:** macOS 26.5.1
* **Runtime:** Python 3.9.6
* **Framework Utama:** TensorFlow 2.20.0, Keras 3.10.0, XGBoost 2.1.4

### Dependensi Pustaka (Library Dependencies)

| Pustaka | Versi | Sumber | Deskripsi / Alasan Dibutuhkan |
|---|---|---|---|
| `tensorflow` | 2.20.0 | PyPI | Pembuatan, penyetelan, dan pelatihan model deep learning LSTM |
| `xgboost` | 2.1.4 | PyPI | Pembuatan dan pelatihan model baseline ensemble XGBoost |
| `scikit-learn` | 1.6.1 | PyPI | Pembagian dataset train/test, data scaling, dan evaluasi metrik (RMSE, MAE, R2) |
| `pandas` | 2.3.3 | PyPI | Manipulasi, pembersihan, dan analisis data deret waktu saham |
| `numpy` | 2.0.2 | PyPI | Operasi matriks dan array multidimensi |
| `yfinance` | 0.2.66 | PyPI | Otomasi pengunduhan data historis harga saham BBRI dari Yahoo Finance |

---

## 2. Rencana Uji Keterulangan (Repeatability Test Plan)

Pengujian keterulangan dilakukan dengan mengeksekusi pipeline pelatihan model sebanyak 3 kali secara berturut-turut pada lingkungan kerja yang sama dengan mengunci nilai random seed.

| Pengujian | Seed | Metrik Utama | Hasil Konsisten? |
|---|---|---|---|
| Run 1 | 42 | RMSE (regresi) | — (Baseline) |
| Run 2 | 42 | RMSE (regresi) | Ya (Hasil identik) |
| Run 3 | 42 | RMSE (regresi) | Ya (Hasil identik) |

### Langkah-langkah Menjamin Determinisme:
1. Menetapkan random seed di tingkat sistem operasi (`PYTHONHASHSEED=0`).
2. Menetapkan seed pada pustaka numerik (`numpy.random.seed(42)`).
3. Menetapkan seed pada modul Python bawaan (`random.seed(42)`).
4. Menetapkan seed pada pustaka deep learning (`tensorflow.random.set_seed(42)`).

---

## 3. Petunjuk Reproduksi Eksperimen (README Eksperimen)

### Langkah 1: Persiapan Lingkungan Kerja
Instal seluruh pustaka dependensi yang dibutuhkan:
```bash
pip install tensorflow==2.20.0 xgboost==2.1.4 scikit-learn==1.6.1 pandas==2.3.3 numpy==2.0.2 yfinance==0.2.66 matplotlib==3.9.4
```

### Langkah 2: Struktur Berkas Kode
Pastikan file kode berada di lokasi berikut:
```
riset-directory/
└── 05-kode/
    ├── data_loader.py       # Preprocessing data
    ├── train_xgboost.py     # Training model XGBoost
    ├── train_lstm.py        # Training model LSTM
    ├── evaluate.py          # Evaluasi metrik performa
    └── config.json          # Berkas konfigurasi hyperparameter & seed
```

### Langkah 3: Eksekusi Eksperimen
Jalankan evaluasi komparatif dengan perintah berikut:
```bash
python riset-directory/05-kode/evaluate.py
```

### Langkah 4: Output yang Diharapkan
1. Tabel perbandingan performa dalam format CSV di `riset-directory/06-output/tables/model_comparison.csv`.
2. Gambar kurva perbandingan prediksi harga saham di `riset-directory/06-output/figures/prediction_vs_actual.png`.
