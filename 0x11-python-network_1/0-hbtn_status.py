#!/usr/bin/python3
# Fetches URL and displays body of response

import urllib.request
with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        htmlpage = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(htmlpage)))
        print("\t- content: {}".format(htmlpage))
        print("\t- utf8 content: {}".format(htmlpage))
