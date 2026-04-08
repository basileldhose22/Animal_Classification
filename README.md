# 🧠 Machine Learning Model Deployment (Streamlit App)

## 📌 Project Overview

This project demonstrates an end-to-end Machine Learning workflow, including data preprocessing, model training, saving models, and deploying them using a Streamlit web application.

The application allows users to input data and get predictions using a trained model.

---

## 🚀 Features

* Data preprocessing and feature engineering
* Multiple ML model training and evaluation
* Model comparison
* Saving trained models using joblib
* Streamlit-based interactive UI

---

## 📂 Project Structure

```
Aaps/
│
├── app.py                # Streamlit application
├── model.pkl             # Trained ML model
├── encoder.pkl           # Saved encoder (LabelEncoder/OneHotEncoder)
├── requirements.txt      # Dependencies
└── README.md             # Project documentation
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <your-repo-link>
cd Aaps
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The app will open in your browser.

---

## 🧩 Dependencies

* streamlit
* pandas
* numpy
* scikit-learn
* joblib

---

## 💾 Saving the Model

During training, models and encoders are saved using:

```python
import joblib

joblib.dump(model, 'model.pkl')
joblib.dump(encoder, 'encoder.pkl')
```

---

## ⚠️ Common Errors & Fixes

### ❌ FileNotFoundError: encoder.pkl

**Cause:** File not found in the directory

**Fix:**

* Ensure `encoder.pkl` exists in the project folder
* Use absolute path if needed:

```python
encoder = joblib.load(r'D:\Aaps\encoder.pkl')
```

---

## 📊 Model Workflow

1. Load dataset
2. Perform EDA (Exploratory Data Analysis)
3. Preprocess data
4. Train multiple models
5. Evaluate models
6. Save best model
7. Deploy using Streamlit

---

## 🧑‍💻 Author

Basil Eldhose

---

## 📄 License

This project is for educational purposes.
