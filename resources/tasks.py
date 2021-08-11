import requests
import json

BASE_URL = 'http://127.0.0.1:5000'
AUTH = ('miguel', 'python')


def reset_tasks_list():
    url = BASE_URL + "/todo/api/v1.0/tasks/reset"
    response = requests.get(url=url, auth = AUTH)
    return response.json()['tasks']


def read_tasks_authorized():
    url = BASE_URL + "/todo/api/v1.0/tasks"
    response = requests.get(url=url, auth=AUTH)
    return response.json()['tasks']


def create_task_authorized(json):
    url = BASE_URL + "/todo/api/v1.0/tasks"
    response_new_task = requests.post(url=url, auth=AUTH, json=json)
    return response_new_task.json()['task']


def update_task_authorized(id, json):
    url = BASE_URL + f"/todo/api/v1.0/tasks/{id}"
    response = requests.put(url=url, auth=AUTH, json=json)
    return response.json()['task']


def delete_task_authorized(id):
    url = BASE_URL + f"/todo/api/v1.0/tasks/{id}"
    response = requests.delete(url=url, auth=AUTH)
    return response.json()['result']


def read_tasks_unauthorized():
    url = BASE_URL + "/todo/api/v1.0/tasks"
    response = requests.get(url=url)
    return response.json()


def create_task_unauthorized(json):
    url = BASE_URL + "/todo/api/v1.0/tasks"
    response_new_task = requests.post(url=url, json=json)
    return response_new_task.json()


def update_task_unauthorized(id, json):
    url = BASE_URL + f"/todo/api/v1.0/tasks/{id}"
    response = requests.put(url=url, json=json)
    return response.json()


def delete_task_unauthorized(id):
    url = BASE_URL + f"/todo/api/v1.0/tasks/{id}"
    response = requests.delete(url=url)
    return response.json()
