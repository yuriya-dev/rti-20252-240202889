# Jadwal & Log Pelaksanaan Penelitian

Catatan kronologis pelaksanaan tiap tahap riset prediksi saham BBRI (LSTM vs XGBoost vs Hybrid).

## Log Pelaksanaan

| Tanggal | Tahap | Aktivitas | Referensi |
|---|---|---|---|
| 2026-06-22 | Tahap 1 | Preprocessing data saham BBRI (OHLCV + indikator teknikal), splitting 80/20 train/test, scaling MinMax, sequence windowing 60 hari | `tahap-1-pengumpulan-dan-preprocessing-data.md` |
| 2026-06-22 | Tahap 2 | Implementasi baseline machine learning XGBoost dengan parameter n_estimators=500 dan max_depth=6 | `tahap-2-implementasi-baseline-xgboost.md` |
| 2026-06-22 | Tahap 3 | Implementasi deep learning LSTM 2 layer (128 dan 64 units) dengan Huber loss dan early stopping patience 15 | `tahap-3-implementasi-lstm.md` |
| 2026-06-22 | Tahap 4 | Penulisan skrip runner otomatis `run_all_experiments.py` untuk 10 kali runs dengan seed `43` s.d. `52`, dan pengumpulan data output di folder `06-output/` | `tahap-4-eksperimen-dan-evaluasi.md` |
| 2026-06-22 | Tahap 5 | Penyusunan laporan penelitian terstruktur dan draf manuskrip paper komparasi model | `tahap-5-draf-paper.md` |

## Status Ringkas

- **Tahap 1**: Selesai
- **Tahap 2**: Selesai
- **Tahap 3**: Selesai
- **Tahap 4**: Selesai
- **Tahap 5**: Selesai

## Item Tindak Lanjut (Checklist Sebelum Submission)

- [x] Pengumpulan dataset historis saham BBRI (2015-2025)
- [x] Preprocessing data (MinMax scaling, data windowing/sequencing 60 hari)
- [x] Implementasi dan penyetelan model baseline XGBoost
- [x] Implementasi dan penyetelan model deep learning LSTM
- [x] Pembuatan dan pelatihan model Hybrid Stacking (LSTM → XGBoost)
- [x] Evaluasi performa (RMSE, MAE, R², MAPE) pada testing set
- [x] Analisis hasil dan visualisasi perbandingan (8 grafik)
- [x] Uji signifikansi statistik Wilcoxon Signed-Rank Test
- [x] Penyusunan proposal penelitian terintegrasi
- [x] Penyusunan draf naskah jurnal ilmiah Sinta
- [x] Reorganisasi program dan output ke riset-directory

## Korespondensi

- **2026-06-22 (Bimbingan Dosen)**: Dosen meminta repositori riset-directory distrukturisasi ulang secara formal (04-data, 05-kode, 06-output). Meminta penyertaan model baseline (XGBoost), deep learning (LSTM), dan model hybrid untuk diuji kestabilannya sebanyak 10 kali run dengan random seed berbeda.
