# Tahap 1 — Pengumpulan & Preprocessing Data Saham BBRI

**Status:** Belum Mulai

---

## 1. Sumber Data & Parameter
* **Emiten:** PT Bank Rakyat Indonesia (Persero) Tbk (BBRI.JK)
* **Periode:** 2015-2025
* **Penyedia Data:** Yahoo Finance API / Investing.com
* **Fitur Utama:** Open, High, Low, Close, Adj Close, Volume (OHLCV)

## 2. Rencana Preprocessing
1. **Handling Missing Values:** Pengecekan hari libur bursa dan interpolasi jika terdapat data kosong.
2. **Feature Engineering:** Penambahan indikator teknikal (misal: Simple Moving Average (SMA), Exponential Moving Average (EMA), Relative Strength Index (RSI)) jika diperlukan.
3. **Data Scaling:** Menggunakan MinMax Scaling untuk menormalkan rentang harga ke skala `[0, 1]`.
4. **Data Windowing:** Pembuatan sequence input (window size, misal: 30 hari data historis) untuk memprediksi harga hari berikutnya ($t+1$).
5. **Data Splitting:** Pembagian dataset secara kronologis (misal: 80% Training Set, 20% Testing Set) tanpa pengocokan acak (non-shuffled) untuk menjaga sifat time-series data.

## 3. Hasil & Output yang Diharapkan
* Dataset bersih berformat CSV di `riset-directory/04-data/`.
* Statistik deskriptif dataset sebelum dan sesudah preprocessing.
