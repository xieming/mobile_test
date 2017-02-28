from http.cookiejar import CookieJar
from urllib.parse import urlencode
from urllib.request import build_opener, HTTPCookieProcessor, urlopen, Request
import lxml.html
from  globals import *


def parse_form(html):
    tree = lxml.html.fromstring(html)
    data = {}

    for e in tree.cssselect('form input'):
        if e.get('name'):
            data[e.get('name')] = e.get('value')

    return data


def login_confluence():
    cj = CookieJar()
    opener = build_opener(HTTPCookieProcessor(cj))
    html = urlopen(CONFLUENCE_LOGIN_URL).read()
    data = parse_form(html)
    data['os_username'] = username
    data['os_password'] = password
    encoded_data = urlencode(data).encode()

    request = Request(CONFLUENCE_LOGIN_URL, encoded_data)
    response = opener.open(request)
    print(response.geturl())

    return opener


def open_specific_confluence_page(page_url, opener):
    request_test_page = Request(page_url)
    test_page_html = opener.open(request_test_page)

    return test_page_html.read()


def login():
    opener = login_confluence()
    device_tracking_page_html = open_specific_confluence_page(CONFLUENCE_DEVICE_TRACKING_URL, opener)
    # print(device_tracking_page_html)
    return device_tracking_page_html


if __name__ == '__main__':
    opener = login_confluence()
    device_tracking_page_html = open_specific_confluence_page(CONFLUENCE_DEVICE_TRACKING_URL, opener)
