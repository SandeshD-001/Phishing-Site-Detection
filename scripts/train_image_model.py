# scripts/train_image_model.py
import os
import cv2
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Ensure the models directory exists
os.makedirs('../models', exist_ok=True)

# Function to load and process images
def load_images(image_dir, label):
    images = []
    labels = []
    for filename in os.listdir(image_dir):
        img_path = os.path.join(image_dir, filename)
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        if img is not None:
            img = cv2.resize(img, (128, 128))  # Resize for consistency
            images.append(img.flatten())
            labels.append(label)
    return images, labels

# Load phishing and legitimate images
phishing_images, phishing_labels = load_images('screenshots/phishing', 1)
legit_images, legit_labels = load_images('screenshots/legitimate', 0)

# Combine and convert to numpy arrays
images = np.array(phishing_images + legit_images)
labels = np.array(phishing_labels + legit_labels)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(images, labels, test_size=0.2, random_state=42)

# Train the model
image_model = RandomForestClassifier()
image_model.fit(X_train, y_train)

# Save the model
with open('../models/image_model.pkl', 'wb') as file:
    pickle.dump(image_model, file)

print("Image model saved successfully.")
