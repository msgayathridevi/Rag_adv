import json
import os

os.makedirs("data/logs", exist_ok=True)

logs = [
    {
        "user": "john",
        "action": "login",
        "status": "success"
    },
    {
        "user": "alice",
        "action": "download_report",
        "status": "success"
    }
]

with open("data/logs/audit_logs.json", "w") as f:
    json.dump(logs, f, indent=4)

print("audit_logs.json created")