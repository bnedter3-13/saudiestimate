# SaudiEstimate

SaudiEstimate is a graduation project: a machine learning system that estimates the fair price of a Saudi property, shows comparable recent sales, flags prices that look too high or too low, and shows price trends by city and district. It is trained on open sale-transaction files published by the Saudi Ministry of Justice (MOJ).

## Folder layout

```
saudiestimate/
  data/raw/          # MOJ quarterly files, never modified, git-ignored
  data/processed/    # pipeline outputs (parquet), git-ignored
  src/saudiestimate/ # package (__init__.py, config.py)
  notebooks/
  tests/
  reports/
  app/               # Streamlit app, later
  requirements.txt, README.md, .gitignore, pyproject.toml
```

## Setup

Requires Python 3.11.

```bash
python3.11 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pip install -e .
```

Put the raw MOJ files in `data/raw/`, unmodified. They are named `MOJ-Sales-YYYY-Qn.csv` (2020-Q4 and 2021-Q1 are `.csv.gz`). The folder is git-ignored, so each team member must copy the files in locally.

## Data source and licence

Data come from the open data of the Ministry of Justice (MOJ) and the Real Estate General Authority (REGA), published under the KSA Open Data Licence. Attribution: Ministry of Justice and REGA.
