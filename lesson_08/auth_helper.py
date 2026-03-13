import requests
from dotenv import load_dotenv
load_dotenv()

base_url = 'https://ru.yougile.com'


def get_token(login, password, name):
    headers = {'Content-Type': 'application/json'}
    data_name = {
        "login": login,
        "password": password,
        "name": name
    }
    resp_id_company = requests.post(base_url+'/api-v2/auth/companies',
                                    data_name, headers)
    id_company = resp_id_company.json()['content'][0]['id']


# получаем токен авторизации
    data_token = {
        "login": login,
        "password": password,
        "companyId": id_company
    }
    resp_token = requests.post(base_url+'/api-v2/auth/keys',
                               data_token, headers)
    return resp_token.json()['key']
