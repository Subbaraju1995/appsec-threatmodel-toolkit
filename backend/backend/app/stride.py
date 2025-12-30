def generate_threat_model(system):
    threats = []

    # Internet-facing system risk
    if system.get("internet_facing"):
        threats.append({
            "category": "Spoofing",
            "threat": "Unauthorized access via weak authentication",
            "risk": "High",
            "mitigation": "Enforce strong authentication and MFA"
        })

    # Sensitive data risk
    if "PII" in system.get("data_types", []):
        threats.append({
            "category": "Information Disclosure",
            "threat": "Exposure of sensitive personal data",
            "risk": "High",
            "mitigation": "Encrypt data at rest and in transit"
        })

    # API availability risk
    threats.append({
        "category": "Denial of Service",
        "threat": "API abuse leading to service unavailability",
        "risk": "Medium",
        "mitigation": "Implement rate limiting and monitoring"
    })

    return threats

