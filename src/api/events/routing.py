from fastapi import APIRouter

router  = APIRouter()

@router.get("/")
def read_events():
    return {1,2,3}


@router.get("/{event_id}")
def get_events(event_id: int):
    return {"id": event_id}