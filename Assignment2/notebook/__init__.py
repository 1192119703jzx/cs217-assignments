from flask import Flask
from notebook.initial import db


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notebook.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from notebook.routes import main_routes
    app.register_blueprint(main_routes)

    with app.app_context():
        from notebook.model import Note, Comment
        db.create_all()

    return app
