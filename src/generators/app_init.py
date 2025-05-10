def generate_app_init(blueprint_list, app_name=None):
    imports = "\n    ".join([f"from .{bp} import bp as {bp}_bp" for bp in blueprint_list])
    regs = "\n    ".join([f"app.register_blueprint({bp}_bp)" for bp in blueprint_list])
    return f"""from flask import Flask, render_template
import os
from .database import db

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config['APP_NAME'] = '{app_name}'
    
    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    # Configure the database
    app.config['DATABASE'] = os.path.join(app.instance_path, '{app_name.lower()}.sqlite')
    
    # Load the instance config, if it exists, when not testing
    if test_config is None:
        # Load the config file if it exists, otherwise create it
        config_path = os.path.join(app.instance_path, 'config.py')
        if os.path.exists(config_path):
            app.config.from_pyfile(config_path)
        else:
            # Generate a new secret key and save it
            secret_key = os.urandom(24).hex()
            with open(config_path, 'w') as f:
                f.write("SECRET_KEY = '{{secret_key}}'\\n".format(secret_key=secret_key))
            app.config['SECRET_KEY'] = secret_key
    else:
        # Load the test config if passed in
        app.config.update(test_config)

    # Initialize the database
    db.init_app(app)
    
    {imports}

    {regs}

    @app.route("/")
    def index():
        return render_template("index.html", app_name=app.config['APP_NAME'])

    return app
"""
