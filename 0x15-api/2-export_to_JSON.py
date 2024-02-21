#!/usr/bin/python3
"""
This module uses the REST API of JSONPlaceholder
of a givin employee ID, returns his/her TODO
list progress and dump in json file
"""


import json
import requests
import sys


def todo():
    """get employee todo list"""
    url_ = "https://jsonplaceholder.typicode.com/"
    if len(sys.argv) > 1:
        user_id = int(sys.argv[1])
        user = requests.get(f"{url_}/users/{user_id}").json()
        tasks = requests.get(f"{url_}/users/{user_id}/todos").json()

        emp_usrname = user.get('username')
        json_file = f"{user_id}.json"

        content_dict = {user_id: []}
        for task in tasks:
            content_dict[user_id].append({
                  "task": task['title'],
                  "completed": task['completed'],
                  "username": emp_usrname})

        with open(json_file, 'w', encoding="utf8") as file:
            json.dump(content_dict, file)
    else:
        print("No ID provided")


if __name__ == "__main__":
    todo()
