#!/usr/bin/python3
"""Return the number of subscribers of a given subreddit"""

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
    headers = {"User-Agent": "PostmanRuntime/7.35.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        subs = response.json()["data"]["subscribers"]
        return subs
    except Exception:
        return 0
