# SaudiEstimate

SaudiEstimate is an Arabic real-estate estimation system: a machine learning model that estimates the fair price of a Saudi property, shows comparable recent sales, flags prices that look too high or too low, and shows price trends by city and district. It is trained on open sale-transaction files published by the Saudi Ministry of Justice (MOJ).

## Architecture

- **Backend:** FastAPI (Python 3.11)
- **Database:** PostgreSQL
- **Frontend:** React, planned for later
- **Streamlit:** fallback UI only, not the primary frontend
- **ML pipeline:** under development

Status: foundation only. There are no API endpoints, database models or ML code yet.

## Folder layout

```
saudiestimate/
  data/raw/          # MOJ quarterly files, never modified, git-ignored
  data/processed/    # pipeline outputs (parquet), git-ignored
  src/saudiestimate/ # Python package (config.py holds paths and settings)
  notebooks/         # EDA and experiments
  tests/
  reports/
  app/               # Streamlit fallback, later
  .env.example       # template for local environment variables
  requirements.txt, pyproject.toml, README.md, .gitignore
```

## Setup

Requires Python 3.11.

```bash
python3.11 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pip install -e .
cp .env.example .env               # then edit values; .env is git-ignored
```

Put the raw MOJ files in `data/raw/`, unmodified. They are named `MOJ-Sales-YYYY-Qn.csv` (2020-Q4 and 2021-Q1 are `.csv.gz`). The folder is git-ignored, so each team member must copy the files in locally.

Run the tests with `pytest`.

## Data source and licence

Data come from the open data of the Ministry of Justice (MOJ) and the Real Estate General Authority (REGA), published under the KSA Open Data Licence. Attribution: Ministry of Justice and REGA.
