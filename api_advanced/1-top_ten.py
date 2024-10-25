#!/usr/bin/python3
"""
Description:
    function that fetched data from a reddit api
    and prints titles of the first 10 article
"""
import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts listed in a subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=9".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    posts = response.json()["data"]["children"]
    for post in posts:
        print(post["data"]["title"])

    posts = response.json().get("data", {}).get("children", [])
    for item in posts:
        print(item.get("data", {}).get("title", None))
