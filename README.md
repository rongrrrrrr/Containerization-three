# Assignment-2 ESG Engagement Score Predictor API

This repository contains a lightweight Flask application that provides a machine learning–based prediction API for estimating ESG (Environmental, Social, and Governance) engagement scores. It uses a simple linear regression model trained on synthetic data with treatment indicators (W) and sustainability spending values (X).

## 🔧 Components Overview

### 1. `app.py`
This is the main application file that sets up a Flask API server. It exposes a `/predict` route, which takes input values for `W` and `X` (via GET parameters), passes them through a trained `LinearRegression` model, and returns the predicted engagement score (`Ŷi`) as a JSON response.

### 2. `Dockerfile`
The `Dockerfile` defines a reproducible environment using a Python 3.10 base image. It installs required dependencies and launches the Flask app in a self-contained container, enabling consistent behavior across different systems and environments.

### 3. `requirements.txt`
This file lists the necessary Python packages, such as `flask`, `scikit-learn`, and `numpy`, which are automatically installed during the Docker build process.

### 🚀 How to Run with Docker
#### 1.docker build -t esg-api .
#### 2.docker run -p 5050:5050 esg-api
#### 3.Then, test the API:
##### For Q1: curl http://localhost:5050/estimate_ate
##### For Q2: curl "http://localhost:5000/predict?W=1&X=20"
✅ Example Response:
{
  "input": {"W": 1.0, "X": 20},
  "predicted_engagement_score": 117.16
}
##### curl http://localhost:5050/estimate_ate
