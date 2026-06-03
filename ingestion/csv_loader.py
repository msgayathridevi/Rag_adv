import pandas as pd
from pathlib import Path


def load_csvs(csv_folder="data/csv"):

    documents = []

    for csv_file in Path(csv_folder).glob("*.csv"):

        df = pd.read_csv(csv_file)

        text = df.to_string(index=False)

        documents.append(
            {
                "content": text,
                "source": csv_file.name,
                "source_type": "csv"
            }
        )

    return documents