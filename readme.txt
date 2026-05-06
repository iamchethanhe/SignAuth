SignAuth – AI-Based Image Forgery Detection and Signature Verification System

Overview

SignAuth is an AI-powered web application developed to detect image forgery and verify signature authenticity using Deep Learning techniques. The system provides a secure and user-friendly platform where users can upload images or signatures and receive real-time verification results.

The project combines Computer Vision, Deep Learning, and Full Stack Web Development to improve digital document security.

⸻

Features

* Secure Login Authentication
* Image Forgery Detection
* Signature Verification
* Real-Time Prediction
* Face Detection for Invalid Signature Uploads
* Signature Validation Check
* Professional Responsive User Interface
* Support for JPG, PNG, and TIFF Images

⸻

Problem Statement

In today’s digital world, forged images and fake signatures are becoming increasingly common. Traditional verification methods are manual, time-consuming, and prone to human error.

There is a need for an automated and intelligent verification system that can:

* detect tampered images
* identify forged signatures
* provide quick and accurate results
* improve digital document security

SignAuth addresses this problem using AI and Deep Learning techniques.

⸻

Proposed Solution

SignAuth is a Flask-based AI verification system that uses Convolutional Neural Networks (CNN) for:

* image forgery detection
* signature authenticity verification

The system allows users to upload files through a web interface, processes them using OpenCV and Deep Learning models, and displays real-time prediction results.

⸻

Technologies Used

Frontend

* HTML5
* CSS3
* Tailwind CSS
* JavaScript

Backend

* Python
* Flask Framework

AI / Deep Learning

* TensorFlow
* Keras
* CNN (Convolutional Neural Network)

Computer Vision

* OpenCV
* NumPy
* PIL (Python Imaging Library)

⸻

System Architecture

User Upload
      ↓
Flask Backend
      ↓
Image Preprocessing
      ↓
CNN Model Prediction
      ↓
Forgery / Signature Result
      ↓
Display Result on Web UI

⸻

Project Modules

1. Login Module

* Provides secure login access
* Validates username and password
* Redirects authenticated users to the home page

⸻

2. Image Forgery Detection Module

* Uploads document/image
* Preprocesses image using OpenCV
* CNN model predicts:
    * Authentic Image
    * Tampered Image

⸻

3. Signature Verification Module

* Uploads signature image
* Detects invalid uploads using face detection
* Validates signature structure
* CNN model predicts:
    * Genuine Signature
    * Forged Signature

⸻

4. Result Display Module

* Displays uploaded image
* Shows prediction result in real time
* Provides user-friendly visualization

⸻

Deep Learning Models Used

1. CNN (Final Model)

CNN was selected as the final model because:

* achieved highest accuracy
* performed better on smaller datasets
* faster and lightweight
* efficient for real-time prediction

Accuracy

* Image Forgery Detection: 88.5%
* Signature Verification: 85.3%

⸻

2. VGG16

* Pretrained CNN architecture
* Deep model with 16 layers
* Good performance but computationally heavy

Accuracy

* Image Forgery Detection: 76.5%
* Signature Verification: 83.1%

⸻

3. ResNet50

* Deep CNN with residual connections
* More complex architecture
* Lower performance for this dataset

Accuracy

* Image Forgery Detection: 55.0%
* Signature Verification: 66.3%

⸻

Evaluation Metrics

The CNN model was evaluated using:

* Accuracy Graph
* Loss Graph
* Confusion Matrix

Confusion Matrix Values

Metric	Value
True Positive (TP)	249
True Negative (TN)	288
False Positive (FP)	25
False Negative (FN)	38

The results show that the model correctly classified most authentic and tampered images.

⸻

Dataset Information

Image Forgery Dataset

Used for training and testing:

* authentic images
* tampered images

⸻

Signature Dataset

Used for:

* genuine signatures
* forged signatures

Supported Formats

* JPG
* PNG
* TIFF

⸻

Image Preprocessing

The uploaded image undergoes preprocessing before prediction:

* image resizing
* normalization
* grayscale conversion
* edge detection
* face detection

This improves model accuracy and prediction quality.

⸻

Face Detection Logic

The system prevents users from uploading human images in the signature verification module.

It uses:

* Haar Cascade Classifier
* OpenCV Face Detection

If a human face is detected, the system displays:

This is a human image, not a signature

⸻

Signature Validation Logic

The system validates whether the uploaded file resembles a signature using:

* edge density
* pixel distribution
* standard deviation
* image structure analysis

If the upload is not a valid signature, the system displays:

Please upload a proper signature image

⸻

Advantages

* Fast and automated verification
* Reduced manual effort
* Improved accuracy
* Real-time prediction
* Enhanced document security
* User-friendly interface

⸻

Limitations

* Accuracy depends on dataset quality
* Limited training data
* No database integration
* Single-user login system

⸻

Future Scope

Future improvements include:

* Face ID Login
* Tampered Area Highlighting
* Tampering Percentage Detection
* Cloud Deployment
* Mobile Application
* Database Integration
* Advanced Pretrained Models

⸻

Installation Guide

1. Clone Repository

git clone <repository_link>
cd SignAuth

⸻

2. Create Virtual Environment

python -m venv venv

⸻

3. Activate Environment

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate

⸻

4. Install Dependencies

pip install -r requirements.txt

⸻

5. Run Application

python app.py

⸻

Default Login Credentials

Username

chethan

Password

chethan123

⸻

Project Structure

SignAuth/
│
├── app.py
├── models/
│   ├── image_model.h5
│   └── sign_model.h5
│
├── static/
│   ├── uploads/
│   └── images/
│
├── templates/
│   ├── login.html
│   ├── index.html
│   ├── about.html
│   └── service.html
│
├── notebook/
├── src/
└── requirements.txt

⸻

My Role in the Project

Full Stack Developer & AI Integration Developer

Responsibilities:

* frontend development
* backend development
* AI model integration
* image preprocessing
* prediction workflow
* result visualization
* testing and debugging

⸻

Conclusion

SignAuth provides an intelligent and reliable solution for:

* image forgery detection
* signature verification

using AI and Deep Learning techniques.

The system improves security, reduces manual effort, and enables real-time digital document verification.

⸻

References

* TensorFlow Documentation
* OpenCV Documentation
* Flask Documentation
* Keras Documentation
* Research Papers on Image Forgery Detection
* Research Papers on Signature Verification