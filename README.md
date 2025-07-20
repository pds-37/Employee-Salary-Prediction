
# 🧠 Employee Salary Prediction using Machine Learning & Streamlit

This project predicts whether a person earns **>50K or <=50K** annually based on demographic and work-related information.  
It is built using **Logistic Regression** and deployed via a **Streamlit web app**.

---

## 🔍 Problem Statement

Build a user-friendly tool that can predict if a person earns more than 50K per year using features like:

- Age
- Education
- Workclass
- Marital Status
- Occupation
- Race, Gender
- Hours Worked Per Week
- Native Country
- Capital Gain/Loss

---

## 📦 Dataset

- **Adult Income Dataset** from UCI Repository  
- `adult 3.csv` used as data source  
- Target Variable: `income` (>50K or <=50K)

---

## 🛠️ Technologies Used

- Python 🐍
- Google Colab (for model training)
- Streamlit (for web app)
- Scikit-learn (Logistic Regression, Evaluation)
- Pandas, NumPy
- GitHub + Streamlit Cloud for deployment

---

## ✅ ML Pipeline Steps

1. **Data Cleaning & Preprocessing**
2. **Label Encoding** of categorical variables
3. **Train-Test Split**
4. **Model Training (Logistic Regression)**
5. **Accuracy Evaluation**
6. **Model Saved as `best_model.pkl`**
7. **Deployed via Streamlit App**

---

## 🚀 Streamlit App Features

- Login authentication (username & password)
- Dropdowns for categorical features
- Custom UI with welcome message and modern layout
- Output: **Predicted Salary Range** (`>50K` or `<=50K`)

---

## 🧪 Sample Prediction

```python
{
  'age': 35,
  'workclass': 'Private',
  'education': 'Bachelors',
  'educational-num': 13,
  'marital-status': 'Married-civ-spouse',
  'occupation': 'Exec-managerial',
  'relationship': 'Husband',
  'race': 'White',
  'gender': 'Male',
  'capital-gain': 0,
  'capital-loss': 0,
  'hours-per-week': 45,
  'native-country': 'India'
}
# Output: >50K
````

---

## 📁 Project Files

* `app.py` – Streamlit App Code
* `best_model.pkl` – Trained ML Model
* `requirement.txt` – Required Libraries
* `EMPLOYEE_SALARY_PREDICTION.ipynb` – Colab Notebook
* `adult 3.csv` – Dataset

---

## 🧑‍💻 How to Run Locally

```bash
# Clone the repository
git clone https://github.com/pds-37/Employee-Salary-Prediction

# Navigate to project folder
cd Employee-Salary-Prediction

# Install dependencies
pip install -r requirement.txt

# Run Streamlit app
streamlit run app.py
```

---

## 🌐 Deployed App

You can access the live app here:
📍[Streamlit Cloud Link](https://<your-streamlit-app-url>) *(TO be updated soon)

---

## 📊 Model Accuracy

* Accuracy Score: **\~82.2%**
* Precision, Recall, F1 Score, Confusion Matrix used for evaluation.

---

## 📄 License

Released under the [MIT License](LICENSE)

---

## 👨‍💻 Author

**Priyanshu Tiwari**
🔗 [LinkedIn](https://www.linkedin.com/in/priyanshu-tiwari-pds37)

```

---

