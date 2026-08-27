from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

# Repo layout is job-copilot/backend/app/core/config.py, so the repo root
# (where the shared .env lives) is three levels up from this file.
_REPO_ROOT_ENV_FILE = Path(__file__).resolve().parents[3] / ".env"


class Settings(BaseSettings):
    """Centralized application configuration, loaded from environment variables / .env.

    Nothing in this app should read os.environ directly — go through Settings
    so there is a single, testable source of truth for configuration.
    """

    model_config = SettingsConfigDict(
        env_file=_REPO_ROOT_ENV_FILE,
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # --- General ---
    environment: str = "development"
    api_v1_prefix: str = "/api/v1"
    project_name: str = "AI Job Application Copilot"

    # --- Database ---
    database_url: str = "postgresql+psycopg://postgres:postgres@localhost:5432/job_copilot"

    # --- Auth ---
    jwt_secret: str = "change-me-in-development"
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 60

    # --- AI ---
    openai_api_key: str | None = None
    openai_model: str = "gpt-4o-mini"

    # --- Storage ---
    storage_provider: str = "local"
    local_storage_path: str = "./storage"
    azure_storage_account: str | None = None
    azure_storage_container: str | None = None
    azure_storage_connection_string: str | None = None

    # --- CORS ---
    cors_origins: str = "http://localhost:5173"

    @property
    def cors_origin_list(self) -> list[str]:
        return [origin.strip() for origin in self.cors_origins.split(",") if origin.strip()]

    @property
    def is_production(self) -> bool:
        return self.environment.lower() == "production"


@lru_cache
def get_settings() -> Settings:
    """Settings are cached so the environment is only parsed once per process."""
    return Settings()
