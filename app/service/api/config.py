from pathlib import Path

from pydantic import ConfigDict
from pydantic_settings import BaseSettings

# Get the project root directory (2 levels up from this file)
project_root = Path(__file__).parent.parent.parent.parent
env_file_path = project_root / ".env"


class Settings(BaseSettings):
    model_config = ConfigDict(env_file=str(env_file_path), case_sensitive=True)

    PROJECT_NAME: str = "Project-Adriane"
    PROJECT_DESCRIPTION: str = "Find your search"
    VERSION: str = "0.1.0"
    API_V1_STR: str = "/api/v1"

    # API tokens
    OPEN_ROUTER_API_KEY: str = ""
    HUGGINGFACE_API_TOKEN: str = ""
    SUPABASE_PASSWORD: str = ""
    SUPABASE_API_KEY: str = ""
    SUPABASE_ACCESS_TOKEN: str = ""
    SUPABASE_PROJECT_ID: str = ""


settings = Settings()
