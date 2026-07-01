import streamlit as st
import pickle

# Load the trained model
with open("model_pickle", "rb") as f:
    model = pickle.load(f)

# Page configuration
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 House Price Prediction")
st.write("Enter the details below to predict the house price.")

# User Inputs
area = st.number_input(
    "Area (sq.ft)",
    min_value=100,
    max_value=10000,
    value=1000,
    step=10
)

bedrooms = st.number_input(
    "Number of Bedrooms",
    min_value=1,
    max_value=10,
    value=2,
    step=1
)

bathrooms = st.number_input(
    "Number of Bathrooms",
    min_value=1,
    max_value=10,
    value=2,
    step=1
)

# Prediction Button
if st.button("Predict Price"):
    features = [[area, bedrooms, bathrooms]]
    prediction = model.predict(features)

    st.success(f"🏡 Estimated House Price: ₹ {prediction[0]:,.2f}")
