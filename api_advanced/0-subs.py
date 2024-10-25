#!/usr/bin/python3
"""
0-subs.py

This module queries the Reddit API and returns the number of subscribers


libraries:
            - requests

Returns:
    _type_: _description_

author: Aimable
year: oct / 2024
"""

import requests


def number_of_subscribers(subreddit):
    """_summary_

    Args:
        d (str): a subreddit

    Returns:
        int: the total number of subscribers of a given subreddit
    """
    url = "https://reddit.com/r/{}/about.json".format(subreddit)

    response = requests.get(url)
    try:
        content = response.json()
        subs = content["data"]["subscribers"]
        return subs
    except:
        return 0
