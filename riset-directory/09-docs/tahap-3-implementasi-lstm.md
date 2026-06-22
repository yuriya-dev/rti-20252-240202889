# Tahap 3 — Implementasi Model LSTM

**Status:** Belum Mulai
**Ketergantungan:** [tahap-1-pengumpulan-dan-preprocessing-data.md](tahap-1-pengumpulan-dan-preprocessing-data.md)

---

## 1. Arsitektur Jaringan LSTM
* **Arsitektur Utama:** Long Short-Term Memory (LSTM) recurrent neural network.
* **Tujuan:** Menguji keunggulan arsitektur deep learning dalam menangkap pola dependensi jangka panjang dan hubungan non-linear.
* **Input Layer:** Tensor 3D `[batch_size, time_steps, features]` (misal: time_steps = 30 hari).
* **Hidden Layers:** Variasi jumlah layer LSTM (1 s.d. 3 layer) dengan unit tersembunyi (misal: 32, 64, 128) dan layer Dropout untuk mencegah overfitting.
* **Output Layer:** Dense layer tunggal dengan aktivasi linear untuk estimasi harga penutupan BBRI.

## 2. Parameter Pembelajaran & Tuning
* **Optimizer:** Adam Optimizer (learning rate default atau disetel).
* **Loss Function:** Mean Squared Error (MSE).
* **Metode Pelatihan:** Batch training dengan EarlyStopping (memantau validation loss) untuk efisiensi training epoch.

## 3. Hasil & Output yang Diharapkan
* Script training model deep learning di `riset-directory/05-kode/`.
* Log hasil training (training loss vs validation loss) untuk analisis stabilitas model.
* Model LSTM tersimpan (.h5 atau SavedModel format Keras).
