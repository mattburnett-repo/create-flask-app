import os
import click

from generators.app_init import generate_app_init
from generators.database import generate_database_module
from generators.wsgi import generate_wsgi
from generators.schema import generate_schema
from generators.templates.base_template import generate_base_template
from generators.templates.index_template import generate_index_template
from generators.templates.empty_template import generate_empty_template
from generators.blueprint_init import generate_blueprint_init

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
        "app/templates/index.html",
        "app/templates/components/_header.html",
        "app/templates/components/_navBar.html",
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
                f.write(dispatch_boilerplate(path, blueprint_list))

    # Write requirements
    req_path = os.path.join(base_dir, "requirements.txt")
    with open(req_path, "w") as req_file:
        req_file.write("flask\nclick\n")

    click.echo(f"✅ Flask app scaffolded successfully at: {base_dir}")
    click.echo(f"✅ Next, create/start a venv, cd to the --output folder ({base_dir}) and run 'pip install -r requirements.txt'")
    click.echo("✅ After that's done, run 'flask run'.")


def dispatch_boilerplate(path, blueprint_list):
    if path == "app/__init__.py":
        return generate_app_init(blueprint_list)
    if path == "app/database.py":
        return generate_database_module()
    if path == "wsgi.py":
        return generate_wsgi()
    if path == "app/schema.sql":
        return generate_schema(blueprint_list)
    if path.endswith("base.html"):
      return generate_base_template()
    if path.endswith("index.html") and "templates/" in path and path.count("/") == 2:
        return generate_index_template()
    if path.endswith("create.html"):
        return generate_empty_template("Create")
    if path.endswith("list.html"):
        return generate_empty_template("List")
    if path.endswith("edit.html"):
        return generate_empty_template("Edit")
    if path.endswith("detail.html"):
        return generate_empty_template("Detail")
    if path.endswith("database.py"):
        return generate_database_module()
    if path.endswith("__init__.py") and path.count("/") == 2:
        return generate_blueprint_init(path)
    return ""


if __name__ == "__main__":
    scaffold_flask_app()
