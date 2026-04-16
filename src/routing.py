from src.predict import predict_risk

# Assign risk to each location
def assign_risk(locations):
    for loc in locations:
        loc['risk'] = predict_risk(loc['Latitude'], loc['Longitude'])
    return locations

# Get safest route (sorted by risk)
def get_safe_route(locations):
    return sorted(locations, key=lambda x: x['risk'])