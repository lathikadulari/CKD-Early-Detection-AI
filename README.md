# 🩺 Chronic Kidney Disease (CKD) Early Detection System

This project is a high-accuracy diagnostic tool designed to assist healthcare professionals in identifying early signs of Chronic Kidney Disease (CKD). By leveraging Machine Learning, this system can analyze complex clinical markers and provide a real-time risk assessment through an interactive dashboard.

## 🌟 Key Technical Highlights
- **97.5% Accuracy:** Optimized K-Nearest Neighbors (KNN) classifier.
- **Advanced Data Recovery:** Implemented **KNN Imputation** to handle missing clinical markers, preserving 100% of the dataset integrity.
- **Precision Scaling:** Utilized **StandardScaler** to ensure unbiased distance calculations between diverse medical features.

## 🚀 Live Demo
[Insert your Streamlit link here after you deploy]

## 🛠️ Tech Stack
- **Languages:** Python
- **Libraries:** Scikit-Learn, Pandas, NumPy, Joblib
- **Deployment:** Streamlit Community Cloud

## 📊 How it Works
The model was trained on the UCI Chronic Kidney Disease dataset. It evaluates features such as Hemoglobin, Blood Pressure, Serum Creatinine, and Albumin levels. Using the **K=5** nearest neighbors approach, it classifies a patient's risk based on the clinical profiles of similar cases in the historical database.

---
*Created as a project for social impact in healthcare AI.*
