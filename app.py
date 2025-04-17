from flask import Flask, jsonify
import numpy as np
import statsmodels.api as sm

app = Flask(__name__)

# === 1. 数据输入 ===
W = np.array([0,1,1,1,0,1,1,0,0,1,1,0,0,1,0,1,0,0,1,1])
X = np.array([19.8,23.4,27.7,24.6,21.5,25.1,22.4,29.3,20.8,20.2,
              27.3,24.5,22.9,18.4,24.2,21.0,25.9,23.2,21.6,22.8])
Y = np.array([137,118,124,124,120,129,122,142,128,114,
              132,130,130,112,132,117,134,132,121,128])

# === 2. 构造设计矩阵 (添加截距项) ===
X_design = np.column_stack((W, X))
X_design = sm.add_constant(X_design)  # 添加常数项 α
model = sm.OLS(Y, X_design).fit()

# === 3. API：返回回归结果 ===
@app.route("/estimate_ate", methods=["GET"])
def estimate_ate():
    coef = model.params  # [α, τ, β]
    pvals = model.pvalues

    return jsonify({
        "α (intercept)": round(coef[0], 3),
        "τ (ATE)": round(coef[1], 3),
        "β (X coefficient)": round(coef[2], 3),
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

