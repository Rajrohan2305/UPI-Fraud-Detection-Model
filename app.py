import streamlit as st
import numpy as np
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
from database import create_tables
from auth import *

# INIT DATABASE
create_tables()

#  Load Model Files
model = pickle.load(open("final_rf_model.pkl", "rb"))
scaler = pickle.load(open("final_scaled.pkl", "rb"))
loaded_features = pickle.load(open("final_features_rf.pkl", "rb"))
label_encoders = pickle.load(open("final_label_encoders_rf.pkl", "rb"))

# Debug prints
print("Loaded Successful")
print("Match status:", model.n_features_in_ == len(loaded_features))

# SESSION STATE
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "role" not in st.session_state:
    st.session_state.role = ""
# modified
def login():
    import streamlit as st
    import time

    # ---------- CSS ----------
    st.markdown("""
    <style>
    /* Animated Background */
    .stApp {
        background: linear-gradient(-45deg, #ff416c, #ff4b2b, #1c92d2, #2c5364);
        background-size: 400% 400%;
        animation: gradientBG 12s ease infinite;
        overflow: hidden;
    }

    @keyframes gradientBG {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    /* Floating Glow Circles */
    .circle {
        position: absolute;
        border-radius: 50%;
        background: rgba(255,255,255,0.15);
        filter: blur(80px);
        animation: float 8s infinite ease-in-out;
    }

    .circle1 { width:200px; height:200px; top:10%; left:5%; }
    .circle2 { width:250px; height:250px; bottom:10%; right:5%; }

    @keyframes float {
        0%,100% {transform: translateY(0);}
        50% {transform: translateY(-50px);}
    }

    /* Glass Card */
    .card {
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(20px);
        padding: 40px;
        border-radius: 20px;
        box-shadow: 0px 10px 40px rgba(0,0,0,0.4);
        max-width: 420px;
        margin: auto;
        margin-top: 80px;
        animation: fadeIn 1.2s ease-in-out;
    }

    @keyframes fadeIn {
        from {opacity: 0; transform: scale(0.9);}
        to {opacity: 1; transform: scale(1);}
    }

    /* Title */
    .main-title {
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        color: white;
        margin-top: 30px;
    }

    .typing {
        text-align: center;
        font-size: 20px;
        color: #ffffff;
        margin-bottom: 20px;
        font-family: monospace;
    }

    /* Inputs */
    .stTextInput input {
        border-radius: 12px;
        padding: 10px;
    }

    /* Button */
    .stButton button {
        width: 100%;
        height: 45px;
        border-radius: 12px;
        background: linear-gradient(to right, #ff416c, #ff4b2b);
        color: white;
        font-size: 16px;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }

    .stButton button:hover {
        transform: scale(1.07);
        box-shadow: 0px 5px 25px rgba(0,0,0,0.4);
    }

    /* Radio */
    .stRadio > div {
        flex-direction: row;
        justify-content: center;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

    # ---------- FLOATING GLOW ----------
    st.markdown('<div class="circle circle1"></div>', unsafe_allow_html=True)
    st.markdown('<div class="circle circle2"></div>', unsafe_allow_html=True)

    # ---------- TITLE ----------
    st.markdown('<div class="main-title">💳 UPI Fraud Detection Model</div>', unsafe_allow_html=True)

    # ---------- TYPING EFFECT ----------
    text_placeholder = st.empty()
    text = "Welcome back... Secure your transactions 🚀"
    st.markdown('<div class="main-title">LOGIN SYSTEM</div>', unsafe_allow_html=True)

    displayed = ""
    for char in text:
        displayed += char
        text_placeholder.markdown(f"<div class='typing'>{displayed}</div>", unsafe_allow_html=True)
        time.sleep(0.02)

    # ---------- CENTER ----------
    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)

        menu = ["User Login", "Signup", "Admin Login"]
        choice = st.radio("", menu)

        email = st.text_input("📧 Email")
        username = st.text_input("👤 Username")
        password = st.text_input("🔑 Password", type="password")

        # USER LOGIN
        if choice == "User Login":
            if st.button("Login"):
                if login_user(email, password):
                    st.session_state.logged_in = True
                    st.session_state.role = "user"
                    st.rerun()
                else:
                    st.error("Invalid Credentials ❌")

        # SIGNUP
        elif choice == "Signup":
            if st.button("Create Account"):
                st.success(register_user(username, email, password))

        # ADMIN LOGIN
        elif choice == "Admin Login":
            if st.button("Admin Login"):
                if email == "rajrohan7386@gmail.com" and password == "Raj@7386":
                    st.session_state.logged_in = True
                    st.session_state.role = "admin"
                    st.rerun()
                else:
                    st.error("Invalid Admin Credentials ❌")

        st.markdown('</div>', unsafe_allow_html=True)
# # LOGIN PAGE
# def login():
#     st.title("🔐 Login System")

#     menu = ["User Login", "Signup", "Admin Login"]
#     choice = st.radio("Select Option", menu)

#     email = st.text_input("Email")
#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password")

#     # USER LOGIN
#     if choice == "User Login":
#         if st.button("Login"):
#             if login_user(email, password):
#                 st.session_state.logged_in = True
#                 st.session_state.role = "user"
#                 st.success("Login Successful ✅")
#                 st.rerun()
#             else:
#                 st.error("Invalid Credentials ❌")

#     # SIGNUP
#     elif choice == "Signup":
#         if st.button("Signup"):
#             result = register_user(username, email, password)
#             st.success(result)

#     # ADMIN LOGIN
#     elif choice == "Admin Login":
#         if st.button("Login as Admin"):
#             if email == "rajrohan7386@gmail.com" and "password == Raj@7386":
#                 st.session_state.logged_in = True
#                 st.session_state.role = "admin"
#                 st.success("Admin Login Successful 🔥")
#                 st.rerun()
#             else:
#                 st.error("Invalid Admin Credentials ❌")


# Main App Function
def main_app():
    st.sidebar.title("💳 UPI Fraud Detection")
    page = st.sidebar.radio("Navigation", ["Home", "Visualization", "About","Admin"])

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

    
    # HOME PAGE
    
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

    
    # VISUALIZATION PAGE
   
    elif page == "Visualization":
        st.title("📊 Data Visualization")
        st.write("Fraud by Transaction_Type")
        st.image(r"C:\Users\rajuh\OneDrive\Pictures\Screenshots\transaction_type.png.png")
        st.write("Fraud by PaymentGateway ")
        st.image(r"C:\Users\rajuh\OneDrive\Pictures\Screenshots\payment_gateway.png")
        st.write("Fraud by Device_os")
        st.image(r"C:\Users\rajuh\OneDrive\Pictures\Screenshots\Device_os.png")
        st.write("Fraud by Merchant_category ")
        st.image(r"C:\Users\rajuh\OneDrive\Pictures\Screenshots\Merchant_category.png")
        st.write("Fraud by Transaction_channel")
        st.image(r"C:\Users\rajuh\OneDrive\Pictures\Screenshots\Transaction_channel.png")

   
    # ABOUT PAGE
   
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
        - mysql
        - machine learning

        ### 🎯 Objective:
        To build a real-time fraud detection system with high accuracy and user-friendly interface.
        """)
        
     # ADMIN PANEL
    elif page == "Admin":

        if st.session_state.role != "admin":
            st.error("Access Denied ❌")
            return

        st.title("📊 Admin Dashboard")

        st.write("### 👥 Users")
        st.table(get_users())

        st.write("### 🕒 Login History")
        history = get_login_history()
        df = pd.DataFrame(history, columns=["ID", "Email", "Time", "Status"])
        st.table(df)

        st.write("### 🚨 Suspicious Logins")
        suspicious = df[df["Status"] == "Suspicious 🚨"]
        st.table(suspicious)


# App Execution

if st.session_state.logged_in:
    main_app()
else:
    login()


# FOOTER

st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")