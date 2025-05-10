def generate_app_init(blueprint_list, app_name=None):
    imports = "\n    ".join([f"from .{bp} import bp as {bp}_bp" for bp in blueprint_list])
    regs = "\n    ".join([f"app.register_blueprint({bp}_bp)" for bp in blueprint_list])
    return f"""from flask import Flask, render_template
import os
from .database import db

def create_app():
    app = Flask(__name__)
    app.config['APP_NAME'] = '{app_name}'
    
    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    # Configure the database
    app.config['DATABASE'] = os.path.join(app.instance_path, '{app_name.lower()}.sqlite')
    
    # Initialize the database
    db.init_app(app)
    
    {imports}

    {regs}

    @app.route("/")
    def index():
        return render_template("index.html", app_name=app.config['APP_NAME'])

    return app
"""
