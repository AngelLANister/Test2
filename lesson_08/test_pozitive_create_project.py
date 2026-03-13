import os
import requests
from lesson_08.auth_helper import get_token, base_url


def create_project():
    token = get_token(
        login=os.getenv('yougile_login'),
        password=os.getenv('yougile_password'),
        name=os.getenv('yougile_name'),
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
    return resp_create_project


def test_create_project():
    resp = create_project()
    assert resp.status_code == 201
