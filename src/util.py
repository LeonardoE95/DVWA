#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

def get_auth_cookie(url, username, password):
    # -----------------------------
    # first, we get the PHPSESSID cookie
    url = url + "/login.php"
    r = requests.get(url)

    # extract PHPSESSID cookie and CSRF token
    cookies = r.headers['Set-Cookie']
    php_id = cookies.split(";")[0].split("=")[1]

    soup = BeautifulSoup(r.text, "html.parser")
    csrf_token = soup.find("input", {"name": "user_token"})['value']
    
    # -----------------------------
    # then we perform the login
    url = url + "/login.php"
    custom_headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": f"PHPSESSID={php_id}; security=low",
    }
    post_data = f"username={username}&password={password}&Login=Login&user_token={csrf_token}"
    r = requests.post(url, headers=custom_headers, data=post_data)

    return php_id
