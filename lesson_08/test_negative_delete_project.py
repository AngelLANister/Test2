import requests
from lesson_08.auth_helper import get_token, base_url
import os


def create_project():
    token = get_token(
        login=os.getenv('yougile_login'),
        password=os.getenv('yougile_password'),
        name=os.getenv('yougile_name')
    )
    headers_auth = {'Content-Type':
                    'application/json',
                    'Authorization': f'Bearer {token}'}
    data_project = {
        "title": "ЭЧ",
        "users": {}
    }
    resp_create_project = requests.post(base_url +
                                        '/api-v2/projects',
                                        json=data_project,
                                        headers=headers_auth)
    return resp_create_project, token


def delete_project():
    resp, token = create_project()
    project_id = resp.json()['id']
    headers_auth = {'Content-Type': 'application/json',
                    'Authorization': f'Bearer {token}'}
    data_delete = {
        "deleted": True,
        "title": "ЭЧ",
        "users": {}
    }
    resp_delete_project = requests.put(base_url +
                                       '/api-v2/projects/' + project_id,
                                       json=data_delete,
                                       headers=headers_auth)
    return resp_delete_project, token


# удаление уже удаленного проекта
def test_repeat_delete_project():
    resp, token = create_project()
    project_id = resp.json()['id']
    headers_auth = {'Content-Type': 'application/json',
                    'Authorization': f'Bearer {token}'}
    data_delete = {
        "deleted": True,
        "title": "ЭЧ",
        "users": {}
    }
    resp_delete_project = requests.put(base_url +
                                       '/api-v2/projects/' + project_id,
                                       json=data_delete,
                                       headers=headers_auth)
    assert resp_delete_project.status_code == 200
