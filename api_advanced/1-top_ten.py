#!/usr/bin/python3
"""
Prints the titles of the first 10 hot posts for a given subreddit.
"""

import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "python-script"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    data = response.json()
    posts = data["data"]["children"]

    for post in posts:
        print(post["data"]["title"])
