# Heart Disease Prediction — Clinical Classification Model

A machine learning project to predict the presence of heart disease in patients using real clinical data from four major hospital datasets. Multiple classification algorithms are compared to identify the best-performing model based on accuracy, precision, and recall.

The best model is deployed as an interactive Streamlit app, allowing users to enter patient information and receive a real-time prediction.

---

## Problem Statement

Predict whether a patient has heart disease based on clinical variables such as chest pain type, cholesterol levels, resting ECG results, and thalassemia — enabling early risk identification in a healthcare setting.

---

## Dataset

- **Source:** UCI Heart Disease Dataset (via Kaggle)
- **Records:** 920 patients across four hospital datasets — Cleveland, Hungary, Switzerland, VA Long Beach
- **Target variable:** `num` — binarized to 0 (no disease) / 1 (disease present)
- **Features include:** Age, Sex, Chest Pain Type (cp), Resting Blood Pressure (trestbps), Serum Cholesterol (chol), Fasting Blood Sugar (fbs), Resting ECG (restecg), Max Heart Rate Achieved (thalch), Exercise-Induced Angina (exang), ST Depression (oldpeak), Slope, Number of Major Vessels (ca), Thalassemia (thal)

---

## Approach

**1. Data Preprocessing**
- Handled missing values across multiple columns (median/mode imputation)
- Encoded categorical variables (chest pain type, thal, slope, restecg) via one-hot encoding
- Applied feature scaling (`StandardScaler`) for distance/margin-based models (KNN, SVC)
- Train/test split: 80/20

**2. Models Compared**

| Model | Accuracy | Precision | Recall | F1-Score |
|---|---|---|---|---|
| Logistic Regression | 79.9% | 0.85 | 0.80 | 0.82 |
| K-Nearest Neighbors | 81.0% | 0.87 | 0.80 | 0.83 |
| **Support Vector Classifier** | **84.2%** | **0.90** | **0.83** | **0.86** |
| Naive Bayes | 80.4% | 0.86 | 0.80 | 0.83 |

**3. Best Model: Support Vector Classifier (SVC)**

SVC was selected as the final model for its highest accuracy and precision — critical in a medical context where false positives carry significant cost.

---

## Explainable AI

SHAP (SHapley Additive exPlanations) was used to improve model transparency. The notebook includes a SHAP summary plot and a SHAP feature importance bar plot, showing which features most influence the model's predictions.

**Key findings:**
- Patients with asymptomatic chest pain showed the highest heart disease prevalence
- Older male patients had a higher likelihood of positive diagnosis
- ST depression (oldpeak) and number of major vessels (ca) were among the strongest predictors

---

## Streamlit Application

The app allows users to:
- Enter patient information
- Predict the presence of heart disease
- View prediction confidence
- Interact with a simple, user-friendly interface

---

## Known Issue (Fixed)

The deployed app initially returned a near-identical prediction regardless of input. Root cause: the SVC model was trained on `StandardScaler`-transformed features, but the inference script was feeding raw, unscaled values directly into the model — pushing every input outside the distribution the model was trained on. Fixed by persisting the fitted scaler (`scaler.pkl`) and applying it to inputs before prediction.

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| Pandas, NumPy | Data manipulation |
| Seaborn, Matplotlib | Exploratory visualizations |
| Scikit-learn | Model training, evaluation |
| SHAP | Model explainability |
| Streamlit | Web app deployment |
| Jupyter Notebook | Development environment |

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

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
streamlit run app.py
```

---

## Results Summary

The Support Vector Classifier achieved the best balance of precision and recall across all four tested models. With a precision of 0.90, the model minimizes false positives — reducing unnecessary alarm for patients who do not have heart disease — while maintaining strong recall (0.83) to capture true cases.

This project demonstrates:
- Clinical dataset preprocessing with real-world missing data
- Systematic multi-model comparison with proper evaluation metrics
- Model selection reasoning based on precision-recall tradeoffs in a healthcare context
- Diagnosing and fixing a real inference-time bug caused by a train/serve preprocessing mismatch

---

## Future Improvements

- Hyperparameter tuning
- Additional explainability methods
- Model deployment to the cloud
- Larger datasets for training
- Performance optimization

---

## Author

**Prekshya Siwakoti**
