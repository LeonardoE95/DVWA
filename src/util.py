#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

from conf import USERNAME, PASSWORD, BASE_URL, PHP_ID, PROXIES

# ----------------------------------------------

# NOTE: this function must be called everytime you restart the docker
# image in order to initialize the database, otherwise the subsequent
# attacks will not work.
# 
def init_app():
    global USERNAME, PASSWORD, BASE_URL, PHP_ID
    
    if not PHP_ID:
        PHP_ID = get_auth_cookie(BASE_URL, USERNAME, PASSWORD)

    url = BASE_URL + "/setup.php"
        
    # extract CSRF token
    custom_headers = { "Cookie": f"PHPSESSID={PHP_ID}; security=low" }    
    r = requests.get(url, headers=custom_headers)
    soup = BeautifulSoup(r.text, "html.parser")
    csrf_token = soup.find("input", {"name": "user_token"})['value']

    # perform DB init
    custom_headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": f"PHPSESSID={PHP_ID}; security=low",
    }
    post_data = f"create_db=Create+%2F+Reset+Database&user_token={csrf_token}"
    r = requests.post(url, headers=custom_headers, data=post_data)

    # check status of DB init
    custom_headers = {
        "Referer": url,
        "Cookie": f"PHPSESSID={PHP_ID}; security=low",
    }
    r = requests.get(url, headers=custom_headers)
    
    return "Database has been created." in r.text 

# ----------------------------------------------

# Performs the basic login to get an authenticated PHPSESSID value,
# which is then return and can be used for further requests.
# 
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

# ----------------------------------------------
    
def http_get(url, difficulty, headers=None, params=None, cookies=None, timeout=None):
    global PHP_ID, USERNAME, PASSWORD
    
    if not PHP_ID:
        PHP_ID = get_auth_cookie(URL, USERNAME, PASSWORD)

    if difficulty not in ["low", "medium", "high"]:
        print(f"[ERROR]: difficulty value ({difficulty}) not supported")
        exit()
        
    custom_headers = {
        "Cookie": f"PHPSESSID={PHP_ID}; security={difficulty};" + create_cookie(cookies),
    }
    
    return requests.get(url, headers=custom_headers, params=params, timeout=timeout)

# ----------------------------------------------

def http_post(url, difficulty, headers=None, data=None, cookies=None, timeout=None):
    global PHP_ID, USERNAME, PASSWORD
    
    if not PHP_ID:
        PHP_ID = get_auth_cookie(URL, USERNAME, PASSWORD)

    if difficulty not in ["low", "medium", "high"]:
        print(f"[ERROR]: difficulty value ({difficulty}) not supported")
        exit()
        
    custom_headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": f"PHPSESSID={PHP_ID}; security={difficulty};" + create_cookie(cookies),
    }
    
    return requests.post(url, headers=custom_headers, data=data, timeout=timeout)

def create_cookie(cookies):
    return ";".join([f"{key}={cookies[key]}" for key in cookies])
