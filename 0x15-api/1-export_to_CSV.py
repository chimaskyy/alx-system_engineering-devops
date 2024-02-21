#!/usr/bin/python3
"""
This module uses the REST API of JSONPlaceholder
of a givin employee ID, returns his/her TODO
list progress and write into csv file
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

        emp_usrname = user.get('username')
        csv_file = f"{user_id}.csv"
        with open(csv_file, 'w', encoding="utf8") as file:
            for task in tasks:
                file.write('"{}","{}","{}","{}"\n'
                           .format(user_id, emp_usrname,
                                   task['completed'], task['title']))


if __name__ == "__main__":
    todo()
