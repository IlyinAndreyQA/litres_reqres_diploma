import allure
import pytest

from litres_reqres_diploma.pages.mobile.litres_app import LitresApp


pytestmark = pytest.mark.mobile


@allure.epic("Litres Mobile")
@allure.feature("Search")
@allure.story("Book search")
@allure.tag("mobile", "search")
@allure.label("owner", "qa.guru student")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Mobile user can search book by title")
def test_mobile_search_book(app):
    LitresApp(app).skip_onboarding().open_search().search("Гарри Поттер").should_have_text("Гарри")


@allure.epic("Litres Mobile")
@allure.feature("Catalog")
@allure.story("Catalog navigation")
@allure.tag("mobile", "catalog")
@allure.label("owner", "qa.guru student")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Mobile user can open catalog")
def test_mobile_open_catalog(app):
    LitresApp(app).skip_onboarding().open_catalog().should_have_text("ЖАНРЫ")


@allure.epic("Litres Mobile")
@allure.feature("Profile")
@allure.story("Profile screen")
@allure.tag("mobile", "profile")
@allure.label("owner", "qa.guru student")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Mobile user can open profile screen")
def test_mobile_open_profile(app):
    LitresApp(app).skip_onboarding().open_profile().should_have_text("Войти")
