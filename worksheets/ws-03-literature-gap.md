# WS-03: Literature Mapping & Gap

> **Bab 3 — Literature Review, Research Gap & Baseline**

---

## Ringkasan Materi

### Literature Review = Positioning, Bukan Ringkasan

Literature review bukan merangkum paper satu per satu. Pendekatan yang benar adalah **concept-centric** — organisasi berdasarkan tema, metode, atau variabel. Tujuan: menemukan **pola, kontradiksi, dan gap**.

### Empat Jenis Research Gap

| Jenis Gap | Deskripsi | Contoh |
|-----------|----------|--------|
| **Performance Gap** | Performa belum memadai | Akurasi deteksi hanya 78% pada kasus tertentu |
| **Method Gap** | Pendekatan belum diterapkan | Belum ada yang pakai transformer untuk task ini |
| **Data Gap** | Dataset terbatas/tidak representatif | Semua studi pakai dataset sintetis |
| **Context Gap** | Belum diuji pada konteks berbeda | Belum ada evaluasi di negara berkembang |

Gap terkuat = kombinasi 2+ jenis.

### Systematic Search Strategy

1. **Database**: IEEE Xplore, ACM DL, Scopus, Google Scholar
2. **Boolean query** yang terdokumentasi eksplisit
3. **Snowballing**: backward (telusuri referensi) + forward (cari yang mengutip)
4. Klaim "belum ada penelitian" harus didukung **bukti pencarian**

### Baseline Selection — 3 Kriteria

| Kriteria | Pertanyaan |
|----------|-----------|
| **Relevan** | Apakah menyelesaikan masalah yang sama? |
| **Representatif** | Apakah mewakili common practice? |
| **State-of-the-Art** | Apakah terbaru/terbaik? |

Membandingkan deep learning 2024 dengan decision tree sederhana tanpa justifikasi = **straw man comparison** (perbandingan tidak jujur).

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan baca literatur | Mencari solusi yang sudah ada | Memahami apa yang belum terjawab |
| Cara membaca paper | Tutorial, how-to | Metode, limitasi, gap |
| Baseline | Framework terpopuler | State-of-the-art yang rigorous |
| Dokumentasi pencarian | Tidak diperlukan | Wajib (reproducible) |

### Istilah Penting

- **Concept-centric** — Organisasi literatur berdasarkan konsep/metode, bukan per penulis
- **Snowballing** — Backward (telusuri referensi) + Forward (cari yang mengutip paper kunci)
- **Research Position** — Pernyataan eksplisit posisi riset terhadap studi sebelumnya
- **Straw man comparison** — Memilih baseline lemah agar metode sendiri terlihat lebih baik

---

## A.3 — Literature Mapping & Gap Identification

LITERATURE MAPPING

Topik      : Implementasi machine learning untuk rekrutmen dan prediksi turnover pada MSDM Indonesia (rujukan WS-02)
Database   : Google Scholar + referensi internal folder paper/ws-03
Query      : ("machine learning" OR "classification" OR "time series") AND ("prediction" OR "detection") AND ("Indonesia" OR "dataset")
Tahun      : 2023-2026
Hasil awal : 10 paper -> Screening -> 10 paper final

Literature Matrix (concept-centric):

