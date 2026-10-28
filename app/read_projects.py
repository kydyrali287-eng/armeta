from sqlalchemy import select
from sqlalchemy.orm import Session
from app.database import engine
from app.models import Project

with Session(engine) as session:
    projects = session.scalars(select(Project)).all() 
# 
#   формирует запрос на получение проектов и выполняет запрос позволяя получить обьекты Project
#   projects = переменная в которой содержится список 
#
#   по смыслу как SELECT * FROM projects;
#  /#
    for project in projects:
        print(project.id, project.name)

