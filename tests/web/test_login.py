import allure
import pytest

from litres_reqres_diploma.pages.login_page import login_page
from litres_reqres_diploma.pages.main_page import main_page


pytestmark = pytest.mark.web


@allure.epic("Litres")
@allure.feature("Authorization")
@allure.story("Login validation")
@allure.tag("web", "login")
@allure.label("owner", "qa.guru student")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Login form shows validation for incorrect email")
def test_login_form_validation():
    main_page.open().open_login_form()
    login_page.submit_email("wrong-email").should_have_validation_message()
