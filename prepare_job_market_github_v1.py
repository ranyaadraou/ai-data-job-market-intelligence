from __future__ import annotations

import json
import shutil
from datetime import datetime
from pathlib import Path

TITLE = "PREPARE AI & DATA JOB MARKET INTELLIGENCE FOR GITHUB"

README = r"""# AI & Data Job Market Intelligence

End-to-end **Web Mining, Data Engineering, NLP, Graph Analytics and Forecasting** project for analysing the evolution of Data & AI skills from large-scale job-market data.

The project builds a complete analytical pipeline from heterogeneous job-offer sources to data quality assessment, NoSQL storage, semantic skill enrichment, graph mining, trend forecasting and an interactive BI dashboard.

## Project overview

The objective is to answer a practical question:

> How can online job-market data be transformed into reliable intelligence about the skills, technologies and domains shaping Data Science and Artificial Intelligence careers?

The consolidated analytical dataset contains **751,801 Data & AI job offers** covering **2020-2026** and an international scope of **165 countries**. The pipeline then transforms these records into structured skill-level and trend-level datasets for downstream analysis.

## End-to-end architecture

```mermaid
flowchart LR
    A[Multi-source Job Data] --> B[Cleaning & Standardization]
    B --> C[Data Quality Framework]
    C --> D[Skills Exploded Dataset]
    D --> E[(MongoDB)]
    E --> F[Web Content Mining]
    F --> G[NLP / TF-IDF / Embeddings]
    G --> H[Domain Classification]
    H --> I[Graph Mining]
    I --> J[Centrality / Louvain Communities]
    J --> K[Trend Analysis]
    K --> L[Prophet / ARIMA / Linear Regression]
    L --> M[Power BI Dashboard]
```

## What this project demonstrates

- Large-scale multi-source data consolidation and standardization
- Data quality assessment before downstream modelling
- Semi-structured storage and analytical querying with MongoDB
- Skill extraction and enrichment from textual job descriptions
- TF-IDF, multi-label representations and sentence embeddings
- Automatic classification of Data & AI job domains
- Skill co-occurrence graph construction and network analysis
- Centrality analysis and Louvain community detection
- Time-series trend analysis using Google Trends data
- Forecasting with Prophet, ARIMA and linear regression
- Business-oriented visual storytelling through Power BI

## Pipeline notebooks

| Step | Notebook | Purpose |
|---|---|---|
| 01 | `01_collecte_et_sources.ipynb` | Source analysis, collection inventory and consolidated dataset validation |
| 02 | `02_cleaning_fusion_dataset.ipynb` | Cleaning, normalization, schema alignment and dataset fusion |
| 03 | `03_data_quality_framework_v2.ipynb` | Missing values, duplicates, temporal/geographic coverage and quality controls |
| 04 | `04_creation_dataset_skills_exploded.ipynb` | Transformation from job-level data to skill-level observations |
| 05 | `05_mongodb_storage.ipynb` | MongoDB collections, indexes and analytical queries |
| 06 | `06_web_content_mining_final_respecte.ipynb` | NLP, TF-IDF, embeddings, skill enrichment and domain classification |
| 07 | `07_web_structure_mining_graph_skills.ipynb` | Skill graphs, centrality, Louvain communities, Google Trends and forecasting |

## Key analytical results

The project highlights several important engineering and analytical observations:

- The consolidated dataset contains **751,801 job offers**.
- Skills are available for approximately **99.96%** of the consolidated records.
- The dataset spans **2020-2026** and **165 countries**.
- The pipeline models skill relationships through a weighted co-occurrence graph.
- Network analysis identifies central and transversal technologies across Data, AI, Cloud and Big Data ecosystems.
- Because the original job dataset is temporally imbalanced, forecasting is supported with a separate Google Trends time series rather than blindly extrapolating the job-count distribution.

## Dashboard

### Global overview

![Global Overview](demo/global-overview.png)

### Skills demand

![Skills Demand](demo/skills-demand.png)

### Future skills

![Future Skills](demo/future-skills.png)

### Morocco market

![Morocco Market](demo/morocco-market.png)

The Power BI source file will be added in a later commit. The dashboard screenshots already document the main analytical views.

## Technology stack

**Data Engineering:** Python, Pandas, NumPy  
**Storage:** MongoDB, PyMongo  
**NLP / Content Mining:** Scikit-learn, Transformers, Sentence Transformers  
**Graph Analytics:** NetworkX, python-louvain  
**Forecasting:** Prophet, ARIMA, Linear Regression, Pytrends  
**Visualization:** Matplotlib, Seaborn, Power BI

## Data availability

Large raw and intermediate datasets are intentionally not included in this repository.

See [`data/README.md`](data/README.md) for the expected datasets and reproducibility notes.

## Running the notebooks

Create a virtual environment and install the dependencies:

```bash
python -m venv .venv
```

Windows:

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
jupyter lab
```

The notebooks are designed as a sequential analytical pipeline. Some steps require the original datasets and a local MongoDB instance.

## Academic context

This project was developed for the **Web Mining (M242)** module at the **National School of Applied Sciences of Tetouan (ENSA Tetouan)**, Abdelmalek Essaadi University, during the **2025-2026 academic year**.

**Supervisor:** Prof. Imad Sassi

### Team

- Nour El Houda Amaziane
- Ranya Adraou
- Aya Ettalbi
- Ouiame Biloul

## Report

The complete academic report is available here:

[`docs/rapport-web-mining.pdf`](docs/rapport-web-mining.pdf)

## Repository status

The analytical pipeline, report and dashboard screenshots are available.  
The Power BI `.pbix` file can be added later without recreating the repository.
"""

