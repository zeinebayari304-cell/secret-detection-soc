import json
from datetime import datetime

alert = {
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "severity": "HIGH",
    "type": "Exposed Secret Detected",
    "source": "GitHub Actions + GitLeaks",
    "description": "Un secret a été détecté dans le code source.",
    "status": "Open"
}

with open("soc_alerts.json", "w", encoding="utf-8") as file:
    json.dump([alert], file, indent=4)

print("Alerte SOC générée avec succès.")