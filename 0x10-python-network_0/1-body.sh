#!/bin/bash
# Takes a URL, sends a GET request to the URL, and displays the body of the response
curl -s -L "${1}"
