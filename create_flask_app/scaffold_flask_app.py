import os
import click

@click.command()
@click.argument("blueprint_list", nargs=-1)
@click.option("--output", "-o", default=".", help="Directory to generate the Flask app in.")
def scaffold_flask_app(blueprint_list, output):
    """
    Scaffold a Flask app with the specified blueprints.
    """
    base_dir = os.path.abspath(output)

    # Core paths
    paths = [
        "app/__init__.py",
        "app/database.py",
        "app/templates/base.html",
        "app/templates/components/_header.html",
        "app/templates/components/_navBar.html",
        "schema.sql",
        "wsgi.py"
    ]

    # Blueprint paths and their templates
    for bp in blueprint_list:
        paths.extend([
            f"app/{bp}/__init__.py",
            f"app/templates/{bp}/create.html",
            f"app/templates/{bp}/list.html",
            f"app/templates/{bp}/edit.html",
            f"app/templates/{bp}/detail.html",
            f"app/templates/{bp}/{bp}_index.html"
        ])

    # Create each path/file
    for path in paths:
        full_path = os.path.join(base_dir, path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        if not os.path.exists(full_path):
            with open(full_path, "w") as f:
                f.write(generate_boilerplate(path, blueprint_list))

    click.echo(f"✅ Flask app scaffolded successfully at: {base_dir}")


def generate_boilerplate(path, blueprint_list):
    if path == "app/__init__.py":
        return generate_init_py(blueprint_list)
    elif path == "app/database.py":
        return """import sqlite3
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
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
"""
    elif path == "wsgi.py":
        return "from app import create_app\n\napp = create_app()\n"
    elif path == "schema.sql":
        schema = ""
        for bp in blueprint_list:
            schema += f"""
CREATE TABLE {bp} (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT
);
"""
        return schema.strip()
    elif path.endswith("base.html"):
        return """<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>{% block title %}My Flask App{% endblock %}</title>
  </head>
  <body>
    {% include 'components/_header.html' %}
    {% include 'components/_navBar.html' %}
    <main>{% block content %}{% endblock %}</main>
  </body>
</html>
"""
    elif "_header.html" in path:
        return "<header><h1>Header</h1></header>"
    elif "_navBar.html" in path:
        return "<nav><ul><li><a href='/'>Home</a></li></ul></nav>"
    elif path.endswith("_index.html"):
        bp_name = path.split("/")[-1].split("_")[0]
        return f"""{{% extends 'base.html' %}}
{{% block content %}}
  <h2>{bp_name.capitalize()} Blueprint</h2>
  <p>This is a placeholder page for the {bp_name} blueprint.</p>
{{% endblock %}}
"""
    elif "__init__.py" in path and "app/" in path and path.count("/") == 2:
        bp_name = path.split("/")[1]
        return f"""from flask import Blueprint, render_template

bp = Blueprint('{bp_name}', __name__, url_prefix='/{bp_name}')

@bp.route('/')
def index():
    return render_template('{bp_name}/{bp_name}_index.html')
"""
    else:
        return ""


def generate_init_py(blueprint_list):
    bp_imports = "\n    ".join([f"from .{bp} import bp as {bp}_bp" for bp in blueprint_list])
    bp_registration = "\n    ".join([f"app.register_blueprint({bp}_bp)" for bp in blueprint_list])
    
    return f"""from flask import Flask

def create_app():
    app = Flask(__name__)
    {bp_imports}

    {bp_registration}

    return app
"""

if __name__ == "__main__":
    scaffold_flask_app()
