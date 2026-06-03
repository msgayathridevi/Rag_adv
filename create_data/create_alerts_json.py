import json
import os

os.makedirs("data/logs", exist_ok=True)

alerts = [
    {
        "alert": "CPU usage high",
        "server": "server-1",
        "severity": "critical"
    },
    {
        "alert": "Disk usage exceeded threshold",
        "server": "server-2",
        "severity": "warning"
    }
]

with open("data/logs/alerts.json", "w") as f:
    json.dump(alerts, f, indent=4)

print("alerts.json created")