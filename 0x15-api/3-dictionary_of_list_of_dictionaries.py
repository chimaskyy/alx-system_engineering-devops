#!/usr/bin/python3
"""
This module uses the REST API of JSONPlaceholder
returns all employee task
list progress and dump in json file
"""


import json
import requests
import sys


def todo():
    """get employee todo list"""
    url_ = "https://jsonplaceholder.typicode.com/"
    all_user = requests.get(f"{url_}/users").json()

    json_file = "todo_all_employees.json"

    dict_of_todo = {}
    for user in all_user:
        user_id = user.get("id")
        emp_usrname = user.get('username')
        user_tasks = requests.get(f"{url_}/users/{user_id}/todos").json()

        dict_of_todo[user_id] = []
        for task in user_tasks:
            dict_of_todo[user_id].append({
                "username": emp_usrname,
                "task": task['title'],
                "completed": task['completed']
            })

        with open(json_file, 'w', encoding="utf8") as file:
            json.dump(dict_of_todo, file)


if __name__ == "__main__":
    todo()
