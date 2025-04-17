from flask import Flask, request, jsonify
import numpy as np
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# === 1. 数据输入 ===
W = np.array([0,1,1,1,0,1,1,0,0,1,1,0,0,1,0,1,0,0,1,1])
X = np.array([19.8,23.4,27.7,24.6,21.5,25.1,22.4,29.3,20.8,20.2,
              27.3,24.5,22.9,18.4,24.2,21.0,25.9,23.2,21.6,22.8])
Y = np.array([137,118,124,124,120,129,122,142,128,114,
              132,130,130,112,132,117,134,132,121,128])

# === 2. 构造设计矩阵 ===
X_design = np.column_stack((W, X))  # 用于 statsmodels 和 sklearn

# === 3. statsmodels OLS 模型用于估计 ATE ===
X_with_const = sm.add_constant(X_design)
ols_model = sm.OLS(Y, X_with_const).fit()

# === 4. sklearn 线性回归模型用于预测 ===
sk_model = LinearRegression().fit(X_design, Y)

# === 5. 接口 1：返回参数估计 ===
@app.route("/estimate_ate", methods=["GET"])
def estimate_ate():
    coef = ols_model.params  # [α, τ, β]
    pvals = ols_model.pvalues

    return jsonify({
        "α (intercept)": round(coef[0], 3),
        "τ (ATE)": round(coef[1], 3),
        "β (X coefficient)": round(coef[2], 3)
    })

# === 6. 接口 2：基于输入预测 engagement score ===
@app.route("/predict")
def predict():
    try:
        w = float(request.args.get("W", 0))
        x = float(request.args.get("X", 0))
        prediction = sk_model.predict([[w, x]])[0]

        with open("output.txt", "w") as f:
            f.write(f"Input W: {w}, X: {x}\nPrediction: {prediction:.2f}\n")

        return jsonify({
            "input": {"W": w, "X": x},
            "predicted_engagement_score": round(prediction, 2)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# === 7. 启动服务 ===
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)




