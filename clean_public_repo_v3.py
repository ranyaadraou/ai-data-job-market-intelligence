from __future__ import annotations

import shutil
from pathlib import Path

TITLE = "CLEAN PUBLIC GITHUB REPOSITORY"

README = """# AI & Data Job Market Intelligence

Academic Web Mining project developed at ENSA Tetouan to study the Data & AI job market from large-scale job-offer data.

The project works with **751,801 job offers from 2020 to 2026**. The goal was to clean and structure the data, analyse the most requested skills, explore relationships between technologies, study market trends and present the results in a Power BI dashboard.

## What we worked on

The project is organised as a complete data-analysis pipeline:

1. **Data collection and source analysis**
   - review of the different job-data sources
   - consolidation of the available datasets

2. **Cleaning and data preparation**
   - schema harmonisation
   - missing-value and duplicate checks
   - standardisation of fields used in the analysis

3. **Data quality**
   - validation of temporal, geographic and skills coverage
   - quality checks before the analytical steps

4. **Skills dataset**
   - transformation of job-level records into skill-level observations
   - preparation of the data used for skills analysis

5. **MongoDB**
   - storage of the cleaned job data
   - analytical queries and indexes for the main collections

6. **Web content mining and NLP**
   - processing of job descriptions
   - skill enrichment
   - TF-IDF and text representations
   - sentence embeddings
   - automatic classification of Data & AI job domains

7. **Graph mining**
   - skill co-occurrence network
   - centrality analysis
   - Louvain communities to identify groups of related technologies

8. **Trend analysis and forecasting**
   - Google Trends data collected with `pytrends`
   - comparison of forecasting approaches including Prophet, ARIMA and linear regression

9. **Power BI dashboard**
   - global market overview
   - skills demand
   - future skills and trends
   - Morocco-focused analysis

## Project workflow

```mermaid
flowchart LR
    A[Job data sources] --> B[Cleaning and standardisation]
    B --> C[Data quality]
    C --> D[Skills dataset]
    D --> E[(MongoDB)]
    E --> F[Web content mining]
    F --> G[NLP and embeddings]
    G --> H[Graph analysis]
    H --> I[Trend analysis and forecasting]
    I --> J[Power BI dashboard]
```

## Notebooks

| Notebook | Main work |
|---|---|
| `01_collecte_et_sources.ipynb` | Sources and consolidated data |
| `02_cleaning_fusion_dataset.ipynb` | Cleaning and dataset fusion |
| `03_data_quality_framework_v2.ipynb` | Data-quality analysis |
| `04_creation_dataset_skills_exploded.ipynb` | Skill-level dataset |
| `05_mongodb_storage.ipynb` | MongoDB storage and queries |
| `06_web_content_mining_final_respecte.ipynb` | NLP and content mining |
| `07_web_structure_mining_graph_skills.ipynb` | Graph mining, trends and forecasting |

## Dashboard

### Global overview

![Global overview](demo/global-overview.png)

### Skills demand

![Skills demand](demo/skills-demand.png)

### Future skills

![Future skills](demo/future-skills.png)

### Morocco market

![Morocco market](demo/morocco-market.png)

## Main technologies

- Python
- Pandas / NumPy
- MongoDB / PyMongo
- Scikit-learn
- Sentence Transformers
- NetworkX
- Louvain community detection
- Prophet / ARIMA
- Pytrends
- Power BI

## Data

The large CSV files used during the project are not included in this repository because of their size. The notebooks show the processing steps and the expected datasets used at each stage.

## Report

The complete academic report is available here:

[Web Mining Project Report](docs/rapport-web-mining.pdf)

## Academic context

This project was completed for the **Web Mining (M242)** module at **ENSA Tetouan — Abdelmalek Essaadi University**, during the 2025–2026 academic year.

**Supervisor:** Prof. Imad Sassi

### Team

- Nour El Houda Amaziane
- Ranya Adraou
- Aya Ettalbi
- Ouiame Biloul
"""

GITIGNORE = """# Python
__pycache__/
*.py[cod]

# Virtual environments
.venv/
venv/
env/

# Jupyter
.ipynb_checkpoints/

# IDE / OS
.vscode/
.idea/
.DS_Store
Thumbs.db

# Local configuration
.env
.env.*
!.env.example

# Local datasets and generated data files
data/
*.csv
*.parquet
*.feather

# Local models / temporary outputs
*.pkl
*.pickle
*.joblib
tmp/
temp/

# Preparation backups
_backup_before_github_prepare_*/

# Keep only the report stored in docs/
rapport-web-mining.pdf

# Python packaging
build/
dist/
*.egg-info/
"""


def main() -> None:
    print()
    print(TITLE)
    print("=" * len(TITLE))

    root = Path.cwd()

    required = [
        root / "01_collecte_et_sources.ipynb",
        root / "05_mongodb_storage.ipynb",
        root / "07_web_structure_mining_graph_skills.ipynb",
    ]
    if not all(p.exists() for p in required):
        raise SystemExit(
            "\nERROR: Run this script from the root of the Web Mining project.\n"
            "No file was changed."
        )

    # Remove preparation backups. These should never be part of the public repo.
    removed_backups = []
    for folder in root.glob("_backup_before_github_prepare_*"):
        if folder.is_dir():
            shutil.rmtree(folder)
            removed_backups.append(folder.name)

    # Remove placeholder README files that were only useful during preparation.
    for rel in ("dashboard/README.md", "data/README.md"):
        path = root / rel
        if path.exists():
            path.unlink()

    # Remove empty placeholder directories.
    for name in ("dashboard", "data"):
        folder = root / name
        if folder.exists() and folder.is_dir():
            try:
                folder.rmdir()
            except OSError:
                # Keep the folder if the user has already added real files.
                pass

    # Rewrite the public README in a simpler, natural project voice.
    (root / "README.md").write_text(README, encoding="utf-8", newline="\n")
    (root / ".gitignore").write_text(GITIGNORE, encoding="utf-8", newline="\n")

    print("README.md rewritten")
    print(".gitignore updated")
    print("dashboard/README.md removed")
    print("data/README.md removed")

    if removed_backups:
        print("Removed backup folders:")
        for name in removed_backups:
            print(" -", name)
    else:
        print("No local preparation backup folder found.")

    print()
    print("DONE.")
    print()
    print("Next commands:")
    print("  git add -A")
    print("  git status")
    print('  git commit -m "Clean repository structure and update README"')
    print("  git push")


if __name__ == "__main__":
    main()
