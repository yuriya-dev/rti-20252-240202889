# Laporan Penelitian

**Judul:** Analisis Komparatif Performa Model LSTM, XGBoost, dan Hybrid Stacking dalam Prediksi Harga Saham BBRI (2015-2025)

**Peneliti:** Wahyu Tri Cahya
**Target Publikasi:** Jurnal Riset Teknologi Informasi / Jurnal Ilmiah Sinta 2/3
**Status Penelitian:** Selesai (Eksperimen 10x Run dan Draf Paper Jurnal Telah Rampung)

---

## 1. Ringkasan Eksekutif
Penelitian ini bertujuan untuk melakukan analisis komparatif performa prediksi pergerakan harga saham harian PT Bank Rakyat Indonesia (Persero) Tbk (BBRI.JK) dari periode 1 Januari 2015 hingga 31 Desember 2025. Model yang dibandingkan meliputi model deep learning **Long Short-Term Memory (LSTM)**, model machine learning **eXtreme Gradient Boosting (XGBoost) Baseline**, serta model **Hybrid Stacking** dua tingkat (LSTM → XGBoost). Untuk menjamin stabilitas hasil eksperimen dari kebetulan statistik, pengujian dilakukan sebanyak 10 kali run terkontrol menggunakan 10 random seed berbeda (`43` s.d. `52`). 

Hasil rata-rata (mean ± std) evaluasi menunjukkan bahwa **XGBoost Baseline** mengungguli kedua model lainnya dengan nilai **MAE sebesar 126.1506 ± 4.5945 Rp**, **RMSE sebesar 188.5673 ± 4.0398 Rp**, **$R^2$ Score sebesar 0.8412 ± 0.0068**, dan **MAPE sebesar 3.1385% ± 0.1263%**. Model **Hybrid Stacking** menempati posisi kedua ($R^2$ = 0.8323 ± 0.0095), diikuti oleh model **LSTM Baseline** di posisi terakhir ($R^2$ = 0.5901 ± 0.0808). Pengujian statistik menggunakan Wilcoxon Signed-Rank Test pada residual error mengonfirmasi bahwa perbedaan performa di antara ketiga model tersebut adalah signifikan secara statistik (p-value < 0.05). Kesimpulan utama penelitian ini menunjukkan bahwa model machine learning ensemble yang berbasis pohon keputusan (XGBoost) dengan fitur lag autoregressive dan indikator teknikal yang representatif lebih tangguh dan stabil dibanding model deep learning murni (LSTM) untuk memprediksi pergerakan saham lokal yang volatil dan memiliki noise tinggi seperti BBRI.

---

## 2. Latar Belakang dan Rumusan Masalah
Prediksi harga saham harian merupakan tantangan besar dalam analisis keuangan kuantitatif karena sifat pasar modal yang dinamis, volatil, non-linear, dan rentan terhadap guncangan eksternal (structural breaks). Saham BBRI sebagai salah satu saham blue-chip berkapitalisasi besar di BEI menjadi pilihan investasi utama bagi investor domestik maupun asing. Namun, pergerakan harganya dipengaruhi secara kuat oleh peristiwa makroekonomi seperti inflasi, tingkat suku bunga Bank Indonesia, serta krisis global seperti Pandemi COVID-19 pada 2020-2021.

Metode peramalan klasik sering kali gagal dalam melakukan estimasi jangka panjang. Model machine learning modern seperti XGBoost dan arsitektur deep learning LSTM ditawarkan sebagai solusi alternatif. Banyak akademisi berasumsi bahwa deep learning atau model hybrid stacking yang kompleks akan selalu menghasilkan prediksi yang lebih unggul dibandingkan model machine learning tabular konvensional. Rumusan masalah penelitian ini dirancang untuk membuktikan asumsi tersebut:
1. Apakah model deep learning LSTM secara konsisten menghasilkan tingkat error (RMSE, MAE, MAPE) yang lebih rendah dibandingkan model XGBoost dan Hybrid Stacking pada saham BBRI?
2. Bagaimana representasi goodness-of-fit ($R^2$) masing-masing model?
3. Apakah perbedaan performa tersebut signifikan secara statistik?

---

## 3. Metodologi dan Pelaksanaan
Penelitian dilaksanakan melalui tahapan pipeline terstruktur:
1. **Pengumpulan Data:** Mengunduh 2.726 baris data saham BBRI (OHLCV) harian dari 2015 s.d. 2025 via `yfinance`.
2. **Feature Engineering:** Membuat indikator teknikal (SMA_20, EMA_50, RSI_14, MACD, ATR_14) dan 60 hari fitur lag penutupan (`Lag_Close_t-1` s.d. `Lag_Close_t-60`).
3. **Preprocessing:** Menskalakan data ke rentang `[0, 1]` menggunakan `MinMaxScaler` dan membagi data secara kronologis (80% training set, 20% testing set).
4. **Implementasi Model:**
   - **LSTM:** Arsitektur 2 layer LSTM (128 dan 64 units) dengan Dropout 0.2, dilatih dengan Adam optimizer dan Huber loss selama maks 100 epoch.
   - **XGBoost:** Model berbasis gradient boosting pohon dengan n_estimators=500 dan max_depth=6.
   - **Hybrid Stacking:** Memasukkan hasil prediksi LSTM scaled Level 1 ke dalam dataset XGBoost Level 2 untuk dilatih sebagai meta-features.
