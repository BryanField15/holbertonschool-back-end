#!/usr/bin/python3
"""Script that shows the progress of a to do list"""
import json
import requests
import sys


if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/"
    user_todos = requests.get(f"{url}users/{sys.argv[1]}/todos").json()
    user_info = requests.get(f"{url}users/{sys.argv[1]}").json()

    user_id = str(sys.argv[1])
    username = user_info.get("username")

    task_list = []
    for todo in user_todos:
        tasks = {
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": username
        }
        task_list.append(tasks)

    final_dict = {
         user_id: task_list
    }

    filename = user_id + ".json"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(final_dict))
