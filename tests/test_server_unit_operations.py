from resources import tasks


def test_read_tasks_authorized():
    # GIVEN
    tasks.reset_tasks_list()

    # WHEN
    start_tasks = tasks.read_tasks_authorized()

    # THEN
    assert (len(start_tasks) == 2)
    assert start_tasks[0]['title'] == 'Buy groceries'
    assert start_tasks[0]['description'] == 'Milk, Cheese, Pizza, Fruit, Tylenol'
    assert start_tasks[0]['done'] == False
    assert start_tasks[1]['title'] == 'Learn Python'
    assert start_tasks[1][
            'description'] == 'Need to find a good Python tutorial on the web'
    assert start_tasks[1]['done'] == False


def test_create_task_authorized():
    # GIVEN
    tasks.reset_tasks_list()
    start_tasks = tasks.read_tasks_authorized()
    json = {
        "description": "Make gym on stadium",
        "done": False,
        "title": "Make gym"
    }

    # WHEN
    new_task = tasks.create_task_authorized(json)
    tasks_after_create = tasks.read_tasks_authorized()
    json['uri'] = new_task['uri']

    # THEN
    assert len(tasks_after_create) == len(start_tasks) + 1
    assert tasks_after_create[0] == start_tasks[0]
    assert tasks_after_create[1] == start_tasks[1]
    assert tasks_after_create[2] == json


def test_update_task_authorized():
    # GIVEN
    tasks.reset_tasks_list()
    start_tasks = tasks.read_tasks_authorized()
    json = {
        "description": "Make gym on stadium",
        "done": False,
        "title": "Make gym"
    }
    new_task = tasks.create_task_authorized(json)
    json_for_update = {
        "description": "Gym on fresh air",
    }

    # WHEN
    tasks.update_task_authorized(2, json_for_update)
    tasks_after_update = tasks.read_tasks_authorized()
    json['uri'] = tasks_after_update[2]['uri']

    # THEN
    assert len(tasks_after_update) == len(start_tasks) + 1
    assert tasks_after_update[0] == start_tasks[0]
    assert tasks_after_update[1]['description'] == json_for_update['description']
    assert tasks_after_update[2] == json


def test_delete_task_authorized():
    # GIVEN
    tasks.reset_tasks_list()
    start_tasks = tasks.read_tasks_authorized()
    json = {
        "description": "Make gym on stadium",
        "done": False,
        "title": "Make gym"
    }
    tasks.create_task_authorized(json)
    tasks_after_create = tasks.read_tasks_authorized()

    # WHEN
    response_deleted = tasks.delete_task_authorized(2)
    tasks_after_delete = tasks.read_tasks_authorized()

    # THEN
    assert response_deleted == True
    assert len(tasks_after_delete) == len(start_tasks)
    assert tasks_after_delete[0] == tasks_after_create[0]
    assert tasks_after_delete[1] == tasks_after_create[2]


def test_read_tasks_unauthorized():
    response = tasks.read_tasks_unauthorized()
    assert response['error'] == 'Unauthorized access'


def test_create_task_unauthorized():
    json = {
        "description": "Make gym on stadium",
        "done": False,
        "title": "Make gym"
    }
    response = tasks.create_task_unauthorized(json)
    assert response['error'] == 'Unauthorized access'


def test_update_task_unauthorized():
    json = {"description": "Gym on fresh air"}
    response = tasks.update_task_unauthorized(2, json)
    assert response['error'] == 'Unauthorized access'


def test_delete_task_unauthorized():
    response = tasks.delete_task_unauthorized(2)
    assert response['error'] == 'Unauthorized access'
