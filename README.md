
# Heart Disease Prediction — Clinical Classification Model

A machine learning project to predict the presence of heart disease in patients using real clinical data from four major hospital datasets. Multiple classification algorithms are compared to identify the best-performing model based on accuracy, precision, and recall.

---

## Problem Statement

Predict whether a patient has heart disease based on clinical variables such as chest pain type, cholesterol levels, resting ECG results, and thalassemia — enabling early risk identification in a healthcare setting.
>>>>>>> c9df8eb18a922bd1635e91df08c15078782d55d2

---

## Dataset

<<<<<<< HEAD
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
=======
- **Source:** UCI Heart Disease Dataset (via Kaggle)
- **Records:** 920 patients across four hospital datasets
  - Cleveland, Hungary, Switzerland, VA Long Beach
- **Target variable:** `num` — binary (0 = No disease, 1 = Disease present)
- **Features include:**
  - Age, Sex, Chest Pain Type (`cp`)
  - Resting Blood Pressure (`trestbps`)
  - Serum Cholesterol (`chol`)
  - Fasting Blood Sugar (`fbs`)
  - Resting ECG results (`restecg`)
  - Max Heart Rate Achieved (`thalch`)
  - Exercise-induced Angina (`exang`)
  - ST depression (`oldpeak`), Slope, CA, Thalassemia (`thal`)

---

## Approach

### 1. Data Preprocessing
- Handled missing values across multiple columns (NaN imputation)
- Encoded categorical variables (chest pain type, thal, slope, restecg)
- Applied feature scaling for distance-based models (KNN, SVC)
- Train/test split: 80/20

### 2. Models Compared

| Model | Accuracy | Precision | Recall | F1-Score |
|---|---|---|---|---|
| Logistic Regression | 79.9% | 0.85 | 0.80 | 0.82 |
| K-Nearest Neighbors | 81.0% | 0.87 | 0.80 | 0.83 |
| **Support Vector Classifier** | **84.2%** | **0.90** | **0.83** | **0.86** |
| Naive Bayes | 80.4% | 0.86 | 0.80 | 0.83 |

### 3. Best Model: Support Vector Classifier (SVC)
- **Accuracy:** 84.2%
- **Precision:** 0.90
- **Recall:** 0.83
- **F1-Score:** 0.86

SVC was selected as the final model for its highest accuracy and precision — critical in a medical context where false positives carry significant cost.

---

## Key Findings

- Patients with **asymptomatic chest pain** showed the highest heart disease prevalence
- **Older male patients** had a higher likelihood of positive diagnosis
- **ST depression (oldpeak)** and **number of major vessels (ca)** were among the strongest predictors
- SVC outperformed all other models, demonstrating the effectiveness of margin-based classifiers on clinical tabular data

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| Pandas, NumPy | Data manipulation |
| Seaborn, Matplotlib | Exploratory visualizations |
| Scikit-learn | Model training, evaluation |
| Jupyter Notebook | Development environment |
>>>>>>> c9df8eb18a922bd1635e91df08c15078782d55d2

---

## Project Structure

```
<<<<<<< HEAD
Heart_Disease_Project/
│
├── app.py
├── heart_classification.ipynb
├── model.pkl
├── scaler.pkl
├── requirements.txt
├── README.md
└── heart_disease_uci.csv
=======
heart-disease-classification/
│
├── heart_classification.ipynb   # Full notebook: EDA, preprocessing, modeling
├── README.md
>>>>>>> c9df8eb18a922bd1635e91df08c15078782d55d2
```

---

<<<<<<< HEAD
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
=======
## Results Summary

The Support Vector Classifier achieved the best balance of precision and recall across all four tested models. With a precision of 0.90, the model minimizes false positives — reducing unnecessary alarm for patients who do not have heart disease — while maintaining strong recall (0.83) to capture true cases.

This project demonstrates:
- Clinical dataset preprocessing with real-world missing data
- Systematic multi-model comparison with proper evaluation metrics
- Model selection reasoning based on precision-recall tradeoffs in healthcare context

---

## Author

**Prekshya Siwakoti**
[GitHub](https://github.com/PrekshyaS12) | [LinkedIn](https://linkedin.com/in/prekshya-siwakoti-31ba1433b)
>>>>>>> c9df8eb18a922bd1635e91df08c15078782d55d2
