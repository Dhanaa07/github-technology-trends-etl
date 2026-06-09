# inspect_schema.py

# Purpose:
# Explore the GitHub API response structure before transformation.

# Before transforming the raw JSON data, it is important to understand:
# - What fields are available
# - How the data is organized
# - Which fields are nested
# - Which fields are useful for analysis

# This helps design the target dataset and select only the attributes required for repository trend analysis.

import json
from pathlib import Path

# Create reports folder if it doesn't already exist.
# This folder will store schema and analysis reports generated
# during the project.
Path("reports").mkdir(exist_ok=True)

# Read the raw JSON response saved during the Extract phase.
# The file contains the original API response from GitHub.
with open(
    "data/raw/github_repos_raw.json",
    "r",
    encoding="utf-8"
) as f:
    data = json.load(f)

# Extract schema information from the JSON response.

# Top-level keys describe the overall API response structure.
top_level_keys = list(data.keys())

# Repository fields describe the attributes available
# for each repository returned by GitHub.
repo_fields = list(data["items"][0].keys())

# Owner fields describe the nested structure inside
# the repository owner object.
owner_fields = list(data["items"][0]["owner"].keys())

# Display schema information in the console.
print("=" * 60)
print("GITHUB API SCHEMA INSPECTION")
print("=" * 60)

print("\nTop Level Keys:")
print(top_level_keys)

print("\nRepository Fields:")
print(repo_fields)

print("\nOwner Fields:")
print(owner_fields)

# Save schema information to a report file.
# This provides documentation of the API structure
# and helps explain transformation decisions later.
with open(
    "reports/schema_summary.txt",
    "w",
    encoding="utf-8"
) as f:

    f.write("GITHUB API SCHEMA SUMMARY\n")
    f.write("=" * 50)

    f.write("\n\nTop Level Keys:\n")
    for key in top_level_keys:
        f.write(f"- {key}\n")

    f.write("\nRepository Fields:\n")
    for field in repo_fields:
        f.write(f"- {field}\n")

    f.write("\nOwner Fields:\n")
    for field in owner_fields:
        f.write(f"- {field}\n")

print("\nSchema summary saved to:")
print("reports/schema_summary.txt")

# Next Step:
# Review the generated schema report and decide which fields
# should be included in the transformed analytical dataset.