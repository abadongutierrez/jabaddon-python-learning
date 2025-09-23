from flask import Blueprint, jsonify, request, make_response

course = Blueprint('course', __name__)

courses = [
    {'id': 1, 'name': 'Introduction to Python'},
    {'id': 2, 'name': 'Advanced Flask Development'},
    {'id': 3, 'name': 'Data Science with Python'},
    {'id': 4, 'name': 'Web Development with Django'}
]

@course.route('/courses', methods=['GET'])
def get_courses():
    name = request.args.get('name')
    # filter courses by name if provided
    filter = courses
    if name:
        filter = [course for course in courses if name.lower() in course['name'].lower()]
    return jsonify(filter), 200

# example of a path parameter with type conversion
# other types: string, float, path, uuid
@course.route('/courses/<int:id>', methods=['GET'])
def get_course(id):
    course = next((course for course in courses if course['id'] == id), None)
    status_code = 200
    json_response = {}
    if course:
        json_response = jsonify(course)
    else:
        json_response = jsonify({'error': f'Course {id} not found'})
        status_code = 404

    r = make_response(json_response)
    r.status_code = status_code
    return r

@course.route('/courses', methods=['POST'])
def add_course():
    if not request.is_json:
        return jsonify({'error': 'Request must be JSON'}), 400
    
    data = request.get_json()
    if 'name' not in data:
        return jsonify({'error': 'Course name is required'}), 400
    
    new_id = max(course['id'] for course in courses) + 1 if courses else 1
    new_course = {'id': new_id, 'name': data['name']}
    courses.append(new_course)
    
    return jsonify(new_course), 201