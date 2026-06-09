# GitHub Technology Trends ETL Pipeline

## Overview

This project is an end-to-end ETL pipeline that collects repository data from the GitHub Search API, transforms it into an analytics-ready format, and generates insights about programming language popularity, repository engagement, and technology trends.

The goal of the project is to demonstrate core Data Engineering concepts including API data extraction, schema inspection, data transformation, data quality checks, aggregation, Parquet storage, and analytics reporting.

---

## Architecture

GitHub API
↓
Raw JSON (Bronze Layer)
↓
Schema Inspection
↓
Data Cleaning & Transformation
↓
Parquet Dataset (Silver Layer)
↓
Aggregations & Business Metrics
↓
Gold Layer
↓
Reports & Visualizations

---

## Project Structure

github-technology-trends-etl/

data/

* raw/

  * github_repos_raw.json
* processed/

  * github_repos_clean.parquet
* gold/

  * language_metrics.parquet
  * topic_metrics.parquet
  * top_repositories.parquet

src/

* extract.py
* inspect_schema.py
* transform.py
* analyse.py
* charts.py

reports/

* schema_summary.txt
* data_quality_report.txt
* analysis_summary.txt
* charts/

README.md
requirements.txt

---

## ETL Workflow

### Extract

Repository data is collected from the GitHub Search API using Python Requests.

The raw API response is stored as JSON in the Bronze Layer for reproducibility and auditing.

### Inspect

The API schema is explored to understand available fields, nested structures, and data types.

A schema report is generated to support transformation design.

### Transform

The raw JSON data is converted into a Pandas DataFrame and transformed into a clean analytics-ready dataset.

Transformations include:

* Selecting relevant fields
* Flattening nested owner objects
* Renaming columns
* Handling missing values
* Removing duplicates
* Creating derived metrics
* Saving as Parquet

Derived metrics:

* repo_age_days
* star_fork_ratio
* viral_repo

### Analyze

The Silver Layer dataset is aggregated into Gold Layer datasets.

Metrics include:

* Repository count by language
* Total stars by language
* Average stars by language
* Total forks by language
* Average forks by language
* Most common technology topics
* Top repositories by stars

---

## Technologies Used

* Python
* Requests
* Pandas
* PyArrow
* Matplotlib
* GitHub REST API
* Parquet

---

## Sample Insights

Insights will vary depending on the collection date.

Example findings from a recent run:

* Python was the most common language among analyzed repositories.
* TypeScript ranked second in repository count.
* Rust achieved one of the highest average star counts.
* AI-related topics such as Claude Code, AI Agents, and LLMs appeared frequently among trending repositories.
* Python generated the highest overall repository volume and community engagement.

---

## Visualizations

The pipeline automatically generates charts including:

* Repository Count by Language
* Total Stars by Language
* Total Forks by Language
* Average Stars by Language
* Average Forks by Language
* Top GitHub Topics

Generated charts are stored in:

reports/charts/

---

## Future Improvements

* GitHub API pagination to collect larger datasets
* Historical trend tracking
* DuckDB integration
* Delta Lake integration
* Automated scheduling with Airflow
* Interactive dashboards using Power BI or Streamlit

---

## Learning Outcomes

This project helped me practice:

* API-based data ingestion
* JSON schema exploration
* Data transformation using Pandas
* Parquet-based data storage
* Data quality validation
* Analytical aggregations
* Data visualization
* End-to-end ETL pipeline development
