import streamlit as st
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Dummy database for signup/login (session-based)
if 'users' not in st.session_state:
    st.session_state.users = {"user@gmail.com": "1234"}
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Load model
model = joblib.load("best_model.pkl")

# Page config
st.set_page_config(page_title="Employee Salary Predictor", page_icon="💼", layout="centered")

# --- Authentication ---
def login_signup():
    st.title("🔐 Welcome to Employee Salary Predictor")

    choice = st.radio("Choose an option", ["Login", "Signup"], horizontal=True)
    email = st.text_input("Email (Gmail only)")
    password = st.text_input("Password", type="password")

    if choice == "Login":
        if st.button("Login"):
            if email in st.session_state.users and st.session_state.users[email] == password:
                st.success("✅ Logged in!")
                st.session_state.logged_in = True
            else:
                st.error("❌ Invalid credentials")
                st.stop()
    else:
        if st.button("Signup"):
            if not email.endswith("@gmail.com"):
                st.warning("⚠️ Please use a valid Gmail address")
            elif email in st.session_state.users:
                st.warning("⚠️ User already exists!")
            else:
                st.session_state.users[email] = password
                st.success("✅ Account created! Please log in now.")
                st.stop()

if not st.session_state.logged_in:
    login_signup()
else:
    # --- Mappings ---
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

    # --- Tabs ---
    tabs = st.tabs(["🏠 Home", "📊 Predict Salary", "📈 Data Visualizer", "🧠 Model Info", "ℹ️ About Developer"])

    # --- Home Tab ---
    with tabs[0]:
        st.header("🏠 Welcome!")
        st.markdown("""
        This application predicts whether an employee's salary is **greater than 50K or not** using Machine Learning.

        **Use Cases:**
        - HRs & Recruiters estimating salary
        - Job seekers checking salary band
        - Learning ML applications with real data

        **Built with ❤️ using Python & Streamlit**
        """)

    # --- Predict Salary Tab ---
    with tabs[1]:
        st.header("📊 Predict Employee Salary")

        age = st.slider("Age", 17, 75, 30)
        workclass = workclass_map[st.selectbox("Workclass", workclass_map.keys())]
        fnlwgt = st.number_input("fnlwgt", 10000, 1000000, 250000)
        education = education_map[st.selectbox("Education", education_map.keys())]
        education_num = st.slider("Education Number", 1, 16, 10)
        marital_status = marital_map[st.selectbox("Marital Status", marital_map.keys())]
        occupation = occupation_map[st.selectbox("Occupation", occupation_map.keys())]
        relationship = relationship_map[st.selectbox("Relationship", relationship_map.keys())]
        race = race_map[st.selectbox("Race", race_map.keys())]
        gender = 1 if st.radio("Gender", ["Male", "Female"]) == "Male" else 0
        capital_gain = st.number_input("Capital Gain", 0, 99999, 0)
        capital_loss = st.number_input("Capital Loss", 0, 99999, 0)
        hours_per_week = st.slider("Hours per Week", 1, 99, 40)
        native_country = native_country_map[st.selectbox("Native Country", native_country_map.keys())]

        if st.button("🚀 Predict"):
            input_data = np.array([[age, workclass, fnlwgt, education, education_num,
                                    marital_status, occupation, relationship, race, gender,
                                    capital_gain, capital_loss, hours_per_week, native_country]])
            prediction = model.predict(input_data)[0]
            result = ">50K" if prediction == 1 else "<=50K"
            st.success(f"💰 **Predicted Salary: {result}**")

    # --- Data Visualizer Tab ---
    with tabs[2]:
        st.header("📈 Data Visualizer")
        st.markdown("**Example:** Salary Distribution by Hours per Week")

        dummy_data = pd.DataFrame({
            "Hours": np.random.randint(20, 60, 100),
            "Salary >50K": np.random.randint(0, 2, 100)
        })

        fig, ax = plt.subplots()
        ax.hist([dummy_data[dummy_data["Salary >50K"] == 1]["Hours"],
                 dummy_data[dummy_data["Salary >50K"] == 0]["Hours"]],
                 label=[">50K", "<=50K"], bins=10, color=["green", "red"], alpha=0.7)
        ax.set_xlabel("Hours per Week")
        ax.set_ylabel("Count")
        ax.legend()
        st.pyplot(fig)

    # --- Model Info Tab ---
    with tabs[3]:
        st.header("🧠 Model Info")
        st.markdown("""
        - **Model Used**: Logistic Regression  
        - **Accuracy**: 82.2%  
        - **Trained on**: Adult Income Dataset  
        - **Features Used**:
          - Age, Workclass, Education, Marital Status
          - Occupation, Relationship, Race, Gender
          - Capital Gain, Capital Loss, Hours/week, Native Country
        """)

    # --- About Developer Tab ---
    with tabs[4]:
        st.header("ℹ️ About Developer")
        st.markdown("""
        **👨‍💻 Priyanshu Tiwari**  
        🔗 [LinkedIn](https://www.linkedin.com/in/priyanshu-tiwari-pds37)  
        💻 [GitHub](https://github.com/pds-37)  

        Built with 🐍 Python + Streamlit
        """)
