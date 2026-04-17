# WS-02: Problem Statement

> **Bab 2 — Problem Formulation & System Context**

---

## Ringkasan Materi

### Problem Formation Model

Masalah riset melewati 5 tahap transformasi. Melompat langsung dari Reality ke Variable adalah kesalahan paling umum.

```
Reality → Observed Issue (Symptom) → Diagnosed Problem (Root Cause)
→ Researchable Problem (Scoped) → Measurable Variable (Operationalized)
```

### Topic ≠ Problem ≠ Research Problem

| Level | Contoh | Status |
|-------|--------|--------|
| **Topik** | Keamanan IoT | Terlalu luas, tidak bisa diuji |
| **Problem** | MQTT tidak terenkripsi | Spesifik tapi belum riset |
| **Research Problem** | Belum ada studi membandingkan overhead TLS 1.3 vs DTLS pada MQTT di IoT RAM < 64KB | Bisa dirancang eksperimennya |

### Symptom vs Root Cause

Apa yang diamati (gejala) ≠ mengapa terjadi (akar masalah). Gunakan **5 Whys** atau **Fishbone Diagram** untuk menggali.

Contoh: "User meninggalkan checkout" (symptom) → "Waktu loading > 8 detik karena API call sequential" (root cause).

### System Thinking

Setiap masalah riset TI harus terikat pada komponen sistem: **Input → Process → Output → Outcome → Constraints → Stakeholders**.

### Problem Quality Check

Masalah riset yang layak harus memenuhi 5 kriteria:
- **Clarity** — Satu orang membaca akan paham
- **Measurability** — Ada metrik kuantitatif
- **Relevance** — Penting untuk domain
- **Testability** — Bisa gagal (falsifiable)
- **Impact** — Ada kontribusi jika terjawab

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan | Menyelesaikan masalah (*solve*) | Memahami dan membuktikan (*understand & prove*) |
| Masalah | Bug, error, fitur belum ada | Gap dalam pengetahuan |
| Scope | Selesaikan semua yang perlu | Batasi agar bisa dibuktikan |
| Output | Working system | Evidence, paper, replicable findings |

### Istilah Penting

- **Problem Statement** — Formulasi tertulis: konteks sistem + gap + dampak + justifikasi
- **System Context** — Deskripsi lengkap: input, proses, output, outcome, constraints, stakeholders
- **Problem Drift** — Masalah "bermutasi" dari pendahuluan ke metodologi karena statement awal tidak presisi
- **Solution-First Thinking** — Memulai dari solusi tanpa masalah yang jelas — berbahaya dalam riset
- **Operational Definition** — Definisi variabel yang cukup jelas agar peneliti lain bisa mengukur hal yang sama

---

## Template A.2 — Problem Statement Builder

```
PROBLEM STATEMENT BUILDER

Domain & Konteks
  Domain   : Manajemen Sumber Daya Manusia (MSDM) berbasis data
  Konteks  : Implementasi machine learning untuk rekrutmen dan prediksi turnover pada organisasi di Indonesia

System Context
  Input       : Data CV kandidat, riwayat kinerja karyawan, absensi, data resign, dan kebijakan HR
  Process     : Integrasi data HR, preprocessing, pelatihan model ML, evaluasi akurasi-fairness, dan rekomendasi keputusan HR
  Output      : Skor kecocokan kandidat, prediksi risiko turnover, dan rekomendasi pelatihan/retensi
  Outcome     : Proses HR lebih cepat, keputusan lebih akurat, dan retensi karyawan meningkat
  Constraints : Kualitas data rendah/tidak terstruktur, privasi-keamanan data, bias algoritma, biaya implementasi, dan resistensi budaya
  Stakeholders: Tim HRD, manajer lini, kandidat dan karyawan, tim IT/data, serta manajemen puncak

Fenomena → Problem
  Fenomena yang diamati             : Adopsi ML di MSDM meningkat karena dorongan efisiensi dan kebutuhan keputusan strategis
  Gejala (symptom) yang terukur     : Screening CV dan analisis turnover memakan waktu lama, akurasi keputusan HR belum konsisten, serta risiko bias/privasi sering dilaporkan
  Masalah yang didiagnosis          : Data HR belum siap analitik (tersebar dan tidak konsisten) serta belum ada evaluasi terpadu untuk kinerja model dan risiko etis
  Masalah riset (researchable)      : Belum jelas seberapa besar ML meningkatkan akurasi prediksi turnover/rekrutmen pada konteks MSDM Indonesia tanpa memperburuk bias dan risiko privasi
  Variabel yang terukur             : F1-score/AUC model, time-to-screening CV, tingkat turnover, demographic parity difference, dan jumlah insiden kepatuhan privasi

Problem Quality Check
  [x] Clarity — Apakah satu orang membaca akan paham?
  [x] Measurability — Apakah ada metrik kuantitatif?
  [x] Relevance — Apakah penting untuk domain?
  [x] Testability — Apakah bisa gagal?
  [x] Impact — Apakah ada kontribusi jika terjawab?

Problem Statement (1 paragraf):
  Berdasarkan temuan literatur pada implementasi machine learning di bidang MSDM, organisasi membutuhkan proses rekrutmen dan retensi yang lebih cepat serta akurat, namun masih menghadapi kendala kualitas data HR, bias algoritma, dan risiko privasi. Masalah riset yang dirumuskan adalah belum tersedianya evaluasi terukur pada konteks MSDM Indonesia untuk membuktikan apakah model machine learning benar-benar meningkatkan kualitas keputusan HR (misalnya prediksi turnover dan seleksi kandidat) sekaligus tetap adil dan patuh privasi. Oleh karena itu, penelitian perlu menguji kinerja model melalui metrik akurasi (F1/AUC), efisiensi proses (time-to-screening), serta metrik fairness dan kepatuhan data agar kontribusinya valid secara teknis dan etis.
```

