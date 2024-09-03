import pickle
import os

# Define the list of URLs to test
test_urls = [
    "https://www.google.com",
    "https://www.wikipedia.org",
    "https://www.amazon.com",
    "https://www.github.com",
    "https://www.microsoft.com",
    "https://www.youtube.com",
    "https://in.linkedin.com"
]

# Load the URL model and vectorizer
models_dir = 'C:\\Users\\ASUS\\OneDrive\\Desktop\\PhishingSiteDetection\\phishing_detection\\detection\\models'

with open(os.path.join(models_dir, 'url_model.pkl'), 'rb') as file:
    url_model = pickle.load(file)

with open(os.path.join(models_dir, 'url_vectorizer.pkl'), 'rb') as file:
    vectorizer = pickle.load(file)

# Function to predict URL
def predict_url(url):
    features = vectorizer.transform([url])
    prediction = url_model.predict(features)
    return 'Legitimate' if prediction[0] else 'Phishing'

# Test each URL
for url in test_urls:
    result = predict_url(url)
    print(f"URL: {url} - Prediction: {result}")