from flask import Flask, request, Response
from joblib import load
import numpy as np

# Create a Flask web application
app = Flask(__name__)

# Load the pre-trained logistic regression model
my_lr_model = load('assets/model/logistic_regression.joblib')

# Define an API endpoint for predictions
@app.route("/get_predictions", methods=['POST'])
def get_predictions():
    try:
        # Receive JSON data from the POST request
        data = request.json

        # Extract user-provided data from JSON
        user_sent_this_data = data.get('mydata')

        # Convert the user data into a NumPy array and reshape it
        user_number = np.array(user_sent_this_data).reshape(1, -1)

        # Use the pre-trained model to make predictions
        model_prediction = my_lr_model.predict(user_number)

        # Return the model's predictions as a response
        return Response(str(model_prediction))

    except Exception as e:
        # Handle exceptions and return an error response with a 500 status code
        return Response(str(e), status=500)

# Run the Flask app
if __name__ == '__main__':
    # Start the Flask app with debugging turned off for production use
    app.run(debug=False)
