#!/usr/bin/python3
"""
0-subs.py

This module queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function returns 0.

Libraries used:
            - requests
Returns:
    on success: int (total subscribers)
    on failure: 0

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
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    response = requests.get(url, allow_redirects=False)
    try:
        total_subs = response.json()["data"]["subscribers"]
        return total_subs
    except:
        return 0
