#!/usr/bin/python3
"""Exports to-do list information for all employees to JSON format."""
import json
import requests


def get_all_employees_todo_progress():
    """
    Retrieve the TODO lists for all employees and export them to a
    single JSON file.

    Returns:
        None: This function exports the data to a JSON file.
    """
    url = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(url).json()

    all_employee_tasks = {}

    for user in users:
        user_id = str(user["id"])
        username = user["username"]

        todos = requests.get(url + f"/{user_id}/todos").json()

        user_tasks = [
            {
                "username": username,
                "task": todo["title"],
                "completed": todo["completed"]
            }
            for todo in todos
        ]

        all_employee_tasks[user_id] = user_tasks

    # Write the dictionary to the JSON file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_employee_tasks, json_file, indent=4)


if __name__ == "__main__":
    get_all_employees_todo_progress()
