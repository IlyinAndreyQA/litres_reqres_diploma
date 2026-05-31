import allure
import pytest

from litres_reqres_diploma.pages.main_page import main_page
from litres_reqres_diploma.utils.json_reader import read_json_resource


pytestmark = pytest.mark.web
search_data = read_json_resource("search_data.json")


@allure.epic("Litres")
@allure.feature("Search")
@allure.story("Catalog search")
@allure.tag("web", "search")
@allure.label("owner", "qa.guru student")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("User can find content by query: {query}")
@pytest.mark.parametrize("case", search_data, ids=[item["query"] for item in search_data])
def test_search_content(case):
    query = case["query"]
    expected = case["expected"]

    main_page.open().search(query).should_have_search_result(expected)
