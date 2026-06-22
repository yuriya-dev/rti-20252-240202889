# Arsitektur & Skema Model

Dokumen ini berisi rancangan arsitektur pemrosesan data, skema model LSTM, XGBoost, dan Hybrid Stacking.

## 1. Alur Pemrosesan Data (Pipeline)

```mermaid
graph TD
    A["Data Mentah Saham BBRI (2015-2025)"] --> B["Feature Engineering: Indikator Teknikal & Lag Features"]
    B --> C["Normalisasi Data (MinMax Scaling)"]
    C --> D["Data Windowing (Sliding Window = 60 hari)"]
    D --> E["Split Kronologis: 80% Train / 20% Test"]
    E --> F["Training Set"]
    E --> G["Testing Set"]
```

## 2. Arsitektur Model LSTM (Deep Learning)

```mermaid
graph TD
    A["Input Layer: 3D Tensor [Batch, 60, 11]"] --> B["LSTM Layer 1 (128 Units, return_sequences=True)"]
    B --> C["Dropout Layer 1 (Rate=0.2)"]
    C --> D["LSTM Layer 2 (64 Units, return_sequences=False)"]
    D --> E["Dropout Layer 2 (Rate=0.2)"]
    E --> F["Dense Output Layer (1 Unit, Linear Activation)"]
```

## 3. Arsitektur Model Hybrid Stacking (LSTM → XGBoost)

Model hybrid dirancang menggunakan arsitektur stacking dua tingkat (two-level stacking classifier/regressor):
- **Level 1 (Base Learner):** Model LSTM dilatih secara independen pada dataset training untuk memprediksi nilai target scaled. Prediksi LSTM pada training set dan testing set diambil sebagai representasi fitur temporal baru.
- **Level 2 (Meta Learner):** Model XGBoost dilatih menggunakan fitur-fitur lag, indikator teknikal, ditambah dengan fitur keluaran prediksi Level 1 dari LSTM. XGBoost belajar meminimalkan sisa kesalahan (residual error) dari LSTM.

```mermaid
graph TD
    A["Input Data: Fitur Lag + Indikator Teknikal"] --> B["Model LSTM (Base Learner)"]
    B --> C["Prediksi LSTM (Scaled Target)"]
    A --> D["Meta-features: Prediksi LSTM + Fitur Input Asli"]
    C --> D
    D --> E["Model XGBoost (Meta Learner)"]
    E --> F["Final Prediction (Reverse Scaled to Rupiah)"]
```

## 4. Hyperparameter Eksperimen Riil

### Model LSTM Baseline
* **Time Steps (Window):** 60 hari
* **LSTM Layer 1:** 128 units (Huber Loss, Adam Optimizer $\eta = 0.001$)
* **LSTM Layer 2:** 64 units
* **Dropout Rate:** 0.2
* **Epochs:** Max 100 dengan Early Stopping (patience=15)
* **Batch Size:** 32

### Model XGBoost Baseline
* **max_depth:** 6
* **learning_rate:** 0.05
* **n_estimators:** 500
* **subsample:** 0.8
* **colsample_bytree:** 0.8

### Model XGBoost Meta-Learner (Hybrid Stacking)
* **max_depth:** 5
* **learning_rate:** 0.03
* **n_estimators:** 600
* **subsample:** 0.8
* **colsample_bytree:** 0.7
* **early_stopping_rounds:** 30
