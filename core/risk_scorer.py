from typing import Dict
import pickle
import os

class RiskScorer:
    def __init__(self):
        model_path = os.path.join(os.path.dirname(__file__), "../data/model.pkl")
        if os.path.exists(model_path):
            with open(model_path, "rb") as f:
                self.model = pickle.load(f)
        else:
            # Placeholder: Simulate trained model
            from sklearn.ensemble import RandomForestClassifier
            self.model = RandomForestClassifier(n_estimators=100)
            # Train on synthetic data (in production, train offline)
            self.model.fit([[0, 0, 0]], [0])

    def score(self, vuln: Dict) -> Dict:
        features = [
            vuln.get("cvss_score", 0),
            1 if "admin" in vuln.get("asset", "").lower() else 0,
            1 if vuln.get("public_poc", False) else 0
        ]
        score = self.model.predict_proba([features])[0][1] * 100
        vuln["risk_score"] = round(score, 2)
        return vuln