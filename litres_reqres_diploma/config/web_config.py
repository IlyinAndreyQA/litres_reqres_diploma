import os

from pydantic import BaseModel


class WebConfig(BaseModel):
    base_url: str = "https://www.litres.ru"
    browser_name: str = "chrome"
    browser_version: str = "128.0"
    window_width: int = 1440
    window_height: int = 900
    timeout: int = 10
    remote_url: str | None = None


def load_web_config() -> WebConfig:
    return WebConfig(
        base_url=os.getenv("WEB_BASE_URL", "https://www.litres.ru"),
        browser_name=os.getenv("BROWSER_NAME", "chrome"),
        browser_version=os.getenv("BROWSER_VERSION", "128.0"),
        window_width=int(os.getenv("BROWSER_WINDOW_WIDTH", "1440")),
        window_height=int(os.getenv("BROWSER_WINDOW_HEIGHT", "900")),
        timeout=int(os.getenv("BROWSER_TIMEOUT", "10")),
        remote_url=os.getenv("REMOTE_URL") or None,
    )
