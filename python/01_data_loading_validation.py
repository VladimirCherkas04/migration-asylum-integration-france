import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

migration = pd.read_csv(BASE_DIR / "migration_records.csv")
asylum = pd.read_csv(BASE_DIR / "asylum_cases.csv")
integration = pd.read_csv(BASE_DIR / "integration_support.csv")
regions = pd.read_csv(BASE_DIR / "regions.csv")

print("MIGRATION")
print(migration.shape)
print(migration.head())

print("\nASYLUM")
print(asylum.shape)
print(asylum.head())

print("\nINTEGRATION")
print(integration.shape)
print(integration.head())

print("\nREGIONS")
print(regions.shape)
print(regions.head())

print("\nMISSING VALUES — MIGRATION")
print(migration.isna().sum())

print("\nMISSING VALUES — ASYLUM")
print(asylum.isna().sum())

print("\nMISSING VALUES — INTEGRATION")
print(integration.isna().sum())

print("\nMISSING VALUES — REGIONS")
print(regions.isna().sum())