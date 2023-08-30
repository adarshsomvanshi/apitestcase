import requests
import json

BASE_URL = "https://todo.pixegami.io/"

def test_can_call_endpoint():
    response = requests.get(BASE_URL)
    assert response.status_code == 200

def test_can_create_task():
    payload = new_payloads()
    response = create_task(payload)
    assert response.status_code == 200
    data = response.json()
    # print(data)

    task_id = data['task']['task_id']
    get_task_response = get_tasks(task_id)
    assert get_task_response.status_code == 200
    get_task = get_task_response.json()
    # print(response1.json())
    assert get_task['content'] == payload["content"]
    # assert get_task['content'] == 'My Content'
    assert get_task['user_id'] == payload["user_id"]

def test_can_update_task():
    payload = new_payloads()
    response = create_task(payload)
    assert response.status_code == 200
    task_id = response.json()['task']['task_id']
    new_payload = {
        'user_id': payload['user_id'],
        'task_id': task_id,
        'content':'Another Content',
        'is_done': True
    }
    update_response = update_task(new_payload)
    assert update_response.status_code == 200

    get_task_response = get_tasks(task_id)
    assert get_task_response.status_code == 200
    get_task = get_task_response.json()
    assert get_task['content'] == new_payload['content']
    assert get_task['is_done'] == new_payload['is_done']

def test_can_list_task():
    n = 10
    for _ in range(n):
        payload = new_payloads()
        response = create_task(payload)
        assert response.status_code == 200
        
    list_task_response = list_tasks('test_user')
    assert list_task_response.status_code == 200
    data = list_task_response.json()

    tasks = data['tasks']
    assert len(tasks) == n
    print(data)

def test_can_delete_task():
    payload = new_payloads()
    response = create_task(payload)
    assert response.status_code == 200
    task_id = response.json()['task']['task_id']

    delete_tasks_response = delete_tasks(task_id)
    assert delete_tasks_response.status_code == 200

    get_task_response = get_tasks(task_id)
    assert get_task_response.status_code == 404

def test_sql_injection():
    BURL = 'https://reqres.in/'
    payloads = [
        "1' OR '1'='1",
        "admin' OR '1'='1'--",
        "1; DROP TABLE users--",
        "' UNION SELECT null, username, password FROM users--",
        "1' UNION SELECT 1, database(), 3--",
        "1' AND 1=2--",
        "' AND 1=1--"
    ]
    endpoints= [
        ("login", 400),
        # ("register", 201),
        # ("profile", 403)
    ]
    for endpoint, expected_status in endpoints:
        for payload in payloads:
            sql_response = requests.post(url=BURL + f"api/{endpoint}", data= payload)
            assert sql_response.status_code == expected_status
    

def create_task(payload):
    return requests.put(BASE_URL + 'create-task', json=payload)

def update_task(payload):
    return requests.put(BASE_URL + 'update-task', json=payload)

def get_tasks(task_id):
    return requests.get(BASE_URL + f'get-task/{task_id}')

def delete_tasks(task_id):
    return requests.delete(BASE_URL + f'delete-task/{task_id}')

def list_tasks(user_id):
    return requests.get(BASE_URL + f'list-tasks/{user_id}')

def new_payloads():
    return {
        "content": "Random Content",
        "user_id": "Random user_id",
        "is_done": False
    }