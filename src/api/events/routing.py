from fastapi import APIRouter
from .schema import EventSchema,EventListSchema,EventCreateSchema, EventUpdateSchema

router  = APIRouter()

@router.get("/")
def read_events() -> EventListSchema:
    return {"results": [{"id": 1}, {"id": 2}]}


@router.get("/{event_id}")
def get_events(event_id: int) ->EventSchema:
    return {"id": event_id}


#send data to api , use post
@router.post("/")
def create_events(payLoad:EventCreateSchema) -> EventSchema:
    print(type(payLoad))
    return {"id": 123}

#send data to api , use update
@router.put("/{event_id }")
def update_events(event_id:int, payLoad:EventUpdateSchema) -> EventSchema:
    print(type(payLoad))
    return {"id": event_id}