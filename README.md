# Diabetes Prediction using Logistic Regression

## 📌 Project Overview

This project builds a **Logistic Regression** model to predict whether a patient has diabetes based on various medical attributes. The project includes complete data preprocessing, exploratory data analysis (EDA), model training, evaluation, and deployment using Streamlit with Ngrok.

---

## 📂 Dataset

The project uses the **Pima Indians Diabetes Dataset**, which contains diagnostic measurements for predicting diabetes.

### Features
- Pregnancies
- Glucose
- Blood Pressure
- Skin Thickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age

### Target
- **Outcome**
  - 0 → Non-Diabetic
  - 1 → Diabetic

---

## 🚀 Project Workflow

### 1. Data Preprocessing
- Loaded the dataset using Pandas.
- Checked dataset information and summary statistics.
- Identified missing and duplicate values.
- Replaced invalid zero values with `NaN` in selected columns.
- Filled missing values using the median.
- Applied outlier capping using the IQR method.

---

### 2. Exploratory Data Analysis (EDA)

Performed visualizations including:

- Histograms
- Boxplots
- Pairplots
- Correlation Heatmap

These visualizations helped understand data distribution, relationships, and feature correlations.

---

### 3. Model Building

The dataset was split into:

- 80% Training Data
- 20% Testing Data

A **Logistic Regression** classifier from Scikit-learn was trained on the processed dataset.

---

### 4. Model Evaluation

The model was evaluated using:

- Accuracy Score
- Precision
- Recall
- F1-Score
- ROC-AUC Score
- Classification Report
- Confusion Matrix
- ROC Curve

---

### 5. Feature Importance

The learned coefficients of the Logistic Regression model were analyzed to understand the impact of each feature on diabetes prediction.

---

### 6. Model Deployment

The trained model was saved as a `.pkl` file using Pickle and prepared for deployment using:

- Streamlit
- Pyngrok

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Pickle
- Streamlit
- Pyngrok

---

## 📁 Project Structure

```
├── Assignment(LR).ipynb
├── diabetes.csv
├── log.pkl
├── README.md
└── requirements.txt
```

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/diabetes-logistic-regression.git
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Notebook

Open the Jupyter Notebook and execute all cells:

```bash
jupyter notebook
```

---

## 📊 Model Performance

The notebook evaluates the model using multiple classification metrics, including:

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC Score

Performance may vary depending on preprocessing techniques and train-test split.

---

## 🔮 Future Improvements

- Hyperparameter tuning
- Cross-validation
- Feature selection
- Model comparison with Decision Tree, Random Forest, XGBoost, and SVM
- Deploy the application on Streamlit Cloud

---

## 👤 Author

**Revanth**

---

## 📜 License

This project is intended for educational and learning purposes.
