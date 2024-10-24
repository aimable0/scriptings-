#!/usr/bin/python3
"""
0-subs.py

This module queries the Reddit API and returns the number of subscribers
URL: https://reddit.com

Libraries:
        - requests

Returns:
    int: total number of subscribers of a given subreddit

Author: Aimable
Date: oct / 2024
"""

import requests


def number_of_subscribers(subreddit):
    """
    The main function that fetches data
    and returns total number of subs of a subreddit

    Args:
        d (str): a subreddit

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
