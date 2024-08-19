import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load your dataset
data = pd.read_excel('C:\\Users\\sahil\\OneDrive\\Desktop\\Rsport_player_dataset.xlsx')

# Specify the features and the target
features = ['Height (cm)', 'Weight (kg)', 'BMI (kg/m^2)', 'Muscle Flexibility', 
            'Agility', 'Age', 'Endurance', 'Reaction Time', 
            'Strength', 'Coordination', 'Speed', 'Balance', 'Gender']
target = 'Suggested Sport'

# Preprocess the data
# Convert 'Gender' to numerical (0 for Male, 1 for Female)
data['Gender'] = data['Gender'].map({'Male': 0, 'Female': 1})

# Separate features and target
X = data[features]
y = data[target]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test_scaled)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {accuracy:.2f}")

# Save the trained model and scaler
joblib.dump(model, 'best_sports_model_updated.pkl')
joblib.dump(scaler, 'scaler.pkl')

print("Model and scaler have been saved successfully.")
