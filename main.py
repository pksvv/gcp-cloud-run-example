from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# In-memory "database"
notes_db = {}

class Note(BaseModel):
    title: str
    content: str

@app.get("/")
def home():
    return {"message": "Notes API is running on Cloud Run!"}

# Create
@app.post("/notes/{note_id}")
def create_note(note_id: int, note: Note):
    if note_id in notes_db:
        raise HTTPException(status_code=400, detail="Note already exists")
    notes_db[note_id] = note
    return {"note_id": note_id, "note": note}

# Read
@app.get("/notes/{note_id}")
def read_note(note_id: int):
    if note_id not in notes_db:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"note_id": note_id, "note": notes_db[note_id]}

# Update
@app.put("/notes/{note_id}")
def update_note(note_id: int, note: Note):
    if note_id not in notes_db:
        raise HTTPException(status_code=404, detail="Note not found")
    notes_db[note_id] = note
    return {"note_id": note_id, "note": note}

# Delete
@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    if note_id not in notes_db:
        raise HTTPException(status_code=404, detail="Note not found")
    del notes_db[note_id]
    return {"message": f"Note {note_id} deleted"}