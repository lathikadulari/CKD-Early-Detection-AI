import streamlit as st
import joblib
import numpy as np

# Load the saved brain and scaler
model = joblib.load('ckd_model.pkl')
scaler = joblib.load('scaler.pkl')

st.title("🩺 CKD Early Detection Dashboard")
st.markdown("Enter the patient's clinical metrics to predict Chronic Kidney Disease.")

# Create input fields
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=1, max_value=100, value=40)
    bp = st.number_input("Blood Pressure (mm/Hg)", min_value=50, max_value=200, value=80)
    hemo = st.number_input("Hemoglobin", min_value=3.0, max_value=20.0, value=15.0)

with col2:
    al = st.selectbox("Albumin Level (0-5)", [0, 1, 2, 3, 4, 5])
    sc = st.number_input("Serum Creatinine", min_value=0.1, max_value=15.0, value=1.2)
    htn = st.selectbox("Hypertension?", ["No", "Yes"])

htn_num = 1 if htn == "Yes" else 0

# Prediction Logic
if st.button("Analyze Patient Data"):
    # Create the input array (ensuring 24 features)
    input_data = np.zeros(24) 
    input_data[0] = age
    input_data[1] = bp
    input_data[3] = al
    input_data[11] = sc
    input_data[14] = hemo
    input_data[18] = htn_num
    
    try:
        # Scale and Predict
        scaled_features = scaler.transform([input_data])
        prediction = model.predict(scaled_features)
        
        if prediction[0] == 1:
            st.error("⚠️ Result: High Risk of Chronic Kidney Disease (CKD)")
        else:
            st.success("✅ Result: Low Risk / Healthy")
    except Exception as e:
        st.error(f"Error: {e}")