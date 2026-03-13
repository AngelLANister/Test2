import requests
from lesson_08.auth_helper import base_url


def test_create_company_auth_none():
    headers_auth = {'Content-Type': 'application/json',
                    'Authorization': 'Bearer None'}
    data_project = {
        "title": "ШЧ",
        "users": {}
    }
    resp_create_project = requests.post(base_url+'/api-v2/projects',
                                        json=data_project,
                                        headers=headers_auth)
    assert resp_create_project.status_code == 401, \
        (f"Ошибка: {resp_create_project.status_code} - "
         f"{resp_create_project.text}")
