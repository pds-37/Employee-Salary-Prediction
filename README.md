# 🧠 Employee Salary Prediction using Machine Learning

This project uses **Logistic Regression** to predict whether a person earns **>50K or <=50K** annually based on the **Adult Census Income dataset**. It is built and executed entirely in **Google Colab** using **Python and Scikit-learn**.

---

## 🔍 Problem Statement

Predict if a person earns more than 50K per year using features like age, education, gender, occupation, hours worked, etc.

---

## 📦 Dataset

- Dataset Name: **Adult Income Dataset**
- Columns include:
  - Age
  - Workclass
  - Education
  - Marital Status
  - Occupation
  - Relationship
  - Race
  - Gender
  - Capital Gain / Loss
  - Hours-per-week
  - Native Country
  - Income Group (Target Variable)

---

## 🛠️ Technologies Used

- Python 🐍
- Google Colab 💻
- Pandas & NumPy
- Scikit-learn (Logistic Regression, Label Encoding, Model Evaluation)
- Matplotlib / Seaborn for visualization

---

## ✅ Steps Performed

1. **Data Cleaning**  
2. **Label Encoding** of Categorical Features  
3. **Feature Scaling**  
4. **Train-Test Split**  
5. **Model Training using Logistic Regression**  
6. **Accuracy & Evaluation Metrics**  
7. **Prediction on Custom Input**

---

## 📊 Model Evaluation

- Accuracy Score: `82.2%`
- Confusion Matrix, Precision, Recall, F1 Score plotted.

---

## 💡 Sample Prediction

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
    'native-country': 'United-States'
}
# Output: >50K
---

## 📁 Project Files

- `EMPLOYEE_SALARY_PREDICTION.ipynb` – Main notebook  
- `adult 3.csv` – Dataset  

---

## 📌 How to Run

1. Open the `.ipynb` file in [Google Colab](https://colab.research.google.com)
2. Upload the CSV file when prompted
3. Run all cells in order
4. Try your own predictions by editing the input dictionary

---

## 📄 License

Released under the [MIT License](LICENSE)

## 👨‍💻 Author
- **Priyanshu Tiwari**  
  🔗 [LinkedIn](https://www.linkedin.com/in/priyanshu-tiwari-pds37)
