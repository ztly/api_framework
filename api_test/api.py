
import requests
from requests import Response


class BaseApi:
    method = "GET"
    url = ""
    params = None
    headers = None
    json = None
    data = None
    cookies = None
    files = None
    auth = None
    timeout = None
    allow_redirects = True
    proxies = None
    hooks = None
    stream = None
    verify = None
    cert = None

    def __init__(self):
        self.response = None

    def set_params(self, **params):
        self.params = params
        return self

    def set_data(self, data):
        self.data = data
        return self

    def set_json(self, json):
        self.json = json
        return self

    def set_cookie(self, key, value):
        self.cookies = self.cookies or {}
        self.cookies.update({key: value})
        return self

    def set_cookies(self, **kwargs):
        self.cookies = self.cookies or {}
        self.cookies.update(kwargs)
        return self

    def run(self, session=None):
        session = session or requests.sessions.Session()
        self.response = session.request(
            self.method,
            self.url,
            params=self.params,
            data=self.data,
            headers=self.headers,
            cookies=self.cookies,
            files=self.files,
            auth=self.auth,
            timeout=self.timeout,
            allow_redirects=self.allow_redirects,
            proxies=self.proxies,
            hooks=self.hooks,
            stream=self.stream,
            verify=self.verify,
            cert=self.cert,
            json=self.json
        )
        return self

    def validate(self, key, expect_value):
        value = self.extract(key)
        assert value == expect_value
        return self

    def extract(self, key):
        value = self.response
        for k in key.split("."):
            if isinstance(value, Response):
                if k == "json()":
                    value = self.response.json()
                else:
                    value = getattr(value, k)
            elif isinstance(value, (requests.structures.CaseInsensitiveDict, dict)):
                value = value[k]
        return value

    def get_response(self) -> Response:
        return self.response

