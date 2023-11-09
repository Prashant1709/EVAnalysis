#Train Data code
# Import necessary libraries
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd

# Load your data
# This is a placeholder, replace this with your actual data loading code
data = pd.read_csv('EV_data.csv')

# Assume you have the following features in your data
features = ['battery_level', 'average_speed', 'temperature', 'terrain_type', 'driving_habits', 'weather_conditions', 'vehicle_condition']
target = 'distance_to_empty'

X = data[features]
y = data[target]

# Preprocess the data
# Standardize the features to have mean=0 and variance=1
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the model
model = Sequential()
model.add(Dense(64, input_dim=len(features), activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(32, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(16, activation='relu'))
model.add(Dense(1, activation='linear'))

# Compile the model
model.compile(loss='mean_squared_error', optimizer='adam')

# Train the model
model.fit(X_train, y_train, epochs=100, batch_size=32, validation_split=0.2)

# Save the model to a .h5 file
model.save('my_model.h5')

# Load the model from the .h5 file
loaded_model = load_model('my_model.h5')

# Use the loaded model to make predictions
predictions = loaded_model.predict(X_test)

# Print the predictions
print(predictions[0][0]/10)
