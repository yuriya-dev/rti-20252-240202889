# 05-kode

Source code implementasi untuk pengujian prediksi harga saham BBRI menggunakan LSTM, XGBoost, dan Hybrid Stacking.

## Struktur Direktori

```text
05-kode/
├── BBRI_Stock_Prediction.ipynb  # Jupyter Notebook utama berisi data preprocessing, model training, dan evaluasi
├── run_all_experiments.py       # Skrip Python runner untuk mengeksekusi notebook otomatis sebanyak 10 kali
└── config_run.json              # Konfigurasi parameter eksekusi (jalur notebook, rentang run, timeout, dll)
```

## Deskripsi Komponen

1. **`BBRI_Stock_Prediction.ipynb`**:
   - Memuat data saham BBRI.
   - Menghitung indikator teknikal (Bollinger Bands, MACD, RSI, ATR) dan fitur lag.
   - Melatih model LSTM Baseline (Deep Learning).
   - Melatih model XGBoost Baseline (Machine Learning).
   - Melatih model Hybrid Stacking (menggabungkan prediksi scaled LSTM + fitur teknikal ke dalam XGBoost Meta-Learner).
   - Menghasilkan plot visualisasi evaluasi dan menyimpan model biner ke dalam folder output.

2. **`run_all_experiments.py`**:
   - Memuat pengaturan dari `config_run.json`.
   - Mengubah seed acak secara dinamis (`42 + run_id`) untuk setiap run.
   - Mengeksekusi notebook secara otomatis dari run-1 hingga run-10 menggunakan preprocessor `nbconvert`.
   - Menyimpan salinan hasil run notebook ter-eksekusi di masing-masing folder output run.

3. **`config_run.json`**:
   - Konfigurasi parameter untuk menjalankan skrip eksperimen otomatis secara aman.

## Cara Menjalankan Eksperimen 10x
Jalankan perintah berikut di terminal dari direktori `05-kode/`:
```bash
python3 run_all_experiments.py
```
