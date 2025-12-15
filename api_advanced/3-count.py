#!/usr/bin/python3
"""
Queries the Reddit API recursively and prints a sorted count of
given keywords found in hot post titles of a subreddit.
"""

import requests


def count_words(subreddit, word_list, after=None, counts={}):
    if not counts:
        for w in word_list:
            w = w.lower()
            counts[w] = counts.get(w, 0)

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "python-script"}
    params = {"after": after}

    r = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if r.status_code != 200:
        return

    data = r.json()["data"]

    for post in data["children"]:
        for word in post["data"]["title"].lower().split():
            if word in counts:
                counts[word] += 1

    if data["after"]:
        return count_words(subreddit, word_list, data["after"], counts)

    for word, count in sorted(
        [(k, v) for k, v in counts.items() if v > 0],
        key=lambda x: (-x[1], x[0])
    ):
        print(f"{word}: {count}")
