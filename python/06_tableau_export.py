import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "tableau_data"

OUTPUT_DIR.mkdir(exist_ok=True)

migration = pd.read_csv(BASE_DIR / "migration_records.csv")
asylum = pd.read_csv(BASE_DIR / "asylum_cases.csv")
integration = pd.read_csv(BASE_DIR / "integration_support.csv")
regions = pd.read_csv(BASE_DIR / "regions.csv")


# 1. Migration by year

migration["year"] = pd.to_datetime(
    migration["date"]
).dt.year

migration_year = (
    migration
    .groupby("year")
    .agg(
        records=("record_id", "count"),
        employed=("employment_status",
                   lambda x: (x == "Employed").sum())
    )
    .reset_index()
)

migration_year["employment_rate"] = (
    migration_year["employed"]
    / migration_year["records"]
    * 100
).round(2)

migration_year.to_csv(
    OUTPUT_DIR / "migration_by_year.csv",
    index=False
)


# 2. Migration by region

migration_region = (
    migration
    .groupby("region_id")
    .agg(
        records=("record_id", "count"),
        employed=("employment_status",
                   lambda x: (x == "Employed").sum())
    )
    .reset_index()
)

migration_region["employment_rate"] = (
    migration_region["employed"]
    / migration_region["records"]
    * 100
).round(2)

migration_region = migration_region.merge(
    regions[["region_id", "region", "main_city"]],
    on="region_id"
)

migration_region.to_csv(
    OUTPUT_DIR / "migration_by_region.csv",
    index=False
)


# 3. Asylum by decision

asylum_decisions = (
    asylum["decision"]
    .value_counts()
    .reset_index()
)

asylum_decisions.columns = ["decision", "cases"]

asylum_decisions["share_percent"] = (
    asylum_decisions["cases"]
    / asylum_decisions["cases"].sum()
    * 100
).round(2)

asylum_decisions.to_csv(
    OUTPUT_DIR / "asylum_decisions.csv",
    index=False
)


# 4. Asylum by region

asylum_region = (
    asylum
    .groupby("region_id")
    .agg(
        cases=("case_id", "count"),
        accepted=("decision",
                  lambda x: (x == "Accepted").sum())
    )
    .reset_index()
)

asylum_region["acceptance_rate"] = (
    asylum_region["accepted"]
    / asylum_region["cases"]
    * 100
).round(2)

asylum_region = asylum_region.merge(
    regions[["region_id", "region", "main_city"]],
    on="region_id"
)

asylum_region.to_csv(
    OUTPUT_DIR / "asylum_by_region.csv",
    index=False
)


# 5. Integration programs

integration_programs = (
    integration
    .groupby("program")
    .agg(
        participants=("support_id", "count"),
        completed=("completed",
                   lambda x: (x == "Yes").sum()),
        employed=("employment_outcome",
                  lambda x: (x == "Employed").sum())
    )
    .reset_index()
)

integration_programs["completion_rate"] = (
    integration_programs["completed"]
    / integration_programs["participants"]
    * 100
).round(2)

integration_programs["employment_rate"] = (
    integration_programs["employed"]
    / integration_programs["participants"]
    * 100
).round(2)

integration_programs.to_csv(
    OUTPUT_DIR / "integration_programs.csv",
    index=False
)


print("TABLEAU EXPORT COMPLETE")
print(f"Files saved to: {OUTPUT_DIR}")
print("\nCreated files:")

for file in OUTPUT_DIR.glob("*.csv"):
    print(file.name)