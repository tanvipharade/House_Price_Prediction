import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("model.pkl")

# Page settings
st.set_page_config(
    page_title="Pune House Price Prediction",
    page_icon="🏠"
)

# Application title
st.title("🏠 Pune House Price Prediction")

st.write(
    "Enter the house area to estimate its price "
    "using a Linear Regression model."
)

# User input
area = st.number_input(
    "Enter House Area (Square Feet)",
    min_value=100.0,
    max_value=10000.0,
    value=1000.0,
    step=50.0
)

# Prediction button
if st.button("Predict House Price"):
    input_data = pd.DataFrame({
        "total_sqft": [area]
    })

    prediction = model.predict(input_data)

    st.success(
        f"Estimated House Price: ₹{prediction[0]:.2f} Lakhs"
    )

st.caption("Developed using Python and Linear Regression.")
