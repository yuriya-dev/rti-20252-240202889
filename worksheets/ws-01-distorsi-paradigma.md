# WS-01: Distorsi & Paradigma

> **Bab 1 — Research Mindset in IT**

---

## Ringkasan Materi

### Research Trust Model

Pengetahuan ilmiah tidak muncul langsung dari kenyataan. Ia melewati **6 tahap transformasi** yang masing-masing rawan distorsi:

```
Reality → Data → Processing → Analysis → Inference → Knowledge
```

Etika mencegah distorsi yang disengaja (fabrikasi, cherry-picking). Validitas mendeteksi distorsi yang tidak disengaja (confounding variable, sampling bias).

### Tiga Jenis Validitas

| Jenis | Pertanyaan | Contoh Ancaman |
|-------|-----------|----------------|
| **Internal Validity** | Apakah hubungan kausal benar ada? | Confounding variable |
| **External Validity** | Apakah bisa digeneralisasi? | Dataset terlalu homogen |
| **Construct Validity** | Apakah mengukur hal yang benar? | Metrik tidak sesuai klaim |

### Paradigma Riset

Mata kuliah ini menggunakan pendekatan **Positivist** (fenomena TI bisa diukur objektif melalui eksperimen terkontrol) diperkuat **Design Science Research** (artefak dibuat sebagai instrumen pengujian hipotesis, bukan tujuan akhir).

### Mode Berpikir Peneliti

**Curious** (mempertanyakan fenomena) → **Critical** (mengevaluasi klaim berdasarkan bukti) → **Systematic** (merancang investigasi terstruktur dan reproducible).

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan | Membuat sistem yang bekerja | Menghasilkan pengetahuan yang valid |
| Pertanyaan khas | "Bagaimana membuatnya jalan?" | "Apakah klaim ini benar?" |
| Ukuran sukses | Sistem berfungsi, client puas | Hipotesis terjawab, temuan tervalidasi |
| Kegagalan | Harus dihindari | Harus dilaporkan (negative result = kontribusi) |

### Istilah Penting

- **Research Mindset** — Pola pikir yang menuntut bukti dan mempertanyakan asumsi
- **Research Ethics** — Prinsip perilaku: kejujuran, objektivitas, keterbukaan, akuntabilitas
- **HARKing** — Hypothesizing After Results are Known — merumuskan hipotesis setelah melihat data
- **Falsifiability** — Hipotesis harus bisa dibuktikan salah

---

## A.1 — Research Mindset Self-Assessment

```
Nama Peneliti    : Wahyu Tri Cahya
Tanggal          : 11 April 2026

1. Ketika membaca klaim "metode X 95% akurat":
   - Pertanyaan pertama saya: Akurasi 95% ini dihitung pada konteks apa, baseline-nya apa, dan dibandingkan dengan metode apa?
   - Data yang dibutuhkan untuk verifikasi: Definisi metrik, ukuran sampel, karakteristik data, metode evaluasi, hasil per skenario, serta error/batasan studi.

2. Posisi paradigma:
   - Pendekatan: [ ] Positivis  [ ] Interpretivis  [ ] Design Science  [x] Mixed
   - Alasan: Studi membandingkan akurasi prediksi metode secara terukur (positivis), namun juga relevan untuk perancangan arsitektur sistem prediksi (design science).

3. Identifikasi distorsi:
   - Asumsi tersembunyi: Model deep learning yang lebih kompleks (LSTM) otomatis lebih baik dari model machine learning tradisional (XGBoost) di semua kondisi.
   - Sumber bias potensial: Selection bias pada periode data (misalnya hanya menguji saat tren bullish) dan data leakage saat split training/testing.
   - Langkah mitigasi: Gunakan time-series cross-validation (walk-forward), setarakan tuning effort, dan laporkan batasan eksperimen.

4. Komitmen etika:
   - Data yang tidak akan dimanipulasi: Hasil metrik error (RMSE/MAE) yang tidak mendukung hipotesis, misalnya jika XGBoost mengungguli LSTM.
   - Batasan yang diakui sejak awal: Kajian hanya diuji pada satu emiten (BBRI) periode 2015-2025, sehingga tidak dapat digeneralisasi untuk seluruh pasar saham.
```

---

## Latihan 1 — Identifikasi Distorsi

Pilih satu paper riset di bidang TI yang mengklaim "metode X meningkatkan performa." Telusuri setiap tahap Research Trust Model.

**Paper yang dipilih:**
> Judul: PREDIKSI HARGA SAHAM BBRI MENGGUNAKAN METODE LSTM DAN XGBOOST
> Penulis (Tahun): Aprilia et al. (2026)

