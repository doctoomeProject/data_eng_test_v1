# 🧠 Data Engineering Technical Test

## 🎯 Objective
The purpose of this challenge is to demonstrate your end-to-end data engineering and analytical skills.
You will design a small but complete data pipeline — from sourcing heterogeneous data to cleaning, transforming, merging, and finally analyzing it — all within a reproducible Dockerized environment.

Specifically, this test will assess your ability to:

1 - Source data from multiple file types and locations (CSV, TXT, Parquet, remote URLs, and S3).
2 - Understand and clean complex data structures, handling missing, inconsistent, or duplicated entries.
3 - Write clean, modular, and functional code with appropriate documentation and organization.
4 - Monitor and analyze data quality using reproducible metrics and visualizations.
5 - Containerize your project for local execution using Docker.
6 - Version your work effectively on GitHub.

## Preparation
To avoid constrains during the 1h interview, the following steps can be done prior:

- Setup a Git Repository for your code.
- Access the data and inspect the formats
- Setup your environment
- # ENSURE EVERY HELPER (Copilot, ChatGPT, etc... is disabled)

## Data

### 📦 Data Sources

| Dataset          | Description                   | Location                                                                                          |
| ---------------- | ----------------------------- | ------------------------------------------------------------------------------------------------- |
| `CIS_bdpm`       | Medicinal product reference   | `s3://data-eng-interviews/CIS_bdpm.txt`                                                           |
| `CIS_CIP_bdpm`   | Product packaging and codes   | `s3://data-eng-interviews/CIS_CIP_bdpm.parquet`                                                   |
| `CIS_COMPO_bdpm` | Product composition details   | `s3://data-eng-interviews/CIS_COMPO_bdpm.csv`                                                     |
| `CIS_CPD_bdpm`   | Public medication information | `https://base-donnees-publique.medicaments.gouv.fr/download/file/CIS_CPD_bdpm.txt`                |


## 🧩 Main Task
You must clean, transform, and merge the four datasets into a single consolidated table.
Once the final table is ready, upload it to:
`s3://data-eng-interviews/results/{your_name}/`

Your code should be structured, efficient, and easily reproducible.

## 📊 Dashboard Requirements
Develop a 3-chart dashboard to perform data quality analysis.
The dashboard should enable monitoring of key metrics such as:
1. Missing Values – Track the evolution of missing data across columns or datasets.
2. Unmerged Rows – Quantify records that could not be matched during the merging process.
3. Duplicate Entries – Detect and analyze duplication patterns in the datasets.

🧭 The dashboard can be developed within a Jupyter Notebook, and it should be able to read from pre-computed intermediate files if needed.

## ⚙️ Deliverables & Execution
Package your full project in a local Docker container.

Include a Dockerfile or docker-compose.yml that builds and runs the pipeline.

Develop your dashboard inside a notebook that can be executed after the pipeline runs.

At the end of the interview, you’ll be asked to:

Push your code into setup repithub.

Run the container to generate the final dataset.

Execute the notebook cells to display your dashboard.

💡 Tip: You may persist intermediate outputs (e.g., CSV or Parquet files) for reuse within the dashboard.

## Data Linkage Chart

The following diagram illustrates the intended relationship between the different data sources:

![alt text](image.png)

## ✅ Evaluation Criteria

| Category                           | Description                                           |
| ---------------------------------- | ----------------------------------------------------- |
| **Data Sourcing**                  | Ability to handle multiple formats and remote sources |
| **Data Cleaning & Transformation** | Quality, logic, and robustness of preprocessing       |
| **Code Structure & Readability**   | Clarity, modularity, and documentation                |
| **Data Analysis & Visualization**  | Quality of dashboard insights and readability         |
| **Reproducibility**                | Dockerization and ease of setup/run                   |
| **Version Control**                | Commit quality, branching, and GitHub organization    |
