#!/bin/bash
# sends a DELETE request to URL passed and displays body of response
curl -sLX DELETE "$1"
