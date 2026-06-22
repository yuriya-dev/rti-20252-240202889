# Tahap 5 — Penulisan Draf Paper Jurnal

**Status:** Selesai
**Ketergantungan:** [tahap-4-eksperimen-dan-evaluasi.md](tahap-4-eksperimen-dan-evaluasi.md)

---

## 1. Tujuan
Menyusun naskah draf paper publikasi ilmiah berdasarkan hasil eksperimen terkontrol 10 run yang membandingkan performa LSTM vs XGBoost vs Hybrid Stacking pada saham BBRI.

## 2. Peta Dokumen & Progres Deliverable
Draf paper telah ditulis secara komprehensif di dalam berkas tunggal yang mewakili template jurnal standar:

| Bagian Dokumen | Lokasi Berkas | Status | Deskripsi |
|---|---|---|---|
| Naskah Gabungan Lengkap | [`07-manuskrip/naskah-jurnal.md`](../07-manuskrip/naskah-jurnal.md) | Selesai | Dokumen jurnal terintegrasi (§1 s.d. §5 + Daftar Pustaka) |
| Laporan Hasil & Latar Belakang | [`08-laporan/laporan-penelitian.md`](../08-laporan/laporan-penelitian.md) | Selesai | Laporan naratif dan peta detail artefak penelitian |

## 3. Catatan Penulisan
- **Metodologi:** Detail preprocessing data (MinMax scaling, sliding window 60 hari), arsitektur model LSTM (128-64 units), parameter XGBoost baseline, dan model Hybrid Stacking terdokumentasi lengkap.
- **Hasil & Pembahasan:** Mengintegrasikan rekapitulasi data mean ± std dari 10 run dan hasil uji statistik Wilcoxon Signed-Rank Test yang dilakukan di Tahap 4.
- **Daftar Pustaka:** Mengacu pada sitasi standar terkait perbandingan model machine learning dan deep learning untuk data keuangan.
