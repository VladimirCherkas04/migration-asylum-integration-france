import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

integration = pd.read_csv(
    BASE_DIR / "integration_support.csv"
)

# 1. Programs
programs = (
    integration["program"]
    .value_counts()
    .reset_index()
)

programs.columns = ["program", "participants"]

print("PROGRAMS")
print(programs)

# 2. Completion rate by program
completion = (
    integration
    .groupby("program")["completed"]
    .apply(lambda x: (x == "Yes").mean() * 100)
    .round(2)
    .sort_values(ascending=False)
)

print("\nCOMPLETION RATE BY PROGRAM")
print(completion)

# 3. Employment outcomes
outcomes = (
    integration["employment_outcome"]
    .value_counts()
    .reset_index()
)

outcomes.columns = ["employment_outcome", "count"]

print("\nEMPLOYMENT OUTCOMES")
print(outcomes)

# 4. Employment outcome rate by program
employment_rate = (
    integration
    .groupby("program")["employment_outcome"]
    .apply(lambda x: (x == "Employed").mean() * 100)
    .round(2)
    .sort_values(ascending=False)
)

print("\nEMPLOYMENT OUTCOME RATE BY PROGRAM")
print(employment_rate)

# 5. Employment outcome by education
education_outcome = (
    integration
    .groupby("education_level")["employment_outcome"]
    .apply(lambda x: (x == "Employed").mean() * 100)
    .round(2)
    .sort_values(ascending=False)
)

print("\nEMPLOYMENT OUTCOME RATE BY EDUCATION")
print(education_outcome)