from django.shortcuts import render
from django.http import HttpResponse
import pickle
import pandas as pd
import os
from django.conf import settings
from .forms import CarPredictionForm
# Create your views here.
from sklearn.preprocessing import LabelEncoder 

def car_price_prediction(request):
    form = CarPredictionForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            # Extract the form data
            fuel_type = form.cleaned_data['fuel_type']
            body_type = form.cleaned_data['body_type']
            transmission = form.cleaned_data['transmission']
            owner_count = form.cleaned_data['owner_count']
            kms_driven = form.cleaned_data['km_driven']
            mileage = form.cleaned_data['mileage']
            Brand = form.cleaned_data['brand']
            Model = form.cleaned_data['model']
            Model_year = form.cleaned_data['model_year']
            IV = form.cleaned_data['insurance_validity']
            en=form.cleaned_data["engine"]
            
            Seats = form.cleaned_data['seats']
            Color = form.cleaned_data['color']
            City = form.cleaned_data['city']

            # Prepare the data for prediction
            
            input_data = pd.DataFrame({
                "Unnamed: 0":0,
                'Fuel Type': [fuel_type],
                'Body Type': [body_type],
                'transmission': [transmission],
                'ownerNo': [owner_count],
                'Brand': [Brand],
                'model': [Model],
                'modelYear': [Model_year],
                'Insurance Validity': [IV],
                'Kms Driven': [kms_driven],
                'Mileage': [mileage],
                "Engine": [en],
                'Seats': [Seats],
                'Color': [Color],
                'City': [City]


                
            })
            model_path = os.path.join(settings.BASE_DIR, 'Car_predict', 'Final_model.pkl')
            encoder_path = os.path.join(settings.BASE_DIR, 'Car_predict', 'encoder.pkl')  # Assuming encoders are saved h
            # Ensure the model file exists at the location
            if not os.path.exists(model_path):
                raise FileNotFoundError(f"Model file not found: {model_path}")

            if not os.path.exists(encoder_path):
                raise FileNotFoundError(f"Label Encoders file not found: {encoder_path}")

            # Load the pre-trained model (pipeline)
            # Load the pre-trained model (pipeline)
            with open(model_path, 'rb') as f:
                model =pickle.load(f)


            with open(encoder_path, 'rb') as f:
                label_encoders = pickle.load(f)

            input_data['Fuel Type'] = label_encoders['Fuel Type'].transform(input_data['Fuel Type'])
            input_data['Body Type'] = label_encoders['Body Type'].transform(input_data['Body Type'])
            input_data['transmission'] = label_encoders['transmission'].transform(input_data['transmission'])
            input_data['Brand'] = label_encoders['Brand'].transform(input_data['Brand'])
            input_data['model'] = label_encoders['model'].transform(input_data['model'])
            input_data['Insurance Validity'] = label_encoders['Insurance Validity'].transform(input_data['Insurance Validity'])
            input_data['Color'] = label_encoders['Color'].transform(input_data['Color'])
            input_data['City'] = label_encoders['City'].transform(input_data['City'])



            # Predict the price
            prediction = model.predict(input_data)

            # Return the result to the template
            return render(request, 'Final.html', {'prediction': round(prediction[0], 2)})
    return render(request, 'Home.html', {'form': form})

