⚡ AI-Powered Energy Consumption Forecasting System

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge&logo=streamlit&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Random%20Forest-green?style=for-the-badge)

## 📌 Overview
An AI-driven interactive dashboard built to forecast electricity consumption for smart grids, buildings, and industries. This system uses Machine Learning to predict future energy demands based on historical time-series data, helping to optimize energy supply, reduce wastage, and make data-driven business decisions.

---

## 💻 Dashboard Previews

Here is a visual overview of the AI Forecasting System:

### 1️⃣ Main Prediction Panel & System Status
![Main Dashboard](<images/AI-Powered Energy Consumption Forecasting (1).png>)

### 2️⃣ Live Energy Trend & Dataset Overview
![Energy Trend](<images/Energy Trend.png>)

### 3️⃣ Usage Analytics: Monthly Patterns & Day Types
![Monthly Pattern](<images/Monthly Energy Pattern.png>)
![Weekday vs Weekend](<images/Weekday vs Weekend Usage (1).png>)

### 4️⃣ AI Intelligence (Actual vs Predicted Forecast)
![AI vs Reality](<images/Energy Forecast Intelligence (AI vs Reality) (1).png>)

*(Note: The above model training snapshot can be found in `images/Model Train.png`)*

---

## 🎯 Problem Statement
Power grids often face challenges in balancing supply and demand. Inefficient energy management leads to blackouts, higher operational costs, and increased carbon footprint. This project addresses the issue by accurately predicting energy usage using Artificial Intelligence.

## 🛠️ Tech Stack & Libraries
* **Language:** Python
* **Data Processing:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn (Random Forest Regressor)
* **Frontend/UI:** Streamlit
* **Visualization:** Plotly, Matplotlib
* **Model Serialization:** Joblib

---

## 📁 Project Structure

```text
AI-Energy-Forecasting/
│
├── data/
│   └── energy_dataset.csv         # Generated virtual dataset
├── images/                        # Dashboard screenshots & assets
├── models/
│   └── rf_model.pkl               # Saved Random Forest model
├── app.py                         # Streamlit Dashboard application
├── train_model.py                 # Script to generate data and train model
├── requirements.txt               # Project dependencies
├── .gitignore                     # Ignored files for Git
└── README.md                      # Project documentation
🚀 How to Run Locally
Follow these steps to run the project on your local machine:

1. Clone the repository:

Bash
git clone https://github.com/dalimkumar452-sudo/AI-Energy-Consumption-Forecasting.git
cd AI-Energy-Forecasting
2. Create a virtual environment & activate it:

Bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
3. Install the required dependencies:

Bash
pip install -r requirements.txt
4. Train the ML model and generate data:

Bash
python train_model.py
5. Launch the Streamlit web app:

Bash
streamlit run app.py
📊 Learning Outcomes & Achievements
Implemented Time-Series Feature Engineering (extracting hours, weekdays, months).

Built and evaluated a Random Forest Regressor model for business-level forecasting.

Designed a fully interactive, dark-themed Streamlit web application.

Handled end-to-end data pipelines from mock data generation to AI model deployment.

Built with ❤️ as a practical approach to Data Science and Machine Learning.