#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

from conf import URL

from sqli.low import sqli_low, PAYLOADS as SQLI_LOW_PAYLOADS
from sqli.medium import sqli_medium, PAYLOADS as SQLI_MEDIUM_PAYLOADS
from sqli.high import sqli_high, PAYLOADS as SQLI_HIGH_PAYLOADS

from sqli_blind.low import sqli_blind_low

from util import init_app

# --------------------------------

def main():
    init_app()

    # -----------------------------
    # sqli_low(URL, SQLI_LOW_PAYLOADS)
    # sqli_medium(URL, SQLI_MEDIUM_PAYLOADS)
    # sqli_high(URL, SQLI_HIGH_PAYLOADS)

    # -----------------------------
    sqli_blind_low(URL)
    
if __name__ == "__main__":
    main()