REQUIREMENTS = """pandas
numpy
matplotlib
seaborn
pymongo
tqdm
scikit-learn
transformers
sentence-transformers
torch
networkx
python-louvain
prophet
pytrends
statsmodels
jupyterlab
"""

GITIGNORE = r"""# Python
__pycache__/
*.py[cod]
*.pyo
*.pyd

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

# Secrets / local configuration
.env
.env.*
!.env.example

# Large datasets and generated analytical files
data/*
!data/README.md
*.csv
*.parquet
*.feather

# Generated models / forecasts
*.pkl
*.pickle
*.joblib

# Local MongoDB / temporary files
mongodb-data/
tmp/
temp/

# Python packaging
build/
dist/
*.egg-info/
"""

DATA_README = r"""# Data

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
"""

DASHBOARD_README = r"""# Power BI Dashboard

The dashboard source file (`.pbix`) will be added in a later commit.

The current repository already contains exported screenshots in the [`demo`](../demo) directory:

- Global Overview
- Skills Demand
- Future Skills
- Morocco Market

When the `.pbix` file is available, place it in this folder and commit it as a normal project update.

If the file is larger than GitHub's normal file-size limit, use Git LFS instead of a regular Git commit.
"""

CONTRIBUTORS = """# Contributors

Academic team project developed at ENSA Tetouan:

- Nour El Houda Amaziane
- Ranya Adraou
- Aya Ettalbi
- Ouiame Biloul

Supervisor: Prof. Imad Sassi
"""


def backup_file(src: Path, backup_root: Path, root: Path) -> None:
    if not src.exists():
        return
    dst = backup_root / src.relative_to(root)
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def patch_mongodb_notebook(path: Path) -> bool:
    if not path.exists():
        return False

    notebook = json.loads(path.read_text(encoding="utf-8"))
    changed = False

    old_path = r"C:\Users\asus\Documents\dataset_WebMining"

    for cell in notebook.get("cells", []):
        source = "".join(cell.get("source", []))

        if old_path in source:
            if cell.get("cell_type") == "markdown":
                replacement = """## 2. Définir le dossier de travail

Les grands fichiers de données ne sont pas versionnés dans GitHub.

Par défaut, ce notebook cherche les fichiers dans le dossier `data/` du dépôt.
Vous pouvez aussi définir la variable d'environnement `WEBMINING_DATA_DIR`
pour utiliser un autre dossier local.
"""
                cell["source"] = replacement.splitlines(keepends=True)
            else:
                replacement = """from pathlib import Path

configured_data_dir = os.getenv("WEBMINING_DATA_DIR")

if configured_data_dir:
    project_path = Path(configured_data_dir).expanduser().resolve()
else:
    project_path = (Path.cwd() / "data").resolve()

if not project_path.exists():
    raise FileNotFoundError(
        f"Data directory not found: {project_path}. "
        "Create ./data or define WEBMINING_DATA_DIR."
    )

os.chdir(project_path)

print("Dossier courant :")
print(os.getcwd())

print("\\nFichiers CSV disponibles dans le dossier :")
for f in os.listdir():
    if f.endswith(".csv"):
        print("-", f)
"""
                cell["source"] = replacement.splitlines(keepends=True)

            changed = True

    if changed:
        path.write_text(
            json.dumps(notebook, ensure_ascii=False, indent=1),
            encoding="utf-8",
        )

    return changed


