import streamlit as st
from predict import predict

# Title
st.title("🏠 Real Estate Price Predictor")

# Description
st.write("Enter property details below:")

# Input
area = st.number_input("Enter Area (sq ft)", min_value=0.0)

# Button
if st.button("Predict Price"):
    result = predict(area)

    # Display result (CLEAN FORMAT)
    st.success(f"💰 Predicted Price: ${int(result):,}")