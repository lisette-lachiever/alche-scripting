#!/usr/bin/python3
"""Prints the titles of the first 10 hot posts for a given subreddit."""

import requests


def top_ten(subreddit):
    """Prints the first 10 hot post titles of a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "python:top.ten.script:v1.0 (by /u/anonymous)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False, timeout=10)
        if response.status_code != 200:
            print(None)
            return

        data = response.json()
        posts = data["data"]["children"]

        for post in posts:
            print(post["data"]["title"])

    except requests.RequestException:
        print(None)