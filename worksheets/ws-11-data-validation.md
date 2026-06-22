# WS-11: Data Validation & Integrity

> **Bab 11 — Validasi Data & Integritas**

---

## Ringkasan Materi

### Data Trust Model

```
Raw Data → Data Cleaning → Consistency Check → Validation Process → Trusted Data
```

Data mentah belum bisa dipercaya. Harus melewati pipeline validasi sebelum siap untuk analisis statistik.

### Empat Pilar Data Quality

| Pilar | Deskripsi | Contoh Pelanggaran |
|-------|----------|-------------------|
| **Accuracy** | Nilai dalam range masuk akal | Akurasi = 1.5 (di luar [0,1]) |
| **Consistency** | Format seragam di semua run | Run 1: CSV, Run 2: JSON |
| **Completeness** | Tidak ada data hilang dari plan | 97 dari 100 run tercatat |
| **Validity** | Data sesuai desain eksperimen | Parameter baseline tercampur treatment |

### Proses Validasi Progresif

1. **Format validation** — Tipe file, header, kolom
2. **Range validation** — Nilai dalam batas logis
3. **Consistency validation** — Format seragam antar-run
4. **Logic validation** — Data cocok dengan desain eksperimen

Jika gagal di langkah awal → tidak perlu lanjut.

### Anomaly Detection — 3 Jenis

| Jenis | Deskripsi | Deteksi |
|-------|----------|---------|
| **Statistical outlier** | Nilai di luar distribusi normal | IQR: < Q1-1.5×IQR atau > Q3+1.5×IQR |
| **Contextual anomaly** | Normal absolut, abnormal dalam konteks | Run 1-10: ~91%, Run 11-20: ~88% |
| **Pattern anomaly** | Pola sistematis (bukan random) | Performa menurun berurutan |

**Prinsip:** Detect → Investigate → Document → Decide — **JANGAN langsung hapus.**

### Engineering vs Research Validation

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan | Data sesuai spesifikasi bisnis | Data layak untuk analisis statistik |
| Missing data | Impute / set default | Investigasi penyebab → dokumentasi |
| Outlier | Bug → fix | Mungkin temuan → investigasi |
| Dokumentasi | Minimal (log error) | Komprehensif (anomali + keputusan) |

### Jebakan Kognitif

1. "Logging otomatis ≠ data benar" → bisa ada bug di logger
2. "Outlier = hapus" → bisa jadi temuan penting
3. "Dataset kecil tidak perlu validasi" → justru lebih rentan
4. "Mean normal = data benar" → [94, 95, 93, **44**, 94] → mean 84% terlihat wajar

---

## Template A.11 — Data Validation Checklist

```
DATA VALIDATION CHECKLIST

Completeness:
  [ ] Semua skenario tercakup
  [ ] Jumlah run sesuai rencana
  [ ] Tidak ada file output hilang
  Missing: ____ dari ____ data points

Format Consistency:
  [ ] Semua file format sama (CSV/JSON/...)
  [ ] Header konsisten
  [ ] Tipe data konsisten (numerik tetap numerik)

Range & Logic:
  [ ] Nilai dalam range masuk akal
  [ ] Tidak ada waktu negatif
  [ ] Metrik 0–100%, tidak di luar range
  Anomali ditemukan: ____________________

Cross-Validation:
  [ ] Run identik → hasil mendekati
  [ ] Trend konsisten dengan ekspektasi teori

Keputusan:
  [ ] Data siap analisis
  [ ] Perlu cleaning
  [ ] Perlu re-run (skenario: ____)
```

---

## Latihan 1 — Completeness Check

Verifikasi apakah semua data yang direncanakan sudah terkumpul.

| Skenario | Run Direncanakan | Run Tercatat | Missing | Alasan |
|----------|-----------------|-------------|---------|--------|
| LSTM Baseline | 10 | 10 | 0 | — |
| XGBoost Baseline | 10 | 10 | 0 | — |
| Hybrid Stacking | 10 | 10 | 0 | — |

**Total expected:** 30 data points (3 model x 10 runs) | **Total actual:** 30 | **Missing:** 0

**Keputusan untuk data missing:**
> Tidak ada data yang hilang. Seluruh 10 run eksekusi untuk ketiga model berhasil dijalankan dengan lengkap dan tersimpan dengan baik di folder output masing-masing run.

---

## Latihan 2 — Anomaly Investigation

Periksa data Anda untuk anomali. Gunakan metode IQR atau z-score.

**Dataset sampel (atau data Anda sendiri):**

| Run | Accuracy (%) |
|-----|-------------|
| 1 | *91.2* |
| 2 | *90.8* |
| 3 | *91.5* |
| 4 | *78.3* |
| 5 | *91.0* |

**Deteksi outlier:**
- Q1 = 90.8 | Q3 = 91.2 | IQR = 0.4
- Batas bawah (Q1 - 1.5×IQR) = 90.2
- Batas atas (Q3 + 1.5×IQR) = 91.8
- Outlier terdeteksi: Run 4 (78.3%)

**Investigasi (untuk setiap outlier):**

| Outlier | Nilai | Kemungkinan Penyebab | Keputusan |
|---------|-------|---------------------|-----------|
| *Run 4* | *78.3%* | *Thermal throttling pada CPU setelah mengeksekusi 3 run berat berturut-turut tanpa jeda pendinginan* | *Re-run secara manual dengan memberikan interval pendinginan 60 detik antar run* |

---

## Latihan 3 — Validation Report

Buat laporan validasi ringkas untuk dataset eksperimen Anda.

**1. Completeness:** 100% data terkumpul (10 dari 10 run selesai)
**2. Format:** [x] Konsisten / [ ] Ada inkonsistensi: ____
**3. Range check (anomali):** Tidak ditemukan anomali. Semua metrik MAE/RMSE bernilai positif dan masuk akal, nilai $R^2$ berada di rentang [0, 1] (0.59 s.d. 0.85), dan visualisasi PNG berhasil dibuat secara utuh.
**4. Logic check:** [x] Parameter sesuai plan / [ ] Ada ketidaksesuaian: ____

**Kesimpulan:** [x] Data siap analisis / [ ] Perlu tindakan: ____

---

## Refleksi

> Apa perbedaan antara "data yang benar" dan "data yang dipercaya"? Mengapa proses validasi formal diperlukan meskipun data dikumpulkan secara otomatis?

> **Perbedaan data yang benar vs data yang dipercaya:**
> Data yang benar adalah data yang secara numerik akurat dan bebas dari bug perhitungan dasar pada saat dicatat. Sementara data yang dipercaya (trusted data) adalah data yang telah divalidasi integritasnya (lengkap, formatnya konsisten di seluruh run, parameternya sesuai dengan design plan, dan bebas dari outlier anomali komputasional) sehingga layak secara ilmiah untuk dianalisis secara statistik.
>
> **Mengapa validasi formal tetap diperlukan:**
> Pengumpulan otomatis (automated logging) tidak menjamin integritas ilmiah. Bug tersembunyi pada pustaka (seperti inisialisasi bobot keras yang mendadak divergen pada seed tertentu), kegagalan koneksi API saat mengunduh data pasar secara real-time, atau degradasi performa perangkat keras (seperti thermal throttling) dapat merusak kualitas data tanpa menghentikan jalannya script (tanpa memicu crash/error). Validasi formal memastikan bahwa anomali-anomali semacam ini dideteksi secara proaktif agar tidak mencemari kesimpulan riset.
