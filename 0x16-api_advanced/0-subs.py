#!/usr/bin/python3
"""Querry number of subscribers."""
import requests

# Reddit API credentials
user_agent = 'rugema3/1.0'


def number_of_subscribers(subreddit):
    """
    Query the Reddit API and return the number of subscribers
    for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers for the subreddit,
        or 0 if the subreddit is invalid or an error occurs.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": user_agent
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the subreddit is invalid (HTTP status code 404)
        if response.status_code == 404:
            return 0

        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
