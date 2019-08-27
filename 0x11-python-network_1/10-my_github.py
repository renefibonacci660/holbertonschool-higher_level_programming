#!/usr/bin/python3
# Takes Github credentials (un & pw) and uses Github API to display "id"
import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, password))
    try:
        print(response.json()["id"])
    except KeyError:
        print("None")
