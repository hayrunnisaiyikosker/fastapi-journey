from fastapi import FastAPI, HTTPException
from app.models import Poll, PollCreate
import uuid

app = FastAPI()


polls_db: dict[str, Poll] = {}

@app.post("/polls")
def create_poll(data: PollCreate):
    poll_id = str(uuid.uuid4())
    poll = Poll(
        id=poll_id,
        question=data.question,
        options=data.options,
        votes={option: 0 for option in data.options}
    )
    polls_db[poll_id] = poll
    return poll

@app.get("/polls")
def list_polls():
    return list(polls_db.values())

@app.get("/polls/{poll_id}")
def get_poll(poll_id: str):
    if poll_id not in polls_db:
        raise HTTPException(status_code=404, detail="Poll not found")
    return polls_db[poll_id]

@app.post("/polls/{poll_id}/vote")
def vote(poll_id: str, option: str):
    if poll_id not in polls_db:
        raise HTTPException(status_code=404, detail="Poll not found")
    poll = polls_db[poll_id]
    if option not in poll.votes:
        raise HTTPException(status_code=400, detail="invalid option")
    poll.votes[option] += 1
    return poll

@app.delete("/polls/{poll_id}")
def delete_poll(poll_id: str):
    if poll_id not in polls_db:
        raise HTTPException(status_code=404, detail="Poll not found")
    del polls_db[poll_id]
    return {"message": "Poll deleted"}