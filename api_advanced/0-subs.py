#!/usr/bin/python3
"""
Module that contains a function to get the number of subscribers
for a given Reddit subreddit using the Reddit API.
"""

import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "python-script"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    data = response.json()
    return data["data"]["subscribers"]
