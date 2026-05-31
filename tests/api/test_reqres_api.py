import allure
import pytest

from litres_reqres_diploma.models.reqres import (
    CreatedUserResponse,
    ErrorResponse,
    RegisterBody,
    SingleUserResponse,
    UpdatedUserResponse,
    UserBody,
    UsersListResponse,
)
from litres_reqres_diploma.utils.schema import validate_schema


pytestmark = pytest.mark.api


@allure.epic("Reqres")
@allure.feature("Users")
@allure.story("Users list")
@allure.tag("api", "get")
@allure.label("owner", "qa.guru student")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Get users list")
def test_get_users_list(api_client):
    response = api_client.get("/users", params={"page": 2})

    assert response.status_code == 200
    validate_schema(response, "users_list.json")
    users = UsersListResponse.model_validate(response.json())
    assert users.page == 2
    assert len(users.data) > 0


@allure.epic("Reqres")
@allure.feature("Users")
@allure.story("Single user")
@allure.tag("api", "get")
@allure.label("owner", "qa.guru student")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Get single user")
def test_get_single_user(api_client):
    response = api_client.get("/users/2")

    assert response.status_code == 200
    validate_schema(response, "single_user.json")
    user = SingleUserResponse.model_validate(response.json())
    assert user.data.id == 2
    assert user.data.email == "janet.weaver@reqres.in"


@allure.epic("Reqres")
@allure.feature("Users")
@allure.story("Create user")
@allure.tag("api", "post")
@allure.label("owner", "qa.guru student")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create user")
def test_create_user(api_client):
    payload = UserBody(name="morpheus", job="leader")
    response = api_client.post("/users", json=payload.model_dump())

    assert response.status_code == 201
    validate_schema(response, "created_user.json")
    created_user = CreatedUserResponse.model_validate(response.json())
    assert created_user.name == payload.name
    assert created_user.job == payload.job
    assert created_user.id


@allure.epic("Reqres")
@allure.feature("Users")
@allure.story("Update user")
@allure.tag("api", "put")
@allure.label("owner", "qa.guru student")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Update user")
def test_update_user(api_client):
    payload = UserBody(name="morpheus", job="zion resident")
    response = api_client.put("/users/2", json=payload.model_dump())

    assert response.status_code == 200
    validate_schema(response, "updated_user.json")
    updated_user = UpdatedUserResponse.model_validate(response.json())
    assert updated_user.name == payload.name
    assert updated_user.job == payload.job


@allure.epic("Reqres")
@allure.feature("Users")
@allure.story("Delete user")
@allure.tag("api", "delete")
@allure.label("owner", "qa.guru student")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Delete user")
def test_delete_user(api_client):
    response = api_client.delete("/users/2")

    assert response.status_code == 204
    assert response.text == ""


@allure.epic("Reqres")
@allure.feature("Registration")
@allure.story("Negative registration")
@allure.tag("api", "negative")
@allure.label("owner", "qa.guru student")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Register user without password")
def test_unsuccessful_registration_without_password(api_client):
    payload = RegisterBody(email="sydney@fife")
    response = api_client.post("/register", json=payload.model_dump_without_none())

    assert response.status_code == 400
    validate_schema(response, "error.json")
    error = ErrorResponse.model_validate(response.json())
    assert error.error == "Missing password"
