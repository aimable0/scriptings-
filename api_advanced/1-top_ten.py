#!/usr/bin/python3
"""
Description:
    function that fetched data from a reddit api
    and prints titles of the first 10 article
"""
import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    response = requests.get(url, allow_redirects=False)
    try:
        content = response.json()
        for i in range(10):
            title = (
                content.get("data", {})
                .get("children", [])[i]
                .get("data", {})
                .get("title", "No title")
            )
            print(title)
    except:
        print(None)
