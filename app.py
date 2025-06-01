import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load model and data
model = pickle.load(open('Prediction.pkl', 'rb'))
data = pickle.load(open('data.pkl', 'rb'))

st.title("🏡 Bangalore House Price Prediction")

# Sidebar Inputs
st.sidebar.header("Enter House Details")

# Location selection
locations = sorted(data['location'].unique())
locations.insert(0, 'Select Location')
location = st.sidebar.selectbox("Select Location", locations)

# Total Square Feet input
total_sqft = st.sidebar.number_input("Total Square Feet", min_value=300, max_value=10000, value=1000)

# Number of Bedrooms (BHK)
bhk = st.sidebar.selectbox("Select BHK", [1, 2, 3, 4, 5])

# Number of Bathrooms
bath = st.sidebar.selectbox("Select Number of Bathrooms", [1, 2, 3, 4, 5])

# Predict Button
if st.sidebar.button("Predict Price"):
    # Prepare the input dataframe
    input_df = pd.DataFrame([[location, total_sqft, bath, bhk]],
                            columns=['location', 'total_sqft', 'bath', 'bhk'])
    
    # Prediction
    prediction = model.predict(input_df)[0]
    
    st.success(f"💰 **Predicted Price:** ₹ {round(prediction, 2)} Lakhs")
