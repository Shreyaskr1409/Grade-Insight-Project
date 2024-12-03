from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

app = Flask(__name__)
CORS(app)

model = joblib.load("../linear_regression_model.pkl")

feature_names = [
    "Hours_Studied", "Attendance", "Parental_Involvement", "Access_to_Resources",
    "Extracurricular_Activities", "Sleep_Hours", "Previous_Scores", "Motivation_Level",
    "Internet_Access", "Tutoring_Sessions", "Family_Income", "Teacher_Quality",
    "School_Type", "Peer_Influence", "Physical_Activity", "Learning_Disabilities",
    "Parental_Education_Level", "Distance_from_Home", "Gender"
]

@app.route("/predict", methods=["POST"])
def predict():
    try:
        input_data = request.json
        app.logger.debug("Received input data: %s", input_data)
        missing_features = [f for f in feature_names if f not in input_data]
        if missing_features:
            return jsonify({"error": f"Missing fields: {missing_features}"}), 400

        try:
            input_array = np.array([[float(input_data[feature]) for feature in feature_names]])
        except ValueError as e:
            app.logger.error(f"Non-numeric input detected: {e}")
            return jsonify({"error": "All input fields must be numeric."}), 400

        prediction = model.predict(input_array)[0]

        coefficients = model.coef_

        response = {
            "predicted_score": round(prediction, 2),
            "coefficients": {feature: round(coeff, 2) for feature, coeff in zip(feature_names, coefficients)}
        }
        return jsonify(response)

    except Exception as e:
        app.logger.error(f"An error occurred: {e}")
        return jsonify({"error": "An internal error occurred. Please try again later."}), 500

if __name__ == "__main__":
    app.run(debug=True)