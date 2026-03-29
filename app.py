import streamlit as st
import joblib

model = joblib.load('model.pkl')

st.title("Earthquake Detection System")

magnitude = st.number_input("Enter Magnitude")
depth = st.number_input("Enter Depth")

if st.button("Predict"):
    result = model.predict([[magnitude, depth]])

    if result[0] == 1:
        st.error("Earthquake Detected ⚠️")
    else:
        st.success("Normal Activity ✅")