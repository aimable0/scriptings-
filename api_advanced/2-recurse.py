#!/usr/bin/python3
"""
Description:
    function that fetches data from a reddit api
    and stores the titles of the all articles
Return:
    list: list of all titles
"""
import requests


def recurse(subreddit, hot_list=[]):
    """extracts the titles of the hot posts listed in a subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return None

    response = response.json()
    posts = response.get("data", {}).get("children", [])
    for item in posts:
        hot_list.append(item.get("data", {}).get("title", None))
    return hot_list
