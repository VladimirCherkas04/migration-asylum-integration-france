import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

asylum = pd.read_csv(BASE_DIR / "asylum_cases.csv")

# 1. Decisions
decisions = (
    asylum["decision"]
    .value_counts()
    .reset_index()
)

decisions.columns = ["decision", "count"]

print("ASYLUM DECISIONS")
print(decisions)

# 2. Decision shares
decision_share = (
    asylum["decision"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
    .reset_index()
)

decision_share.columns = ["decision", "share_percent"]

print("\nDECISION SHARES")
print(decision_share)

# 3. Countries of citizenship
citizenship = (
    asylum["country_of_citizenship"]
    .value_counts()
    .reset_index()
)

citizenship.columns = ["country_of_citizenship", "cases"]

print("\nTOP COUNTRIES OF CITIZENSHIP")
print(citizenship.head(10))

# 4. Protection type
protection = (
    asylum["protection_type"]
    .value_counts(dropna=False)
    .reset_index()
)

protection.columns = ["protection_type", "cases"]

print("\nPROTECTION TYPES")
print(protection)

# 5. Acceptance rate by age group
age_acceptance = (
    asylum
    .groupby("age_group")["decision"]
    .apply(lambda x: (x == "Accepted").mean() * 100)
    .round(2)
    .sort_values(ascending=False)
)

print("\nACCEPTANCE RATE BY AGE GROUP")
print(age_acceptance)