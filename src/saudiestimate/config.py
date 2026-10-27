"""Project constants. No logic."""
from pathlib import Path

# Paths (relative to the repo root)
ROOT = Path(__file__).resolve().parents[2]
DATA_RAW = ROOT / "data" / "raw"
DATA_PROCESSED = ROOT / "data" / "processed"
REPORTS_DIR = ROOT / "reports"

# MOJ spells some region names differently across files; map to one spelling
REGION_MAP = {
    "منطقة مكة المكرمة": "منطقة مكة المكرمه",
    "المنطقة الشرقية": "منطقة الشرقية",
    "منطقة المدينة المنورة": "منطقة المدينة المنوره",
}

# Property classes kept in the pipeline: residential, commercial, agricultural
KEPT_CLASSES = ["سكني", "تجاري", "زراعي"]
