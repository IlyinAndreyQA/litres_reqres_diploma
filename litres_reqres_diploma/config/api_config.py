import os

from pydantic import BaseModel


class ApiConfig(BaseModel):
    base_url: str = "https://reqres.in/api"
    api_key: str | None = None


def load_api_config() -> ApiConfig:
    return ApiConfig(
        base_url=os.getenv("API_BASE_URL", "https://reqres.in/api"),
        api_key=os.getenv("REQRES_API_KEY"),
    )
