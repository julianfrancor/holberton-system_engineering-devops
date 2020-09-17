#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given
subreddit. If an invalid subreddit is given, the function should
return 0.
"""

import requests


def number_of_subscribers(subreddit):
    """Function that queries the Reddit API and
    returns the number of subscribers"""
    URL = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "iOSJulian:myappJulian:v1 (by /u/julianfrancor)"}
    req = requests.get(URL, headers=headers)
    about_dictionary = req.json()
    data = about_dictionary.get('data')
    if data is None:
        return 0
    total_subscribers = data.get('subscribers')
    if total_subscribers is None:
        return 0
    return total_subscribers
