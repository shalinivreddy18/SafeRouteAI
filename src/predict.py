import pandas as pd
import pickle

# Load model
with open('models/risk_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Function to predict risk
def predict_risk(lat, lon, hour=14, day=2, month=4, crime_type=3, arrest=0, domestic=0):
    sample = pd.DataFrame([{
        'Latitude': lat,
        'Longitude': lon,
        'Arrest': arrest,
        'Domestic': domestic,
        'hour': hour,
        'day': day,
        'month': month,
        'crime_type': crime_type
    }])
    
    return model.predict(sample)[0]

# Function to convert score → level
def get_risk_level(score):
    if score < 2:
        return "Low Risk"
    elif score < 4:
        return "Medium Risk"
    else:
        return "High Risk"