#!/bin/bash
# Requesting response from server to display message
curl -s 0.0.0.0:5000/catch_me -X PUT -Ld "user_id=98" -H "Origin: HolbertonSchool"
