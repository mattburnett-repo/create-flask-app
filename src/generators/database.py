def generate_database_module():
    return """import sqlite3
from datetime import datetime
import os

import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()

    # Create tables. Drop existing tables if they exist.
    with current_app.open_resource('database/schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

    # Insert sample data
    with current_app.open_resource('database/sample-data.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    \"\"\"Clear the existing data, create new tables, and insert sample data.\"\"\"
    # Ensure the instance folder exists
    try:
        os.makedirs(current_app.instance_path)
    except OSError:
        pass
    
    # Create the database file if it doesn't exist
    if not os.path.exists(current_app.config['DATABASE']):
        open(current_app.config['DATABASE'], 'a').close()
    
    init_db()
    click.echo('Initialized the database. Database is located at: ' + current_app.config['DATABASE'])


sqlite3.register_converter(
    "timestamp", lambda v: datetime.fromisoformat(v.decode())
)


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
"""