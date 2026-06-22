# Tahap 3 — Implementasi Model LSTM

**Status:** Selesai
**Ketergantungan:** [tahap-1-pengumpulan-dan-preprocessing-data.md](tahap-1-pengumpulan-dan-preprocessing-data.md)

---

## 1. Arsitektur Jaringan LSTM (Deep Learning)
* **Tipe Model:** Sequential Recurrent Neural Network (RNN) dengan LSTM cells.
* **Tujuan:** Menguji performa representasi fitur otomatis dan dependensi temporal non-linear jangka panjang.
* **Input Layer:** Tensor 3D dengan dimensi `[batch_size, time_steps, features]` (time_steps = 60 hari, features = 11 kolom input).
* **Hidden Layers:**
  - **LSTM Layer 1:** 128 units, `return_sequences=True` (untuk melatih layer berikutnya).
  - **Dropout Layer 1:** Rate = 0.2 (mencegah overfitting/ko-adaptasi neuron).
  - **LSTM Layer 2:** 64 units, `return_sequences=False` (merangkum sequence menjadi flat vector).
  - **Dropout Layer 2:** Rate = 0.2.
* **Output Layer:** Dense layer tunggal dengan unit = 1 dan aktivasi linear untuk mengestimasi harga penutupan ternormalisasi hari esok.

## 2. Parameter Pembelajaran & Tuning
* **Optimizer:** Adam Optimizer dengan learning rate $\eta = 0.001$.
* **Loss Function:** Huber Loss (lebih robust terhadap outliers dibanding MSE).
* **Callbacks Pelatihan:**
  - **EarlyStopping:** Memantau `val_loss` dengan parameter `patience=15` dan `restore_best_weights=True` untuk memotong iterasi epoch jika model mulai overfit.
  - **ReduceLROnPlateau:** Menurunkan learning rate dengan faktor 0.5 jika `val_loss` tidak turun dalam 8 epoch (min_lr = $1 \times 10^{-6}$).
  - **ModelCheckpoint:** Menyimpan model dengan validation loss terbaik ke berkas `lstm_best_model.keras`.
* **Metode Pelatihan:** Dilatih selama maksimum 100 epoch dengan batch size = 32. Pengacakan dimatikan (`shuffle=False`) karena sifat time-series.

## 3. Hasil & Output yang Dihasilkan
- Model neural network disimpan otomatis per run: [`model_lstm_bbri.keras`](../06-output/run-1/model_lstm_bbri.keras) dan [`lstm_best_model.keras`](../06-output/run-1/lstm_best_model.keras).
- Grafik plot training history (Huber Loss vs Epoch, MAE vs Epoch) berhasil disimpan sebagai [`03_lstm_training.png`](../06-output/run-1/03_lstm_training.png).