| Study | Tahun | Method | Data | Result | Limitation |
|-------|-------|--------|------|--------|------------|
| Wardhana et al. | 2023 | Logistic Regression, Random Forest, SVM, Decision Tree, XGBoost | Profil Kesehatan Indonesia 2016-2021 (multi-penyakit, sosio-demografi) | Decision Tree paling akurat secara umum; untuk kusta akurasi tertinggi 0.72 (RF/DT/XGBoost) | Domain kesehatan, belum konteks HR; evaluasi berfokus akurasi klasifikasi |
| Wibowo & Isnain | 2025 | Perbandingan 15 classifier + tuning (final: RF, Extra Trees, K-NN, NuSVC) | ESC-50 (2,000 audio, 50 kelas) | K-NN terbaik dengan akurasi test 63%; model lain cenderung overfitting | Akurasi masih moderat; keragaman suara tinggi menurunkan generalisasi |
| Ashari & Suhendar | 2024 | LSTM 3 layer + dropout + hyperparameter tuning | Data harga beras + cuaca harian Jateng 2017-2024 (2,682 baris) | MAE 0.141, MAPE 1.256%, RMSE 0.205 | Konteks tunggal (Jawa Tengah), belum dibandingkan luas lintas domain |
| Fauzan et al. | 2025 | Naive Bayes, Decision Tree, Random Forest + fitur TF-IDF dan numerik URL | 651,191 URL (benign, phishing, defacement, malware) | RF terbaik (akurasi 97%), DT 96%, NB 85%; recall phishing pada NB rendah | Kinerja kelas phishing belum merata; butuh data lebih besar/beragam dan sistem real-time |
| Alkayes & Sugihartono | 2025 | Komparasi XGBoost vs LSTM | Time series harga saham Tesla | LSTM lebih baik: MAE 13.4788, RMSE 17.8713, R2 0.9271 (vs XGBoost) | Hanya satu aset; faktor makro/sentimen belum dimasukkan |
| Rosyd et al. | 2024 | LSTM (optimasi Adam) | Harga saham BBCA 2020-2023 | RMSE 40.85, MAPE 0.71%, MSE 6662.76 | Satu emiten, tanpa baseline pembanding non-LSTM |
| Aprilia et al. | 2026 | LSTM, XGBoost, Hybrid LSTM-XGBoost | Harga penutupan BBRI 2015-2025 | Hybrid terbaik: RMSE 193.98, MAE 159.56, R2 0.93 | Fokus satu saham; validasi eksternal lintas aset belum ada |
| Kevin et al. | 2025 | Hybrid LSTM-XGBoost vs model tunggal | USD/IDR + BI7DRR + inflasi + DXY (2020-2024) | Hybrid terbaik: MAPE 1.359%, MAE 216.488, RMSE 271.776, R2 0.333 | Daya jelaskan variansi masih rendah; butuh perbaikan arsitektur dan preprocessing |
| Ulya et al. | 2025 | XGBoost regression vs LSTM regression (+ variabel eksternal) | Harga harian bitcoin + sentimen + Google Trends | LSTM terbaik: RMSE 1378.55 USD, R2 92%; XGBoost overfit (RMSE 5169.898, R2 -13%) | Domain kripto sangat volatil; hasil sulit ditransfer ke domain lain |
| Indriyanti & Fajriah | 2025 | Komparatif LSTM vs XGBoost | Radiasi matahari per jam (NASA POWER) Jakarta-Bogor 2013-2022 | Error LSTM lebih rendah (RMSE 29.24/30.73; MAE 15.63/16.89) dibanding XGBoost | Ringkasan R2 tidak lengkap, interpretasi performa sebagian bersifat kontekstual |

Pola yang ditemukan:
  Metode dominan     : LSTM, XGBoost/RF, dan pendekatan hybrid LSTM-XGBoost dengan skema komparatif + tuning.
  Dataset umum       : Mayoritas data deret waktu domain-spesifik (finansial/ekonomi), ditambah klasifikasi domain kesehatan-audio-siber.
  Limitasi berulang  : Overfitting dan ketidakstabilan lintas data, generalisasi rendah antar konteks, serta minim evaluasi fairness-privacy.

GAP IDENTIFICATION

Gap 1: [Jenis: method + context]
  Deskripsi    : Belum ada kerangka evaluasi model ML yang simultan menilai akurasi, fairness, dan privasi untuk keputusan HR di Indonesia.
  Bukti        : Sepuluh paper berfokus pada akurasi/error teknis; tidak ada yang melaporkan metrik fairness (mis. demographic parity/equal opportunity) maupun kepatuhan privasi data personal.
  Signifikansi : Keputusan rekrutmen/turnover berdampak langsung pada manusia; model akurat tapi bias atau melanggar privasi tidak layak diterapkan.

Gap 2: [Jenis: data + performance]
  Deskripsi    : Belum tersedia bukti performa model yang stabil pada dataset HR Indonesia yang representatif dan tidak seimbang.
  Bukti        : Kinerja berubah tajam antar studi: K-NN hanya 63% (audio), NB 85% vs RF 97% (phishing), LSTM gagal berat pada satu studi nilai tukar (MAPE 60.793; R2 negatif) tetapi unggul pada studi lain.
  Signifikansi : Tanpa data HR lokal yang kuat, hasil eksperimen sulit digeneralisasi ke kebijakan SDM organisasi Indonesia.

