#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

from sqli.low import sqli_low
from sqli.medium import sqli_medium
from sqli.high import sqli_high

from sqli_blind.low import sqli_blind_low
from sqli_blind.medium import sqli_blind_medium

from util import init_app

# --------------------------------

def main():
    init_app()

    # -----------------------------
    # sqli_low()
    # sqli_medium()
    # sqli_high()

    # -----------------------------
    # sqli_blind_low()
    # sqli_blind_medium()
    
if __name__ == "__main__":
    main()
