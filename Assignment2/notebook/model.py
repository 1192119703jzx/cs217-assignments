from notebook.initial import db


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    comments = db.relationship('Comment', backref='note', lazy='joined')

    def __repr__(self):
        return '<Note %r>' % self.title

    @classmethod
    def add_note(cls, title, content):
        try:
            if cls.query.filter_by(title=title).first():
                raise ValueError("A note with this title already exists.")

            new_note = cls(title=title, content=content)
            db.session.add(new_note)
            db.session.commit()
            return new_note
        except Exception as e:
            db.session.rollback()
            return e

    @classmethod
    def delete_note(cls, note_id):
        try:
            note = cls.query.get(note_id)
            if note is None:
                raise ValueError("Note with this title does not exist.")
            comments = Comment.query.filter_by(note_id=note_id).all()
            for comment in comments:
                db.session.delete(comment)
            db.session.delete(note)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return False


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    note_id = db.Column(db.Integer, db.ForeignKey('note.id'), nullable=False)
    
    def __repr__(self):
        return '<Comment %r>' % self.content

    @classmethod
    def add_comment(cls, note_id, content):
        try:
            new_comment = cls(content=content, note_id=note_id)
            db.session.add(new_comment)
            db.session.commit()
            return new_comment
        except Exception as e:
            db.session.rollback()
            return e
