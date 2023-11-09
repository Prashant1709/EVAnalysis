#Generate Data code
import pandas as pd
import numpy as np

# Number of samples
n = 1000

# Generate random data
data = pd.DataFrame({
    'battery_level': np.random.rand(n) * 100,  # Battery level as a percentage
    'average_speed': np.random.rand(n) * 120,  # Speed in km/h
    'temperature': np.random.rand(n) * 40,  # Temperature in Celsius
    'terrain_type': np.random.randint(0, 2, n),  # Terrain type (0 for flat, 1 for hilly)
    'driving_habits': np.random.randint(0, 2, n),  # Driving habits (0 for aggressive, 1 for conservative)
    'weather_conditions': np.random.randint(0, 4, n),  # Weather conditions (0 for sunny, 1 for cloudy, 2 for rainy, 3 for snowy)
    'vehicle_condition': np.random.rand(n) * 100,  # Vehicle condition as a percentage
})

# Assume a simple linear relationship with the target
data['distance_to_empty'] = data['battery_level'] - data['average_speed'] * 0.05 + data['temperature'] * 0.1 - data['terrain_type'] * 10 - data['driving_habits'] * 5 + data['weather_conditions'] * 2 + data['vehicle_condition'] * 0.1

# Add some noise to the target
data['distance_to_empty'] += np.random.randn(n) * 10

# Save the data to a CSV file
data.to_csv('EV_data.csv', index=False)
