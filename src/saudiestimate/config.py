"""Project constants and environment-based settings."""
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

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


class Settings(BaseSettings):
    """Read from environment variables or a local .env file (never committed)."""

    model_config = SettingsConfigDict(env_file=ROOT / ".env", extra="ignore")

    app_env: str = "development"
    # No default: the database is not wired up yet, so it stays unset until configured
    database_url: str | None = None


def get_settings() -> Settings:
    return Settings()
