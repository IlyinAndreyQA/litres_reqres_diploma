import os

from pydantic import BaseModel


class LocalMobileConfig(BaseModel):
    remote_url: str = "http://localhost:4723"
    platform_name: str = "Android"
    device_name: str = "Pixel_5"
    app_package: str = "ru.litres.android"
    app_activity: str = "ru.litres.android.ui.splash.SplashActivity"
    auto_grant_permissions: bool = True


class BrowserStackMobileConfig(BaseModel):
    remote_url: str = "http://hub.browserstack.com/wd/hub"
    user_name: str
    access_key: str
    platform_name: str = "Android"
    device_name: str = "Google Pixel 7"
    platform_version: str = "13.0"
    app: str
    project_name: str = "Litres diploma"
    build_name: str = "Mobile tests"
    session_name: str = "Litres Android test"


def load_local_mobile_config() -> LocalMobileConfig:
    return LocalMobileConfig(
        remote_url=os.getenv("MOBILE_REMOTE_URL", "http://localhost:4723"),
        platform_name=os.getenv("MOBILE_PLATFORM_NAME", "Android"),
        device_name=os.getenv("MOBILE_DEVICE_NAME", "Pixel_5"),
        app_package=os.getenv("MOBILE_APP_PACKAGE", "ru.litres.android"),
        app_activity=os.getenv("MOBILE_APP_ACTIVITY", "ru.litres.android.ui.splash.SplashActivity"),
    )


def load_browserstack_mobile_config() -> BrowserStackMobileConfig:
    return BrowserStackMobileConfig(
        remote_url=os.getenv("BROWSERSTACK_REMOTE_URL", "http://hub.browserstack.com/wd/hub"),
        user_name=os.getenv("BROWSERSTACK_USER_NAME", ""),
        access_key=os.getenv("BROWSERSTACK_ACCESS_KEY", ""),
        platform_name=os.getenv("BROWSERSTACK_PLATFORM_NAME", "Android"),
        device_name=os.getenv("BROWSERSTACK_DEVICE_NAME", "Google Pixel 7"),
        platform_version=os.getenv("BROWSERSTACK_PLATFORM_VERSION", "13.0"),
        app=os.getenv("BROWSERSTACK_APP", ""),
        project_name=os.getenv("BROWSERSTACK_PROJECT_NAME", "Litres diploma"),
        build_name=os.getenv("BROWSERSTACK_BUILD_NAME", "Mobile tests"),
        session_name=os.getenv("BROWSERSTACK_SESSION_NAME", "Litres Android test"),
    )
