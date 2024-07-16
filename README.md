# Diabetes Predictor
This tool leverages machine learning algorithms to analyze patient data and predict the likelihood of diabetes. It is designed to assist healthcare professionals in making early diagnoses and gives treatment plans.

## Features
- Machine Learning Model: Utilizes a trained machine learning model to predict diabetes based on patient metrics.
- User-Friendly Interface: Provides an intuitive interface for inputting patient data and receiving real-time predictions.

## Technologies Used
- Programming Language: Python
- Libraries: Pandas, OS, Webbrowser
- Machine Learning Algorithm: DecisionTreeClassifier

# Requirements
- python 3
- install django (pip install django)

# Steps to run project:
- Navigate to project directory
- Run following commands in cmd
  - python manage.py migrate
  - python manage.py createsuperuser
  - python manage.py runserver
  - Locate: http://localhost:8000/


## Working:
Signup -> Login -> Predict Diabetes -> prompt displays that whether the diabetes predicted or not

## To check DB : 
   - Locate: http://127.0.0.1:8000/admin/ and logging in with the superuser credentials.






