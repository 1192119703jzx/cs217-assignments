from flask import request, render_template, redirect, url_for, Blueprint
from notebook.model import Note, Comment

main_routes = Blueprint('main_routes', __name__)

@main_routes.route('/')
def home():
    all_notes = Note.query.all()
    return render_template('home.html', all_notes=all_notes)

@main_routes.route('/note')
def note_detail():
    note_name = request.args.get('name')
    if note_name is None:
        return "Note name is required", 400
    note = Note.query.filter_by(title=note_name).first()
    if note is None:
        return f"Note with name {note_name} not found.", 404
    return render_template('item.html', note=note)

@main_routes.route('/search')
def search():
    query = request.args.get('q')
    if query is None:
        return "Required search term", 400
    name_match = Note.query.filter(Note.title.contains(query)).all()
    content_match = Note.query.filter(Note.content.contains(query)).all()
    comment_match = Comment.query.filter(Comment.content.contains(query)).all()
    return render_template('search.html', query=query, name_match=name_match, content_match=content_match, comment_match=comment_match)

@main_routes.route('/add_note', methods=['POST'])
def add_note():
    title = request.form.get('title')
    content = request.form.get('content')
    if title is None or content is None:
        return "You need both title and content.", 400
    
    try:
        Note.add_note(title, content)
    except ValueError as e:
        return str(e), 400
    return redirect(url_for('main_routes.home'))

@main_routes.route('/delete_note', methods=['POST'])
def delete_note():
    note_id = request.form.get('note_id')
    if note_id:
        try:
            Note.delete_note(note_id)
        except ValueError as e:
            return str(e), 400
    return redirect(url_for('main_routes.home'))

@main_routes.route('/add_comment', methods=['POST'])
def add_comment():
    note_id = request.form.get('note_id')
    content = request.form.get('comment_content')
    if content is None:
        return "Comment content is required.", 400
    try:
        Comment.add_comment(note_id, content)
    except ValueError as e:
        return str(e), 400
    name = Note.query.get(note_id).title
    return redirect(url_for('main_routes.note_detail', name=name))