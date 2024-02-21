#!/usr/bin/python3
"""
This module uses the REST API of JSONPlaceholder
of a givin employee ID, returns his/her TODO
list progress
"""

import requests
import sys


def todo():
    """get employee todo list"""
    url_ = "https://jsonplaceholder.typicode.com/"
    if len(sys.argv) > 1:
        user_id = int(sys.argv[1])
        user = requests.get(f"{url_}/users/{user_id}").json()
        tasks = requests.get(f"{url_}/users/{user_id}/todos").json()

        employee_name = user.get('name')
        num_task = len(tasks)
        task_completed = 0

        for task_ in tasks:
            if task_["completed"] is True:
                task_completed += 1
        print(f"Employee {employee_name} is\
              done with tasks {task_completed}/{num_task}:")
        for task_ in tasks:
            if task_["completed"] is True:
                print(f"\t {task_['title']}")
    else:
        print("No ID provided")


if __name__ == "__main__":
    todo()
