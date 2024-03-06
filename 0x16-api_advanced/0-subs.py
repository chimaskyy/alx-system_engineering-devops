#!/usr/bin/python3
"""
This script queries the Reddit API and
returns the number of subscribers for a
given subreddit. If an invalid subreddit is
given, the function should return 0.
"""

import requests
import sys


def number_of_subscribers(subreddit):
    """Query  Reddit API"""

    if subreddit is None:
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {"User-Agent": "MyTest"}

    response = requests.get(url, headers=headers)
    data = response.json()

    try:

        subscribers = data['data']['subscribers']
        return subscribers
    except Exception:
        return 0
