import allure
import pytest

from litres_reqres_diploma.pages.main_page import main_page


pytestmark = pytest.mark.web


@allure.epic("Litres")
@allure.feature("Navigation")
@allure.story("Catalog sections")
@allure.tag("web", "navigation")
@allure.label("owner", "qa.guru student")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("User can open audiobooks section")
def test_open_audiobooks_section():
    main_page.open().open_audiobooks().should_have_text("Аудиокниги")


@allure.epic("Litres")
@allure.feature("Navigation")
@allure.story("Catalog sections")
@allure.tag("web", "navigation")
@allure.label("owner", "qa.guru student")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("User can open genres catalog")
def test_open_genres_catalog():
    main_page.open().open_genres().should_have_text("Легкое чтение")


@allure.epic("Litres")
@allure.feature("Navigation")
@allure.story("Popular books")
@allure.tag("web", "navigation")
@allure.label("owner", "qa.guru student")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("User can open popular books section")
def test_open_popular_books():
    main_page.open().open_popular_books().should_have_text("Популяр")


@allure.epic("Litres")
@allure.feature("Cart")
@allure.story("Cart page")
@allure.tag("web", "cart")
@allure.label("owner", "qa.guru student")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("User can open cart page")
def test_open_cart():
    main_page.open().open_cart().should_have_text("Корзин")


@allure.epic("Litres")
@allure.feature("Subscriptions")
@allure.story("Subscription page")
@allure.tag("web", "subscription")
@allure.label("owner", "qa.guru student")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("User can open subscriptions section")
def test_open_subscriptions():
    main_page.open().open_subscriptions().should_have_text("Подпис")
