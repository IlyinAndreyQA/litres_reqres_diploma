import json
import logging

import allure
import curlify
import requests


class ReqresClient:
    def __init__(self, base_url: str, api_key: str | None = None):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})
        if api_key:
            self.session.headers.update({"x-api-key": api_key})

    @allure.step("{method} {path}")
    def request(self, method: str, path: str, **kwargs) -> requests.Response:
        response = self.session.request(method, f"{self.base_url}{path}", timeout=15, **kwargs)
        self._attach_request_response(response)
        return response

    def get(self, path: str, **kwargs) -> requests.Response:
        return self.request("GET", path, **kwargs)

    def post(self, path: str, **kwargs) -> requests.Response:
        return self.request("POST", path, **kwargs)

    def put(self, path: str, **kwargs) -> requests.Response:
        return self.request("PUT", path, **kwargs)

    def delete(self, path: str, **kwargs) -> requests.Response:
        return self.request("DELETE", path, **kwargs)

    @staticmethod
    def _attach_request_response(response: requests.Response) -> None:
        request = response.request
        curl = curlify.to_curl(request)
        logging.info(curl)

        allure.attach(curl, "curl", allure.attachment_type.TEXT)
        allure.attach(
            json.dumps(dict(response.headers), indent=2, ensure_ascii=False),
            "response_headers",
            allure.attachment_type.JSON,
        )

        try:
            body = json.dumps(response.json(), indent=2, ensure_ascii=False)
            attachment_type = allure.attachment_type.JSON
        except ValueError:
            body = response.text
            attachment_type = allure.attachment_type.TEXT

        allure.attach(body, "response_body", attachment_type)

