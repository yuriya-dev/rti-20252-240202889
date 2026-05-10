# WS-06: System-Experiment Mapping

> **Bab 6 — System Design sebagai Experimental Artifact**

---

## Ringkasan Materi

### Sistem = Instrumen Pengujian, Bukan Produk

Seorang engineer bertanya "apakah sistem bekerja?" — seorang peneliti bertanya "apa yang bisa dibuktikan sistem ini?" Sistem dalam riset adalah **artifact** — objek yang sengaja dibuat untuk menguji klaim spesifik.

### System as Experiment Model

```
RQ → Variable → System Component → Experimental Setup → Output
```

Setiap komponen sistem harus bisa ditelusuri ke variabel riset (top-down), dan setiap pengukuran harus menjawab RQ (bottom-up).

### Mapping Variabel ke Komponen

| Tipe Variabel | Peran di Sistem | Contoh |
|---------------|----------------|--------|
| **IV** (Independent) | Modul yang bisa di-toggle/swap | Algoritma A vs B |
| **DV** (Dependent) | Modul pengukuran | Logger, metrics collector |
| **CV** (Control) | Config yang dikunci | Dataset, parameter tetap |

Jika variabel tidak bisa di-map ke komponen apapun → arsitektur perlu didesain ulang.

### 4 Prinsip Desain Eksperimental

| Prinsip | Pertanyaan Kunci |
|---------|-----------------|
| **Traceability** | Komponen ini melayani variabel yang mana? |
| **Modularity** | Bisakah IV diubah tanpa memengaruhi yang lain? |
| **Controllability** | Apakah CV dieksternalisasi ke config file? |
| **Measurability** | Apakah sistem otomatis menghasilkan data yang dibutuhkan? |

### Variable Isolation melalui Arsitektur

- **Modular architecture** — Pisahkan berdasarkan variabel
- **Configuration-driven** — Ubah config (YAML/JSON), bukan code
- **Feature toggles** — On/off flag untuk ablation study

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan sistem | Memenuhi kebutuhan user | Menguji hipotesis, menghasilkan bukti |
| Arsitektur | Optimasi performa & skalabilitas | Optimasi isolasi variabel & reprodusibilitas |
| Konfigurasi | Sering hardcoded | Dieksternalisasi ke config file |
| Fitur tambahan | Menambah nilai user | Menambah noise jika tidak terkait RQ |

### Istilah Penting

- **Artifact** — Objek yang sengaja dibuat untuk memecahkan masalah atau menguji proposisi
- **Traceability** — Kemampuan menelusuri hubungan RQ → variabel → komponen → output
- **Variable Isolation** — Mengubah hanya satu variabel sambil menahan yang lain konstan
- **Ablation Study** — Menguji kontribusi tiap komponen dengan melepasnya satu per satu
- **Configuration-driven Execution** — Semua parameter di config file, bukan hardcoded

---

## Template A.6 — Mapping RQ ke Arsitektur Sistem

```
SYSTEM-EXPERIMENT MAPPING

Research Question: Apakah LSTM menghasilkan MAE dan RMSE lebih rendah serta R2 lebih tinggi dibanding baseline XGBoost pada dataset harga penutupan harian saham BBRI (2015-2025) dari Investing.com/Yahoo Finance?

Variable → Component Mapping:
| Variabel | Tipe | Komponen Sistem | Cara Manipulasi/Pengukuran |
|----------|------|-----------------|---------------------------|
| Jenis model (LSTM vs XGBoost) | IV   | Modul model | Ganti `model_type` di config dan jalankan pipeline pelatihan | 
| Akurasi prediksi harga saham | DV   | Modul evaluasi metrik | Hitung RMSE, MAE, R2, MAPE pada test set dan simpan ke report |
| Dataset dan konfigurasi tetap | CV   | Data loader + preprocessing | Kunci dataset BBRI 2015-2025, split 80/20, window 30, MinMax, seed 42 |

4 Prinsip Desain:
  [x] Traceability — Setiap komponen bisa ditelusuri ke variabel
  [x] Variable Isolation — IV bisa diubah tanpa mengubah CV
  [x] Measurement Integration — Pengukuran DV built-in
  [x] Reproducibility — Setup bisa direkonstruksi

Experimental Setup:
  Input data     : Harga penutupan harian BBRI 2015-2025 (OHLCV jika tersedia)
  Parameter      : Split 80/20, window size 30, MinMax scaling, seed 42
  Output format  : Tabel metrik (RMSE/MAE/R2/MAPE), plot prediksi vs aktual, log konfigurasi
```

