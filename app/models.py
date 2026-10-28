from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Project(Base):
    __tablename__ = "projects" #говорим sqlalchemy что проект соотвемтвует таблице преоктов 

    id: Mapped[int] = mapped_column(primary_key=True)
    #/
    # говорим что название столбца int
    # Mapped[int] ожидаемый тип
    # primary_key=True = первичный ключ для идентефикаций записи 
    # /#

    name: Mapped[str] = mapped_column(String(120), nullable= False)
    #/
    # nullable = защищаем SQL от null
    # /#

    