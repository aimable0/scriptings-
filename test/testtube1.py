#!/usr/bin/python3
"""
Description:
    function that fetched data from a reddit api
    and prints titles of the first 10 article
"""
import requests


def recurse(subreddit, hot_list=[]):
    """prints the titles of the first 10 hot posts listed in a subreddit"""
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
