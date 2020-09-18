#!/usr/bin/python3
"""recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit.
    If no results are found for the given subreddit, the function should
    return None."""

    URL = "https://www.reddit.com/r/{}/hot.json?after={}".format(
        subreddit, after)
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
        hot_list.append(children['data']['title'])
    af = data.get('after')
    if af is not None:
        return recurse(subreddit, hot_list, af)
    return(hot_list)
