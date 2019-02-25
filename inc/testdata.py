#!/usr/bin/env python
# coding: utf8

from urllib.parse import urlparse
import sys


def create_test_data(urls, method, burp_url, wo_burp_extend, timeout):
    testdata = []

    if "http" in burp_url or "/" in burp_url:
        print("\033[31m[ x ]\033[0m Please remove http(s) or slashes from your burp url, I'll handle that!")
        sys.exit(1)

    for url in urls:
        parser = urlparse(url)
        hostname = parser.hostname

        if wo_burp_extend:
            new_burp_url = "http://{}".format(burp_url)
        else:
            new_burp_url = "http://{}.{}".format(hostname, burp_url)

        testdata.append([hostname, url, method, new_burp_url, timeout])

    return testdata
