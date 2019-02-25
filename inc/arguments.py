#!/usr/bin/env python
# coding: utf8

import argparse


def getArguments():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-b", "--burp-url",
        help="burpurl",
        type=str,
        dest="burpurl",
        default=None,
        required=True
    )

    parser.add_argument(
        "-wbe", "--without-burp-extension",
        help="Do not prepend hostname before burpurl",
        dest="burp_extend",
        default=False,
        action='store_true'
    )

    parser.add_argument(
        "-u", "--urllist",
        help="Path to url list",
        type=str,
        dest="urllist",
        required=True
    )

    parser.add_argument(
        "-t", "--threads",
        help="Max. threads, default: 5",
        type=int,
        dest="max_threads",
        default=5
    )

    parser.add_argument(
        "-to", "--timeout",
        help="Timeout in seconds for each request, default: 3",
        type=int,
        dest="timeout",
        default=3
    )

    parser.add_argument(
        "-m", "--method",
        help="HTTP method, default: GET",
        type=str,
        dest="method",
        default="GET",
        choices=[
            "GET",
            "get",
            "POST",
            "post",
            "HEAD",
            "head"
            "PUT",
            "put",
            "OPTIONS",
            "options",
            "DELETE",
            "delete",
        ]
    )

    args = parser.parse_args()

    return args.burpurl, args.burp_extend, args.urllist, args.max_threads, args.method, args.timeout
