import cv2
import pytesseract
import joblib
import numpy as np
import re

# Load the trained phishing text classifier and vectorizer
model = joblib.load("phishing_text_classifier.joblib")
vectorizer = joblib.load("tfidf_vectorizer.joblib")

# Function to extract text from an image using Tesseract OCR
def extract_text_from_image(image_file):
    # Read the image file directly from the uploaded file object
    image_bytes = np.frombuffer(image_file.read(), np.uint8)
    image = cv2.imdecode(image_bytes, cv2.IMREAD_COLOR)
    
    # Convert the image to grayscale for better OCR accuracy
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply a bilateral filter to reduce noise while keeping edges sharp
    gray = cv2.bilateralFilter(gray, 11, 17, 17)
    
    # Use Tesseract OCR to extract text from the processed image
    extracted_text = pytesseract.image_to_string(gray)
    return extracted_text

# Function to classify extracted text as phishing or legitimate
def classify_text(text):
    # Preprocess the text for prediction
    text_vector = vectorizer.transform([text])
    
    # Predict using the loaded model
    prediction = model.predict(text_vector)
    
    # Return classification result
    return "Phishing" if prediction[0] == 1 else "Legitimate"
