import json
from pathlib import Path


def load_jsons(json_folder="data/logs"):

    documents = []

    for json_file in Path(json_folder).glob("*.json"):

        with open(json_file, "r") as f:
            data = json.load(f)

        documents.append(
            {
                "content": json.dumps(data, indent=2),
                "source": json_file.name,
                "source_type": "json"
            }
        )

    return documents