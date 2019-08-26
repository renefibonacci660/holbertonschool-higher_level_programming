#!/usr/bin/python3
#
#
#
import sys
from urllib.request import Request, urlopen
from urllib.error import HTTPError


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urlopen(Request(url)) as response:
            response = response.read()
            print(response.decode("utf-8"))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
