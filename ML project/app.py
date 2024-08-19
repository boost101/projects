from flask import Flask, request, render_template ,Request
import numpy as np
import pandas as pd
import joblib
import traceback

# Initialize the Flask app
app = Flask(__name__)

# Load the trained model and scaler
try:
    model = joblib.load('best_sports_model_updated.pkl')
    scaler = joblib.load('scaler.pkl')
except FileNotFoundError as e:
    print(f"Error loading files: {e}")
    exit(1)

# Updated sport mapping (ensure this matches the encoding order in your dataset)
sport_mapping = {0: "Soccer", 1: "Basketball", 2: "Tennis", 3: "Swimming", 4: "Athletics"}

@app.route('/')      #get method is requested from server
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        data = request.form

        # Extract features from the form data
        features = np.array([
            float(data.get('Height (cm)', 0)), 
            float(data.get('Weight (kg)', 0)), 
            float(data.get('BMI (kg/m^2)', 0)), 
            float(data.get('Muscle Flexibility', 0)),
            float(data.get('Agility', 0)), 
            float(data.get('Age', 0)), 
            float(data.get('Endurance', 0)), 
            float(data.get('Reaction Time', 0)),
            float(data.get('Strength', 0)), 
            float(data.get('Coordination', 0)), 
            float(data.get('Speed', 0)), 
            float(data.get('Balance', 0)), 
            float(data.get('Gender', 0))
        ]).reshape(1, -1)
        
        # Create a DataFrame with the appropriate column names
        columns = ['Height (cm)', 'Weight (kg)', 'BMI (kg/m^2)', 'Muscle Flexibility', 
                   'Agility', 'Age', 'Endurance', 'Reaction Time', 
                   'Strength', 'Coordination', 'Speed', 'Balance', 'Gender']
        features_df = pd.DataFrame(features, columns=columns)
        
        # Scale the features using the same scaler used in training
        features_scaled = scaler.transform(features_df)
        
        # Make prediction
        prediction = model.predict(features_scaled)
        predicted_sport = sport_mapping.get(int(prediction[0]), "Unknown")
        
        # Render the result page with the predicted sport
        return render_template('result.html', predicted_sport=predicted_sport)
    
    except Exception as e:
        print("Error during prediction:", str(e))
        traceback.print_exc()
        return render_template('result.html', predicted_sport="Error occurred")

if __name__ == '__main__':
    app.run(debug=True, port=5000)




# Invoke-RestMethod -Uri http://127.0.0.1:5000/predict -Method Post -Body @{
#     height_cm = 170
#     weight_kg = 65
#     bmi = 22.5
#     muscle_flexibility = 8.5
#     agility = 7.2
#     age = 12
#     endurance = 6.9
#     reaction_time = 0.45
#     strength = 7.8
#     coordination = 7.0
#     speed = 6.5
#     balance = 7.1
#     gender = 0
# }
