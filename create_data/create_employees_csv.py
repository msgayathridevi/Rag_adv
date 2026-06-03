import pandas as pd
import os

os.makedirs("data/csv", exist_ok=True)

df = pd.DataFrame([
    [1, "John", "Engineering", 90000],
    [2, "Alice", "Finance", 120000],
    [3, "Bob", "HR", 80000]
], columns=["employee_id", "name", "department", "salary"])

df.to_csv("data/csv/employees.csv", index=False)

print("employees.csv created")