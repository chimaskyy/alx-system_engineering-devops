#!/usr/bin/python3
"""
This script queries the Reddit API and
prints the titles of the first 10 hot
posts listed for a given subreddit.
"""


import requests


def top_ten(subreddit):
    """Query Reddit API for a givrn subreddit"""

    if subreddit is None:
        print("None")

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-agent": "Google Chrome Version 122.0.6261.95"}
    params = {'limit': 10}
    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    try:
        all_post = data['data']['children']

        for post in all_post:
            post_title = post['data']['title']
            print(post_title)

    except Exception:
        print("None")
