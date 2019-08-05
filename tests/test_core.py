#!/usr/bin/env python
# coding=utf-8
from tests.api.httpbin import HttpGet, HttpPost, HttpGetCookies


def test_get():

    HttpGet().\
        run().\
        validate("status_code", 200).\
        validate("headers.server", "nginx")


def test_get_with_paramers():

    HttpGet().\
        set_params(hello="world").\
        run().\
        validate("status_code", 200).\
        validate("headers.server", "nginx").\
        validate("json().args.hello", "world").\
        validate("json().headers.Accept", "application/json")

def test_post():

    HttpPost().\
        set_json({"you": "me"}).\
        run().\
        validate("status_code", 200).\
        validate("headers.server", "nginx")


def test_parameters_share():
    user_id = "123"
    HttpGet(). \
        set_params(user_id=user_id). \
        run(). \
        validate("status_code", 200). \
        validate("headers.server", "nginx"). \
        validate("json().args.user_id", "123"). \
        validate("json().headers.Accept", "application/json").\
        validate("json().url", "https://httpbin.org/get?user_id={}".format(user_id))

    HttpPost().\
        set_json({"user_id": user_id}).\
        run().\
        validate("status_code", 200).\
        validate("headers.server", "nginx").\
        validate("json().json.user_id", user_id)


def test_set_cookies():
    HttpGetCookies().\
        set_cookie("zt", "345").\
        run().\
        validate("json().cookies.zt", "345")


def test_parameters_extract():
    # setp 1: get value
    cookie =HttpGetCookies().\
        set_cookie("sm", "789").\
        run().\
        extract("json().cookies.sm")
    assert cookie == "789"

    # step 2: user value as paramter
    HttpPost(). \
        set_json({"user_id": cookie}). \
        run(). \
        validate("status_code", 200). \
        validate("headers.server", "nginx"). \
        validate("json().json.user_id", cookie)

