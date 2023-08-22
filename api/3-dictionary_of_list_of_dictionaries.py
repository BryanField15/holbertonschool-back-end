#!/usr/bin/python3
"""Script to export data in the JSON format"""
import json
import requests
import sys


if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/"
    all_todos = requests.get(f"{url}todos/").json()
    all_users = requests.get(f"{url}users/").json()

    final_dict = {}

    for user in all_users:
        user_id = user.get("id")
        user_name = user.get("username")

        user_related_todos = [
            todo for todo in all_todos if todo['userId'] == user_id
        ]

        task_list = []
        for todo in user_related_todos:
            tasks = {
                "username": user_name,
                "task": todo.get("title"),
                "completed": todo.get("completed"),
            }
            task_list.append(tasks)

            final_dict[user_id] = task_list

    filename = "todo_all_employees.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(final_dict, f)
