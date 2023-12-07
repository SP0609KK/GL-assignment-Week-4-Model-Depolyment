# GL-assignment-Week-4-Model-Depolyment
Simple Flask API for Logistic Regression Predictions

This Flask API offers a user-friendly way to incorporate a logistic regression model into web applications. Users can send data to /get_predictions, and the API promptly responds with model predictions.

Model Setup: Load a pre-trained logistic regression model using the joblib library from the specified path ('assets/model/logistic_regression.joblib').

API Usage: The app has one simple API endpoint (/get_predictions). Users can send input data as JSON in a POST request to get predictions. How It Works: When a request is made, the app extracts user-provided data from the JSON and prepares it for the logistic regression model by converting it into a format the model understands.

Get Predictions: The logistic regression model predicts outcomes based on the user's input.

Results: The app returns the model's predictions in a straightforward string format in the HTTP response.

Error Handling: Basic error handling is included. If something goes wrong, an error message is returned with a 500 status code.

Ready for Use: Run the script, and the Flask app starts. The API is then ready for use. The debug mode is set to False for smooth production use.
