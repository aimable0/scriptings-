#!/usr/bin/python3
"""
Description:
    function that fetched data from a reddit api
    and prints titles of the first 10 article
"""
import requests
import rich
import pathlib
import json


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts listed in a subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=9".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    response = response.json()
    posts = response.get("data", {}).get("children", [])
    for item in posts:
        print(item.get("data", {}).get("title", None))
