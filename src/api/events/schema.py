from pydantic import BaseModel
from typing import List

class EventSchema(BaseModel):
    id: int


#{"id" : 12}

class EventListSchema(BaseModel):
    results: List[EventSchema]

class EventCreateSchema(BaseModel):
    path:str

class EventUpdateSchema(BaseModel):
    description:str