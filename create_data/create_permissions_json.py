import json
import os

os.makedirs("data/metadata", exist_ok=True)

permissions = {
    "admin": ["all"],
    "hr": ["hr_documents"],
    "finance": ["finance_documents"],
    "employee": ["public_documents"]
}

with open("data/metadata/permissions.json", "w") as f:
    json.dump(permissions, f, indent=4)

print("permissions.json created")