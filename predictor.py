#Predict the DTE code
from keras.models import load_model
import numpy as np

# Load the model from the .h5 file
model = load_model('my_model.h5')

# Ask the user to enter values for the features
battery_level = float(input("Enter the battery level (0-100): "))
average_speed = float(input("Enter the average speed (km/h): "))
temperature = float(input("Enter the temperature (Celsius): "))
terrain_type = int(input("Enter the terrain type (0 for flat, 1 for hilly): "))
driving_habits = int(input("Enter the driving habits (0 for aggressive, 1 for conservative): "))
weather_conditions = int(input("Enter the weather conditions (0 for sunny, 1 for cloudy, 2 for rainy, 3 for snowy): "))
vehicle_condition = float(input("Enter the vehicle condition (0-100): "))

# Create a numpy array with the feature values
features = np.array([[battery_level, average_speed, temperature, terrain_type, driving_habits, weather_conditions, vehicle_condition]])

# Use the model to predict the distance to empty
distance_to_empty = model.predict(features)

# Print the predicted distance to empty
print(f"The predicted distance to empty is: {distance_to_empty[0][0]/10}")
