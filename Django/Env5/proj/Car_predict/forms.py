from django import forms

class CarPredictionForm(forms.Form):
    FUEL_CHOICES = [
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('Lpg', 'Lpg'),
        ('Cng', 'Cng'),
        ('Electric', 'Electric'),
    ]

    BODY_CHOICES = [
        ('Hatchback', 'Hatchback'),
        ('SUV', 'SUV'),
        ('Sedan', 'Sedan'),
        ('MUV', 'MUV'),
        ('Coupe', 'Coupe'),
        ('Minivans', 'Minivans'),
        ('Convertibles', 'Convertibles'),
        ('Hybrids', 'Hybrids'),
        ('Wagon', 'Wagon'),
        ('Pickup Trucks', 'Pickup Trucks'),
    ]
    
    TRANSMISSION_CHOICES = [
        ('Manual', 'Manual'),
        ('Automatic', 'Automatic'),
    ]
    
    OWNER_CHOICES = [(str(i), str(i)) for i in range(6)]  # Owner count from 0 to 5
    
    # Car Brands choices
    BRAND_CHOICES = [
        ('Maruti', 'Maruti'),
        ('Ford', 'Ford'),
        ('Tata', 'Tata'),
        ('Hyundai', 'Hyundai'),
        ('Jeep', 'Jeep'),
        ('Datsun', 'Datsun'),
        ('Honda', 'Honda'),
        ('Mahindra', 'Mahindra'),
        ('Mercedes-Benz', 'Mercedes-Benz'),
        ('BMW', 'BMW'),
        ('Renault', 'Renault'),
        ('Audi', 'Audi'),
        ('Toyota', 'Toyota'),
        ('Mini', 'Mini'),
        ('Kia', 'Kia'),
        ('Skoda', 'Skoda'),
        ('Volkswagen', 'Volkswagen'),
        ('Volvo', 'Volvo'),
        ('MG', 'MG'),
        ('Nissan', 'Nissan'),
        ('Fiat', 'Fiat'),
        ('Mahindra Ssangyong', 'Mahindra Ssangyong'),
        ('Mitsubishi', 'Mitsubishi'),
        ('Jaguar', 'Jaguar'),
        ('Land Rover', 'Land Rover'),
        ('Chevrolet', 'Chevrolet'),
        ('Citroen', 'Citroen'),
        ('Opel', 'Opel'),
        ('Mahindra Renault', 'Mahindra Renault'),
        ('Isuzu', 'Isuzu'),
        ('Lexus', 'Lexus'),
        ('Porsche', 'Porsche'),
        ('Hindustan Motors', 'Hindustan Motors'),
    ]
    
    # Model choices (can be populated dynamically depending on the brand selected)
    MODEL_CHOICES = [
        ('Maruti Celerio', 'Maruti Celerio'),
        ('Ford Ecosport', 'Ford Ecosport'),
        ('Tata Tiago', 'Tata Tiago'),
        ('Hyundai Xcent', 'Hyundai Xcent'),
        ('Maruti SX4 S Cross', 'Maruti SX4 S Cross'),
        ('Jeep Compass', 'Jeep Compass'),
        ('Datsun GO', 'Datsun GO'),
        ('Hyundai Venue', 'Hyundai Venue'),
        ('Maruti Ciaz', 'Maruti Ciaz'),
        ('Maruti Baleno', 'Maruti Baleno'),
        ('Hyundai Grand i10', 'Hyundai Grand i10'),
        ('Honda Jazz', 'Honda Jazz'),
        ('Mahindra XUV500', 'Mahindra XUV500'),
        ('Mercedes-Benz GLA', 'Mercedes-Benz GLA'),
        ('Hyundai i20', 'Hyundai i20'),
        ('Tata Nexon', 'Tata Nexon'),
        ('Honda City', 'Honda City'),
        ('BMW 5 Series', 'BMW 5 Series'),
        ('Maruti Swift', 'Maruti Swift'),
        # Add more models as needed
    ]
    
    YEAR_CHOICES = [
        (2015, '2015'),
        (2018, '2018'),
        (2014, '2014'),
        (2020, '2020'),
        (2017, '2017'),
        (2021, '2021'),
        (2019, '2019'),
        (2022, '2022'),
        (2016, '2016'),
        (2011, '2011'),
        (2009, '2009'),
        (2013, '2013'),
        (2010, '2010'),
        (2008, '2008'),
        (2006, '2006'),
        (2012, '2012'),
        (2005, '2005'),
        (2007, '2007'),
        (2023, '2023'),
        (1998, '1998'),
        (2004, '2004'),
        (2003, '2003'),
        (2001, '2001'),
        (2002, '2002'),
        (2000, '2000'),
        (1985, '1985'),
        (1997, '1997'),
        (1999, '1999'),
    ]

    SEAT_CHOICES = [
        (2, '2'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    ]
    
    CITY_CHOICES = [
        ('Bangalore', 'Bangalore'),
        ('Chennai', 'Chennai'),
        ('Delhi', 'Delhi'),
        ('Hyderabad', 'Hyderabad'),
        ('Jaipur', 'Jaipur'),
        ('Kolkata', 'Kolkata'),
    ]

    ENGINE_CHOICES = [
        (998, '998cc'),
        (1497, '1497cc'),
        (1199, '1199cc'),
        (1197, '1197cc'),
        (1248, '1248cc'),
        (1956, '1956cc'),
        (1198, '1198cc'),
        (1462, '1462cc'),
        (2179, '2179cc'),
        (1950, '1950cc'),
        (1396, '1396cc'),
        (1995, '1995cc'),
        (1498, '1498cc'),
        (4663, '4663cc'),
        (1086, '1086cc'),
        (1991, '1991cc'),
        # Add more engine capacities as needed
    ]
    
    # Form Fields
    fuel_type = forms.ChoiceField(choices=FUEL_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    body_type = forms.ChoiceField(choices=BODY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    transmission = forms.ChoiceField(choices=TRANSMISSION_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    owner_count = forms.ChoiceField(choices=OWNER_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    # Additional fields for car specifications
    brand = forms.ChoiceField(choices=BRAND_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    model = forms.ChoiceField(choices=MODEL_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    model_year = forms.ChoiceField(choices=YEAR_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    insurance_validity = forms.ChoiceField(choices=[
        ('Third Party', 'Third Party'),
        ('Comprehensive', 'Comprehensive'),
        ('Zero Dep', 'Zero Dep'),
        ('Not Available', 'Not Available')
    ], widget=forms.Select(attrs={'class': 'form-control'}))

    km_driven = forms.IntegerField(min_value=0, max_value=1000000, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    mileage = forms.FloatField(min_value=0, max_value=100, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    seats = forms.ChoiceField(choices=SEAT_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    color = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.ChoiceField(choices=CITY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    engine = forms.ChoiceField(choices=ENGINE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    # Add other fields as necessary, such as mileage, seats, etc.
