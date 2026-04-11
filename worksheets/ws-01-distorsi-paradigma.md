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
   - Alasan: Studi membandingkan efektivitas metode secara terukur (positivis), namun juga relevan untuk perancangan praktik/metode implementasi di konteks nyata (design science).

3. Identifikasi distorsi:
   - Asumsi tersembunyi: Metode yang paling sering dipakai otomatis paling efektif di semua konteks.
   - Sumber bias potensial: Selection bias pada pemilihan paper (hanya 23 dari ribuan hasil awal), publication bias, dan perbedaan konteks antar studi kasus.
   - Langkah mitigasi: Nyatakan kriteria seleksi secara transparan, pisahkan analisis frekuensi vs efektivitas, serta laporkan batas generalisasi.

4. Komitmen etika:
   - Data yang tidak akan dimanipulasi: Hasil studi yang tidak mendukung hipotesis, outlier, dan data yang menurunkan signifikansi.
   - Batasan yang diakui sejak awal: Kajian hanya berbasis SLR pada periode dan sumber tertentu, sehingga tidak mewakili seluruh proyek TI.
```

---

## Latihan 1 — Identifikasi Distorsi

Pilih satu paper riset di bidang TI yang mengklaim "metode X meningkatkan performa." Telusuri setiap tahap Research Trust Model.

**Paper yang dipilih:**
> Judul: ANALISIS PERBANDINGAN METODE MANAJEMEN PROYEK TI YANG PALING SERING DIGUNAKAN DI INDONESIA DAN LUAR NEGERI: A LITERATURE REVIEW
> Penulis (Tahun): Afifa Witania dkk. (tahun tidak dicantumkan eksplisit pada naskah lampiran)

| Tahap | Apa yang Dilakukan | Potensi Distorsi |
|-------|-------------------|-----------------|
| Reality → Data | Menentukan RQ, lalu mencari paper di Google Scholar dan DOAJ dengan kata kunci Agile, Scrum, Kanban, Waterfall, dan manajemen proyek. | Basis data terbatas pada dua sumber; kemungkinan studi relevan di sumber lain tidak terambil. |
| Data → Processing | Melakukan eliminasi duplikat, seleksi rentang tahun, relevansi, lalu QA hingga tersisa 23 paper. | Selection bias tinggi karena penyaringan sangat ketat; studi yang tidak memenuhi indeks tertentu bisa terbuang walau relevan. |
| Processing → Analysis | Mengekstrak metode, lokasi, tahun, dan simpulan tiap paper; menghitung frekuensi metode per wilayah. | Heterogenitas konteks studi kasus (jenis industri, skala proyek, kapabilitas tim) membuat perbandingan tidak sepenuhnya setara. |
| Analysis → Inference | Menarik simpulan metode paling sering dan paling efektif untuk Indonesia vs luar negeri. | Risiko mencampur klaim frekuensi dengan efektivitas; hubungan kausal belum tentu terbukti. |
| Inference → Knowledge | Menyajikan rekomendasi metode untuk praktik manajemen proyek TI. | Over-generalisasi karena bukti berasal dari sampel terbatas dan periode tertentu. |

**Distorsi paling besar di tahap:** Analysis -> Inference

**Dua distorsi spesifik yang teridentifikasi:**
1. Selection bias: dari ribuan hasil awal hanya sedikit paper yang lolos, sehingga komposisi bukti bisa tidak representatif.
2. Frequency-effectiveness conflation: metode yang paling sering muncul dianggap paling efektif tanpa pembuktian kausal yang kuat.

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

**Topik riset:** Perbandingan penggunaan dan efektivitas metode manajemen proyek TI (Agile, Scrum, Kanban, Waterfall, Hybrid) di Indonesia dan luar negeri.

| Kriteria | Positivis | Interpretivis | Design Science |
|----------|-----------|---------------|----------------|
| Kesesuaian dengan topik (1–5) | 4 | 2 | 3 |
| Jenis data yang dikumpulkan | Data terukur: jumlah studi per metode, indikator keberhasilan proyek, perbandingan performa lintas studi. | Data naratif: wawancara praktisi, pengalaman tim, konteks budaya organisasi. | Data desain artefak/proses: rancangan kerangka metode, uji penerapan bertahap, umpan balik implementasi. |
| Limitasi paradigma | Sulit mengontrol semua variabel konteks riil proyek TI; hasil bisa tampak objektif tetapi tetap dipengaruhi confounder. | Generalisasi rendah karena sangat kontekstual dan subjektif. | Fokus pada artefak dapat menggeser fokus dari pengujian klaim kausal yang ketat. |

**Paradigma yang dipilih:** Positivis (diperkuat perspektif Design Science)
**Alasan:** Topik utama menuntut pembandingan berbasis bukti terukur, tetapi rekomendasi praktik membutuhkan sudut pandang perancangan solusi yang dapat diterapkan di konteks proyek nyata.

---

## Refleksi

> Sebelum membaca materi ini, apakah pernah mempertanyakan klaim "95% akurat"? Setelah memahami rantai distorsi, pertanyaan apa yang sekarang akan diajukan saat membaca paper?

**Jawaban:**
> Sebelumnya saya cenderung menerima klaim efektivitas sebagai fakta jika banyak paper menyatakan "berhasil". Setelah memahami rantai distorsi, saya lebih hati-hati pada proses transformasi data hingga kesimpulan.
> Pertanyaan yang sekarang saya ajukan saat membaca paper: apakah frekuensi penggunaan dipisahkan dari efektivitas, bagaimana kriteria seleksi data ditentukan, dan sejauh mana hasil dapat digeneralisasi ke konteks proyek lain.
