#!/usr/bin/env python
# coding=utf-8

import requests
from requests import Response


class BaseApi:
    method = "GET"
    url = ""
    params = {}
    headers = {}
    json = {}
    data = ""
    cookies = {}

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
        self.cookies.update({key: value})
        return self

    def run(self):
        self.response = requests.request(
            self.method,
            self.url,
            params=self.params,
            data=self.data,
            json=self.json,
            headers=self.headers,
            cookies=self.cookies
        )
        print("response===================%s" %self.response.json())
        return self

    def validate(self, key, expect_value):
        value = self.extract(key)
        assert value == expect_value
        return self

    # 用例中既有validate又有extract时，extract要放在会后，此方法不能链式调用
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
            print("key--------\n%s" % k, "\nvalue--------\n%s" % value, type(value))
        return value


