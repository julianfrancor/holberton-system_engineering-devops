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

    URL = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "iOSJulian:myappJulian:v1 (by /u/julianfrancor)"}
    payload = {'after': after}

    response = requests.get(URL, headers=headers, params=payload)

    mydictionary = response.json()
    data = mydictionary.get('data')
    if data is None:
        return None
    after_value = data.get('after')
    if after_value is None:
        return(hot_list)
    childrens = data.get('children')
    if childrens is None:
        return None

    for children in childrens:
        hot_list.append(children['data']['title'])
    return recurse(subreddit, hot_list, after_value)
