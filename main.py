projects = []
state = {"next_id" : 0}

def validate_project_name(name):
    if not isinstance(name, str):
        raise ValueError ("Некорректное название проекта")
    name = name.strip()
    if len(name) < 3 or len(name) > 120:
        raise ValueError ("Некорректное название проекта")
    return name

def create_project(projects, name, state):
    name = validate_project_name(name)
    project = {
        "id" : state["next_id"] + 1,
        "name" : name
    }
    projects.append(project)
    state["next_id"] += 1
    return project

def list_projects(projects):
    return list(projects)

def count_projects(projects):
    return len(projects)

def find_p(projects, project_id):
    for p in projects:
        if p["id"] == project_id:
            return p
    return None

def delete_project(projects, project_id):
    found = find_p(projects, project_id)

    if found is None:
        return None
    projects.remove(found)

    return found

def rename_project(projects, project_id, new_name):
    found = find_p(projects, project_id)
    if found is None:
        return None
    new_name = validate_project_name(new_name)
    found["name"] = new_name
    return found
    

def test_individual_name(name):
    try:
        create_project([], name, state)
    except ValueError:
        pass
    else:
        raise AssertionError("Ожидалась ошибка ValueErrorы")


def test_create_project():
    statee = {"next_id": 0}
    test_projects = []

    project1 = create_project(test_projects, "Yoo", statee)
    project2 = create_project(test_projects, "      Road  ", statee)

    n1 = "AB"
    n2 = ""
    n3 = "          "
    n4 = "A" * 121

    assert project1["id"] == 1
    assert project1["name"] == "Yoo"
    assert project2["name"] == "Road"
    assert project2["id"] == 2
    assert rename_project(test_projects, 1, "Hello") == {"id": 1, "name": "Hello"}
    assert rename_project(test_projects, 999, "Heo") == None
    try:
        rename_project(test_projects, 1, "AB")
    except ValueError:
        print("test01 passed")
    else:
        raise AssertionError("Expected ValueError")
    assert len(test_projects) == 2
    assert count_projects(test_projects) == 2
    assert find_p(test_projects, 1)["name"] == "Hello"  
    assert find_p(test_projects , 999) is None
    assert delete_project(test_projects, 999) is None
    assert delete_project(test_projects, 1) == {"id": 1, "name": "Hello"}
    assert find_p(test_projects, 1) is None
    assert count_projects(test_projects) == 1
    assert create_project(test_projects, "Hospital", statee)
    assert delete_project(test_projects, 3) == {"id": 3, "name": "Hospital"}
    assert create_project(test_projects, "Airport", statee)
    assert find_p(test_projects, 4)["id"] == 4
    assert find_p(test_projects, 2)["id"] == 2
    test_individual_name(n1)
    test_individual_name(n4)
    test_individual_name(n2)
    test_individual_name(n3)

def main():
    while True:
        print("=== ConstructAudit AI ===\n"\
            "Выберите действие:\n" \
            "1. Создать проект\n" \
            "2. Показать все проекты\n" \
            "3. Найти проект по ID\n" \
            "4. Посчитать проекты\n"\
            "5. Удалить проект\n"\
            "6. Переименовать проект проект\n"\
            "7. Выход"
            )
        number = input()
        if number == "1":
            name = input("имя для нового проекта: ")
            try:
                create_project(projects, name, state)

            except ValueError:
                print("Некорректное название проекта")
                continue
        elif number == "2":
            print(list_projects(projects))

        elif number == "3":
            try:
                project_id = input("Введите айдишку:")
                progg = int(project_id)
            except ValueError:
                print("Введите число!")
                continue
            print(find_p(projects, progg))

        elif number == "4":
            print(count_projects(projects))
        elif number == "5":
            try:
                project_id = input("Введите айдишку:")
                progg = int(project_id)
            except ValueError:
                print("Введите число!")
                continue
            print(delete_project(projects, progg))
        elif number == "6":
            try:
                project_id = input("Введите айдишку:")
                progg = int(project_id)
                name = input("имя для нового проекта: ")
            except ValueError:
                print("Введите число!")
                continue
            try:
                print(rename_project(projects, progg, name))
    
            except ValueError:
                print("Некорректное название проекта")
                continue
        elif number == "7":
            break
    return 
test_create_project()
print("tests passed!")
main()
