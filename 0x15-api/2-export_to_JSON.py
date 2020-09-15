#!/usr/bin/python3
"""Gather data from an API"""

from sys import argv
import json
import requests


DOMAIN = "https://jsonplaceholder.typicode.com"


def employee_name(user_id):
    """Gets the name of the employee"""
    URL = "{}/users/{}".format(DOMAIN, user_id)
    req = requests.get(URL)
    mydict = req.json()
    EMPLOYEE_NAME = mydict.get("username")
    if EMPLOYEE_NAME is None:
        exit()
    return (EMPLOYEE_NAME)


def total_tasks_by_id(user_id):
    """Function that returns total number of tasks by id,
        which is the sum of completed and non-completed tasks
    """
    URL = "{}/users/{}/todos".format(DOMAIN, user_id)
    req = requests.get(URL)
    mydict = req.json()
    return mydict


def completed_tasks(user_id):
    """Function that returns number of completed tasks
    https://jsonplaceholder.typicode.com/users/2/todos?completed=true"""

    URL = "{}/users/{}/todos?completed=true".format(DOMAIN, user_id)
    req = requests.get(URL)
    mydict = req.json()
    NUMBER_OF_DONE_TASKS = len(mydict)
    return (NUMBER_OF_DONE_TASKS)


def tasks_name(user_id):
    """Gets the name of the employee"""
    URL = "{}/users/{}/todos?completed=true".format(DOMAIN, user_id)
    req = requests.get(URL)
    list_of_dicts = req.json()
    completed_tasks_titles = []
    for dictionary in list_of_dicts:
        completed_tasks_titles.append(dictionary["title"])
    return completed_tasks_titles


def constructor(user_id):
    """display on the standard output the employee TODO list progress"""
    username = employee_name(user_id)
    dict_total_tasks = total_tasks_by_id(user_id)
    create_json(user_id, username, dict_total_tasks)


def create_json(user_id, username, dict_total_tasks):
    """Function to create a json file"""

    my_object = {}
    list_of_dicts = []
    for task in dict_total_tasks:
        list_of_dicts.append({"task": task.get("title"),
                              "completed": task.get("completed"),
                              "username": username})
    my_object[user_id] = list_of_dicts

    with open("{}.json".format(user_id), mode='w',
              encoding='UTF8') as filename:
        json.dump(my_object, filename)


if __name__ == "__main__":
    if len(argv) == 2 and argv[1].isdigit():
        user_id = int(argv[1])
        constructor(user_id)
