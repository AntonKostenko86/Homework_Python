import requests


class ProjectAPI:
    # Инициализация
    def __init__(self, url, login, password, companyId) -> None:
        self.url = url
        self.token = self.get_token(login, password, companyId)

    # Получить ключ авторизации
    def get_token(self, login, password, companyId):
        payload = {
            'login': login,
            'password': password,
            'companyId': companyId
        }
        resp = requests.post(self.url + '/auth/keys/get', json=payload)
        return resp.json()[0]['key']

    # Получить список проектов компании
    def get_project_list(self):
        key = self.token
        headers = {
            'Authorization': f'Bearer {key}',
            'Content-Type': 'application/json'
        }
        resp = requests.get(self.url + '/projects', headers=headers)
        return resp.json()['content']

    # Создать проект
    def create_project(self, title, users):
        key = self.token
        headers = {
            'Authorization': f'Bearer {key}',
            'Content-Type': 'application/json'
        }
        body = {
            'title': title,
            'users': users
        }
        resp = requests.post(self.url + '/projects',
                             headers=headers, json=body
                             )
        return resp

    # Получить проект по id
    def get_project_id(self, project_id):
        key = self.token
        headers = {
            'Authorization': f'Bearer {key}',
            'Content-Type': 'application/json'
        }
        resp = requests.get(self.url + f'/projects/{project_id}',
                            headers=headers
                            )
        return resp

    # Изменить название проекта
    def edit_project(self, project_id, new_deleted, new_title, new_users):
        key = self.token
        headers = {
            'Authorization': f'Bearer {key}',
            'Content-Type': 'application/json'
        }
        body = {
            "deleted": new_deleted,
            "title": new_title,
            "users": new_users
        }
        resp = requests.put(self.url + f'/projects/{project_id}',
                            headers=headers, json=body
                            )
        return resp
