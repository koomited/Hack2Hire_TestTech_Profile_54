from pydantic import BaseModel
import numpy as np
import pandas as pd
import pickle
from flask import Flask, request, jsonify

# Import model
with open('best_rf.pkl', 'rb') as f:
    model = pickle.load(f)

# Format data with Pydantic
class DataEntry(BaseModel):
    Credit_amount: float
    Age: int
    Duration: float
    Purpose: int

# Create the Flask application
app = Flask(__name__)

# Home route
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the API for credit score prediction!"})

# Prediction route
@app.route("/predict", methods=["POST"])
def predict():
    if not request.is_json:
        return jsonify({"error": "Invalid content type. Expected JSON."}), 400

    try:
        # Parse and validate input data
        data = DataEntry(**request.json)
        data_df = pd.DataFrame([data.dict()])

        # Make predictions
        credit_score_proba = model.predict_proba(data_df)[:, 1]  # Probability for the positive class
        prediction = model.predict(data_df)

        # Prepare results
        results = data.dict()
        results["prediction"] = int(prediction[0])
        results["credit_score"] = round(float(credit_score_proba[0]),4)
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Run the application
if __name__ == "__main__":
    app.run(debug=True, port=8000)
