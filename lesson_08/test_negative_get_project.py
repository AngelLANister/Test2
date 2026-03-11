import requests
from lesson_08.auth_helper import get_token, base_url
import os


def test_get_project_non_exist():
    token = get_token(
        login=os.getenv('yougile_login'),
        password=os.getenv('yougile_password'),
        name=os.getenv('yougile_name')
    )
    headers_auth = {'Content-Type':
                    'application/json',
                    'Authorization': f'Bearer {token}'}
    resp_get_project = requests.get(base_url +
                                    '/api-v2/projects/' + 'unknown',
                                    headers=headers_auth)
    assert resp_get_project.status_code == 404
