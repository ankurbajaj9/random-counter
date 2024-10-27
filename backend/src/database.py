from flask_sqlalchemy import SQLAlchemy
import os


def get_db(app):
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_host = os.getenv('DB_HOST', 'app-postgresql')
    db_port = os.getenv('DB_PORT', '5432')

    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/'
    db = SQLAlchemy(app)
    return db
