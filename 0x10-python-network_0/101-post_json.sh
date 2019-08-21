#!/bin/bash
# Sends JSON POST request to a URL passed as first argument
curl -sH "Content-Type: application/json" "$1" -d @$2
