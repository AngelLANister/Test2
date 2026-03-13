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
        "title": "НГЧ",
        "users": {}
    }
    resp = requests.post(base_url +
                                        '/api-v2/projects',
                                        json=data_project,
                                        headers=headers_auth)
    return resp, token


def test_get_project():
    resp, token = create_project()
    project_id = resp.json()['id']
    headers_auth = {'Content-Type':
                    'application/json',
                    'Authorization': f'Bearer {token}'}
    resp_get_project = requests.get(base_url +
                                    '/api-v2/projects/'
                                    + project_id, headers=headers_auth)
    assert resp_get_project.json()['title'] == "НГЧ"
