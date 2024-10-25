#!/usr/bin/python3
"""
Description:
    function that fetches data from a reddit api
    and stores the titles of the all articles
Return:
    list: list of all titles
"""
import requests


def count_words(
    subreddit,
    word_list,
    words_dict={},
    after=None,
):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"limit": "100", "after": after}

    # send the request
    response = requests.get(url, params=params, allow_redirects=False)

    # check for invalid subreddit
    if response.status_code != 200:
        return None

    posts = response.json().get("data", {}).get("children", [])

    # save the titles to a list
    for post in posts:
        title = post["data"]["title"]
        title_words = title.split(" ")
        for word in word_list:
            if word in title_words:
                for title_word in title_words:
                    if word == title_word:
                        words_dict[word] = words_dict.get(word, 0) + 1
                    else:
                        continue
            else:
                continue

    after = response.json().get("data", {}).get("after", None)

    if after is not None:
        return count_words(subreddit, word_list, words_dict, after)
    else:
        # print the data...
        for word, count in words_dict.items():
            print(word, count)
