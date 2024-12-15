import pickle
import pandas as pd
import streamlit as slt
import numpy as np

# Page settings
slt.set_page_config(layout="wide")

# Option menu
page = slt.sidebar.selectbox("Select a Page", ["CarDekho-Price Prediction", "User Guide"])

# CarDekho-Price Prediction Page
if page == "CarDekho-Price Prediction":
    slt.header(':blue[CarDekho-Price Prediction 🚗]')

    # Define the hardcoded choices for the dropdowns
    FUEL_CHOICES = ['Petrol', 'Diesel', 'Lpg', 'Cng', 'Electric']
    BODY_CHOICES = ['Hatchback', 'SUV', 'Sedan', 'MUV', 'Coupe', 'Minivans', 'Convertibles', 'Hybrids', 'Wagon', 'Pickup Trucks']
    TRANSMISSION_CHOICES = ['Manual', 'Automatic']
    OWNER_CHOICES = [0, 1, 2, 3, 4, 5]
    BRAND_CHOICES = [
        'Maruti', 'Ford', 'Tata', 'Hyundai', 'Jeep', 'Datsun', 'Honda', 'Mahindra', 'Mercedes-Benz', 'BMW',
        'Renault', 'Audi', 'Toyota', 'Mini', 'Kia', 'Skoda', 'Volkswagen', 'Volvo', 'MG', 'Nissan', 'Fiat',
        'Mahindra Ssangyong', 'Mitsubishi', 'Jaguar', 'Land Rover', 'Chevrolet', 'Citroen', 'Opel', 'Mahindra Renault',
        'Isuzu', 'Lexus', 'Porsche', 'Hindustan Motors'
    ]
    MODEL_CHOICES = [
        'Maruti Celerio', 'Ford Ecosport', 'Tata Tiago', 'Hyundai Xcent', 'Maruti SX4 S Cross', 'Jeep Compass',
        'Datsun GO', 'Hyundai Venue', 'Maruti Ciaz', 'Maruti Baleno', 'Hyundai Grand i10', 'Honda Jazz',
        'Mahindra XUV500', 'Mercedes-Benz GLA', 'Hyundai i20', 'Tata Nexon', 'Honda City', 'BMW 5 Series', 'Maruti Swift'
    ]
    YEAR_CHOICES = [2015, 2018, 2014, 2020, 2017, 2021, 2019, 2022, 2016, 2011, 2009, 2013, 2010, 2008, 2006, 2012, 2005, 2007, 2023, 1998, 2004, 2003, 2001, 2002, 2000, 1985, 1997, 1999]
    SEAT_CHOICES = [2, 4, 5, 6, 7, 8, 9, 10]
    CITY_CHOICES = ['Bangalore', 'Chennai', 'Delhi', 'Hyderabad', 'Jaipur', 'Kolkata']
    ENGINE_CHOICES = [998, 1497, 1199, 1197, 1248, 1956, 1198, 1462, 2179, 1950, 1396, 1995, 1498, 4663, 1086, 1991]

    col1, col2 = slt.columns(2)
    with col1:
        Ft = slt.selectbox("Fuel Type", FUEL_CHOICES)
        Bt = slt.selectbox("Body Type", BODY_CHOICES)
        Tr = slt.selectbox("Transmission", TRANSMISSION_CHOICES)
        Owner = slt.selectbox("Owner", OWNER_CHOICES)
        Brand = slt.selectbox("Brand", BRAND_CHOICES)
        Model = slt.selectbox("Model", MODEL_CHOICES)
        Model_year = slt.selectbox("Model Year", YEAR_CHOICES)
        IV = slt.selectbox("Insurance Validity", ['Third Party', 'Comprehensive', 'Zero Dep', 'Not Available'])
        Km = slt.slider("Kilometers Driven", min_value=100, max_value=100000, step=1000)
        ML = slt.number_input("Mileage", min_value=5, max_value=50, step=1)
        seats = slt.selectbox("Seats", SEAT_CHOICES)
        color = slt.selectbox("Color", ['White', 'Black', 'Red', 'Blue', 'Silver', 'Green', 'Yellow', 'Brown', 'Grey'])
        city = slt.selectbox("City", CITY_CHOICES)
        en = slt.selectbox("Engine", ENGINE_CHOICES)

    # Prediction at the bottom
    with col2:
        Submit = slt.button("Predict")
        predicted_price = None  # Initialize prediction variable to store result

        if Submit:
            try:
                # Load the trained model pipeline (Final_model)
                with open('Final_model.pkl', 'rb') as files:
                    pipeline = pickle.load(files)
            except FileNotFoundError:
                slt.error("Model file not found! Please check the file path.")
                slt.stop()

            try:
                # Load the encoder dictionary
                with open('encoder.pkl', 'rb') as enc_file:
                    label_encoders = pickle.load(enc_file)
            except FileNotFoundError:
                slt.error("Encoder file not found! Please check the file path.")
                slt.stop()

            # Input data
            input_data = pd.DataFrame({
                "Unnamed: 0": [0],
                'Fuel Type': [Ft],
                'Body Type': [Bt],
                'transmission': [Tr],
                'ownerNo': [Owner],
                'Brand': [Brand],
                'model': [Model],
                'modelYear': [Model_year],
                'Insurance Validity': [IV],
                'Kms Driven': [Km],
                'Mileage': [ML],
                "Engine": [en],
                'Seats': [seats],
                'Color': [color],
                'City': [city]
            })

            # Display the selected details
            data = [Ft, Bt, Tr, Owner, Brand, Model, Model_year, IV, Km, ML, seats, color, city]
            slt.write("**Selected Details:**")
            slt.write(data)

            # Manually encode categorical columns using the stored encoders
            try:
                input_data['Fuel Type'] = label_encoders['Fuel Type'].transform(input_data['Fuel Type'])
                input_data['Body Type'] = label_encoders['Body Type'].transform(input_data['Body Type'])
                input_data['transmission'] = label_encoders['transmission'].transform(input_data['transmission'])
                input_data['Brand'] = label_encoders['Brand'].transform(input_data['Brand'])
                input_data['model'] = label_encoders['model'].transform(input_data['model'])
                input_data['Insurance Validity'] = label_encoders['Insurance Validity'].transform(input_data['Insurance Validity'])
                input_data['Color'] = label_encoders['Color'].transform(input_data['Color'])
                input_data['City'] = label_encoders['City'].transform(input_data['City'])

                # Make the prediction
                prediction = pipeline.predict(input_data)
                predicted_price = round(prediction[0], 2)  # Store predicted price for display
            except Exception as e:
                slt.error(f"Error during transformation or prediction: {str(e)}")

        # Display the predicted price at the bottom
        if predicted_price is not None:
            slt.subheader(f"The predicted price of the car is: ₹{predicted_price} Lakhs")
            
