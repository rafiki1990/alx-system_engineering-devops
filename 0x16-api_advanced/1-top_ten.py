#!/usr/bin/python3
"""Return the top 10 hot topic."""

import requests


def top_ten(subreddit):
    """
    Query the Reddit API and print the titles of the first
    10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?"
    headers = {
        "User-Agent": "rugema3/1.0"
    }

    params = {"limit": 10}

    try:
        response = requests.get(
                url,
                headers=headers,
                params=params,
                allow_redirects=False
                )

        # Check if the subreddit is invalid (HTTP status code 404)
        if response.status_code == 404:
            print("None")
            return

        data = response.json()
        posts = data['data']['children']

        if not posts:
            print("No hot posts found in this subreddit.")
            return

        for i, post in enumerate(posts):
            print(f"{post['data']['title']}")

    except Exception as e:
        print(f"An error occurred: {e}")
