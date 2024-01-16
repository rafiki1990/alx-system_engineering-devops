#!/usr/bin/python3
"""Return the results using recurssive functions."""
import requests


def recurse(subreddit, hot_list=None, after="", count=0):
    """
    Recursively query the Reddit API and count the total number of hot
    articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
        after (str): A token for pagination (used for recursion).
        total_count (int): The count of hot articles (used for recursion).

    Returns:
        int or None: The total count of hot articles or None if
        no results are found.
    """
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "rugema3/1.0"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 30
    }

    try:
        response = requests.get(
                url,
                headers=headers,
                params=params,
                allow_redirects=False
                )

        if response.status_code == 404:
            return None

        results = response.json().get("data")
        after = results.get("after")
        count += results.get("dist")
        for child in results.get("children"):
            hot_list.append(child.get("data").get("title"))

        if after is not None:
            return recurse(subreddit, hot_list, after, count)
        return hot_list

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
