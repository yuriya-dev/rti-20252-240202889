# WS-12: Result Presentation & Visualization

> **Bab 12 — Penyajian Hasil & Visualisasi**

---

## Ringkasan Materi

### Data → Insight Model

```
Validated Data → Structured Presentation → Visualization → Pattern Recognition → Insight
```

Penyajian **mendahului** analisis. Tabel dan grafik membantu peneliti "melihat" data sebelum menghitung. Langsung ke uji statistik tanpa visualisasi berisiko kesimpulan yang secara teknis benar tapi kontekstual salah (Anscombe's Quartet, 1973).

### Tabel = Presisi, Grafik = Pola

Keduanya **saling melengkapi**:
- Tabel: angka presisi, self-contained (dipahami tanpa teks), sortable
- Grafik: pola visual, tren, perbandingan cepat

### Jenis Grafik Berdasarkan Tujuan

| Tujuan | Jenis Grafik |
|--------|-------------|
| Perbandingan antar-skenario | Bar chart (grouped/stacked) |
| Distribusi per-skenario | Box plot / violin plot |
| Tren temporal | Line chart |
| Korelasi dua variabel | Scatter plot |
| Proporsi (total = 100%) | Pie chart (hati-hati!) |

### Contoh Tabel Hasil yang Baik

| Model | Accuracy (%) | F1-Score (%) | Training Time (min) |
|-------|-------------|-------------|---------------------|
| BERT | 88.4 ± 1.2 | 87.1 ± 1.4 | 45.2 ± 3.1 |
| LSTM | 86.1 ± 1.8 | 84.5 ± 2.0 | 12.8 ± 1.2 |
| SVM | 82.3 ± 0.9 | 80.7 ± 1.1 | 0.3 ± 0.1 |

*N=10 per model. Mean ± std. Diurutkan berdasarkan Accuracy.*

### Visualization Bias — Yang Harus Dihindari

| Bias | Deskripsi | Dampak |
|------|----------|--------|
| Truncated axis | Y tidak dari 0 | Memperbesar perbedaan kecil |
| Inconsistent scale | Dua grafik skala beda | Perbandingan menyesatkan |
| Cherry-picked data | Hanya tampilkan yang "menang" | Selektif, tidak jujur |
| 3D effects | Efek 3D tanpa dimensi data ke-3 | Distorsi tanpa informasi |
| Missing error bar | Tidak ada variabilitas | Menyembunyikan ketidakpastian |

### Engineering vs Research Presentation

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan grafik | Dashboard monitoring | Mendukung argumen ilmiah |
| Informasi wajib | KPI, threshold | Mean, std, CI, N, p-value |
| Bias handling | Less critical | Wajib dihindari (peer-review) |

---

## Template A.12 — Result Presentation Plan

```
RESULT PRESENTATION PLAN

Research Question : Apakah LSTM menghasilkan MAE dan RMSE lebih rendah serta R² lebih tinggi
                    dibanding baseline XGBoost pada dataset harga penutupan harian saham BBRI
                    (2015–2025)?
Metrik Utama      : MAE (Rp) dan RMSE (Rp) — primary; R² dan MAPE (%) — secondary

Tabel Hasil (mean ± std, N=10 run per skenario):
| Skenario              | MAE — mean ± std (Rp)   | RMSE — mean ± std (Rp)  | R² — mean ± std | MAPE — mean ± std (%) | n  |
|-----------------------|------------------------|------------------------|-----------------|----------------------|----|
| XGBoost Baseline      | 126.15 ± 4.59          | 188.57 ± 4.04          | 0.8412 ± 0.0068 | 3.14 ± 0.13          | 10 |
| Hybrid LSTM→XGBoost   | 128.61 ± 6.63          | 193.76 ± 5.46          | 0.8323 ± 0.0095 | 3.19 ± 0.19          | 10 |
| LSTM Baseline         | 229.03 ± 26.45         | 301.61 ± 30.94         | 0.5901 ± 0.0808 | 5.56 ± 0.64          | 10 |

Visualisasi yang Direncanakan:
| # | Jenis Grafik             | Pesan Utama                                          | Metrik                     |
|---|--------------------------|------------------------------------------------------|----------------------------|
| 1 | Grouped bar chart + error bar | Perbandingan mean MAE dan RMSE antar 3 model   | Mean MAE ± std, Mean RMSE ± std |
| 2 | Box plot                 | Distribusi dan variabilitas R² per skenario          | Semua nilai R² (10 run)    |
| 3 | Line chart (time-series) | Perbandingan prediksi vs harga aktual BBRI           | y_pred vs y_true test set  |
| 4 | Rolling MAE line chart   | Konsistensi model sepanjang test set (60-day window) | Rolling MAE per hari       |

Bias Check:
  [x] Y-axis mulai dari 0 (atau dijustifikasi)
  [x] Error bar/CI ditampilkan
  [x] Semua data disertakan (tidak cherry-picked)
  [x] Tidak menggunakan 3D tanpa alasan
```

---

## Latihan 1 — Tabel Hasil

Buat tabel hasil eksperimen Anda (boleh dengan data simulasi jika belum punya data riil).

**Tabel 1. Perbandingan Performa Model Prediksi Harga Saham BBRI (2015–2025)**

*N = 10 run per skenario. Mean ± std. Diurutkan berdasarkan MAE (metrik utama). Data dari `06-output/run-1` s.d. `run-10`.*

| Skenario                 | MAE (mean ± std, Rp) | RMSE (mean ± std, Rp) | R² (mean ± std) | MAPE (mean ± std, %) | n  |
|--------------------------|----------------------|----------------------|-----------------|----------------------|----|
| **XGBoost Baseline**     | **126.15 ± 4.59**    | **188.57 ± 4.04**    | **0.8412 ± 0.0068** | **3.14 ± 0.13**  | 10 |
| Hybrid (LSTM→XGBoost)    | 128.61 ± 6.63        | 193.76 ± 5.46        | 0.8323 ± 0.0095 | 3.19 ± 0.19          | 10 |
| LSTM Baseline            | 229.03 ± 26.45       | 301.61 ± 30.94       | 0.5901 ± 0.0808 | 5.56 ± 0.64          | 10 |

> **Catatan interpretasi:** XGBoost Baseline mengungguli LSTM di seluruh metrik dengan selisih MAE ~45% lebih rendah (126 vs 229 Rp). Hybrid Stacking tidak menghasilkan peningkatan signifikan atas XGBoost saja (MAE hanya 2% lebih tinggi, p = 0.0056). Variabilitas LSTM (std = 26.45 Rp) jauh lebih tinggi dibanding XGBoost (std = 4.59 Rp), menunjukkan XGBoost lebih stabil lintas seed.

**Checklist tabel:**
- [x] Self-contained (judul jelas, satuan ada, N tercantum)
- [x] Mean ± std (bukan single number)
- [x] Diurutkan berdasarkan metrik utama (MAE ascending)
- [x] Format konsisten di semua baris

---

## Latihan 2 — Rencana Visualisasi

Rencanakan 2-3 grafik untuk menyajikan data dari Latihan 1. Setiap grafik = satu pesan.

| # | Jenis Grafik | Pesan | Data yang Digunakan | File Referensi |
|---|-------------|-------|---------------------|----------------|
| 1 | **Grouped bar chart + error bar** | XGBoost dan Hybrid jauh lebih akurat dari LSTM; XGBoost dan Hybrid setara | Mean MAE ± std dan Mean RMSE ± std per skenario (3 kelompok) | `06-output/run-*/hasil_metrik_komparasi.csv`, `06-komparasi_metrik.png` |
| 2 | **Box plot** | Distribusi R² XGBoost sangat rapat (stabil), LSTM sangat lebar (tidak stabil) | Semua nilai R² dari 10 run per skenario | `06-output/run-*/hasil_metrik_komparasi.csv` |
| 3 | **Line chart (time-series overlay)** | XGBoost dan Hybrid mengikuti tren aktual lebih dekat daripada LSTM | Harga aktual + y_pred LSTM/XGBoost/Hybrid pada test set | `06-output/run-1/05_prediksi_vs_aktual.png`, `hasil_prediksi_lengkap.csv` |
| 4 | **Rolling MAE line chart** | XGBoost mempertahankan MAE rendah sepanjang test set; LSTM melonjak di periode volatil | Rolling MAE 60-hari tiap model | `06-output/run-1/08_rolling_mae.png` |

> Semua grafik tersebut sudah dihasilkan secara otomatis oleh `05-kode/BBRI_Stock_Prediction.ipynb` dan tersimpan di `06-output/run-1/` s.d. `run-10/`. Grafik #1 dan #3 adalah yang paling krusial untuk mendukung argumen ilmiah di manuskrip.

---

## Latihan 3 — Bias Detection

Evaluasi visualisasi berikut untuk bias (skenario dari contoh):

**Skenario:** Metode A = 91.2%, Metode B = 90.8%. Bar chart dengan Y-axis mulai dari 90%.

| Pertanyaan | Jawaban |
|-----------|---------|
| Apakah Y-axis menyesatkan? | **Ya** — dengan Y-axis mulai dari 90%, batang A terlihat ±2× lebih tinggi dari B, padahal perbedaan absolutnya hanya 0.4 pp. Ini adalah *truncated axis bias* klasik. |
| Apakah error bar ditampilkan? | **Tidak** — tanpa error bar/CI, kita tidak tahu apakah perbedaan 0.4% ini secara statistik signifikan atau hanya noise. |
| Apakah semua kondisi ditampilkan? | Bergantung konteks — jika hanya dua dari banyak metode yang ditampilkan, ini berpotensi *cherry-picking*. |
| Apa solusinya? | (1) Mulai Y-axis dari 0, atau tambahkan axis break yang eksplisit. (2) Tambahkan error bar ± std atau 95% CI. (3) Tampilkan semua kondisi eksperimen. (4) Laporkan p-value untuk membuktikan signifikansi. |

**Evaluasi grafik riset BBRI dari Latihan 2:**

| Bias | Grafik #1 (Bar) | Grafik #2 (Box Plot) | Grafik #3 (Line) | Grafik #4 (Rolling) |
|------|:--------------:|:--------------------:|:----------------:|:-------------------:|
| Truncated axis | ✅ Mulai dari 0 | ✅ Full range | ✅ Harga aktual | ✅ Full range |
| Error bar/CI ditampilkan | ✅ ± std bar | ✅ IQR + whisker | ➖ N/A | ➖ N/A |
| Semua kondisi ditampilkan | ✅ 3 model | ✅ 3 model | ✅ 3 model | ✅ 3 model |
| Tidak ada efek 3D | ✅ | ✅ | ✅ | ✅ |

- [x] Semua bias check lulus untuk keempat grafik
- [ ] Ada yang perlu diperbaiki: *Grafik #3 line chart sebaiknya mencantumkan bandwidth prediksi (min/max dari 10 run) sebagai shaded area untuk menunjukkan variabilitas antar-seed secara jujur.*

---

## Refleksi

> Mengapa tabel dan grafik keduanya diperlukan — tidak cukup salah satu saja? Pernahkah Anda membuat grafik yang (tanpa sengaja) menyesatkan?

> **Mengapa keduanya diperlukan:**
> Tabel dan grafik melayani dua kebutuhan kognitif yang berbeda dan saling tidak dapat digantikan. Tabel memberikan **presisi numerik**: pembaca bisa membandingkan angka secara eksak (contoh: MAE XGBoost 126.15 Rp vs Hybrid 128.61 Rp — selisih 1.9%), memeriksa ukuran variabilitas (std), dan memverifikasi klaim dalam review. Tanpa tabel, pembaca tidak bisa mereplikasi temuan. Sebaliknya, grafik memberikan **persepsi pola visual** yang tidak bisa dicerna dari tabel: tren temporal, distribusi, dan perbandingan relatif ditangkap dalam hitungan detik. Misalnya, dari tabel saja sulit segera "melihat" bahwa LSTM sangat tidak stabil (std = 26.45 Rp vs XGBoost 4.59 Rp), tetapi box plot langsung mengungkapkannya. Prinsip Anscombe's Quartet (1973) membuktikan bahwa empat dataset dengan mean dan std identik bisa memiliki pola yang sama sekali berbeda — hanya tampak jelas di scatter plot. Riset yang hanya menyajikan tabel berisiko melewatkan anomali pola; yang hanya menyajikan grafik tidak bisa diverifikasi angkanya.
>
> **Pengalaman membuat grafik yang (tidak sengaja) menyesatkan:**
> Dalam proses eksplorasi awal riset ini, kami sempat memplot bar chart MAE ketiga model dengan Y-axis yang di-zoom ke rentang 100–250 Rp (bukan mulai dari 0). Hasilnya, batang LSTM terlihat sekitar 3× lebih tinggi dari XGBoost secara visual, padahal perbedaan absolutnya "hanya" ~100 Rp dari baseline sekitar 125 Rp. Grafik itu secara teknis tidak salah, tetapi secara visual dramatis berlebihan. Setelah menemukan bias ini, kami mengubah Y-axis ke 0 dan menambahkan error bar — hasilnya jauh lebih jujur meski perbedaannya tetap jelas terlihat signifikan, karena selisih 45% MAE memang besar secara substantif.
