#!/usr/bin/env python
# coding: utf8
import os
import sys


def get_urls(url_list):
    if not os.path.exists(url_list):
        print("\033[31m[ x ]\033[0m No list full of juicy urls found...")
        sys.exit(1)

    urls = open(url_list, "r").read().splitlines()

    if len(urls) == 0:
        print("\033[31m[ x ]\033[0m List seems to be empty...")
        sys.exit(1)

    return urls
