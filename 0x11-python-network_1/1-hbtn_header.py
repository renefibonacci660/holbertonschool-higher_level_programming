#!/usr/bin/python3
# Grabs URL from sys input
# Opens url and checks for X-Request-Id in getheaders()
# Prints arg after X-Request-Id if found "data[1]"

import sys
import urllib.request

if __name__ == "__main__":

    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        for data in response.getheaders():
            if data[0] == "X-Request-Id":
                print(data[1])
