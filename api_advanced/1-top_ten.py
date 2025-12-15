#!/usr/bin/python3
"""Defines a function to print the top ten hot posts of a subreddit"""
import requests


def top_ten(subreddit):
    """Prints the titles of the top ten hot posts for a subreddit"""
    URL = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    HEADERS = {"User-Agent": "python:top.ten.script:v1.0 (by /u/anonymous)"}

    try:
        RESPONSE = requests.get(URL, headers=HEADERS, allow_redirects=False, timeout=10)
        HOT_POSTS = RESPONSE.json().get("data", {}).get("children", [])
        [print(post.get("data", {}).get("title")) for post in HOT_POSTS]
    except Exception:
        print(None)