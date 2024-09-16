import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler

# Title of the Streamlit app
st.title("Loyal Customer Prediction App")

# Load the saved Logistic Regression model
classifier = joblib.load('c2_Classifier_LoyalCustomers')

# Function to take user input for model features
def user_input_features():
    DemAffl = st.number_input(" Demographic Affluence", min_value=0, max_value=100)
    DemAge = st.number_input(" Demographic Age", min_value=0, max_value=100)
    DemClusterGroup = st.number_input(" Cluster Group", min_value=0, max_value=100)
    DemGender = st.selectbox(" Gender", options=[0, 1], format_func=lambda x: 'Male' if x == 0 else 'Female')
    DemReg = st.number_input(" Region", min_value=0, max_value=100)
    DemTVReg = st.number_input(" TV Region", min_value=0, max_value=100)
    PromTime = st.number_input(" Promotion Time", min_value=0, max_value=100)
    PromSpend = st.number_input(" Promotion Spend", min_value=0, max_value=100)
    LoyalTime = st.number_input(" Loyalty Time", min_value=0, max_value=100)

    # Collect all inputs into a dictionary
    data = {
        'DemAffl': DemAffl,
        'DemAge': DemAge,
        'DemClusterGroup': DemClusterGroup,
        'DemGender': DemGender,
        'DemReg': DemReg,
        'DemTVReg': DemTVReg,
        'PromTime': PromTime,
        'PromSpend': PromSpend,
        'LoyalTime': LoyalTime
    }
    
    # Convert the input data into a DataFrame
    features = pd.DataFrame(data, index=[0])
    return features

# Display a form for user input
st.header("Input Customer Details")
input_df = user_input_features()

# When the user clicks "Predict", show the prediction
if st.button("Predict Loyalty"):
    # Standardize the input data if required (optional based on your model training)
    scaler = StandardScaler()
    input_scaled = scaler.fit_transform(input_df)

    # Predict using the pre-trained logistic regression model
    prediction_prob = classifier.predict_proba(input_scaled)
    prediction = classifier.predict(input_scaled)

    # Display the prediction result
    st.subheader("Prediction Probability")
    st.write(f"Probability of being Loyal: {prediction_prob[0][1]:.2f}")
    st.write(f"Probability of not being Loyal: {prediction_prob[0][0]:.2f}")

    # Display the predicted class
    st.subheader("Prediction Result")
    if prediction[0] == 1:
        st.success("This customer is predicted to be **Loyal**.")
    else:
        st.warning("This customer is predicted to be **Not Loyal**.")
