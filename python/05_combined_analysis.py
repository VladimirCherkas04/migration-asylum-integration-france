import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

migration = pd.read_csv(BASE_DIR / "migration_records.csv")
asylum = pd.read_csv(BASE_DIR / "asylum_cases.csv")
integration = pd.read_csv(BASE_DIR / "integration_support.csv")
regions = pd.read_csv(BASE_DIR / "regions.csv")


# 1. Migration employment by region

migration_region = (
    migration
    .groupby("region_id")
    .agg(
        records=("record_id", "count"),
        employed=("employment_status", lambda x: (x == "Employed").sum())
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

print("MIGRATION EMPLOYMENT BY REGION")
print(
    migration_region[
        ["region", "main_city", "records", "employment_rate"]
    ]
    .sort_values("employment_rate", ascending=False)
)


# 2. Asylum acceptance by region

asylum_region = (
    asylum
    .groupby("region_id")
    .agg(
        cases=("case_id", "count"),
        accepted=("decision", lambda x: (x == "Accepted").sum())
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

print("\nASYLUM ACCEPTANCE BY REGION")
print(
    asylum_region[
        ["region", "main_city", "cases", "acceptance_rate"]
    ]
    .sort_values("acceptance_rate", ascending=False)
)


# 3. Integration employment outcome

integration_summary = (
    integration
    .groupby("program")
    .agg(
        participants=("support_id", "count"),
        employed=("employment_outcome", lambda x: (x == "Employed").sum()),
        completed=("completed", lambda x: (x == "Yes").sum())
    )
    .reset_index()
)

integration_summary["employment_rate"] = (
    integration_summary["employed"]
    / integration_summary["participants"]
    * 100
).round(2)

integration_summary["completion_rate"] = (
    integration_summary["completed"]
    / integration_summary["participants"]
    * 100
).round(2)

print("\nINTEGRATION PROGRAM SUMMARY")
print(
    integration_summary.sort_values(
        "employment_rate",
        ascending=False
    )
)


# 4. Overall project indicators

overall_migration_employment = (
    (migration["employment_status"] == "Employed").mean() * 100
)

overall_asylum_acceptance = (
    (asylum["decision"] == "Accepted").mean() * 100
)

overall_integration_employment = (
    (integration["employment_outcome"] == "Employed").mean() * 100
)

print("\nOVERALL INDICATORS")

print(
    f"Migration employment rate: "
    f"{overall_migration_employment:.2f}%"
)

print(
    f"Asylum acceptance rate: "
    f"{overall_asylum_acceptance:.2f}%"
)

print(
    f"Integration employment outcome rate: "
    f"{overall_integration_employment:.2f}%"
)