def main() -> None:
    print()
    print(TITLE)
    print("=" * len(TITLE))

    root = Path.cwd()

    expected = [
        root / "01_collecte_et_sources.ipynb",
        root / "02_cleaning_fusion_dataset.ipynb",
        root / "03_data_quality_framework_v2.ipynb",
        root / "04_creation_dataset_skills_exploded.ipynb",
        root / "05_mongodb_storage.ipynb",
        root / "06_web_content_mining_final_respecte.ipynb",
        root / "07_web_structure_mining_graph_skills.ipynb",
        root / "demo" / "global-overview.png",
        root / "demo" / "skills-demand.png",
        root / "demo" / "future-skills.png",
        root / "demo" / "morocco-market.png",
        root / "rapport-web-mining.pdf",
    ]

    missing = [str(p.name) for p in expected if not p.exists()]
    if missing:
        print("\nERROR: this does not look like the project root.")
        print("Missing:")
        for item in missing:
            print(" -", item)
        print("\nNo file was changed.")
        raise SystemExit(1)

    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup = root / f"_backup_before_github_prepare_{stamp}"

    files_to_backup = [
        root / "05_mongodb_storage.ipynb",
        root / "rapport-web-mining.pdf",
        root / "README.md",
        root / "requirements.txt",
        root / ".gitignore",
        root / "CONTRIBUTORS.md",
        root / "data" / "README.md",
        root / "dashboard" / "README.md",
    ]

    for src in files_to_backup:
        backup_file(src, backup, root)

    (root / "docs").mkdir(exist_ok=True)
    (root / "data").mkdir(exist_ok=True)
    (root / "dashboard").mkdir(exist_ok=True)

    report_src = root / "rapport-web-mining.pdf"
    report_dst = root / "docs" / "rapport-web-mining.pdf"

    if report_src.exists():
        shutil.copy2(report_src, report_dst)
        report_src.unlink()

    patched = patch_mongodb_notebook(root / "05_mongodb_storage.ipynb")

    (root / "README.md").write_text(README, encoding="utf-8", newline="\n")
    (root / "requirements.txt").write_text(REQUIREMENTS, encoding="utf-8", newline="\n")
    (root / ".gitignore").write_text(GITIGNORE, encoding="utf-8", newline="\n")
    (root / "data" / "README.md").write_text(DATA_README, encoding="utf-8", newline="\n")
    (root / "dashboard" / "README.md").write_text(
        DASHBOARD_README,
        encoding="utf-8",
        newline="\n",
    )
    (root / "CONTRIBUTORS.md").write_text(
        CONTRIBUTORS,
        encoding="utf-8",
        newline="\n",
    )

    print(f"\nBackup created: {backup.name}")
    print("README.md created")
    print("requirements.txt created")
    print(".gitignore created")
    print("data/README.md created")
    print("dashboard/README.md created")
    print("CONTRIBUTORS.md created")
    print("Report moved to docs/rapport-web-mining.pdf")
    print(
        "05_mongodb_storage.ipynb local path patched"
        if patched
        else "05_mongodb_storage.ipynb did not need path patching"
    )

    print("\nDONE.")
    print("\nNext commands:")
    print("  git init")
    print("  git branch -M main")
    print('  git add .')
    print('  git commit -m "Initial release: AI & Data Job Market Intelligence"')


if __name__ == "__main__":
    main()
