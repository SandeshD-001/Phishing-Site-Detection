import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pickle
import os

# Load the dataset
csv_file_path = 'C:\\Users\\ASUS\\OneDrive\\Desktop\\PhishingSiteDetection\\phishing_detection\\scripts\\phishing_site_urls.csv'
print(f"Reading data from {csv_file_path}")
data = pd.read_csv(csv_file_path)
print("Data loaded successfully.")

# Display first few rows of the dataset to verify correct loading
print(data.head())

# Check the total number of entries
print(f"Total number of entries: {len(data)}")

# Verify the column names
print(f"Column names: {data.columns}")

# Check for any missing values
print(f"Missing values:\n{data.isnull().sum()}")

# Ensure the data has the correct columns
if 'URL' not in data.columns or 'Label' not in data.columns:
    raise ValueError("CSV file must contain 'URL' and 'Label' columns.")

# Prepare the feature and target variable
urls = data['URL']
labels = data['Label'].apply(lambda x: 1 if x == 'bad' else 0)

# Vectorize the URLs
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(urls)

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)

# Train the model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Create the directory if it doesn't exist
models_dir = 'C:\\Users\\ASUS\\OneDrive\\Desktop\\PhishingSiteDetection\\phishing_detection\\detection\\models'
os.makedirs(models_dir, exist_ok=True)

# Save the model and vectorizer
with open(os.path.join(models_dir, 'url_model.pkl'), 'wb') as file:
    pickle.dump(model, file)

with open(os.path.join(models_dir, 'url_vectorizer.pkl'), 'wb') as file:
    pickle.dump(vectorizer, file)

print("Model and vectorizer saved successfully.")
