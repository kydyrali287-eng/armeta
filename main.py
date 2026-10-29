projects = []

def create_project(projects, name):
    project = {
        "id" : len(projects) + 1,
        "name" : name
    }
    projects.append(project)
    return project

def list_projects(projects):
    return list(projects)

def get_project_by_id(projects, project_id):
    for p in projects:
        if p["id"] == project_id:
            return p

    return None

def count_projects(projects):
    return len(projects)

def find_p(projects, projects_id):
    for p in projects:
        if p["id"] == projects_id:
            return p
    return None


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
            create_project(projects, name)
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
    
main()
