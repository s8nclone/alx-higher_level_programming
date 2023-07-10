#!/bin/bash
# Makes a request to a specific url that causes the server to respond with a specific message
curl -sL 0.0.0.0:5000/catch_me_3 -X PUT -H "Origin:HolbertonSchool"
