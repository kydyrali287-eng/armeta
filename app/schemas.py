from pydantic import BaseModel, Field
from typing import Literal
from decimal import Decimal 

class ProjectCreate(BaseModel):
    name: str = Field(min_length=3, max_length = 120)
# python -c "from app.schemas import ProjectCreate; print (ProjectCreate(name='ConstructionAuditAi'))" 


class DocumentRead(BaseModel):
    id: int = Field(gt = 0) #идентификатор документа | gt = строго больше нуля
    project_id: int = Field(gt = 0) #к какому преокту относится документ
    filename: str = Field(min_length=1) #имя загружаемого файла
    document_type: Literal["estimate", "avr", "specification"] #тип загружаемого документа 

class WorkItemExtracted(BaseModel):
    document_id: int = Field(gt = 0) # строго больше нуля
    code: str = Field(min_length=1)
    name: str = Field(min_length= 1)
    unit: str = Field(min_length=1)
    quantity: Decimal = Field(ge = 0) # 0 больше либо равно нулю
    unit_price: Decimal = Field(ge = 0) # 0 больше либо равно нулю
    source_ref: str = Field(min_length=1)
