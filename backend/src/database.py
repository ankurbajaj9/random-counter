from flask_sqlalchemy import SQLAlchemy


def get_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@db:5432/users'
    db = SQLAlchemy(app)
    return db
