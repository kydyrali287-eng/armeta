import json

def validate_name(name):
    if not isinstance(name, str):
        raise ValueError ("Некорректное название проекта")
    name = name.strip()
    if len(name) < 3 or len(name) > 120:
        raise ValueError ("Некорректное название проекта")
    return name

def validate_docuemnt_name(name):
    if not isinstance(name, str):
        raise ValueError ("Некорректное название документа")
    name = name.strip()
    if len(name) < 1 or len(name) > 120:
        raise ValueError ("Некорректное название документа")
    return name

class Document:
    def __init__(self, id, filename):
        self.filename = validate_docuemnt_name(filename)
        self.id =id

    def rename(self, new_name):
        new_name = validate_docuemnt_name(new_name)
        self.filename = new_name

    def to_dict(self):
        return {
            "id": self.id,
            "filename" : self.filename
        }

class Project:
    def __init__(self, id, name):
        self.id = id
        self.name = validate_name(name)
        self.documents_id = 1
        self.documents = []

    def rename(self,  new_name):
        new_name = validate_name(new_name)
        self.name = new_name

    def to_dict(self):
        documents_data = []
        for doc in self.documents:
            documents_data.append(doc.to_dict())
        return {
            "id" : self.id,
            "name" : self.name, 
            "next_documents_id" : self.documents_id,
            "documents" : documents_data
        }

    
    def add_document(self, filename):
        dc_id = self.documents_id 
        document = Document(dc_id, filename)
        self.documents.append(document)
        self.documents_id += 1
        return document

    def find_document_by_id(self, document_id):
        for doc in self.documents:
            if doc.id == document_id:
                return doc
        return None

    def delete_document(self, document_id):
        doc = self.find_document_by_id(document_id)
        if doc == None:
            return None
        self.documents.remove(doc)
        return doc

    def rename_document(self, documents_id, new_name):
        doc = self.find_document_by_id(documents_id)
        if doc == None:
            return None
        doc.rename(new_name)
        return doc
        
    def list_documents(self):
        return list(self.documents)

    def count_documents(self):
        return len(self.documents)

class ProjectManager:
    def __init__(self):
        self.projects = []
        self.next_id = 0

    def to_dict(self):
        projects_data = []
        for p in self.projects:
            projects_data.append(p.to_dict())
        return {
            "next_id" : self.next_id,
            "projects": projects_data 
        }

    def create(self, name):
        pg_id = self.next_id + 1
        project = Project(pg_id, name)
        self.projects.append(project)
        self.next_id += 1
        return project

    def find_by_id(self, project_id):
        for p in self.projects:
            if p.id == project_id:
                return p
        return None

    def delete(self, project_id):
        prog = self.find_by_id(project_id)
        if prog == None:
            return None
        self.projects.remove(prog)
        return prog

    def rename(self, project_id, new_name):
        prog = self.find_by_id(project_id)
        if prog == None:
            return None
        prog.rename(new_name)
        return prog

    def list_projects(self):
        return list(self.projects)

    def count_projects(self):
        return len(self.projects)

    def save_to_json(self, path):
        data = self.to_dict()
        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent = 4,ensure_ascii= False)
        return data

    def load_from_json(self, path):
        with open(path, "r",encoding = "utf-8") as file:
            data = json.load(file)

        self.projects.clear()
        self.next_id = data["next_id"]

        for p in data["projects"]:
            project = Project(p["id"], p["name"])

            project.documents_id = p["next_documents_id"]

            for d in p["documents"]:
                doc = Document(
                    d["id"],
                    d["filename"]
                )

                project.documents.append(doc)

            self.projects.append(project)


def test_json_roundtrip():
    manager = ProjectManager()

    p1 = manager.create("Astana")
    p2 = manager.create("Almaty")

    p1.add_document("act.pdf")
    p1.add_document("smeta.xlsx")
    p2.add_document("contract.pdf")

    manager.save_to_json("test_data.json")

    loaded = ProjectManager()
    loaded.load_from_json("test_data.json")

    assert loaded.count_projects() == 2

    new_p1 = loaded.find_by_id(1)
    new_p2 = loaded.find_by_id(2)

    assert new_p1.name == "Astana"
    assert new_p2.name == "Almaty"

    assert new_p1.count_documents() == 2
    assert new_p2.count_documents() == 1

    assert new_p1.find_document_by_id(1).filename == "act.pdf"
    assert new_p1.find_document_by_id(2).filename == "smeta.xlsx"
    assert new_p2.find_document_by_id(1).filename == "contract.pdf"

    print("Test 1 passed!")

def test_json_ids():
    manager = ProjectManager()

    p1 = manager.create("Astana")

    p1.add_document("act.pdf")
    p1.add_document("smeta.pdf")

    p1.delete_document(2)

    manager.save_to_json("test_ids.json")

    loaded = ProjectManager()
    loaded.load_from_json("test_ids.json")

    p = loaded.find_by_id(1)

    d3 = p.add_document("report.pdf")

    assert d3.id == 3
    assert p.count_documents() == 2

    p2 = loaded.create("Almaty")

    assert p2.id == 2

    print("Test 2 passed!")

def test_json_empty():
    manager = ProjectManager()

    manager.save_to_json("test_empty.json")

    loaded = ProjectManager()
    loaded.load_from_json("test_empty.json")

    assert loaded.count_projects() == 0
    assert loaded.next_id == 0

    p = loaded.create("Astana")

    assert p.id == 1

    print("Test 3 passed!")

test_json_roundtrip()
test_json_ids()
test_json_empty()

print("ALL JSON TESTS PASSED!")