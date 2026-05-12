from __future__ import annotations

import os
from pathlib import Path
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


ROOT_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT_DIR / 'data'
UPLOAD_DIR = DATA_DIR / 'uploads'
OUTPUT_DIR = ROOT_DIR / 'output'


class Settings(BaseSettings):
    app_name: str = 'Resume Optimizer'
    app_env: str = Field(default='development', alias='APP_ENV')
    app_host: str = Field(default='127.0.0.1', alias='APP_HOST')
    app_port: int = Field(default=8000, alias='APP_PORT')
    upload_dir: str = str(UPLOAD_DIR)
    output_dir: str = str(OUTPUT_DIR)
    max_upload_size_mb: int = 10
    openai_api_key: str | None = Field(default=None, alias='OPENAI_API_KEY')

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        extra='ignore',
        populate_by_name=True,
    )


settings = Settings()

os.makedirs(settings.upload_dir, exist_ok=True)
os.makedirs(settings.output_dir, exist_ok=True)
