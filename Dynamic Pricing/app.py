import streamlit as st
import numpy as np
import pickle

# Load the trained model
with open('random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)

def get_vehicle_type_numeric(vehicle_type):
    vehicle_type_mapping = {
        "Premium": 1,
        "Economy": 0
    }
    vehicle_type_numeric = vehicle_type_mapping.get(vehicle_type)
    return vehicle_type_numeric

# Function to predict price
def predict_price(number_of_riders, number_of_drivers, vehicle_type, expected_ride_duration):
    vehicle_type_numeric = get_vehicle_type_numeric(vehicle_type)
    if vehicle_type_numeric is None:
        raise ValueError("Invalid vehicle type")
    
    input_data = np.array([[number_of_riders, 
                            number_of_drivers, 
                            vehicle_type_numeric, 
                            expected_ride_duration]])
    predicted_price = model.predict(input_data)
    return predicted_price[0]

# Streamlit application
def main():
    st.title("Ride Cost Prediction")

    # Input fields
    number_of_riders = st.number_input("Number of Riders", min_value=1, value=1)
    number_of_drivers = st.number_input("Number of Drivers", min_value=1, value=1)
    vehicle_type = st.selectbox("Vehicle Type", ["Premium", "Economy"])
    expected_ride_duration = st.number_input("Expected Ride Duration (minutes)", min_value=1, value=30)

    if st.button("Predict"):
        try:
            predicted_price = predict_price(number_of_riders, number_of_drivers, vehicle_type, expected_ride_duration)
            st.write(f"Predicted ride cost: ${predicted_price:.2f}")
        except ValueError as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
