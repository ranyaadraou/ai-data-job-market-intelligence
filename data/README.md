# Data

The large raw and intermediate datasets used by this project are not committed to GitHub.

The analytical workflow references datasets such as:

- `final_data_ai_jobs_clean_2020_2026.csv`
- `final_data_ai_jobs_clean_reduced_2020_2026.csv`
- `final_data_ai_jobs_skills_exploded.csv`
- `final_data_ai_jobs_content_enriched.csv`
- `final_data_ai_jobs_skills_exploded_enriched.csv`
- `google_trends_data.csv`
- quality-analysis exports
- graph-analysis exports
- forecasting exports

The consolidated project dataset contains 751,801 Data & AI job offers.

## Why the datasets are excluded

The raw and intermediate files are large and originate from multiple public datasets, APIs and collected web sources. Keeping them outside the repository makes the Git history lighter and avoids redistributing source data without checking the corresponding source terms.

## Local setup

Place the required local datasets in this directory, or adapt the notebook paths to your local data location.

The MongoDB notebook can also use the environment variable:

```text
WEBMINING_DATA_DIR
```

Example in PowerShell:

```powershell
$env:WEBMINING_DATA_DIR="C:\path\to\your\dataset_WebMining"
```
