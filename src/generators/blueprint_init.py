def generate_blueprint_init(path):
    bp_name = path.split("/")[1]
    return f"""from flask import Blueprint, render_template

bp = Blueprint('{bp_name}', __name__, url_prefix='/{bp_name}')

@bp.route('/')
def index():
    return render_template('{bp_name}/list.html')
"""
