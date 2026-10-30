projects = []

def validate_project_name(name):
    if not isinstance(name, str):
        raise ValueError ("Некорректное название проекта")
    name = name.strip()
    if len(name) < 3 or len(name) > 120:
        raise ValueError ("Некорректное название проекта")
    return name

def create_project(projects, name):
    name = validate_project_name(name)
    project = {
        "id" : len(projects) + 1,
        "name" : name
    }
    projects.append(project)
    return project

def list_projects(projects):
    return list(projects)

def count_projects(projects):
    return len(projects)

def find_p(projects, projects_id):
    for p in projects:
        if p["id"] == projects_id:
            return p
    return None

def test_individual_name(name):
    try:
        create_project([], name)
    except ValueError:
        pass
    else:
        raise AssertionError("Ожидалась ошибка ValueErrorы")


def test_create_project():
    test_projects = []

    project1 = create_project(test_projects, "Yoo")
    project2 = create_project(test_projects, "      Road  ")

    n1 = "AB"
    n2 = ""
    n3 = "          "
    n4 = "A" * 121

    assert project1["id"] == 1
    assert project1["name"] == "Yoo"
    assert project2["name"] == "Road"
    assert project2["id"] == 2
    assert len(test_projects) == 2
    assert count_projects(test_projects) == 2
    assert find_p(test_projects, 1)["name"] == "Yoo"
    assert find_p(test_projects , 999) is None

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
            "5. Выход"
            )
        number = input()
        if number == "1":
            name = input("имя для нового проекта: ")
            try:
                create_project(projects, name)

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
            break
    return 
test_create_project()
print("tests passed!")
main()
