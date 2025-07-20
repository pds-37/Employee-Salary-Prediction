# ✅ Streamlit App for Employee Salary Prediction

import streamlit as st
import joblib
import numpy as np

# Dummy credentials
auth_user = "user"
auth_pass = "1234"

# Load model
model = joblib.load("best_model.pkl")

# Page configuration
st.set_page_config(page_title="Employee Salary Predictor", page_icon="💼")

# Welcome message
st.title(":sparkles: Welcome to Employee Salary Predictor")
st.markdown("""
Predict whether an employee earns **>50K** or **<=50K** based on various personal and work attributes.
Please login to continue.
""")

# Login section
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if username == auth_user and password == auth_pass:
            st.session_state.logged_in = True
            st.success("\u2705 Logged in successfully!")
        else:
            st.error("\u274c Incorrect username or password.")
    st.stop()

# Mappings for categorical fields
workclass_map = {
    "Private": 0, "Self-emp-not-inc": 1, "Self-emp-inc": 2, "Federal-gov": 3,
    "Local-gov": 4, "State-gov": 5, "Without-pay": 6, "Never-worked": 7, "Others": 8
}
education_map = {
    "Preschool": 0, "1st-4th": 1, "5th-6th": 2, "7th-8th": 3, "9th": 4, "10th": 5,
    "11th": 6, "12th": 7, "HS-grad": 8, "Some-college": 9, "Assoc-acdm": 10,
    "Assoc-voc": 11, "Bachelors": 12, "Masters": 13, "Doctorate": 14, "Prof-school": 15
}
marital_map = {
    "Never-married": 0, "Married-civ-spouse": 1, "Divorced": 2,
    "Separated": 3, "Widowed": 4, "Married-spouse-absent": 5, "Others": 6
}
occupation_map = {
    "Tech-support": 0, "Craft-repair": 1, "Other-service": 2, "Sales": 3,
    "Exec-managerial": 4, "Prof-specialty": 5, "Handlers-cleaners": 6,
    "Machine-op-inspct": 7, "Adm-clerical": 8, "Farming-fishing": 9,
    "Transport-moving": 10, "Priv-house-serv": 11, "Protective-serv": 12,
    "Armed-Forces": 13, "Others": 14
}
relationship_map = {
    "Wife": 0, "Own-child": 1, "Husband": 2, "Not-in-family": 3, "Other-relative": 4, "Unmarried": 5
}
race_map = {
    "White": 0, "Asian-Pac-Islander": 1, "Amer-Indian-Eskimo": 2, "Other": 3, "Black": 4
}
native_country_map = {
    "United-States": 0, "India": 1, "China": 2, "Britain": 3, "Others": 4
}

st.subheader(":mag: Fill Employee Details for Salary Prediction")

# Inputs
age = st.slider("Age", 17, 75, 30)
workclass_label = st.selectbox("Workclass", list(workclass_map.keys()))
workclass = workclass_map[workclass_label]

fnlwgt = st.number_input("fnlwgt", 10000, 1000000, 250000)
education_label = st.selectbox("Education", list(education_map.keys()))
education = education_map[education_label]
education_num = st.slider("Education Number", 1, 16, 10)
marital_label = st.selectbox("Marital Status", list(marital_map.keys()))
marital_status = marital_map[marital_label]
occupation_label = st.selectbox("Occupation", list(occupation_map.keys()))
occupation = occupation_map[occupation_label]
relationship_label = st.selectbox("Relationship", list(relationship_map.keys()))
relationship = relationship_map[relationship_label]
race_label = st.selectbox("Race", list(race_map.keys()))
race = race_map[race_label]
gender = st.radio("Gender", ["Male", "Female"])
gender = 1 if gender == "Male" else 0
capital_gain = st.number_input("Capital Gain", 0, 99999, 0)
capital_loss = st.number_input("Capital Loss", 0, 99999, 0)
hours_per_week = st.slider("Hours per Week", 1, 99, 40)
native_label = st.selectbox("Native Country", list(native_country_map.keys()))
native_country = native_country_map[native_label]

# Predict
if st.button("Predict Salary"):
    input_data = np.array([[age, workclass, fnlwgt, education, education_num, marital_status,
                            occupation, relationship, race, gender, capital_gain, capital_loss,
                            hours_per_week, native_country]])
    prediction = model.predict(input_data)[0]
    result = ">50K" if prediction == 1 else "<=50K"
    st.success(f"\ud83d\udcb0 Predicted Salary: {result}")
