# Matriks Literatur

Berikut adalah matriks pemetaan artikel ilmiah/referensi yang relevan dengan topik perbandingan LSTM dan XGBoost untuk prediksi harga saham.

| Penulis | Tahun | Algoritma/Model | Dataset & Emiten | Hasil Temuan Kunci | Limitasi/Gap Riset |
|---|---|---|---|---|---|
| Hochreiter & Schmidhuber | 1997 | LSTM | Synthetic & general sequential data | Memperkenalkan arsitektur LSTM gating mechanism untuk mengatasi vanishing gradient. | Tidak dievaluasi secara spesifik pada data derau (noise) keuangan. |
| Chen & Guestrin | 2016 | XGBoost | Tabular datasets | Memperkenalkan XGBoost yang memiliki performa sangat cepat, regularisasi internal, dan efisiensi memori tinggi. | Tidak dioptimalkan secara temporal/sekuensial untuk time series saham. |
| Wolpert | 1992 | Stacking Generalization | General classification/regression | Memformulasikan konsep Stacking untuk menggabungkan beberapa base learner ke meta-learner. | Tidak menyentuh integrasi deep learning temporal (LSTM) ke dalam meta-learner pohon. |
| Kim | 2017 | LSTM | KOSPI Stock Index | LSTM terbukti mampu menangkap volatilitas non-linear indeks saham lebih baik daripada model linear konvensional. | Tidak membandingkan secara komparatif dengan model ensemble berbasis pohon seperti XGBoost. |
| Zhang et al. | 2019 | XGBoost vs LSTM | S&P 500 Index | XGBoost terbukti lebih unggul dalam stabilitas pada pengujian berulang data tabular indeks keuangan dengan fitur lag. | Hanya diuji pada indeks pasar besar, bukan emiten individual yang memiliki noise/volatilitas lebih ekstrem. |
| Cahya | 2026 | LSTM, XGBoost, Hybrid Stacking | Saham BBRI (2015-2025) | XGBoost Baseline secara konsisten mengungguli LSTM dan Hybrid Stacking. Stacking tidak meningkatkan hasil karena akumulasi noise. | Terbatas pada satu emiten perbankan besar (BBRI). |
