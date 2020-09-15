#!/usr/bin/python3
"""Gather data from an API"""

import requests
from sys import argv


DOMAIN = "https://jsonplaceholder.typicode.com"


def employee_name(user_id):
    """Gets the name of the employee"""
    URL = "{}/users/{}".format(DOMAIN, user_id)
    req = requests.get(URL)
    mydict = req.json()
    EMPLOYEE_NAME = mydict.get("name")
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
    TOTAL_NUMBER_OF_TASKS = len(mydict)
    return(TOTAL_NUMBER_OF_TASKS)


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
    name = employee_name(user_id)
    total_tasks = total_tasks_by_id(user_id)
    done_tasks = completed_tasks(user_id)
    list_tasks_titles = tasks_name(user_id)
    """Employee EMPLOYEE_NAME is done with tasks
    (NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):\n  TASK_TITLE"""
    message = "Employee {} is done with tasks({}/{}):".format(
        name, done_tasks, total_tasks)
    print(message)
    for TASK_NAME in list_tasks_titles:
        print("\t {}".format(TASK_NAME))


if __name__ == "__main__":
    if len(argv) == 2 and argv[1].isdigit():
        user_id = int(argv[1])
        constructor(user_id)
