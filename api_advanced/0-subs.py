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
    Fetches the total number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The total number of subscribers, or 0 if the subreddit is invalid.
    """
    URL = f"https://reddit.com/r/{subreddit}/about.json"
    HEADERS = {"User-Agent": "PostmanRuntime/7.35.0"}

    try:
        RESPONSE = requests.get(URL, headers=HEADERS, allow_redirects=False)
        subs = RESPONSE.json()["data"]["subscribers"]
        return subs
    except Exception:
        return 0
