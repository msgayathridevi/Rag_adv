import pandas as pd
import os

os.makedirs("data/csv", exist_ok=True)

df = pd.DataFrame([
    ["India", 100000],
    ["USA", 300000],
    ["Europe", 200000]
], columns=["region", "revenue"])

df.to_csv("data/csv/sales.csv", index=False)

print("sales.csv created")