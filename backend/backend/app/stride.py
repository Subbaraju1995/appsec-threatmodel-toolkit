def generate_threat_model(system):
    threats = []

    # -----------------------------
    # STRIDE: Information Disclosure
    # -----------------------------
    if "PII" in system.get("data_types", []):
        threats.append({
            "category": "Information Disclosure",
            "threat": "Exposure of sensitive personal data",
            "likelihood": 3,
            "impact": 4,
            "risk_score": 12,
            "severity": "High",
            "mitigation": "Encrypt data at rest and in transit"
        })

    # -----------------------------
    # STRIDE: Denial of Service
    # -----------------------------
    threats.append({
        "category": "Denial of Service",
        "threat": "API abuse leading to service unavailability",
        "likelihood": 2,
        "impact": 2,
        "risk_score": 4,
        "severity": "Medium",
        "mitigation": "Implement rate limiting and monitoring"
    })

    # -----------------------------
    # AWS-Specific Threats
    # -----------------------------
    aws = system.get("aws", {})

    if aws.get("s3_public"):
        threats.append({
            "category": "Information Disclosure",
            "threat": "Public S3 bucket exposing sensitive data",
            "likelihood": 3,
            "impact": 4,
            "risk_score": 12,
            "severity": "High",
            "mitigation": "Block public access and enforce bucket policies"
        })

    if aws.get("iam_wildcards"):
        threats.append({
            "category": "Elevation of Privilege",
            "threat": "Overly permissive IAM roles with wildcard permissions",
            "likelihood": 3,
            "impact": 5,
            "risk_score": 15,
            "severity": "Critical",
            "mitigation": "Apply least privilege IAM policies"
        })

    if not aws.get("api_gateway_auth"):
        threats.append({
            "category": "Spoofing",
            "threat": "Unauthenticated API Gateway endpoints",
            "likelihood": 4,
            "impact": 3,
            "risk_score": 12,
            "severity": "High",
            "mitigation": "Enable IAM, Cognito, or Lambda authorizers"
        })

    if aws.get("security_groups_open"):
        threats.append({
            "category": "Tampering",
            "threat": "Security Groups allow unrestricted inbound traffic",
            "likelihood": 4,
            "impact": 4,
            "risk_score": 16,
            "severity": "Critical",
            "mitigation": "Restrict inbound rules and use VPC security controls"
        })

    return threats




