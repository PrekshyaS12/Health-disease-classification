# Heart Disease Prediction using Machine Learning

## Project Overview

This project predicts whether a patient has heart disease using machine learning algorithms. Multiple classification models were trained and evaluated, and the best-performing model was selected for deployment.

The application is deployed as an interactive web app using Streamlit, allowing users to enter patient information and receive a prediction in real time.

---

## Dataset

The project uses the Heart Disease dataset containing patient medical information such as:

- Age
- Resting Blood Pressure
- Cholesterol
- Maximum Heart Rate
- Oldpeak
- Number of Major Vessels
- Chest Pain Type
- Resting ECG
- Exercise-Induced Angina
- Thalassemia
- Other clinical features

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- SHAP
- Streamlit
- Pickle

---

## Machine Learning Models

The following models were trained and compared:

- Logistic Regression
- K-Nearest Neighbors (KNN)
- Support Vector Classifier (SVC)
- Gaussian Naive Bayes

---

## Best Model

**Support Vector Classifier (SVC)**

Performance on the test set:

- Accuracy: **84%**
- Precision: **90%**
- Recall: **83%**
- F1-score: **86%**

The SVC model achieved the highest accuracy among all evaluated models and was selected as the final prediction model.

---

## Explainable AI

To improve model transparency, SHAP (SHapley Additive exPlanations) was used.

The notebook includes:

- SHAP Summary Plot
- SHAP Feature Importance Bar Plot

These visualizations help explain which features have the greatest influence on the model's predictions.

---

## Streamlit Application

The Streamlit application allows users to:

- Enter patient information
- Predict the presence of heart disease
- View prediction confidence
- Interact with a simple and user-friendly interface

---

## Project Structure

```
Heart_Disease_Project/
│
├── app.py
├── heart_classification.ipynb
├── model.pkl
├── scaler.pkl
├── requirements.txt
├── README.md
└── heart_disease_uci.csv
```

---

## Installation

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
streamlit run app.py
```

---

## Known Issue (Fixed)

The deployed app initially returned a near-identical prediction regardless
of input. Root cause: the SVC model was trained on `StandardScaler`-
transformed features, but the inference script was feeding raw, unscaled
values directly into the model — pushing every input outside the
distribution the model was trained on. Fixed by persisting the fitted
scaler (`scaler.pkl`) and applying it to inputs before prediction.

---

## Future Improvements

- Hyperparameter tuning
- Additional explainability methods
- Model deployment to the cloud
- Larger datasets for training
- Performance optimization

---

##  Project By

**Prekshya Siwakoti**
