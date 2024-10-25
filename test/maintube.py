#!/usr/bin/python3
"""
Description:
    function that fetches data from a reddit api
    and stores the titles of the all articles
Return:
    list: list of all titles
"""
import requests


def check_word_count(words_to_search, word_trash):
    words_to_search = sorted(words_to_search)
    print(len(word_trash))
    print(word_trash[:10])
    for word in words_to_search:
        if word in word_trash:
            print(word)
            count = 0
            for item in word_trash:
                if word == item:
                    count += 1
            print(word, ":", count)
        else:
            continue


def count_words(subreddit, word_list=[]):
    """extracts the titles of the hot posts listed in a subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return None

    response = response.json()
    posts = response.get("data", {}).get("children", [])

    hot_list = []
    for item in posts:
        hot_list.append(item.get("data", {}).get("title", None))

    # create a trash
    word_trash = []
    for title in hot_list:
        title_words = title.split(" ")
        for word in title_words:
            word_trash.append(word)

    check_word_count(word_list, word_trash)


count_words(
    "programming",
    ["react", "python", "java", "javascript" "scala", "no_results_for_this_one", "the"],
)
