import os

import pytest
from appium import webdriver as appium_webdriver
from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from litres_reqres_diploma.api.reqres_client import ReqresClient
from litres_reqres_diploma.config.api_config import load_api_config
from litres_reqres_diploma.config.mobile_config import (
    load_browserstack_mobile_config,
    load_local_mobile_config,
)
from litres_reqres_diploma.config.web_config import load_web_config
from litres_reqres_diploma.utils import allure_attach


load_dotenv()


def pytest_addoption(parser):
    web_config = load_web_config()
    parser.addoption("--browser_name", default=web_config.browser_name)
    parser.addoption("--browser_version", default=web_config.browser_version)
    parser.addoption("--mobile_context", default=os.getenv("MOBILE_CONTEXT", "local"))


@pytest.fixture(scope="session")
def api_client():
    api_config = load_api_config()
    if not api_config.api_key or api_config.api_key == "YOUR_REQRES_API_KEY":
        pytest.skip("REQRES_API_KEY is required for ReqRes API tests")

    return ReqresClient(api_config.base_url, api_config.api_key)


@pytest.fixture(scope="function")
def app(request):
    if os.getenv("RUN_MOBILE", "false").lower() != "true":
        pytest.skip("Set RUN_MOBILE=true to run Appium mobile tests")

    mobile_context = request.config.getoption("--mobile_context")

    if mobile_context == "browserstack":
        config = load_browserstack_mobile_config()
        if not config.user_name or not config.access_key or not config.app:
            pytest.skip("BrowserStack credentials and app id are required for mobile tests")

        options = UiAutomator2Options()
        options.platform_name = config.platform_name
        options.device_name = config.device_name
        options.platform_version = config.platform_version
        options.app = config.app
        options.set_capability(
            "bstack:options",
            {
                "userName": config.user_name,
                "accessKey": config.access_key,
                "projectName": config.project_name,
                "buildName": config.build_name,
                "sessionName": config.session_name,
            },
        )
        remote_url = config.remote_url
    else:
        config = load_local_mobile_config()
        options = UiAutomator2Options()
        options.platform_name = config.platform_name
        options.device_name = config.device_name
        options.app_package = config.app_package
        options.app_activity = config.app_activity
        options.auto_grant_permissions = config.auto_grant_permissions
        remote_url = config.remote_url

    driver = appium_webdriver.Remote(remote_url, options=options)

    yield driver

    allure_attach.add_mobile_screenshot(driver)
    driver.quit()


@pytest.fixture(scope="function", autouse=True)
def browser_management(request):
    if "web" not in request.keywords:
        yield
        return

    web_config = load_web_config()
    browser.config.base_url = web_config.base_url
    browser.config.window_width = web_config.window_width
    browser.config.window_height = web_config.window_height
    browser.config.timeout = web_config.timeout

    options = Options()
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-infobars")

    if web_config.remote_url:
        options.set_capability("browserName", request.config.getoption("--browser_name"))
        options.set_capability("browserVersion", request.config.getoption("--browser_version"))
        options.set_capability("selenoid:options", {"enableVNC": True, "enableVideo": True})
        browser.config.driver = webdriver.Remote(command_executor=f"{web_config.remote_url}/wd/hub", options=options)

    yield

    allure_attach.add_screenshot()
    allure_attach.add_html()
    allure_attach.add_browser_logs()
    allure_attach.add_selenoid_video(web_config.remote_url)
    browser.quit()