Baseline Selection:
| Baseline | Relevansi | Representatif | Source |
|----------|-----------|---------------|--------|
| Random Forest + feature engineering tabular | Cocok untuk klasifikasi data terstruktur (profil kandidat/riwayat karyawan) | Muncul di banyak studi dan konsisten kuat pada klasifikasi | Wardhana et al. (2023); Fauzan et al. (2025) |
| Hybrid LSTM-XGBoost time series | Cocok untuk dinamika temporal turnover + koreksi residual non-linear | Berkinerja terbaik pada beberapa studi runtun waktu kompleks | Aprilia et al. (2026); Kevin et al. (2025) |

---

## Latihan 1 — Concept-Centric Literature Table

Gunakan topik riset dari WS-02. Cari minimal 5 paper relevan menggunakan Google Scholar atau database lain.

**Topik riset:** Implementasi machine learning untuk rekrutmen dan prediksi turnover dalam MSDM Indonesia
**Query pencarian:** ("machine learning" OR "random forest" OR "LSTM") AND ("recruitment" OR "turnover prediction" OR "classification") AND ("fairness" OR "privacy" OR "Indonesia")
**Database:** Google Scholar + referensi paper/ws-03

| # | Study | Tahun | Method | Dataset | Result | Limitasi |
|---|-------|-------|--------|---------|--------|----------|
| 1 | Wardhana et al. | 2023 | Logistic Regression, RF, SVM, DT, XGBoost | Profil Kesehatan Indonesia 2016-2021 | DT paling akurat secara umum; untuk kusta akurasi tertinggi 0.72 | Fokus kesehatan, belum konteks HR/fairness |
| 2 | Wibowo & Isnain | 2025 | Multi-classifier + tuning (K-NN, RF, Extra Trees, NuSVC) | ESC-50 (2,000 audio) | K-NN terbaik, akurasi test 63% | Overfitting pada sebagian model; performa moderat |
| 3 | Ashari & Suhendar | 2024 | LSTM + dropout + hyperparameter tuning | Harga beras dan cuaca Jateng (2,682 data) | MAE 0.141; MAPE 1.256%; RMSE 0.205 | Konteks satu wilayah, belum pembanding lintas model luas |
| 4 | Fauzan et al. | 2025 | Naive Bayes, DT, RF + TF-IDF URL features | 651,191 URL phishing/benign/malware/defacement | RF 97%, DT 96%, NB 85% | Kelas phishing tetap menantang; perlu data lebih beragam |
| 5 | Alkayes & Sugihartono | 2025 | XGBoost vs LSTM | Time series harga saham Tesla | LSTM unggul (MAE 13.4788; RMSE 17.8713; R2 0.9271) | Hanya Tesla, faktor makro/sentimen belum dipakai |
| 6 | Rosyd et al. | 2024 | LSTM (Adam) | Harga saham BBCA 2020-2023 | RMSE 40.85; MAPE 0.71%; MSE 6662.76 | Tidak dibandingkan dengan model alternatif |
| 7 | Aprilia et al. | 2026 | LSTM vs XGBoost vs Hybrid | Harga saham BBRI 2015-2025 | Hybrid terbaik (RMSE 193.98; MAE 159.56; R2 0.93) | Satu emiten; generalisasi lintas sektor belum teruji |
| 8 | Kevin et al. | 2025 | Hybrid LSTM-XGBoost | Nilai tukar USD/IDR + BI7DRR + inflasi + DXY | Hybrid terbaik (MAPE 1.359%; MAE 216.488; RMSE 271.776; R2 0.333) | R2 rendah; model masih butuh optimasi lanjut |
| 9 | Ulya et al. | 2025 | XGBoost regression vs LSTM regression + eksternal variabel | Bitcoin harian + sentimen + GTI | LSTM terbaik (RMSE 1378.55; R2 92%); XGBoost overfit (R2 -13%) | Data sangat volatil; transfer ke domain non-kripto terbatas |
| 10 | Indriyanti & Fajriah | 2025 | LSTM vs XGBoost | Radiasi matahari per jam Jakarta-Bogor 2013-2022 | LSTM menunjukkan error lebih rendah dibanding XGBoost | Ringkasan metrik tidak sepenuhnya konsisten antar bagian |