---

## Latihan 1 — Variable-to-Component Mapping

Gunakan RQ dan variabel dari WS-05. Petakan ke komponen sistem.

**RQ:** Apakah LSTM menghasilkan MAE dan RMSE lebih rendah serta R2 lebih tinggi dibanding baseline XGBoost pada dataset harga penutupan harian saham BBRI (2015-2025) dari Investing.com/Yahoo Finance?

| Variabel | Tipe | Komponen Sistem | Cara Manipulasi / Pengukuran |
|----------|------|-----------------|---------------------------|
| Jenis model | IV | Modul model (swap LSTM <-> XGBoost) | Ganti config `model_type` |
| Akurasi prediksi | DV | Modul evaluasi metrik | Hitung RMSE/MAE/R2/MAPE pada test set |
| Konfigurasi eksperimen | CV | Data loader + preprocessing | Kunci dataset, split, window, scaler, seed |

**Apakah semua variabel bisa di-map?** [x] Ya / [ ] Tidak
> Jika tidak, komponen apa yang perlu ditambahkan? N/A

---

## Latihan 2 — 4 Prinsip Desain

Evaluasi desain sistem terhadap 4 prinsip.

| Prinsip | Status | Bukti / Penjelasan |
|---------|--------|-------------------|
| Traceability | Ya | Setiap modul (data, model, evaluasi) ditautkan ke variabel riset |
| Modularity | Ya | Model LSTM/XGBoost dapat ditukar tanpa mengubah preprocessing |
| Controllability | Ya | Semua CV dikunci di config dan dicatat di log |
| Measurability | Ya | Metrik dihitung otomatis dan diekspor |

**Prinsip mana yang paling sulit dipenuhi?** Controllability
**Strategi untuk mengatasinya:**
> Kunci semua CV di config, log versi library, dan gunakan split kronologis yang konsisten.

---

## Latihan 3 — Ablation Study Planning

Jika sistem memiliki 3 komponen utama, rencanakan ablation study.

| Kondisi | Komponen A | Komponen B | Komponen C | Hasil yang Diharapkan |
|---------|-----------|-----------|-----------|----------------------|
| Full | ON indikator teknikal | ON windowing sequence | ON MinMax scaling | Baseline penuh |
| – A | OFF (tanpa indikator) | ON | ON | Error naik, terutama pada XGBoost |
| – B | ON | OFF (tanpa windowing) | ON | LSTM kehilangan pola temporal, error naik |
| – C | ON | ON | OFF (tanpa scaling) | Training LSTM tidak stabil, error naik |

**Komponen mana yang diprediksi paling berkontribusi?** Komponen B (windowing sequence)
**Mengapa?**
> Windowing memberi konteks temporal yang diperlukan LSTM untuk belajar pola deret waktu.

---

## Refleksi

> Apa risiko jika sistem dibangun seperti produk (monolitik, fitur lengkap) lalu baru dilakukan eksperimen? Mengapa arsitektur modular penting untuk riset?

**Jawaban:**
> Sistem monolitik sulit mengisolasi variabel, sehingga perubahan kecil bisa memengaruhi banyak komponen.
> Arsitektur modular penting agar IV bisa diubah tanpa mengganggu CV dan pengukuran DV tetap konsisten.
