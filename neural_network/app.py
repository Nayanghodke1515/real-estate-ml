import streamlit as st
from model import train_model, predict

st.title("🧠 Student Score Predictor (Neural Network)")

hours = st.number_input("Hours of Study", min_value=0.0)

if st.button("Train Model"):
    train_model()
    st.success("Model Trained!")

if st.button("Predict Score"):
    result = predict(hours)
    st.success(f"Predicted Score: {int(result)}")