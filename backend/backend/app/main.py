import json
from stride import generate_threat_model

def main():
    with open("../../examples/sample_system.json") as f:
        system = json.load(f)

    threats = generate_threat_model(system)

    print(f"\n=== Threat Model for {system['system_name']} ===\n")

    for item in threats:
        print(f"[{item['category']}] {item['threat']}")
        print(f"Likelihood: {item['likelihood']}")
        print(f"Impact: {item['impact']}")
        print(f"Risk Score: {item['risk_score']} ({item['risk']})")
        print(f"Mitigation: {item['mitigation']}\n")

if __name__ == "__main__":
    main()


