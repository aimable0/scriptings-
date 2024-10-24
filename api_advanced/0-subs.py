#!/usr/bin/python3
"""
0-subs.py

This module queries the Reddit API and returns the number of subscribers
(not active users, total subscribers)
for a given subreddit. If an invalid subreddit is given,
the function should return 0.
URL: https://reddit.com

Libraries used:
            - reqeusts
Returns:
    on succes: int (total subs)
    on fail: 0

Author: Aimable
Date: October 2024
"""

import requests


def number_of_subscribers(subreddit):
    """
    The main function that fetches data
    and returns total number of subs of a subreddit

    Args:
        subreddit (str): a subreddit name

    Returns:
        int: the total number of subscribers of a given subreddit
    """
    url = f"https://reddit.com/r/{subreddit}/about.json"

    response = requests.get(url)
    try:
        content = response.json()
        subs = content["data"]["subscribers"]
        return subs
    except:
        return 0
