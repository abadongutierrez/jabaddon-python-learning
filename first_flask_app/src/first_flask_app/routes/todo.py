from flask import Blueprint, render_template, request, redirect, url_for, flash
from datetime import datetime

todo_bp = Blueprint('todo', __name__)

# In-memory storage for todos (replace with database in production)
todos = []
next_id = 1

def create_todo(title, description="", completed=False):
    global next_id
    now = datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
    todo = {
        'id': next_id,
        'title': title,
        'description': description,
        'completed': completed,
        'created_at': now,
        'updated_at': now
    }
    next_id += 1
    return todo

def find_todo(todo_id):
    return next((todo for todo in todos if todo['id'] == todo_id), None)

@todo_bp.route('/todo')
def list_todos():
    """Display all todos with forms to manage them"""
    completed_filter = request.args.get('filter')
    filtered_todos = todos

    if completed_filter == 'completed':
        filtered_todos = [todo for todo in todos if todo['completed']]
    elif completed_filter == 'pending':
        filtered_todos = [todo for todo in todos if not todo['completed']]

    return render_template('todo_list.html',
                         todos=filtered_todos,
                         current_filter=completed_filter)

@todo_bp.route('/todo', methods=['POST'])
def create_todo_item():
    """Create a new todo from form submission"""
    title = request.form.get('title', '').strip()
    description = request.form.get('description', '').strip()

    if not title:
        flash('Title is required!', 'error')
        return redirect(url_for('todo.list_todos'))

    todo = create_todo(title=title, description=description)
    todos.append(todo)
    flash('Todo created successfully!', 'success')

    return redirect(url_for('todo.list_todos'))

@todo_bp.route('/todo/<int:todo_id>/update', methods=['POST'])
def update_todo(todo_id):
    """Update an existing todo from form submission"""
    todo = find_todo(todo_id)
    if not todo:
        flash(f'Todo {todo_id} not found!', 'error')
        return redirect(url_for('todo.list_todos'))

    title = request.form.get('title', '').strip()
    description = request.form.get('description', '').strip()
    # When a checkbox is checked, its name appears in request.form
    completed = 'completed' in request.form

    if not title:
        flash('Title is required!', 'error')
        return redirect(url_for('todo.list_todos'))

    todo['title'] = title
    todo['description'] = description
    todo['completed'] = completed
    todo['updated_at'] = datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S')

    flash('Todo updated successfully!', 'success')
    return redirect(url_for('todo.list_todos'))

@todo_bp.route('/todo/<int:todo_id>/delete', methods=['POST'])
def delete_todo(todo_id):
    """Delete a todo from form submission"""
    todo = find_todo(todo_id)
    if not todo:
        flash(f'Todo {todo_id} not found!', 'error')
        return redirect(url_for('todo.list_todos'))

    todos.remove(todo)
    flash('Todo deleted successfully!', 'success')
    return redirect(url_for('todo.list_todos'))

@todo_bp.route('/todo/<int:todo_id>/toggle', methods=['POST'])
def toggle_todo(todo_id):
    """Toggle completion status of a todo"""
    todo = find_todo(todo_id)
    if not todo:
        flash(f'Todo {todo_id} not found!', 'error')
        return redirect(url_for('todo.list_todos'))

    todo['completed'] = not todo['completed']
    todo['updated_at'] = datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S')

    status = 'completed' if todo['completed'] else 'pending'
    flash(f'Todo marked as {status}!', 'success')
    return redirect(url_for('todo.list_todos'))