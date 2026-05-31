import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class LitresApp:
    app_package = "ru.litres.android.audio"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def _click_if_present(self, locator: tuple[str, str]) -> bool:
        elements = self.driver.find_elements(*locator)
        if elements:
            elements[0].click()
            return True
        return False

    @allure.step("Skip first launch screens if they are shown")
    def skip_onboarding(self) -> "LitresApp":
        self.driver.activate_app(self.app_package)
        self.wait.until(lambda driver: driver.current_package == self.app_package)
        self._select_content_language_if_needed()
        self._skip_intro_if_needed()
        return self

    def _select_content_language_if_needed(self) -> None:
        russian_language = (
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().textContains("РУССКИЙ")',
        )
        choose_button = (AppiumBy.ID, f"{self.app_package}:id/choosebutton")

        if self._click_if_present(russian_language):
            self.wait.until(ec.element_to_be_clickable(choose_button)).click()

    def _skip_intro_if_needed(self) -> None:
        possible_buttons = [
            (AppiumBy.ID, f"{self.app_package}:id/skipButton"),
            (AppiumBy.ID, f"{self.app_package}:id/button_skip"),
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Пропустить")'),
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Позже")'),
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Не сейчас")'),
        ]

        for locator in possible_buttons:
            if self._click_if_present(locator):
                break

    @allure.step("Open search")
    def open_search(self) -> "LitresApp":
        self.wait.until(
            ec.element_to_be_clickable(
                (AppiumBy.ID, f"{self.app_package}:id/nav_search")
            )
        ).click()
        return self

    @allure.step("Search for book: {query}")
    def search(self, query: str) -> "LitresApp":
        search_input = self.wait.until(
            ec.presence_of_element_located(
                (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText")')
            )
        )
        search_input.send_keys(query)
        self.driver.press_keycode(66)
        return self

    @allure.step("Open profile")
    def open_profile(self) -> "LitresApp":
        self.wait.until(
            ec.element_to_be_clickable(
                (AppiumBy.ID, f"{self.app_package}:id/nav_profile")
            )
        ).click()
        return self

    @allure.step("Open catalog")
    def open_catalog(self) -> "LitresApp":
        self.wait.until(
            ec.element_to_be_clickable(
                (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Жанры")')
            )
        ).click()
        return self

    @allure.step("Check text is visible: {text}")
    def should_have_text(self, text: str) -> "LitresApp":
        self.wait.until(
            ec.presence_of_element_located(
                (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().textContains("{text}")')
            )
        )
        return self
