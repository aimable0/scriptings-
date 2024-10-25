#!/usr/bin/python3
"""
Description:
    function that fetched data from a reddit api
    and prints titles of the first 10 article
"""
import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

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
    except requests.RequestException:
        print("None")
