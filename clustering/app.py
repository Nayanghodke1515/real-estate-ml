import streamlit as st
from cluster import get_clusters

st.title("📊 Customer Segmentation (Clustering)")

if st.button("Run Clustering"):
    data = get_clusters()
    st.write(data)