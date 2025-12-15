#!/usr/bin/python3
"""
Returns a list of titles of all hot articles for a given subreddit
using recursion.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "python-script"}
    params = {"after": after}

    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
    )

    if response.status_code != 200:
        return None

    data = response.json()
    posts = data["data"]["children"]

    if not posts:
        return hot_list

    for post in posts:
        hot_list.append(post["data"]["title"])

    after = data["data"]["after"]

    if after is None:
        return hot_list

    return recurse(subreddit, hot_list, after)
