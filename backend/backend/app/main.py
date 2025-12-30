import json
from stride import generate_threat_model

def main():
    with open("../../examples/sample_system.json") as f:
        system = json.load(f)

    threats = generate_threat_model(system)

    print(f"\n=== Threat Model for {system['system_name']} ===\n")

    for item in threats:
        print(f"[{item['category']}] {item['threat']}")
        print(f"Risk Level : {item['risk']}")
        print(f"Mitigation : {item['mitigation']}\n")

if __name__ == "__main__":
    main()

