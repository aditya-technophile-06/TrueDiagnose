
# True Diagnose: AI-Powered Medical Diagnosis Web Application

![Logo](logo.png)

## Project Overview

True Diagnose is a machine learning-powered web application designed to assist in medical diagnosis. This project leverages machine learning and deep learning models trained on large datasets to predict various diseases based on user-provided medical data. The system enables users to detect potential health issues and schedule appointments with doctors if needed. The application also offers a secure communication feature via email between patients and doctors, providing a streamlined healthcare experience.

## Why This Project?

Errors in human diagnosis are inevitable, but machine learning models can significantly improve the accuracy of medical predictions. By harnessing the power of AI, we ensure more reliable health assessments. Extensive research in allopathic, homeopathic, and ayurvedic fields led us to utilize allopathic datasets due to the availability of data. This project uses datasets sourced from Kaggle and UCI Machine Learning repositories for accurate health predictions.

## Key Features

 - Disease Prediction: Detects and predicts the likelihood of common diseases based on uploaded medical data.
 - Appointment Scheduling: Allows users to book appointments with doctors for further consultation.
 - Patient-Doctor Communication: Provides an email-based communication system for secure interaction between patients and healthcare providers.
 - User-Friendly Interface: Designed with an intuitive and accessible UI for seamless interaction.

## Diseases Covered

    1. Diabetes
    2. Breast Cancer
    3. Heart Disease
    4. Kidney Disease
    5. Liver Disease
    6. Malaria (Deep Learning)
    7. Pneumonia (Deep Learning)

# Technology Stack

+ Front-End: HTML, CSS, JavaScript
+ Back-End: Flask (Python)
+ Machine Learning Models: Trained using Python (scikit-learn, TensorFlow)
+ Deep Learning Models: Convolutional Neural Networks (CNN) for Malaria and Pneumonia
+ Database: SQLite for data management
+ Deployment: Flask for web app hosting

## Model Accuracy

| Disease | Type of Model    | Accuracy   |
| :-------- | :------- | :------------------------- |
| `Diabetes` | `Machine Learning Model` | `98.25 % `|
| `Breast Cancer` | `Machine Learning Model` | `98.25 % `|
| `Heart Disease    ` | `Machine Learning Model` | `85.25 % `|
| `Kidney Disease` | `Machine Learning Model` | `99 % `|
| `Liver Disease` | `Machine Learning Model` | `78 % `|
| `Malaria` | `Deep Learning Model (CNN)` | `96 % `|
| `Pneumonia` | `Deep Learning Model (CNN)` | `95 % `|

## Directory Structure

    ├── app.py                        # Main application code
    ├── notebooks/                    # Jupyter Notebooks for training models
    ├── models/                       # Trained model files (.pkl)
    ├── templates/                    # HTML Templates
    │   ├── home.html
    │   ├── contact.html
    │   ├── about_us.html
    │   ├── services.html
    │   ├── css/
    │   ├── js/
    │   └── images/
    ├── static/                       # Static files (logos, images, fonts)
    ├── readme.md                     # Project readme file
    ├── runtime.txt                   # Runtime configuration
    └── requirements.txt              # Dependencies for the project

## How to Run the Project

  Clone the repository:
  
  ```bash
        git clone https://github.com/your-username/true-diagnose.git
  ```

  Set up the environment:

  ```bash
        pip install -r requirements.txt
  ```

  Run the application:

  ```bash
        python app.py
  ```

  Open http://127.0.0.1:5000/ in your browser to access the web application.

## Datasets Used

1. [Diabetes Dataset](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)
2. [Breast Cancer Dataset](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data)
3. [Heart Disease Dataset](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data)
4. [Kidney Disease Dataset](https://www.kaggle.com/datasets/mansoordaku/ckdisease)
5. [Liver Disease Dataset](https://www.kaggle.com/datasets/uciml/indian-liver-patient-records)
6. [Malaria Dataset](https://www.kaggle.com/datasets/iarunava/cell-images-for-detecting-malaria)
7. [Pneumonia Dataset](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia)

## Technical Details

- Python Version: 3.6.8
- Flask Web Framework for the front and back-end
- Machine Learning models trained using scikit-learn
- Deep Learning models built with TensorFlow

## Screenshots

![App Demo](TrueDiagnose_DemoVideo.mp4)