**Pola yang terlihat — Metode dominan:** LSTM, XGBoost/RF, dan hybrid LSTM-XGBoost dalam eksperimen komparatif.
**Limitasi yang berulang:** Overfitting/instabilitas lintas dataset, domain sangat spesifik, serta belum ada fairness-privacy assessment.

---

## Latihan 2 — Gap Identification

Berdasarkan tabel di Latihan 1, identifikasi gap.

| Jenis Gap | Ditemukan? | Gap Statement |
|-----------|-----------|---------------|
| Performance Gap | [x] Ya / [ ] Tidak | Performa model sangat sensitif terhadap domain; ada kasus model tunggal gagal (mis. R2 negatif pada beberapa eksperimen), namun unggul di studi lain. |
| Method Gap | [x] Ya / [ ] Tidak | Studi dominan optimasi akurasi/error, belum mengintegrasikan evaluasi fairness, bias, dan privasi untuk keputusan berisiko tinggi seperti HR. |
| Data Gap | [x] Ya / [ ] Tidak | Belum ada dataset HR Indonesia yang representatif untuk menguji recruitment-turnover sekaligus mengukur fairness/privacy. |
| Context Gap | [x] Ya / [ ] Tidak | Referensi kini mencakup kesehatan, audio, siber, finansial, nilai tukar, dan energi, namun tetap belum spesifik pada konteks organisasi HR Indonesia. |

**Gap utama yang dipilih:** Kombinasi Method Gap + Context Gap (didukung Data Gap)
**Mengapa gap ini penting (bukan sekadar "belum ada yang meneliti")?**
> Karena model untuk keputusan SDM tidak cukup hanya akurat. Model juga harus adil antar kelompok, patuh privasi data personal, dan tervalidasi pada konteks organisasi Indonesia agar keputusan rekrutmen/retensi tidak menimbulkan risiko etis, hukum, dan operasional.

---

## Latihan 3 — Baseline Selection

Pilih 2 baseline dari literatur yang sudah dibaca.

| # | Baseline | Mengapa Relevan | Mengapa Representatif | Apakah SOTA? | Sumber |
|---|----------|----------------|----------------------|-------------|--------|
| 1 | Random Forest + engineered tabular features | Cocok untuk klasifikasi kandidat/risiko turnover dari fitur terstruktur HR | Sering muncul dan performanya konsisten kuat pada studi klasifikasi | Bukan SOTA mutlak, tapi baseline kuat dan jujur | Wardhana et al. (2023); Fauzan et al. (2025) |
| 2 | Hybrid LSTM-XGBoost | Cocok untuk tren temporal turnover sekaligus koreksi residual non-linear | Berulang menunjukkan peningkatan atas model tunggal pada data runtun waktu kompleks | Relatif modern/kuat untuk time series, tetapi tetap perlu validasi domain HR | Aprilia et al. (2026); Kevin et al. (2025) |

**Apakah pemilihan baseline ini bisa dianggap straw man?** [ ] Ya / [x] Tidak
> Justifikasi: Kedua baseline mewakili praktik kuat di literatur. RF adalah baseline klasik kompetitif pada data tabular, sedangkan hybrid LSTM-XGBoost merepresentasikan baseline temporal modern yang sering mengungguli model tunggal pada data dinamis.

---

## Refleksi

> Apa perbedaan antara "belum ada yang meneliti ini" (klaim tanpa bukti) dengan research gap yang valid? Bagaimana cara membuktikan bahwa sebuah gap benar-benar ada?

**Jawaban:**
> Klaim "belum ada yang meneliti" hanya opini jika tidak ada jejak pencarian, matriks studi, dan pembanding yang jelas. Research gap yang valid harus menunjukkan pola literatur, bukti limitasi berulang, serta alasan ilmiah mengapa limitasi itu penting untuk diteliti.
> Cara membuktikannya: dokumentasikan query dan database, susun tabel concept-centric lintas paper, tunjukkan kontradiksi/limitasi terukur (misalnya overfitting, performa kelas minoritas, atau konteks yang belum diuji), lalu turunkan gap ke pertanyaan riset dan baseline yang dapat diuji ulang.
