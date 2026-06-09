import pandas as pd

df = pd.read_parquet(
    "data/processed/github_repos_clean.parquet"
)

print("Columns:")
print(df.columns.tolist())

print("\nFirst 5 Records:")
print(df.head())

