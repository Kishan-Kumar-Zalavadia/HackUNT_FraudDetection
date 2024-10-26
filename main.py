import pandas as pd
import numpy as np
from flask import Flask, request, jsonify
import pickle
from sklearn.ensemble import RandomForestClassifier

# Create Flask app
app = Flask(__name__)

# Load the trained model (you need to save the model after training)
model = pickle.load(open("fraud_model.pkl", "rb"))

# Define a prediction route
@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the POST request.
    data = request.get_json(force=True)
    
    # Extract input features
    input_data = pd.DataFrame([data])
    
    # Feature engineering (you can modify as per your original code)
    input_data['errorBalanceOrig'] = input_data['newBalanceOrig'] + input_data['amount'] - input_data['oldBalanceOrig']
    input_data['errorBalanceDest'] = input_data['oldBalanceDest'] + input_data['amount'] - input_data['newBalanceDest']

    # Predict using the model
    prediction = model.predict(input_data)
    print("coming")
    # Return prediction
    return jsonify({'isFraud': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
