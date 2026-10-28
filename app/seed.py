from sqlalchemy.orm import Session
from app.database import engine
from app.models import Project

with Session(engine) as session: #создание сессии
    project = Project(name="ConstructionAuditAI") 
    session.add(project) # добавление в сессию обьекта с именем выше
    session.commit() # сохранение изменений 

    session.refresh(project) # обновление обьекта

    print(project.id, project.name) # принтим айдишку и имя 