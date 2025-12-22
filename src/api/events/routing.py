from fastapi import APIRouter
from .schema import EventSchema,EventListSchema

router  = APIRouter()

@router.get("/")
def read_events() -> EventListSchema:
    return {"results": [{"id": 1}, {"id": 2}]}


@router.get("/{event_id}")
def get_events(event_id: int) ->EventSchema:
    return {"id": event_id}