---

## Latihan 1 — Dari Topik ke Masalah Riset

Pilih satu topik di bidang TI yang diminati. Transformasikan melalui 5 tahap Problem Formation Model.

**Topik awal:** Implementasi machine learning untuk rekrutmen dan prediksi turnover dalam MSDM

| Tahap | Hasil |
|-------|-------|
| Reality | Perusahaan membutuhkan keputusan MSDM yang cepat dan akurat, tetapi banyak proses HR masih manual. |
| Observed Issue (Symptom) | Waktu screening CV lama, identifikasi risiko resign terlambat, dan keputusan HR tidak konsisten antar evaluator. |
| Diagnosed Problem (Root Cause) | Data HR tersebar/tidak terstruktur, belum ada model prediksi yang tervalidasi, serta kontrol bias dan privasi belum terintegrasi. |
| Researchable Problem | Pada konteks MSDM Indonesia, belum ada evaluasi terukur yang menunjukkan model ML dapat meningkatkan akurasi rekrutmen/turnover sekaligus menjaga fairness dan privasi. |
| Measurable Variable | AUC/F1 prediksi turnover, waktu rata-rata screening CV, precision seleksi kandidat, demographic parity difference, dan jumlah temuan pelanggaran privasi. |

**Apakah terjebak solution-first thinking?** [ ] Ya / [x] Tidak
> Jika ya, kembali ke tahap mana? -

---

## Latihan 2 — System Context Decomposition

Gambarkan konteks sistem dari masalah riset di Latihan 1.

| Komponen | Deskripsi |
|----------|----------|
| Input | Data kandidat (CV, pengalaman, kompetensi), data historis karyawan (kinerja, absensi, mutasi, resign), dan kebijakan HR. |
| Process | Pembersihan dan integrasi data HR, pelatihan model ML, validasi model, evaluasi fairness, lalu penyajian rekomendasi untuk HRD. |
| Output | Skor kecocokan kandidat, prediksi risiko turnover, serta rekomendasi intervensi retensi/pelatihan. |
| Outcome | Efisiensi proses HR meningkat, keputusan lebih berbasis data, dan potensi turnover dapat diintervensi lebih awal. |
| Constraints | Data tidak lengkap, isu privasi dan keamanan, potensi bias algoritma, biaya infrastruktur/SDM data, dan resistensi budaya organisasi. |
| Stakeholders | HRD, manajer unit, karyawan, kandidat, tim data/IT, direksi, serta unit kepatuhan/hukum. |

**Komponen mana yang paling relevan dengan masalah riset?** Process dan Constraints

---

## Latihan 3 — Problem Quality Check

Evaluasi problem statement yang sudah dibuat menggunakan 5 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Clarity | 5 | Problem statement sudah menyebut domain, konteks, gap, dan batasan evaluasi. |
| Measurability | 5 | Variabel operasional jelas: AUC/F1, waktu screening, metrik fairness, dan indikator privasi. |
| Relevance | 5 | Isu efisiensi, bias, dan privasi pada HR berbasis ML sangat relevan dengan transformasi digital MSDM. |
| Testability | 4 | Hipotesis dapat diuji empiris, namun hasil sangat bergantung pada kualitas dan kelengkapan data organisasi. |
| Impact | 5 | Hasil riset berpotensi langsung memperbaiki kualitas keputusan HR dan tata kelola AI di organisasi. |

**Skor total:** 24 / 25

**Problem statement versi final (1 paragraf):**
> Implementasi machine learning pada MSDM menjanjikan efisiensi dan akurasi dalam rekrutmen serta prediksi turnover, tetapi organisasi masih menghadapi kualitas data yang rendah, risiko bias algoritma, dan tantangan privasi. Problem riset yang diajukan adalah belum adanya bukti terukur pada konteks MSDM Indonesia mengenai kemampuan model ML untuk meningkatkan kualitas keputusan HR tanpa mengorbankan fairness dan kepatuhan data. Penelitian karena itu perlu mengevaluasi model secara simultan pada aspek akurasi, efisiensi proses, fairness, dan privasi agar kontribusi teknologi dapat diadopsi secara bertanggung jawab.

---

## Refleksi

> Bandingkan "masalah" yang biasa ditemui saat coding (bug, error) dengan masalah riset. Apa perbedaan fundamental dalam cara mendefinisikan dan mendekati keduanya?

**Jawaban:**
> Masalah saat coding biasanya bersifat deterministik: ada perilaku yang diharapkan, ada gejala error, lalu diperbaiki sampai sistem kembali benar. Fokusnya adalah penyelesaian cepat terhadap penyebab teknis yang spesifik.
> Masalah riset bersifat epistemik: yang dicari adalah gap pengetahuan yang belum terjawab, sehingga perlu definisi variabel, batasan konteks, hipotesis yang bisa diuji, dan bukti yang dapat direplikasi. Jadi, pendekatannya bukan hanya “memperbaiki”, tetapi “membuktikan” dengan metode yang terukur.
