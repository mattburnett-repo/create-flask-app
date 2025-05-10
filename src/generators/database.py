def generate_database_module():
    return """import sqlite3
import click
from flask import current_app, g
from flask.cli import with_appcontext

# (get_db, close_db, init_db, init_app functions here)
"""