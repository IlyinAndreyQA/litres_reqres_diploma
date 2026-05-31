import allure
from selene import be, browser, have


class LoginPage:
    @allure.step("Submit login form with email: {email}")
    def submit_email(self, email: str) -> "LoginPage":
        browser.element("[data-testid='auth__input--enterEmailOrLogin']").should(be.visible).type(email)
        browser.element("[data-testid='auth__button--continue']").should(be.enabled).click()
        return self

    @allure.step("Check validation message is shown")
    def should_have_validation_message(self) -> "LoginPage":
        browser.element("body").should(have.text("Пользователь не найден"))
        return self


login_page = LoginPage()

