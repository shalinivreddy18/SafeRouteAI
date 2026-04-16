import folium
from src.predict import predict_risk, get_risk_level

# ============================================
# STEP 1: Take user input
# ============================================

start_lat = float(input("Enter start latitude: "))
start_lon = float(input("Enter start longitude: "))

end_lat = float(input("Enter end latitude: "))
end_lon = float(input("Enter end longitude: "))

# ============================================
# STEP 2: Generate multiple routes
# ============================================

route1 = [
    {'Latitude': start_lat, 'Longitude': start_lon},
    {'Latitude': (start_lat + end_lat)/2, 'Longitude': (start_lon + end_lon)/2},
    {'Latitude': end_lat, 'Longitude': end_lon}
]

route2 = [
    {'Latitude': start_lat, 'Longitude': start_lon},
    {'Latitude': start_lat + 0.02, 'Longitude': start_lon + 0.02},
    {'Latitude': end_lat, 'Longitude': end_lon}
]

# ============================================
# STEP 3: Calculate route risk
# ============================================

def calculate_route_risk(route):
    total = 0
    for loc in route:
        risk = predict_risk(loc['Latitude'], loc['Longitude'])
        loc['risk'] = risk
        total += risk
    return total

risk1 = calculate_route_risk(route1)
risk2 = calculate_route_risk(route2)

# ============================================
# STEP 4: Compare routes
# ============================================

if risk1 < risk2:
    safest_route = route1
    print("\n✅ Route 1 is SAFEST")
else:
    safest_route = route2
    print("\n✅ Route 2 is SAFEST")

print(f"Route 1 Risk: {risk1:.2f}")
print(f"Route 2 Risk: {risk2:.2f}")

# ============================================
# STEP 5: Map Visualization
# ============================================


# Draw Route 1 (Blue)
coords1 = [(loc['Latitude'], loc['Longitude']) for loc in route1]
folium.PolyLine(coords1, color="blue", weight=3).add_to(m)

# Draw Route 2 (Red)
coords2 = [(loc['Latitude'], loc['Longitude']) for loc in route2]
folium.PolyLine(coords2, color="red", weight=3).add_to(m)

# Draw Safest Route (Green)
safe_coords = [(loc['Latitude'], loc['Longitude']) for loc in safest_route]
folium.PolyLine(safe_coords, color="green", weight=5).add_to(m)

# Add markers
for loc in safest_route:
    level = get_risk_level(loc['risk'])
    folium.Marker(
        [loc['Latitude'], loc['Longitude']],
        popup=f"Risk: {loc['risk']:.2f} ({level})"
    ).add_to(m)

# Save map
m.save("map.html")

print("\n🗺️ Map saved as map.html")