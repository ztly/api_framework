#!/usr/bin/env python
# coding=utf-8
from api_test.api import BaseApi


class HttpGet(BaseApi):
    url = "http://httpbin.org/get"
    params = {}
    headers = {"accept": "application/json"}
    method = "GET"


class HttpPost(BaseApi):
    url = "http://httpbin.org/post"
    headers = {"accept": "application/json"}
    json = {"hello": "world"}
    method = "POST"


class HttpGetCookies(BaseApi):
    """
    curl -X GET "http://httpbin.org/cookies" -H "accept: application/json"
    """
    url = "http://httpbin.org/cookies"
    headers = {"accept": "application/json"}
    cookies = {"freeform": "123"}
    method = "GET"


