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
| Wardhana et al. | 2023 | Logistic Regression, Random Forest, SVM, Decision Tree, XGBoost | Profil Kesehatan Indonesia 2016-2021 (multi-penyakit, sosio-demografi) | Decision Tree paling akurat secara umum; untuk kusta akurasi tertinggi 0.72 (RF/DT/XGBoost). | Domain kesehatan, belum konteks HR; evaluasi berfokus akurasi klasifikasi. |
| Wibowo & Isnain | 2025 | Perbandingan 15 classifier + tuning (final: RF, Extra Trees, K-NN, NuSVC) | ESC-50 (2,000 audio, 50 kelas) | K-NN terbaik dengan akurasi test 63%; model lain cenderung overfitting. | Akurasi masih moderat; keragaman suara tinggi menurunkan generalisasi. |
| Ashari & Suhendar | 2024 | LSTM 3 layer + dropout + hyperparameter tuning | Data harga beras + cuaca harian Jateng 2017-2024 (2,682 data) | MAE 0.141, MAPE 1.256%, RMSE 0.205. | Konteks tunggal (Jawa Tengah), belum dibandingkan luas lintas domain. |
| Fauzan et al. | 2025 | Naive Bayes, Decision Tree, Random Forest + fitur TF-IDF dan numerik URL | 651,191 URL (benign, phishing, defacement, malware) | RF terbaik (akurasi 97%), DT 96%, NB 85%; recall phishing pada NB rendah. | Kinerja kelas phishing belum merata; butuh data lebih besar/beragam dan sistem real-time. |
| Alkayes & Sugihartono | 2025 | Komparasi XGBoost vs LSTM | Time series harga saham Tesla | LSTM lebih baik: MAE 13.4788, RMSE 17.8713, R2 0.9271 (vs XGBoost). | Hanya satu aset; faktor makro/sentimen belum dimasukkan. |
| Rosyd et al. | 2024 | LSTM (optimasi Adam) | Harga saham BBCA 2020-2023 | RMSE 40.85, MAPE 0.71%, MSE 6662.76. | Satu emiten, tanpa baseline pembanding non-LSTM. |
| Aprilia et al. | 2026 | LSTM, XGBoost, Hybrid LSTM-XGBoost | Harga penutupan BBRI 2015-2025 | Hybrid terbaik: RMSE 193.98, MAE 159.56, R2 0.93. | Fokus satu saham; validasi eksternal lintas aset belum ada. |
| Kevin et al. | 2025 | Hybrid LSTM-XGBoost vs model tunggal | USD/IDR + BI7DRR + inflasi + DXY (2020-2024) | Hybrid terbaik: MAPE 1.359%, MAE 216.488, RMSE 271.776, R2 0.333. | Daya jelaskan variansi masih rendah; butuh perbaikan arsitektur dan preprocessing. |
| Ulya et al. | 2025 | XGBoost regression vs LSTM regression (+ variabel eksternal) | Harga harian bitcoin + sentimen + Google Trends | LSTM terbaik: RMSE 1378.55 USD, R2 92%; XGBoost overfit (RMSE 5169.898, R2 -13%). | Domain kripto sangat volatil; hasil sulit ditransfer ke domain lain. |
| Indriyanti & Fajriah | 2025 | Komparatif LSTM vs XGBoost | Radiasi matahari per jam (NASA POWER) Jakarta-Bogor 2013-2022 | Error LSTM lebih rendah (RMSE 29.24/30.73; MAE 15.63/16.89) dibanding XGBoost. | Ringkasan R2 tidak lengkap, interpretasi performa sebagian bersifat kontekstual. |

