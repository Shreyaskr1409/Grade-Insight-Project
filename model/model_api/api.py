from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load("../linear_regression_model.pkl")

# Feature names (update based on your dataset)
feature_names = [
    "Hours_Studied", "Attendance", "Parental_Involvement", "Access_to_Resources",
    "Extracurricular_Activities", "Sleep_Hours", "Previous_Scores", "Motivation_Level",
    "Internet_Access", "Tutoring_Sessions", "Family_Income", "Teacher_Quality",
    "School_Type", "Peer_Influence", "Physical_Activity", "Learning_Disabilities",
    "Parental_Education_Level", "Distance_from_Home", "Gender"
]

@app.route("/predict", methods=["POST"])
def predict():
    # Get input data
    input_data = request.json

    # Validate input
    missing_features = [f for f in feature_names if f not in input_data]
    if missing_features:
        return jsonify({"error": f"Missing fields: {missing_features}"}), 400

    # Prepare input array
    input_array = np.array([[input_data[feature] for feature in feature_names]])

    # Make prediction
    prediction = model.predict(input_array)[0]

    # Extract coefficients
    coefficients = model.coef_

    # Return prediction and coefficients rounded off to 2 decimal places
    response = {
        "predicted_score": round(prediction, 2),
        "coefficients": {feature: round(coeff, 2) for feature, coeff in zip(feature_names, coefficients)}
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
