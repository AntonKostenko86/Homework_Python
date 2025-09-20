from ProjectAPI import ProjectAPI


# Константы
login = 'antonio.bannety.86@gmail.com'
password = 'Bannety1808'
companyId = '63376eae-5f71-4c3b-8cc6-837f9d091004'
userId = '323a4b87-8023-40b7-8f93-1fbf702a0ee4'
new_title = 'lesson_08'
user_role = 'admin'
user = {userId: user_role}
title_edit = 'lesson_08_new'
title_edited = 'lesson_08_update'
title_id = 'hw_08'
deleted = False
new_title_negative = ''
title_id_negative = '666'
userId_negative = '666'
user_negative = {userId_negative: user_role}


api = ProjectAPI('https://ru.yougile.com/api-v2', login, password, companyId)


def test_create_projects_positive():
    # Количество проектов до
    projects_before = api.get_project_list()
    len_before = len(projects_before)

    # Создание проекта
    result = api.create_project(new_title, user)
    new_id = result.json()['id']

    # Количество проектов после
    projects_after = api.get_project_list()
    len_after = len(projects_after)

    # Проверка
    assert result.status_code == 201
    assert len_after - len_before == 1
    assert projects_after[-1]['title'] == new_title
    assert projects_after[-1]['id'] == new_id


def test_create_project_negative():
    # Количество проектов до
    projects_before = api.get_project_list()
    len_before = len(projects_before)

    # Создание проекта с пустым названием
    result = api.create_project(new_title_negative, user)

    # Количество проектов после
    projects_after = api.get_project_list()
    len_after = len(projects_after)

    # Проверка
    assert result.status_code == 400
    assert len_after - len_before == 0


def test_get_project_id_positive():
    # Создание проекта
    result = api.create_project(title_id, user)
    project_id = result.json()['id']

    # Обращаемся к проекту
    new_project = api.get_project_id(project_id)

    # Проверка
    assert new_project.status_code == 200
    assert new_project.json()['title'] == title_id
    assert new_project.json()['users'] == user
    assert new_project.json()['id'] == project_id

    # Очистка данных после теста
    api.edit_project(project_id, True, title_id, user)


def test_get_project_id_negative():
    # Обращаемся к проекту с несуществующим id
    new_project = api.get_project_id(title_id_negative)

    # Проверка
    assert new_project.status_code == 404


def test_edit_project_positive():
    # Создание проекта
    result = api.create_project(title_edit, user)
    project_id = result.json()['id']

    # Изменение проекта
    edited = api.edit_project(project_id, deleted, title_edited, user)

    # Проверка
    assert edited.status_code == 200

    # Обращаемся к проекту
    project_title = api.get_project_id(project_id).json()['title']

    # Проверка
    assert project_title == title_edited

    # Очистка данных после теста
    api.edit_project(project_id, True, title_edited, user)


def test_edit_project_negative():
    # Создание проекта
    result = api.create_project(title_edit, user)
    project_id = result.json()['id']

    # Попытка изменить проект с неверным id роли
    edited = api.edit_project(project_id, deleted, title_edited, user_negative)

    # Проверка
    assert edited.status_code == 400

    # Очистка данных после теста
    api.edit_project(project_id, True, title_edited, user)
