#!/usr/bin/python3
# Takes in a URL and email address
# Sends POST request to passed URL
# Displays body of response

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email = {"email": sys.argv[2]}
    response = requests.post(url, email)
    print(response.text)
