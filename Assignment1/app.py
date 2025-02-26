from flask import Flask, request, render_template, redirect, url_for
import json
import os
from note import NoteBook

# create a notebook object, use local json file to store notes
json_file_path = 'notebook.json'
if not os.path.exists(json_file_path):
    with open(json_file_path, 'w') as file:
        json.dump({}, file)
notebook = NoteBook(json_file_path)

app = Flask(__name__)

@app.route('/')
def home():
    all_notes = notebook.show_all_notes()
    return render_template('home.html', all_notes=all_notes)

@app.route('/note')
def note_detail():
    note_name = request.args.get('name')
    if note_name is None:
        return "Note name is required", 400
    note_content=notebook.search_name(note_name)
    if note_content is None:
        return "Note with name {note_name} not found.", 404
    return render_template('item.html', note_name=note_name, note_content=note_content)

@app.route('/search')
def search():
    query = request.args.get('q')
    if query is None:
        return "Required search term", 400
    name_match = notebook.name_exists(query)
    conetent_match = notebook.search_string(query)
    return render_template('search.html', query=query, name_match=name_match, content_match=conetent_match)

@app.route('/add_note', methods=['POST'])
def add_note():
    title = request.form.get('title')
    content = request.form.get('content')
    if title is None or content is None:
        return "You need both title and content.", 400
    notebook.create_note(title, content)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)