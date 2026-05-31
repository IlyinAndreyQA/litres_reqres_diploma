import allure
from selene import be, browser, have
from urllib.parse import quote


class MainPage:
    @allure.step("Open Litres main page")
    def open(self) -> "MainPage":
        browser.open("/")
        return self

    @allure.step("Search for text: {query}")
    def search(self, query: str) -> "MainPage":
        browser.open(f"/search/?q={quote(query)}")
        return self

    @allure.step("Open authorization form")
    def open_login_form(self) -> "MainPage":
        browser.element("[data-testid='header__login-button--desktop'], [data-testid='tab-login'], a[href='/auth/login/']").should(be.visible).click()
        return self

    @allure.step("Open audiobooks section")
    def open_audiobooks(self) -> "MainPage":
        browser.element("a[href*='audioknigi'], a[href*='audio']").should(be.visible).click()
        return self

    @allure.step("Open genres catalog")
    def open_genres(self) -> "MainPage":
        browser.element("[data-testid='header-catalog-button']").should(be.visible).click()
        return self

    @allure.step("Open popular books section")
    def open_popular_books(self) -> "MainPage":
        browser.element("a[href*='popular'], a[href*='best']").should(be.visible).click()
        return self

    @allure.step("Open cart")
    def open_cart(self) -> "MainPage":
        browser.element("a[href*='cart'], [data-testid*='cart']").should(be.visible).click()
        return self

    @allure.step("Open subscriptions section")
    def open_subscriptions(self) -> "MainPage":
        browser.element("[data-testid='lowerMenu__item--subscription'], a[href='/litres_subscription/']").should(be.visible).click()
        return self

    @allure.step("Check search result contains: {expected_text}")
    def should_have_search_result(self, expected_text: str) -> "MainPage":
        browser.all("a, h1, h2, h3").element_by(have.text(expected_text)).should(be.visible)
        return self

    @allure.step("Check current url contains: {expected_part}")
    def should_have_url(self, expected_part: str) -> "MainPage":
        browser.should(have.url_containing(expected_part))
        return self

    @allure.step("Check page contains text: {expected_text}")
    def should_have_text(self, expected_text: str) -> "MainPage":
        browser.element("body").should(have.text(expected_text))
        return self


main_page = MainPage()
