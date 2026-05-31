import base64
import json

import allure
import requests
from selene import browser


def add_screenshot() -> None:
    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name="screenshot",
        attachment_type=allure.attachment_type.PNG,
    )


def add_html() -> None:
    allure.attach(
        browser.driver.page_source,
        name="page_source",
        attachment_type=allure.attachment_type.HTML,
    )


def add_browser_logs() -> None:
    try:
        logs = browser.driver.get_log("browser")
    except Exception:
        return

    allure.attach(
        json.dumps(logs, indent=2, ensure_ascii=False),
        name="browser_logs",
        attachment_type=allure.attachment_type.JSON,
    )


def add_selenoid_video(remote_url: str | None) -> None:
    if not remote_url:
        return

    session_id = browser.driver.session_id
    video_url = f"{remote_url.rstrip('/')}/video/{session_id}.mp4"
    try:
        video = requests.get(video_url, timeout=10)
    except requests.RequestException:
        return

    if video.status_code == 200:
        html = (
            "<html><body><video width='100%' height='100%' controls autoplay>"
            f"<source src='data:video/mp4;base64,{base64.b64encode(video.content).decode()}' type='video/mp4'>"
            "</video></body></html>"
        )
        allure.attach(html, name="video", attachment_type=allure.attachment_type.HTML)


def add_mobile_screenshot(driver) -> None:
    allure.attach(
        driver.get_screenshot_as_png(),
        name="mobile_screenshot",
        attachment_type=allure.attachment_type.PNG,
    )
