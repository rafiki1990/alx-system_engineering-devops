#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""
import json
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Retrieve the employee's TODO list and export it to a JSON file.

    Args:
        employee_id (int): The ID of the employee for whom you want to fetch
        the TODO list.

    Returns:
        None: This function exports the data to a JSON file.
    """
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(employee_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": employee_id}).json()

    # Define the JSON file name as USER_ID.json
    json_file_name = f"{employee_id}.json"

    # Create a dictionary with the user's ID as the key and a list of tasks
    user_tasks = {
        str(employee_id): [
            {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": username,
            }
            for todo in todos
        ]
    }

    # Write the dictionary to the JSON file
    with open(json_file_name, "w") as json_file:
        json.dump(user_tasks, json_file, indent=4)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
