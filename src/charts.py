# charts.py

# Purpose:

# Generate visualizations from Gold Layer datasets.

#

# Output:

# reports/charts/

# ├── language_repo_count.png

# ├── avg_stars_by_language.png

# ├── avg_forks_by_language.png

# └── top_topics.png

from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

# Create charts folder if it doesn't exist.

Path("reports/charts").mkdir(
parents=True,
exist_ok=True
)

# Load Gold Layer datasets.

language_metrics = pd.read_parquet(
"data/gold/language_metrics.parquet"
)

topic_metrics = pd.read_parquet(
"data/gold/topic_metrics.parquet"
)

# --------------------------------------------------

# Chart 1 - Repository Count by Language

# --------------------------------------------------

top_languages = (
language_metrics
.sort_values(
"repo_count",
ascending=False
)
.head(10)
)

plt.figure(figsize=(10, 6))
plt.bar(
top_languages["language"],
top_languages["repo_count"]
)

plt.title("Repository Count by Language")
plt.xlabel("Language")
plt.ylabel("Repository Count")

plt.tight_layout()

plt.savefig(
"reports/charts/language_repo_count.png"
)

plt.close()

# --------------------------------------------------
# Chart 2 - Total Stars by Language
# --------------------------------------------------

top_stars = (
language_metrics
.sort_values(
"total_stars",
ascending=False
)
.head(10)
)

plt.figure(figsize=(10, 6))
plt.bar(
top_stars["language"],
top_stars["total_stars"]
)

plt.title("Total Stars by Language")
plt.xlabel("Language")
plt.ylabel("Total Stars")

plt.tight_layout()

plt.savefig(
"reports/charts/total_stars_by_language.png"
)

plt.close()

# --------------------------------------------------
# Chart 3 - Total Forks by Language
# --------------------------------------------------

top_forks = (
language_metrics
.sort_values(
"total_forks",
ascending=False
)
.head(10)
)

plt.figure(figsize=(10, 6))
plt.bar(
top_forks["language"],
top_forks["total_forks"]
)

plt.title("Total Forks by Language")
plt.xlabel("Language")
plt.ylabel("Total Forks")

plt.tight_layout()

plt.savefig(
"reports/charts/total_forks_by_language.png"
)

plt.close()


# --------------------------------------------------
# Chart 4 - Average Stars by Language
# --------------------------------------------------

top_stars = (
language_metrics
.sort_values(
"avg_stars",
ascending=False
)
.head(10)
)

plt.figure(figsize=(10, 6))
plt.bar(
top_stars["language"],
top_stars["avg_stars"]
)

plt.title("Average Stars by Language")
plt.xlabel("Language")
plt.ylabel("Average Stars")

plt.tight_layout()

plt.savefig(
"reports/charts/avg_stars_by_language.png"
)

plt.close()

# --------------------------------------------------
# Chart 5 - Average Forks by Language
# --------------------------------------------------

top_forks = (
language_metrics
.sort_values(
"avg_forks",
ascending=False
)
.head(10)
)

plt.figure(figsize=(10, 6))
plt.bar(
top_forks["language"],
top_forks["avg_forks"]
)

plt.title("Average Forks by Language")
plt.xlabel("Language")
plt.ylabel("Average Forks")

plt.tight_layout()

plt.savefig(
"reports/charts/avg_forks_by_language.png"
)

plt.close()

# --------------------------------------------------
# Chart 6 - Top Topics
# --------------------------------------------------

top_topics = topic_metrics.head(10)

plt.figure(figsize=(10, 6))
plt.bar(
top_topics["topic"],
top_topics["repo_count"]
)

plt.title("Most Common GitHub Topics")
plt.xlabel("Topic")
plt.ylabel("Repository Count")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
"reports/charts/top_topics.png"
)

plt.close()

print("Charts generated successfully.")
