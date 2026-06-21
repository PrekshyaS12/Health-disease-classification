# Heart Disease Prediction — Clinical Classification Model

A machine learning project to predict the presence of heart disease in patients using real clinical data from four major hospital datasets. Multiple classification algorithms are compared to identify the best-performing model based on accuracy, precision, and recall.

---

## Problem Statement

Predict whether a patient has heart disease based on clinical variables such as chest pain type, cholesterol levels, resting ECG results, and thalassemia — enabling early risk identification in a healthcare setting.

---

## Dataset

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

---

## Project Structure

```
heart-disease-classification/
│
├── heart_classification.ipynb   # Full notebook: EDA, preprocessing, modeling
├── README.md
```

---

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
