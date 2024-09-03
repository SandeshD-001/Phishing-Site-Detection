Phishing Detection Web Application
Overview
    This Phishing Detection Web Application is designed to help users identify potential phishing websites in real time by analyzing the URLs they provide. The project is built using Django and incorporates a machine learning model trained on a dataset of phishing and legitimate URLs. The application provides a user-friendly interface where users can input a URL and receive immediate feedback on whether the URL is safe or potentially harmful.

Features
    Real-Time Phishing Detection: Users can enter a URL, and the application will analyze it using a machine learning model to determine whether it is legitimate or a phishing attempt.
Machine Learning Model: The backend uses a Logistic Regression model trained on a dataset of phishing and legitimate URLs. The model is saved and loaded for predictions within the application.
Dynamic User Interface: The application features a responsive and visually appealing UI with smooth animations and color-coded results to clearly indicate the safety status of the entered URL.
Recent URL Suggestions: The application tracks recent URLs entered by the user, providing suggestions in a dropdown menu for easy access.
Session Management: Recent URLs are stored in the user's session, ensuring that they are available throughout the session without requiring persistent storage.
Color-Coded Feedback: The background color of the result page dynamically changes based on the detection outcome:
Red for phishing URLs
Green for legitimate URLs
Pink for URLs not found in the training dataset

How It Works
    Input URL: The user inputs a URL into the form on the homepage.
Phishing Detection: The URL is analyzed using the trained machine learning model to predict whether it is a phishing site.
Result Display: The application displays the result, with the background color of the page indicating the status:
Phishing: The URL is identified as a phishing attempt.
Legitimate: The URL is safe to visit.
Not Found: The URL is not present in the training dataset.
Recent URLs: Recently entered URLs are suggested in a dropdown menu when the user clicks the input field.
