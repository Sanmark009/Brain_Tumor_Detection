
# 🧠 Brain Tumor Detection System

## 📌 Overview

Brain Tumor Detection is a machine learning / deep learning-based system designed to identify the presence of tumors in brain MRI scans. The goal is to assist medical professionals in faster and more accurate diagnosis.

---

## 🎯 Objective

* Detect whether a brain MRI image contains a tumor or not
* Classify tumor types (if applicable)
* Reduce manual diagnosis time
* Improve accuracy using AI models

---

## 🛠️ Tech Stack

| Layer       | Technology Used              |
| ----------- | ---------------------------- |
| Frontend    | HTML, CSS, JavaScript        |
| Backend     | Python (Flask / Django)      |
| ML/DL Model | TensorFlow / Keras / PyTorch |
| Database    | MySQL (optional)             |
| Tools       | OpenCV, NumPy, Matplotlib    |

---

## 📂 Dataset

* MRI Brain Scan Images
* Categories:

  * Tumor
  * No Tumor
* Source: Kaggle / Medical datasets

---

## ⚙️ Working Process

### 1. Data Collection

* Gather MRI scan images from datasets

### 2. Data Preprocessing

* Resize images
* Normalize pixel values
* Remove noise
* Data augmentation (optional)

### 3. Model Building

* Use CNN (Convolutional Neural Network)
* Layers:

  * Convolution Layer
  * Pooling Layer
  * Fully Connected Layer

### 4. Training

* Train model with labeled data
* Use epochs and batch size

### 5. Testing

* Evaluate model accuracy on test data

### 6. Prediction

* Upload MRI image
* Model predicts:

  * Tumor / No Tumor

---

## 🧠 Model Architecture (CNN)

```
Input Image
     ↓
Convolution Layer
     ↓
ReLU Activation
     ↓
Pooling Layer
     ↓
Flatten Layer
     ↓
Fully Connected Layer
     ↓
Output (Tumor / No Tumor)
```

---

## 📊 Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1-Score

---

## 🚀 Features

* User-friendly interface
* Fast prediction
* High accuracy detection
* Scalable system

---

## ⚠️ Limitations

* Depends on dataset quality
* Not a replacement for doctors
* Requires large training data

---

## 🔮 Future Enhancements

* Multi-class tumor classification
* Integration with hospital systems
* Real-time detection
* Mobile app support

---

## 📌 Conclusion

This project demonstrates how AI can be leveraged in healthcare to assist in early detection of brain tumors, improving diagnosis efficiency and supporting medical professionals.



Brain_Tumor_Dataset Link
.h5 file:
https://drive.google.com/file/d/17CNNdckAsXnhompleKW7xNHpYDZlXh8G/view?usp=sharing
Dataset_Link:
https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset
