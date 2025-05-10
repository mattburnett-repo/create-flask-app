def generate_app_init(blueprint_list):
    imports = "\n    ".join([f"from .{bp} import bp as {bp}_bp" for bp in blueprint_list])
    regs = "\n    ".join([f"app.register_blueprint({bp}_bp)" for bp in blueprint_list])
    return f"""from flask import Flask, render_template

def create_app():
    app = Flask(__name__)
    {imports}

    {regs}

    @app.route("/")
    def index():
        return render_template("index.html")

    return app
"""
