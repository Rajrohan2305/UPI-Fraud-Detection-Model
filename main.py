import streamlit as st
import numpy as np
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# 🔁 Load Model Files
# -----------------------------
model = pickle.load(open("final_rf_model.pkl", "rb"))
scaler = pickle.load(open("final_scaled.pkl", "rb"))
loaded_features = pickle.load(open("final_features_rf.pkl", "rb"))
label_encoders = pickle.load(open("final_label_encoders_rf.pkl", "rb"))

# Debug prints (optional)
print("Loaded Successful")
print("Match status:", model.n_features_in_ == len(loaded_features))

# -----------------------------
# 🔄 Session State
# -----------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

# -----------------------------
# 🔑 Login Function
# -----------------------------
def login():
    st.title("🔐 Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username != "" and password != "":
            st.session_state.logged_in = True
            st.session_state.username = username
            st.rerun()
        else:
            st.warning("Enter both username and password")

# -----------------------------
# 🏠 Main App Function
# -----------------------------
def main_app():
    st.sidebar.title("💳 UPI Fraud Detection")
    page = st.sidebar.radio("Navigation", ["Home", "Visualization", "About"])

    st.sidebar.video("UPI_Fraud_Detection_Using_Machine_Learning_Algorithms(480p).mp4")

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

    # =========================
    # HOME PAGE
    # =========================
    if page == "Home":
        st.title("💳 UPI Fraud Detection System")
        st.subheader("🔍 Detect fraudulent transactions using Machine Learning")

        # ----------- User Inputs -----------
        transaction_type = st.selectbox(
            "Transaction Type",
            label_encoders["Transaction_Type"].classes_
        )

        payment_gateway = st.selectbox(
            "Payment Gateway",
            label_encoders["Payment_Gateway"].classes_
        )

        transaction_city = st.selectbox(
            "Transaction City",
            label_encoders["Transaction_City"].classes_
        )

        transaction_state = st.selectbox(
            "Transaction State",
            label_encoders["Transaction_State"].classes_
        )

        device_os = st.selectbox(
            "Device OS",
            label_encoders["Device_OS"].classes_
        )

        merchant_category = st.selectbox(
            "Merchant Category",
            label_encoders["Merchant_Category"].classes_
        )

        transaction_channel = st.selectbox(
            "Transaction Channel",
            label_encoders["Transaction_Channel"].classes_
        )

        amount = st.slider("Transaction Amount", 0, 999, 10)

        # ----------- Prediction -----------
        if st.button("Predict Fraud"):

            input_data = {
                "Transaction_Type": label_encoders["Transaction_Type"].transform([transaction_type])[0],
                "Payment_Gateway": label_encoders["Payment_Gateway"].transform([payment_gateway])[0],
                "Transaction_City": label_encoders["Transaction_City"].transform([transaction_city])[0],
                "Transaction_State": label_encoders["Transaction_State"].transform([transaction_state])[0],
                "Device_OS": label_encoders["Device_OS"].transform([device_os])[0],
                "Merchant_Category": label_encoders["Merchant_Category"].transform([merchant_category])[0],
                "Transaction_Channel": label_encoders["Transaction_Channel"].transform([transaction_channel])[0],
                "amount": amount
            }

            # Fill missing columns
            for col in loaded_features:
                if col not in input_data:
                    input_data[col] = 0

            input_df = pd.DataFrame([input_data])
            input_df = input_df[loaded_features]

            input_scaled = scaler.transform(input_df)

            prediction = model.predict(input_scaled)[0]
            probability = model.predict_proba(input_scaled)[0][1]

            if prediction == 1:
                st.error("Fraud Transaction Detected 🚨")
            else:
                st.success("✅ Safe Transaction")

            st.write(f"Fraud Probability: {probability:.2f}")
            st.progress(int(probability * 100))

    # =========================
    # VISUALIZATION PAGE
    # =========================
    elif page == "Visualization":
        st.title("📊 Data Visualization")
        st.write("Visualization coming soon...")

    # =========================
    # ABOUT PAGE
    # =========================
    elif page == "About":
        st.title("📘 About Project")

        st.markdown("""
        ### 💡 Project: UPI Fraud Detection System

        This project uses Machine Learning to detect fraudulent UPI transactions.

        ### ⚙️ Technologies Used:
        - Python
        - Streamlit
        - Scikit-learn
        - Pandas, NumPy
        - Matplotlib, Seaborn

        ### 🎯 Objective:
        To build a real-time fraud detection system with high accuracy and user-friendly interface.
        """)

# -----------------------------
# 🚀 App Execution
# -----------------------------
if st.session_state.logged_in:
    main_app()
else:
    login()

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")