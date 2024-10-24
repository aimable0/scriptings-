#!/usr/bin/python3
"""
0-subs.py

This module extracts data from:
URL: https://reddit.com

Libraries used:
            - reqeusts

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
