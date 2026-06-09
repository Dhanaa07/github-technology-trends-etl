# analyze.py
# Purpose:
# Read the Silver Layer dataset and generate business metrics
# for language trends, repository popularity, and technology topics.

# Outputs:
# - language_metrics.parquet
# - topic_metrics.parquet
# - top_repositories.parquet
# - analysis_summary.txt

from pathlib import Path
import pandas as pd

# Create Gold layer folder if it doesn't exist.
Path("data/gold").mkdir(parents=True, exist_ok=True)

# Create charts folder for future visualizations.
Path("reports/charts").mkdir(parents=True, exist_ok=True)

# --------------------------------------------------
# Load Silver Layer Dataset
# --------------------------------------------------

print("Loading Silver Layer dataset...")
df = pd.read_parquet(
"data/processed/github_repos_clean.parquet"
)
print(f"Records Loaded: {len(df)}")

# --------------------------------------------------
# Gold Layer 1 - Language Metrics
# --------------------------------------------------

# Calculate:
# - Repository count per language
# - total stars per language
# - Average stars per language
# - total forks per language
# - Average forks per language

language_metrics = (
df.groupby("language")
.agg(
repo_count=("repo_name", "count"),
total_stars=("stars", "sum"),
avg_stars=("stars", "mean"),
total_forks=("forks", "sum"),
avg_forks=("forks", "mean")
)
.reset_index()
)

# Round numeric values for readability.
language_metrics["avg_stars"] = (
language_metrics["avg_stars"].round(2)
)

language_metrics["avg_forks"] = (
language_metrics["avg_forks"].round(2)
)

# Save Gold dataset.
language_metrics.to_parquet(
"data/gold/language_metrics.parquet",
index=False
)

print("Language metrics saved.")

# --------------------------------------------------
# Gold Layer 2 - Top Repositories
# --------------------------------------------------

# Top repositories ranked by stars.
top_repositories = (
df.sort_values(
by="stars",
ascending=False
)
.head(10)
)

top_repositories.to_parquet(
"data/gold/top_repositories.parquet",
index=False
)

print("Top repositories saved.")

# --------------------------------------------------
# Gold Layer 3 - Topic Metrics
# --------------------------------------------------

# Topics are currently stored as:
# "ai,llm,agent"

# Split them into individual topics and count frequency.

all_topics = []

for topic_string in df["topics"]:
    if pd.notna(topic_string):

        topics = topic_string.split(",")
        for topic in topics:
            topic = topic.strip()
            if topic and topic != "No topics":
                all_topics.append(topic)

topic_metrics = (
pd.Series(all_topics)
.value_counts()
.reset_index()
)

topic_metrics.columns = [
"topic",
"repo_count"
]

topic_metrics.to_parquet(
"data/gold/topic_metrics.parquet",
index=False
)

print("Topic metrics saved.")

# --------------------------------------------------
# Analysis Summary Report
# --------------------------------------------------

most_common_language = (
language_metrics.sort_values(
"repo_count",
ascending=False
)
.iloc[0]
)

highest_star_language = (
language_metrics.sort_values(
"avg_stars",
ascending=False
)
.iloc[0]
)

most_common_topic = (
topic_metrics.iloc[0]
if len(topic_metrics) > 0
else None
)

with open(
    "reports/analysis_summary.txt",
    "w",
    encoding="utf-8"
) as f:
    f.write("GITHUB TECHNOLOGY TRENDS ANALYSIS\n")
    f.write("=" * 60)

    f.write(
        f"\n\nTotal Repositories Analyzed: {len(df)}"
    )

    f.write(
        f"\nMost Common Language: "
        f"{most_common_language['language']}"
    )

    f.write(
        f"\nRepositories Using Language: "
        f"{most_common_language['repo_count']}"
    )

    f.write(
        f"\nHighest Average Stars: "
        f"{highest_star_language['language']}"
    )
    
    f.write(
        f"\nAverage Stars: "
        f"{highest_star_language['avg_stars']}"
    )

    if most_common_topic is not None:

        f.write(
            f"\nMost Common Topic: "
            f"{most_common_topic['topic']}"
        )

        f.write(
            f"\nTopic Frequency: "
            f"{most_common_topic['repo_count']}"
        )


print("Analysis summary saved.")

# --------------------------------------------------
# Console Preview
# --------------------------------------------------

print("\nTop Languages:")
print(
language_metrics.sort_values(
"repo_count",
ascending=False
).head()
)

print("\nTop Topics:")
print(topic_metrics.head())

print("\nAnalysis Complete.")
