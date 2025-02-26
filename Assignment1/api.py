from fastapi import FastAPI, File, UploadFile
from note import NoteBook
import json
import os
from pydantic import BaseModel

# create a notebook object, use local json file to store notes
json_file_path = 'notebook.json'
if not os.path.exists(json_file_path):
    with open(json_file_path, 'w') as file:
        json.dump({}, file)
notebook = NoteBook(json_file_path)

app = FastAPI()

# return a text string with hints to the user on how to access the API
@app.get("/")
def home():
    return {"message": "To access a list with all note names, go to /list. To access a specific note with its name, go to /note/{note_name}. To access a list all notes that match the search term, go to /find?term={string}."}

# return a list of all note names
@app.get("/list")
def list_notes():
    return {"notes": list(notebook.show_all_notes())}

# return the content of a note with a specific name
@app.get("/note/{note_name}")
def get_note_with_name(note_name: str):
    return notebook.search_name(note_name)

# return a list of all note names that contain a specific string
@app.get("/find")
def find_string(term: str):
    return {"term": term, "matching notes": notebook.search_string(term)}

class Note(BaseModel):
    name: str
    content: str

# add a new note
@app.post("/add")
async def add_note(note: Note):
    notebook.create_note(note.name, note.content)
    return {"message": "Note is successfully added."}
