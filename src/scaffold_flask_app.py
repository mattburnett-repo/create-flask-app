import os
import click

from generators.app_init import generate_app_init
from generators.database import generate_database_module
from generators.wsgi import generate_wsgi
from generators.schema import generate_schema
from generators.templates.base import generate_base_template
from generators.templates.components import generate_component_templates
from generators.templates.index import generate_index_template
from generators.templates.empty import generate_empty_template
from generators.blueprint_init import generate_blueprint_init

@click.command()
@click.argument("blueprint_list", nargs=-1)
@click.option("--app-name", "-a", required=True, help="Name of your Flask application.")
def scaffold_flask_app(blueprint_list, app_name):
    """
    Scaffold a Flask app with the specified blueprints.
    """
    # Convert app_name to a valid directory name (lowercase, replace spaces with underscores)
    base_dir = os.path.abspath(app_name.lower().replace(" ", "_"))

    # Core paths
    paths = [
        "app/__init__.py",
        "app/database.py",
        "app/templates/base.html",
        "app/templates/index.html",
        "app/templates/components/_navbar.html",
        "app/templates/components/_flashMsgDisplay.html",
        "app/schema.sql",
        "requirements.txt",
        "wsgi.py"
    ]

    # Blueprint paths and their templates
    for bp in blueprint_list:
        bp_folder = f"app/{bp}"
        tpl_folder = f"app/templates/{bp}"
        paths.extend([
            f"{bp_folder}/__init__.py",
            f"{tpl_folder}/create.html",
            f"{tpl_folder}/list.html",
            f"{tpl_folder}/edit.html",
            f"{tpl_folder}/detail.html",
        ])

    # Create files
    for path in paths:
        full_path = os.path.join(base_dir, path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        if not os.path.exists(full_path):
            with open(full_path, "w") as f:
                f.write(dispatch_boilerplate(path, blueprint_list, app_name))

    # Write requirements
    req_path = os.path.join(base_dir, "requirements.txt")
    with open(req_path, "w") as req_file:
        req_file.write("flask\nclick\n")

    click.echo(f"✅ Flask app '{app_name}' scaffolded successfully at: {base_dir}")
    click.echo("✅ Next, create/start a venv.")
    click.echo(f"✅ After that's done, run , 'cd {app_name} && pip install -r requirements.txt && flask run'.")


def dispatch_boilerplate(path, blueprint_list, app_name):
    if path == "app/__init__.py":
        return generate_app_init(blueprint_list, app_name)
    if path == "app/database.py":
        return generate_database_module()
    if path == "wsgi.py":
        return generate_wsgi()
    if path == "app/schema.sql":
        return generate_schema(blueprint_list)
    if path.endswith("base.html"):
      return generate_base_template(app_name)
    if path.endswith("index.html") and "templates/" in path and path.count("/") == 2:
        return generate_index_template(app_name)
    if path.endswith("_navbar.html") or path.endswith("_flashMsgDisplay.html"):
        return generate_component_templates(path, blueprint_list, app_name)
    if path.endswith("create.html"):
      bp_name = path.split('/')[-2]  # Gets the blueprint name from the path
      return generate_empty_template("Create", bp_name, app_name)
    if path.endswith("list.html"):
      bp_name = path.split('/')[-2]
      return generate_empty_template("List", bp_name, app_name)
    if path.endswith("edit.html"):
      bp_name = path.split('/')[-2]
      return generate_empty_template("Edit", bp_name, app_name)
    if path.endswith("detail.html"):
      bp_name = path.split('/')[-2]
      return generate_empty_template("Detail", bp_name, app_name)
    if path.endswith("database.py"):
        return generate_database_module()
    if path.endswith("__init__.py") and path.count("/") == 2:
        return generate_blueprint_init(path, app_name)
    return ""


if __name__ == "__main__":
    scaffold_flask_app()
