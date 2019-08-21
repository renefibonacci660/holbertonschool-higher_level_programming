#!/bin/bash
# Gives only status code of passed in URL
curl -so /dev/null -w "%{http_code}" "$1"
