# 🚨 UPI Fraud Detection System

Fraud in digital payments is increasing rapidly as online transactions.
This project focuses on building a Machine Learning system that
intelligently detects whether a UPI transaction is "legitimate" or
"fraudulent" based on transaction behavior and patterns.

The model is trained using transaction features and deployed as an
interactive web application using Streamlit.

------------------------------------------------------------------------

## 🎯 Project Objective

The goal of this project is to simulate a real-world fraud detection
system that:

-   Analyzes transaction details
-   Identifies suspicious behavior
-   Predicts fraudulent transactions
-   Displays fraud probability score

------------------------------------------------------------------------

## 🧠 Machine Learning Pipeline

This project follows a complete end-to-end ML workflow:

1.  Data Cleaning & Preprocessing\
2.  Label Encoding for categorical features\
3.  Train-Test Split\
4.  Feature Scaling using StandardScaler\
5.  Model Training using Random Forest\
6.  Model Evaluation\
7.  Deployment using Streamlit

------------------------------------------------------------------------

## 🤖 Model Used

**Algorithm:** Random Forest Classifier

### Why Random Forest?

-   Handles both categorical and numerical data
-   Performs well on non-linear relationships
-   Reduces overfitting compared to Decision Trees
-   Effective for fraud detection problems

------------------------------------------------------------------------

## 📊 Features Used

-   Transaction Type\
-   Payment Gateway\
-   Transaction City\
-   Transaction State\
-   Device Operating System\
-   Transaction Frequency\
-   Merchant Category\
-   Transaction Channel\
-   Transaction Amount Deviation\
-   Days Since Last Transaction\
-   Transaction Amount

------------------------------------------------------------------------

## 📈 Model Evaluation

The model performance was evaluated using:

-   Accuracy
-   Confusion Matrix
-   Precision & Recall
-   Classification Report
-   ROC-AUC Score

> In fraud detection systems, Recall and ROC-AUC are more important than
> Accuracy due to class imbalance.

------------------------------------------------------------------------

## 📊 Data Visualization

To better understand the dataset and model behavior, the following
libraries were used:

-   Matplotlib
-   Seaborn

These were used for:

-   Confusion Matrix visualization
-   Feature importance plots
-   Distribution analysis
-   Correlation heatmaps

------------------------------------------------------------------------

## 🖥️ Web Application

The project is deployed using Streamlit and provides:

-   Interactive UI
-   Dropdown selections for categorical features
-   Real-time fraud prediction
-   Fraud probability score display

------------------------------------------------------------------------

## 🛠️ Tech Stack

-   Python
-   Pandas
-   NumPy
-   Scikit-learn
-   Matplotlib
-   Seaborn
-   Streamlit
-   Pickle

------------------------------------------------------------------------

## 📂 Project Structure

UPI_model/ │ ├── main.py ├──final_rf_model.pkl ├──final_scaled.pkl ├──
final_label_encoders_rf.pkl ├── final_features_rf.pkl ├─└── README.md---- Requirements.txt 

------------------------------------------------------------------------

## 🚀 How to Run Locally

1.  Clone the repository:

    git clone https://github.com/your-username/upi-fraud-detection.git

2.  Navigate to project folder:

    cd upi-fraud-detection

3.  Install dependencies:

    pip install -r requirements.txt

4.  Run the application:

    streamlit run app.py

------------------------------------------------------------------------

## 🌐 Live Demo

(Add your deployed Streamlit link here)

------------------------------------------------------------------------

## 🔮 Future Improvements

-   Handle class imbalance using SMOTE\
-   Compare with XGBoost model\
-   Improve UI with risk-level indicators\
-   Add real-time fraud simulation

------------------------------------------------------------------------

## 👨‍💻 Author

Raj Rohan pandit\
B.Tech -- Artificial Intelligence & Machine Learning\
Aspiring ML Engineer \| Data Science Enthusiast

------------------------------------------------------------------------

⭐ If you found this project useful, consider giving it a star!
