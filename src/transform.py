#bronze - raw json
#select useful fields
#flatten nested columns
#rename columns for clarity
#handle missing values
#remove duplicates
#create derived columns
#save as parquet for efficient storage and analysis -> silver layer

import json
from pathlib import Path
from datetime import datetime

import pandas as pd

# Create processed data folder if it doesn't exist.
Path("data/processed").mkdir(parents=True, exist_ok=True)

# Read raw GitHub API response generated during the Extract phase.
with open(
    "data/raw/github_repos_raw.json",
    "r",
    encoding="utf-8"
) as f:
    data = json.load(f)

# Store transformed repository records.
repos = []

# Iterate through all repositories returned by GitHub.
for repo in data["items"]:

 repos.append({

    # Repository name
    "repo_name": repo["name"],

    # Flatten nested owner object
    "owner": repo["owner"]["login"],

    # Programming language
    "language": repo["language"],

    # Popularity metric
    "stars": repo["stargazers_count"],

    # Community adoption metric
    "forks": repo["forks_count"],

    # Convert list of topics into comma-separated text
    "topics": ",".join(repo["topics"])
    if repo["topics"] else None,

    # Repository description
    "description": repo["description"],

    # Repository creation date
    "created_at": repo["created_at"],

    # Repository URL
    "repo_url": repo["html_url"]
 })

# Convert repository records into a Pandas DataFrame.
df = pd.DataFrame(repos)

print("Initial Record Count:", len(df))

# --------------------------------------------------
# Data Quality Checks & Cleaning
# --------------------------------------------------

# Remove records with missing language values.

# Language is required for trend analysis.
df = df.dropna(subset=["language"])

# Remove duplicate repositories if any exist.
df = df.drop_duplicates()

# Replace missing descriptions with a placeholder.
df["description"] = df["description"].fillna(
"No description provided"
)

# Replace missing topics with a placeholder.
df["topics"] = df["topics"].fillna(
"No topics"
)

# Convert created_at from text to datetime.
df["created_at"] = pd.to_datetime(df["created_at"])

# --------------------------------------------------
# Derived Columns
# --------------------------------------------------

# Calculate repository age in days.
today = pd.Timestamp.now(tz="UTC")

df["repo_age_days"] = (
today - df["created_at"]
).dt.days

# Calculate star-to-fork ratio.
# Indicates popularity relative to community contribution.
df["star_fork_ratio"] = (
df["stars"] /
(df["forks"] + 1)
).round(2)

# Flag highly popular repositories.
df["viral_repo"] = df["stars"].apply(
lambda x: "Yes" if x >= 50000 else "No"
)

print("Final Record Count:", len(df))

# --------------------------------------------------
# Save Silver Layer Dataset
# --------------------------------------------------

output_file = (
"data/processed/github_repos_clean.parquet"
)

df.to_parquet(
output_file,
index=False
)

print(
f"Silver layer dataset saved to: {output_file}"
)

# --------------------------------------------------
# Data Quality Report
# --------------------------------------------------

with open(
    "reports/data_quality_report.txt",
    "w",
    encoding="utf-8"
) as f:


    f.write("DATA QUALITY REPORT\n")
    f.write("=" * 50)

    f.write(
        f"\n\nTotal Records: {len(repos)}"
    )

    f.write(
        f"\nRecords After Cleaning: {len(df)}"
    )

    f.write(
        f"\nMissing Languages Removed: "
        f"{pd.DataFrame(repos)['language'].isna().sum()}"
    )

    f.write(
        f"\nDuplicate Records Removed: "
        f"{len(pd.DataFrame(repos)) - len(pd.DataFrame(repos).drop_duplicates())}"
    )

print(
"Data quality report saved to reports/data_quality_report.txt"
)
