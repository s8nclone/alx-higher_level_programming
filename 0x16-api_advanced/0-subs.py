#!/usr/bin/python3
"""
Function that queries the Reddit API and returns 
Subscribers for a given Reddit subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """Returns total number of subscribers on a given subreddit."""
    link = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(link, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    res = response.json().get("data")
    return res.get("subscribers")
