#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles of
the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """Function that queries the Reddit API and prints the titles of
    the first 10 hot posts"""
    URL = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "iOSJulian:myappJulian:v1 (by /u/julianfrancor)"}
    req = requests.get(URL, headers=headers)
    about_dictionary = req.json()
    data = about_dictionary.get('data')
    if data is None:
        print("None")
        return
    childrens = data.get('children')
    if childrens is None:
        print("None")
        return
    for children in childrens:
        myTitle = children.get('data').get('title')
        print(myTitle)
