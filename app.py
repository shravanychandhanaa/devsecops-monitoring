from flask import Flask, jsonify
import requests

app = Flask(__name__)

GITHUB_RAW_URL = "https://raw.githubusercontent.com/shravanychandhanaa/devsecops-monitoring/main/reports/trivy.json"

# 🔁 Toggle this for testing
TEST_MODE = True   # 👉 Set to False for real data

def get_vulnerability_counts():
    try:
        response = requests.get(GITHUB_RAW_URL)

        # Handle empty or invalid response
        if not response.text.strip():
            return {"error": "Empty JSON from GitHub"}

        data = response.json()

        counts = {"critical": 0, "high": 0, "medium": 0}

        for result in data.get("Results", []):
            for vuln in result.get("Vulnerabilities", []) or []:
                severity = vuln.get("Severity", "").lower()
                if severity in counts:
                    counts[severity] += 1

        return counts

    except Exception as e:
        return {"error": str(e)}

@app.route("/")
def home():
    return "DevSecOps Monitoring API Running"

@app.route("/metrics")
def metrics():
    # 🧪 TEST DATA (for Grafana Pie Chart)
    if TEST_MODE:
        return jsonify({
            "critical": 10,
            "high": 10,
            "medium": 5
        })

    # 🔴 REAL DATA
    return jsonify(get_vulnerability_counts())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
