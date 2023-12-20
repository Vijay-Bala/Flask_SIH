import requests
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
req_f1 = requests.get(url='http://127.0.0.1:5000/api/flow/f1')
req_f2 = requests.get(url='http://127.0.0.1:5000/api/flow/f2')
dif = req_f1.json()[-1]['value']-req_f2.json()[-1]['value'] 
# Load the pre-trained model
model = load_model('pressure_pranched_DNN.h5')

# Function to preprocess input data
def preprocess_input(input_data):
    # Implement your preprocessing logic here if needed
    # Example: Convert input_data to a numpy array or perform other transformations
    preprocessed_data = np.array(input_data)
    return preprocessed_data

# Function to make predictions
def predict(input_data):
    preprocessed_data = preprocess_input(input_data)
    predictions = model.predict(preprocessed_data)
    return predictions

if __name__ == "__main__":
    # Example usage:
    # Replace the following input_data with the actual input data for prediction
    input_data = [[req_f1.json()[-1]['value'], req_f2.json()[-1]['value'] ]]  # Replace with your input features
    
    # Make predictions
    predictions = predict(input_data)

    print("Predictions:")
    print(predictions)
