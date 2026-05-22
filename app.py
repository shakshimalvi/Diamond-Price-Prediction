import streamlit as st
import pandas as pd
import joblib

# Load Model
model = joblib.load("diamond_model.pkl")

st.title("💎 Diamond Price Prediction")

st.write("Enter Diamond Details")

# User Inputs
carat = st.number_input("Carat", min_value=0.1, max_value=5.0)

cut = st.selectbox(
    "Cut",
    ["Fair", "Good", "Very Good", "Premium", "Ideal"]
)

color = st.selectbox(
    "Color",
    ["D", "E", "F", "G", "H", "I", "J"]
)

clarity = st.selectbox(
    "Clarity",
    ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"]
)

depth = st.number_input("Depth")

table = st.number_input("Table")

x = st.number_input("Length (x)")
y = st.number_input("Width (y)")
z = st.number_input("Height (z)")

# Encoding
cut_map = {
    "Fair":0,
    "Good":1,
    "Very Good":2,
    "Premium":3,
    "Ideal":4
}

color_map = {
    "D":0,
    "E":1,
    "F":2,
    "G":3,
    "H":4,
    "I":5,
    "J":6
}

clarity_map = {
    "I1":0,
    "SI2":1,
    "SI1":2,
    "VS2":3,
    "VS1":4,
    "VVS2":5,
    "VVS1":6,
    "IF":7
}

# Convert Input
input_data = pd.DataFrame({
    "carat":[carat],
    "cut":[cut_map[cut]],
    "color":[color_map[color]],
    "clarity":[clarity_map[clarity]],
    "depth":[depth],
    "table":[table],
    "x":[x],
    "y":[y],
    "z":[z]
})

# Prediction
if st.button("Predict Price Category"):

    prediction = model.predict(input_data)

    if prediction[0] == 0:
        st.success("💰 Low Price Diamond")

    elif prediction[0] == 1:
        st.success("💎 Medium Price Diamond")

    else:
        st.success("👑 High Price Diamond")