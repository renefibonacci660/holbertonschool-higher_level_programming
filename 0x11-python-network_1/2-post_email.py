#!/usr/bin/python3
# Takes a URL and email from system
# Sends post request with urlopen
# decodes with utf-8

import sys
from urllib.request import Request, urlopen
from urllib.parse import urlencode

if __name__ == "__main__":
    url = sys.argv[1]
    email = urlencode({'email': sys.argv[2]})
    data = email.encode('ascii')
    postreq = Request(url, data)

    with urlopen(postreq) as request:
        response = request.read()
    print(response.decode("utf-8"))
