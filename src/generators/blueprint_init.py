def generate_blueprint_init(path, app_name=None):
    bp_name = path.split("/")[1]
    return f"""from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.database import db

bp = Blueprint('{bp_name}', __name__, url_prefix='/{bp_name}')

@bp.route('/')
def index():
    # Get all items from the database
    results = db.get_db().execute(f'SELECT * FROM {bp_name}').fetchall()
    return render_template('{bp_name}/list.html', 
                         blueprint_name='{bp_name}',
                         results=results)

@bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        conn = db.get_db()
        conn.execute(f'INSERT INTO {bp_name} (name, description) VALUES (?, ?)',
                  (name, description))
        conn.commit()
        flash('Item created successfully!', 'success')
        return redirect(url_for('{bp_name}.index'))
    return render_template('{bp_name}/create.html', blueprint_name='{bp_name}')

@bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    conn = db.get_db()
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        conn.execute(f'UPDATE {bp_name} SET name = ?, description = ? WHERE id = ?',
                  (name, description, id))
        conn.commit()
        flash('Item updated successfully!', 'success')
        return redirect(url_for('{bp_name}.index'))
    
    result = conn.execute(f'SELECT * FROM {bp_name} WHERE id = ?', (id,)).fetchone()
    return render_template('{bp_name}/edit.html', 
                         blueprint_name='{bp_name}',
                         result=result)

@bp.route('/<int:id>/delete', methods=['POST'])
def delete(id):
    conn = db.get_db()
    conn.execute(f'DELETE FROM {bp_name} WHERE id = ?', (id,))
    conn.commit()
    flash('Item deleted successfully!', 'success')
    return redirect(url_for('{bp_name}.index'))
"""
