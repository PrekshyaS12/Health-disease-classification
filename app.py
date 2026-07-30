import streamlit as st
import pickle
import numpy as np

# Load Model

model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb")) 

st.set_page_config(page_title="Heart Disease Prediction", page_icon="❤️")

st.title("Heart Disease Prediction")
st.write("Enter the patient's information below to predict whether heart disease is present.")


# Numerical Inputs

age = st.number_input("Age", min_value=20, max_value=100, value=50)

trestbps = st.number_input(
    "Resting Blood Pressure (trestbps)",
    min_value=80,
    max_value=250,
    value=120,
)

chol = st.number_input(
    "Cholesterol (chol)",
    min_value=100,
    max_value=700,
    value=200,
)

thalch = st.number_input(
    "Maximum Heart Rate (thalach)",
    min_value=60,
    max_value=250,
    value=150,
)

oldpeak = st.number_input(
    "Oldpeak",
    min_value=0.0,
    max_value=10.0,
    value=1.0,
    step=0.1,
)

ca = st.selectbox("Number of Major Vessels (ca)", [0, 1, 2, 3, 4])

# Categorical Inputs

sex = st.selectbox("Sex", ["Female", "Male"])

cp = st.selectbox(
    "Chest Pain Type",
    [
        "Typical Angina",
        "Atypical Angina",
        "Non-anginal Pain",
        "Asymptomatic"
    ]
)

fbs = st.selectbox(
    "Fasting Blood Sugar > 120 mg/dl",
    ["False", "True"]
)

restecg = st.selectbox(
    "Resting ECG",
    [
        "LV Hypertrophy",
        "Normal",
        "ST-T Abnormality"
    ]
)

exang = st.selectbox(
    "Exercise Induced Angina",
    ["False", "True"]
)

slope = st.selectbox(
    "Slope of Peak Exercise ST Segment",
    [
        "Downsloping",
        "Flat",
        "Upsloping"
    ]
)

thal = st.selectbox(
    "Thal",
    [
        "Fixed Defect",
        "Normal",
        "Reversible Defect"
    ]
)

# One-Hot Encoding

sex_Male = 1 if sex == "Male" else 0

cp_atypical = 1 if cp == "Atypical Angina" else 0
cp_non = 1 if cp == "Non-anginal Pain" else 0
cp_typical = 1 if cp == "Typical Angina" else 0

fbs_true = 1 if fbs == "True" else 0

restecg_normal = 1 if restecg == "Normal" else 0
restecg_st = 1 if restecg == "ST-T Abnormality" else 0

exang_true = 1 if exang == "True" else 0

slope_flat = 1 if slope == "Flat" else 0
slope_up = 1 if slope == "Upsloping" else 0

thal_normal = 1 if thal == "Normal" else 0
thal_reverse = 1 if thal == "Reversible Defect" else 0

# Prediction

if st.button("Predict"):

    sample = np.array([[

        age,
        trestbps,
        chol,
        thalch,
        oldpeak,
        ca,

        sex_Male,

        cp_atypical,
        cp_non,
        cp_typical,

        fbs_true,

        restecg_normal,
        restecg_st,

        exang_true,

        slope_flat,
        slope_up,

        thal_normal,
        thal_reverse

    ]])
    sample_scaled = scaler.transform(sample)

    prediction = model.predict(sample_scaled)[0]
    probability = model.predict_proba(sample_scaled)[0]

    if prediction == 1:
        st.error("⚠️ Heart Disease Detected")
        st.write(f"Confidence: **{probability[1]*100:.2f}%**")
    else:
        st.success("✅ No Heart Disease Detected")
        st.write(f"Confidence: **{probability[0]*100:.2f}%**")