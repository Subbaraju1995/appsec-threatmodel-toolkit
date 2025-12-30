def score_risk(likelihood, impact):
    score = likelihood * impact
    if score >= 7:
        severity = "High"
    elif score >= 4:
        severity = "Medium"
    else:
        severity = "Low"
    return score, severity


def generate_threat_model(system):
    threats = []

    # Information Disclosure (PII)
    if "PII" in system.get("data_types", []):
        score, severity = score_risk(likelihood=3, impact=3)
        threats.append({
            "category": "Information Disclosure",
            "threat": "Exposure of sensitive personal data",
            "likelihood": 3,
            "impact": 3,
            "risk_score": score,
            "risk": severity,
            "mitigation": "Encrypt data at rest and in transit"
        })

    # Denial of Service
    score, severity = score_risk(likelihood=2, impact=2)
    threats.append({
        "category": "Denial of Service",
        "threat": "API abuse leading to service unavailability",
        "likelihood": 2,
        "impact": 2,
        "risk_score": score,
        "risk": severity,
        "mitigation": "Implement rate limiting and monitoring"
    })

    return threats


