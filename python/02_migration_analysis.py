import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

migration = pd.read_csv(BASE_DIR / "migration_records.csv")

# 1. Employment status
employment = (
    migration["employment_status"]
    .value_counts()
    .reset_index()
)

employment.columns = ["employment_status", "count"]

print("EMPLOYMENT STATUS")
print(employment)

# 2. Activity types
activities = (
    migration["activity_type"]
    .value_counts()
    .reset_index()
)

activities.columns = ["activity_type", "count"]

print("\nACTIVITY TYPES")
print(activities)

# 3. Education and employment
education_employment = (
    migration
    .groupby("education_level")["employment_status"]
    .value_counts()
    .unstack(fill_value=0)
)

print("\nEDUCATION × EMPLOYMENT")
print(education_employment)

# 4. Employment rate by education
employment_rate = (
    migration
    .groupby("education_level")["employment_status"]
    .apply(lambda x: (x == "Employed").mean() * 100)
    .round(2)
    .sort_values(ascending=False)
)

print("\nEMPLOYMENT RATE BY EDUCATION")
print(employment_rate)