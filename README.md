# Containerization-three
## Setup & Run with Docker
### 1. Build Docker image
docker build -t my-api .
### 2. Run Docker container (port mapped to 5050)
docker run -p 5050:5050 my-api
### 3. Make a test request (example: x = 5)
curl http://localhost:5050/estimate_ate