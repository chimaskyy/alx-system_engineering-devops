#!/usr/bin/python3
"""
this script is a recursive function that queries
the Reddit API and returns a list containing the
titles of all hot articles for a given subreddit.
If no results are found for the given subreddit,
the function should return None.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):

    """Use recursion to get all hot articles from a subreddit"""

    if not subreddit:
        return (None)
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    headers = {"User-Agent": "Google Chrome Version 122.0.6261.95"}
    params = {'after': after, 'count': 10}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        after = data.get('after')

        if after:
            recurse(subreddit, hot_list, after)

        titles = data['data']['children']
        for title in titles:
            hot = title['data']['title']
            hot_list.append(hot)

        return len(hot_list)
    else:
        return (None)

