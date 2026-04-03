import streamlit as st
from predict import predict

st.title("🏦 Loan Approval Predictor")

st.write("Enter applicant details:")

income = st.number_input("Income", min_value=0.0)
loan = st.number_input("Loan Amount", min_value=0.0)
credit = st.number_input("Credit Score", min_value=0.0)

if st.button("Check Approval"):
    result = predict([income, loan, credit])

    if result == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Rejected")