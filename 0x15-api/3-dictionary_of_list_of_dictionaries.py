#!/usr/bin/python3
"""Gather data from an API"""

from sys import argv
import json
import requests


def connection():
    """connection to the API"""
    full_tasks = requests.get("https://jsonplaceholder.typicode.com/todos")
    full_users = requests.get("https://jsonplaceholder.typicode.com/users")

    total_tasks = full_tasks.json()
    total_users = full_users.json()
    return total_tasks, total_users


def constructor():
    """display on the standard output the employee TODO list progress"""
    all_tasks, all_users = connection()
    create_json(all_tasks, all_users)


def create_json(all_tasks, all_users):
    """Function to create a json file"""

    my_object = {}
    for user in all_users:
        list_of_dicts = []
        for task in all_tasks:
            if task.get("userId") == user.get("id"):
                list_of_dicts.append({"username": user.get("username"),
                                      "task": task.get("title"),
                                      "completed": task.get("completed")})
        my_object[user.get("id")] = list_of_dicts

    with open("todo_all_employees.json", mode='w',
              encoding='UTF8') as filename:
        json.dump(my_object, filename)


if __name__ == "__main__":
    constructor()
