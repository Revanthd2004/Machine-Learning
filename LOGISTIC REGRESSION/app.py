import streamlit as st
import pickle
import pandas as pd
import numpy as np
import warnings as wr
wr.filterwarnings('ignore')
from sklearn.preprocessing import StandardScaler
model=pickle.load(open('log.pkl','rb'))

Pregnancies = st.sidebar.number_input("Pregnancies")
Glucose = st.sidebar.number_input("Glucose")
BloodPressure = st.sidebar.number_input("Blood Pressure")
SkinThickness = st.sidebar.number_input("Skin Thickness")
Insulin = st.sidebar.number_input("Insulin")
BMI = st.sidebar.number_input("BMI")
DiabetesPedigreeFunction = st.sidebar.number_input("Diabetes Pedigree Function")
Age = st.sidebar.number_input("Age")

# Prediction Button
st.title("Diabetes Prediction App")
if st.button("Predict"):
    input_data = np.array([[Pregnancies,
                            Glucose,
                            BloodPressure,
                            SkinThickness,
                            Insulin,
                            BMI,
                            DiabetesPedigreeFunction,
                            Age]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("Person is Diabetic")
    else:
        st.success("Person is Not Diabetic")