5. **Eksekusi Otomatis:** Menggunakan skrip runner `run_all_experiments.py` untuk mengulang eksekusi 10 kali secara berturut-turut untuk 10 random seed berbeda guna menghindari bias inisialisasi parameter acak.

---

## 4. Hasil Penelitian
Hasil pengumpulan data metrik kinerja dari 10 run dirangkum pada tabel berikut:

### Tabel Perbandingan Metrik Kinerja (Rata-rata ± Standar Deviasi)

| Model | MAE (Rp) | RMSE (Rp) | R² Score | MAPE (%) |
|-------|----------|-----------|----------|----------|
| **LSTM Baseline** | 229.0273 ± 26.4501 | 301.6060 ± 30.9412 | 0.5901 ± 0.0808 | 5.5588 ± 0.6445 |
| **XGBoost Baseline** | **126.1506 ± 4.5945** | **188.5673 ± 4.0398** | **0.8412 ± 0.0068** | **3.1385 ± 0.1263** |
| **Hybrid Stacking** | 128.6106 ± 6.6277 | 193.7625 ± 5.4648 | 0.8323 ± 0.0095 | 3.1868 ± 0.1862 |

### Hasil Uji Signifikansi Statistik (Wilcoxon Signed-Rank Test pada Run 1)
- **LSTM vs XGBoost:** p-value $\approx 3.65 \times 10^{-53}$ (Signifikan)
- **Hybrid vs LSTM:** p-value $\approx 2.77 \times 10^{-49}$ (Signifikan)
- **Hybrid vs XGBoost:** p-value $\approx 0.0056$ (Signifikan)

---

## 5. Kendala dan Catatan Lingkungan
- Pelatihan LSTM rentan terhadap ketidakstabilan konvergensi tergantung pada inisialisasi bobot acak (terlihat dari standar deviasi MAE LSTM sebesar 26.45 Rp, jauh lebih besar dibanding XGBoost yang hanya 4.59 Rp).
- Model Hybrid Stacking membutuhkan waktu eksekusi lebih lama karena harus melakukan feedforward prediksi LSTM pada Level 1 sebelum melatih XGBoost Level 2.
- Data saham BBRI memiliki *structural break* yang tajam pada tahun 2020 akibat krisis COVID-19, menyebabkan model LSTM murni kesulitan melacak pergeseran tren secara fleksibel dibanding model berbasis pohon (XGBoost) yang lebih reaktif terhadap perubahan volatilitas (didukung fitur ATR_14).

---

## 6. Kesimpulan dan Saran
- **Kesimpulan:** XGBoost Baseline terbukti sebagai model prediksi paling akurat, stabil, dan efisien secara komputasi untuk meramalkan harga saham BBRI. Model Hybrid Stacking tidak mampu mengungguli XGBoost karena besarnya residual error dari model LSTM yang ikut tersalurkan ke meta-learner.
- **Saran:** Untuk penelitian selanjutnya, disarankan menguji arsitektur deep learning yang lebih adaptif seperti Gated Recurrent Units (GRU) atau Transformer (Attention Mechanism), serta menambahkan fitur sentimen berita bursa saham.

---

## 7. Lampiran — Peta Artefak Penelitian

| Folder | Isi | Status |
|---|---|---|
| [01-proposal/](../01-proposal/) | Proposal penelitian komparatif LSTM, XGBoost, dan Hybrid | Selesai |
| [02-literatur/](../02-literatur/) | Matriks studi literatur & tinjauan pustaka | Selesai |
| [03-teori/](../03-teori/) | Diagram arsitektur data pipeline, LSTM, dan Hybrid Stacking | Selesai |
| [04-data/](../04-data/) | Berkas dataset BBRI mentah dan hasil pembersihan (`bbri_clean.csv`) | Selesai |
| [05-kode/](../05-kode/) | Jupyter Notebook utama, skrip runner 10x, dan parameter konfigurasi JSON | Selesai |
| [06-output/](../06-output/) | Rekaman 10 folder run berisi 8 grafik visualisasi PNG dan 3 tabel evaluasi CSV per run | Selesai |
| [07-manuskrip/](../07-manuskrip/) | Draf naskah paper jurnal ilmiah lengkap siap submit | Selesai |
| [08-laporan/](../08-laporan/) | Laporan akhir konsolidasi penelitian (dokumen ini) | Selesai |
| [09-docs/](../09-docs/) | Dokumen status kemajuan dan rencana pelaksanaan teknis | Selesai |
