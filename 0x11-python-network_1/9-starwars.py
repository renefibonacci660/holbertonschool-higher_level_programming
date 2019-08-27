#!/usr/bin/python3
# Takes a string and sends search request to Star Wars API
# Uses string as search value of request
# Body Response is JSON and converted to Pythn dict
import sys
import requests

if __name__ == "__main__":
    searchItem = {"search": sys.argv[1]}
    url = "https://swapi.co/api/people"
    response = requests.get(url, params=searchItem)
    jsonResponse = response.json()
    print("Number of results: {}".format(jsonResponse["count"]))
    for result in jsonResponse["results"]:
        print(result["name"])
