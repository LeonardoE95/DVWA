#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

from conf import URL

from sqli.easy import sqli_easy, PAYLOADS as SQLI_EASY_PAYLOADS
from sqli.medium import sqli_medium, PAYLOADS as SQLI_MEDIUM_PAYLOADS
from sqli.hard import sqli_hard, PAYLOADS as SQLI_HARD_PAYLOADS

# --------------------------------

def main():
    # sqli_easy(URL, SQLI_EASY_PAYLOADS)
    # sqli_medium(URL, SQLI_MEDIUM_PAYLOADS)
    # sqli_hard(URL, SQLI_HARD_PAYLOADS)

    # -----------------------------
    
if __name__ == "__main__":
    main()
