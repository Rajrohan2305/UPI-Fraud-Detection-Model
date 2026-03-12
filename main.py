import streamlit as st
import numpy as np
import pandas as pd
import pickle

model=pickle.load(open("final_rf_model.pkl","rb"))
scaler=pickle.load(open("final_scaled.pkl","rb"))
loaded_features=pickle.load(open("final_features_rf.pkl","rb"))
label_encoders=pickle.load(open("final_label_encoders_rf.pkl","rb"))
print("Loaded Sucessful")
print(scaler.scale_)
print(scaler.mean_)
print(f"loaded_features:{loaded_features}")
print(model.n_features_in_)
print(len(loaded_features))
print("match status:",model.n_features_in_==len(loaded_features))
print("Every thing is correct !")
print(label_encoders.keys())




st.title("UPI Fraud Detection System")

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

transaction_frequency = st.slider("Transaction Frequency",0,50,10)

merchant_category = st.selectbox(
    "Merchant Category",
    label_encoders["Merchant_Category"].classes_
)

transaction_channel = st.selectbox(
    "Transaction Channel",
    label_encoders["Transaction_Channel"].classes_
)

transaction_amount_deviation = st.slider("Transaction Amount Deviation",0,50,2)

days_since_last_transaction = st.slider("Days Since Last Transaction", 0,31,2)

amount = st.slider("Transaction Amount",0,1000,100)

# ----------- Prediction -----------

if st.button("Predict Fraud"):

    # Encode categorical values
    input_data = {
        "Transaction_Type": label_encoders["Transaction_Type"].transform([transaction_type])[0],
        "Payment_Gateway": label_encoders["Payment_Gateway"].transform([payment_gateway])[0],
        "Transaction_City": label_encoders["Transaction_City"].transform([transaction_city])[0],
        "Transaction_State": label_encoders["Transaction_State"].transform([transaction_state])[0],
        "Device_OS": label_encoders["Device_OS"].transform([device_os])[0],
        "Transaction_Frequency": transaction_frequency,
        "Merchant_Category": label_encoders["Merchant_Category"].transform([merchant_category])[0],
        "Transaction_Channel": label_encoders["Transaction_Channel"].transform([transaction_channel])[0],
        "Transaction_Amount_Deviation": transaction_amount_deviation,
        "Days_Since_Last_Transaction": days_since_last_transaction,
        "amount": amount
    }

    # Convert to DataFrame
    input_df = pd.DataFrame([input_data])

    # Reorder columns to match training
    input_df = input_df[loaded_features]

    # Scale
    input_scaled = scaler.transform(input_df)

    # Predict
    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0][1]

    if prediction == 1:
        st.error("Fraud Transaction Detected 🚨")
    else:
        st.success("Legitimate Transaction ✅")

    st.write(f"Fraud Probability: {probability:.2f}")
    st.progress(int(probability * 100))