# User Guide Page
elif page == "User Guide":
    slt.header('User Guide for Streamlit-based CarDekho Price Prediction Application') 
    slt.write(""" 
    This guide explains how to interact with the CarDekho-Price Prediction application built using Streamlit. 
    The app allows users to input car details and predict the price based on various features like brand, model, fuel type, etc.
    
    **Steps to Use:**
    
    **STEP_1 Input Fields (Left Column):**
    In the first column, users will provide the following details about the car:
    - **Fuel Type:** Select the fuel type of the car from options like Petrol, Diesel, LPG, CNG, Electric.
    - **Body Type:** Choose the body type of the car. Options include Hatchback, SUV, Sedan, MUV, Coupe, etc.
    - **Transmission:** Choose whether the car has a Manual or Automatic transmission.
    - **Owner:** Select how many previous owners the car has had, ranging from 0 to 5.
    - **Brand:** Select the car brand from the available list of brands in the dataset.
    - **Model:** After selecting the brand, the app will automatically filter and display the relevant car models. Choose the model from the dropdown.
    - **Model Year:** Choose the year when the car was manufactured.
    - **Insurance Validity:** Select the insurance type (e.g., Third Party, Comprehensive, Zero Dep, etc.).
    - **Kilometers Driven:** Use the slider to enter how many kilometers the car has been driven (between 100 and 100,000 km).
    - **Mileage:** Enter the car's mileage using the number input (range 5–50 km/litre).
    - **Seats:** Select the number of seats in the car from the dropdown.
    - **Color:** Choose the color of the car.
    - **City:** Select the city where the car is located from the dropdown list.
    
    **STEP_2. Prediction Button (Right Column):**
    - **Submit Button:** Once all input fields are filled, press the Predict button in the second column to trigger the price prediction.
    
    **Output:**
    The predicted price of the car will appear on the screen in the format: The price of the [Brand] car is: [Price] lakhs.
    
    **Example Workflow:**
    1. Select Fuel type as Petrol.
    2. Choose Body type as Sedan.
    3. Pick Automatic transmission.
    4. Select that the car has had 3 previous owners.
    5. Choose BMW as the Brand.
    6. After selecting the brand, a filtered list of models will appear. Choose the BMW 5 Series model.
    7. Choose 2011 for the Model Year.
    8. Select Third Party insurance for Insurance Validity.
    9. Use the slider to set Kilometers Driven to 100000 km.
    10. Enter the Mileage as 18 km/litre.
    11. Choose 5 seats for the car.
    12. Select Bangalore as the color.
    13. Choose Delhi as the city.
    14. Press Predict.
    
    The app will display the entered details and the predicted price of the car, e.g., The price of the BMW car is: 21.11 lakhs.
    """)

    slt.header('Developed by **Mohammed Riyaskhan!**')
    slt.write("If you want to explore more cars, click the link below!")
    slt.image("c:/Users/USER/Pictures/wallaper/ezgif.com-gif-maker-1.png")
    BOOK_HERE = "Book here"
    slt.markdown(f"[{BOOK_HERE}](https://www.cardekho.com/)") 
