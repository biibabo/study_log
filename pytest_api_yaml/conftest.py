# -*- coding: utf-8 -*-
# @Time    : 2023/2/2 4:45 PM
# @Author  : junbo.zhao
# @File    : conftest.py
import json

import pytest
import requests

from config.conf import test_Referer, test_Origin, test_url


@pytest.fixture(autouse=True)
def test_onlinecookie():
    url = ""
    data = {}
    r = requests.post(url, data=data)
    print(r.json())
    print(r.headers['Set-Cookie'])
    onlinecookie = r.headers['Set-Cookie']
    return onlinecookie


@pytest.fixture(autouse=True)
def test_testcookie():
    url = ""
    data = {}
    r = requests.post(url, data=data)
    print(r.json())
    print(r.headers['Set-Cookie'])
    testcookie = r.headers['Set-Cookie']
    return testcookie

