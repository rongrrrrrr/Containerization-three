from flask import Flask, request, jsonify
from sklearn.linear_model import LinearRegression
import numpy as np

app = Flask(__name__)

# Training data
# W: treatment indicator (0 or 1)
# X: sustainability spending
# y: engagement score
W = np.array([0,1,1,1,0,1,1,0,0,1,1,0,0,1,0,1,0,0,1,1])
X_feat = np.array([19.8,23.4,27.7,24.6,21.5,25.1,22.4,29.3,20.8,20.2,
                   27.3,24.5,22.9,18.4,24.2,21.0,25.9,23.2,21.6,22.8])
Y = np.array([137,118,124,124,120,129,122,142,128,114,
              132,130,130,112,132,117,134,132,121,128])

# Reshape and combine features
X_train = np.column_stack((W, X_feat))

# Train linear regression model
model = LinearRegression().fit(X_train, Y)

@app.route("/predict")
def predict():
    
        w = float(request.args.get("W", 0))
        x = float(request.args.get("X", 0))
        prediction = model.predict([[w, x]])[0]

        # Log prediction
        with open("output.txt", "w") as f:
            f.write(f"Input W: {w}, X: {x}\nPrediction: {prediction:.2f}\n")

        return jsonify({
            "input": {"W": w, "X": x},
            "predicted_engagement_score": round(prediction, 2)
        })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
