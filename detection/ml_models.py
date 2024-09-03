import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

# Load the model and vectorizer
with open('C:/Users/ASUS/OneDrive/Desktop/PhishingSiteDetection/phishing_detection/detection/models/url_model.pkl', 'rb') as file:
    url_model = pickle.load(file)

with open('C:/Users/ASUS/OneDrive/Desktop/PhishingSiteDetection/phishing_detection/detection/models/url_vectorizer.pkl', 'rb') as file:
    vectorizer = pickle.load(file)

# Load the dataset of known URLs
csv_file_path = 'C:/Users/ASUS/OneDrive/Desktop/PhishingSiteDetection/phishing_detection/scripts/phishing_site_urls.csv'
data = pd.read_csv(csv_file_path)
known_urls = set(data['URL'])

def predict_phishing(url_or_image_path):
    if is_url(url_or_image_path):
        return predict_url(url_or_image_path)
    else:
        return 'Unknown input type'

def predict_url(url):
    if url not in known_urls:
        return 'Not found'
    
    features = vectorizer.transform([url])
    prediction = url_model.predict(features)
    return 'Phishing' if prediction[0] else 'Legitimate'

def is_url(input):
    # Logic to determine if input is a URL (e.g., using regex or domain knowledge)
    return True  # Placeholder logic
