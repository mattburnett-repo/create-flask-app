def generate_app_init(blueprint_list, app_name=None):
    imports = "\n    ".join([f"from .{bp} import bp as {bp}_bp" for bp in blueprint_list])
    regs = "\n    ".join([f"app.register_blueprint({bp}_bp)" for bp in blueprint_list])
    return f"""from flask import Flask, render_template

def create_app():
    app = Flask(__name__)
    app.config['APP_NAME'] = '{app_name}'
    {imports}

    {regs}

    @app.route("/")
    def index():
        return render_template("index.html", app_name=app.config['APP_NAME'])

    return app
"""