| Tahap | Apa yang Dilakukan | Potensi Distorsi |
|-------|-------------------|-----------------|
| Reality → Data | Mengumpulkan data historis harga saham BBRI dari Yahoo Finance. | Data yang hilang pada hari libur bursa tidak ditangani dengan benar, menyebabkan anomali harga. |
| Data → Processing | Melakukan normalisasi MinMax dan membagi data training/testing. | Data leakage jika pembagian tidak kronologis (menggunakan data masa depan untuk training). |
| Processing → Analysis | Melatih model LSTM dan XGBoost, lalu menghitung RMSE dan MAE. | Hyperparameter tuning pada LSTM dilakukan lebih ekstensif daripada XGBoost sehingga perbandingan tidak fair. |
| Analysis → Inference | Menyimpulkan bahwa LSTM selalu lebih unggul dari XGBoost. | Mengabaikan faktor volatilitas pasar yang menyebabkan performa model berfluktuasi di periode tertentu. |
| Inference → Knowledge | Merekomendasikan LSTM sebagai model mutlak untuk prediksi saham. | Over-generalisasi karena model hanya diuji pada satu saham tanpa memperhatikan aset lain. |

**Distorsi paling besar di tahap:** Processing -> Analysis

**Dua distorsi spesifik yang teridentifikasi:**
1. Tuning effort tidak setara: Model LSTM dioptimasi secara maksimal sedangkan XGBoost hanya menggunakan parameter bawaan.
2. Data leakage: Pembagian dataset dilakukan secara acak (random split) bukan kronologis (time-based split) pada data deret waktu.

---

## Latihan 2 — Analisis Kasus Etika

Skenario: Seorang peneliti menemukan bahwa jika 3 data point outlier dihapus, hasil eksperimennya menjadi signifikan. Dengan outlier, hasilnya tidak signifikan.

| Perspektif | Analisis |
|------------|---------|
| Kejujuran ilmiah | Kedua hasil wajib dilaporkan (dengan dan tanpa outlier), termasuk alasan metodologis jika outlier dikeluarkan. |
| Transparansi | Prosedur pembersihan data harus ditulis sebelum analisis utama, bukan setelah melihat hasil signifikan. |
| Peer review | Reviewer harus dapat menilai apakah penghapusan outlier valid secara statistik atau hanya upaya membuat hasil terlihat signifikan. |

**Keputusan akhir dan justifikasi:**
> Outlier tidak boleh dihapus secara sepihak. Keputusan yang etis adalah melaporkan dua skenario dan menempatkan analisis sensitifitas sebagai bagian hasil. Dengan cara ini, kesimpulan tetap jujur, dapat direplikasi, dan tidak terjebak cherry-picking.

---

## Latihan 3 — Posisi Paradigma

**Topik riset:** Perbandingan akurasi metode LSTM dan XGBoost untuk prediksi harga saham BBRI (2015-2025).

| Kriteria | Positivis | Interpretivis | Design Science |
|----------|-----------|---------------|----------------|
| Kesesuaian dengan topik (1–5) | 5 | 1 | 3 |
| Jenis data yang dikumpulkan | Data terukur: metrik error (RMSE, MAE, R2), harga historis saham. | Data naratif: wawancara dengan trader, sentimen pasar subjektif. | Data desain artefak: rancangan arsitektur sistem prediksi harga saham. |
| Limitasi paradigma | Kesulitan memodelkan kejadian tidak terduga (black swan events) yang mempengaruhi harga saham. | Tidak menghasilkan model prediksi kuantitatif yang bisa diuji akurasinya secara matematis. | Fokus pada pembuatan aplikasi/sistem, bisa mengabaikan pembuktian kausalitas antar variabel riset. |

**Paradigma yang dipilih:** Positivis (diperkuat perspektif Design Science)
**Alasan:** Riset membandingkan performa dua algoritma secara empiris menggunakan metrik terukur, namun artefak sistem juga dibangun sebagai instrumen eksperimen.

---

## Refleksi

> Sebelum membaca materi ini, apakah pernah mempertanyakan klaim "95% akurat"? Setelah memahami rantai distorsi, pertanyaan apa yang sekarang akan diajukan saat membaca paper?

**Jawaban:**
> Sebelumnya saya cenderung menerima klaim efektivitas sebagai fakta jika banyak paper menyatakan "berhasil". Setelah memahami rantai distorsi, saya lebih hati-hati pada proses transformasi data hingga kesimpulan.
> Pertanyaan yang sekarang saya ajukan saat membaca paper: apakah frekuensi penggunaan dipisahkan dari efektivitas, bagaimana kriteria seleksi data ditentukan, dan sejauh mana hasil dapat digeneralisasi ke konteks proyek lain.
