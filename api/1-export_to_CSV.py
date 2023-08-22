#!/usr/bin/python3
"""Script that shows the progress of a to do list"""
import csv
import json
import requests
import sys


if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/"
    user_todos = requests.get(f"{url}users/{sys.argv[1]}/todos").json()
    user_info = requests.get(f"{url}users/{sys.argv[1]}").json()

    for todo in user_todos:
        todo["username"] = user_info["username"]
        del todo["id"]

    user_id = sys.argv[1]
    with open(f"{user_id}.csv", 'w', newline='') as csv_file:
        fieldnames = ["userId", "username", "completed", "title"]
        writer = csv.DictWriter(csv_file,
                                fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)
        for row in user_todos:
            writer.writerow(row)
