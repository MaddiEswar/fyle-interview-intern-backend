@app.route('/principal/assignments', methods=['GET'])
def get_principal_assignments():
    principal_header = request.headers.get('X-Principal')
    if not principal_header or not json.loads(principal_header).get('principal_id'):
        return jsonify({'error': 'Unauthorized'}), 403
    
    assignments = Assignment.query.filter(Assignment.state.in_(['SUBMITTED', 'GRADED'])).all()
    return jsonify({'data': [assignment.to_dict() for assignment in assignments]}), 200

@app.route('/principal/teachers', methods=['GET'])
def get_principal_teachers():
    principal_header = request.headers.get('X-Principal')
    if not principal_header or not json.loads(principal_header).get('principal_id'):
        return jsonify({'error': 'Unauthorized'}), 403

    teachers = User.query.filter_by(role='teacher').all()
    return jsonify({'data': [teacher.to_dict() for teacher in teachers]}), 200

@app.route('/principal/assignments/grade', methods=['POST'])
def grade_principal_assignment():
    principal_header = request.headers.get('X-Principal')
    if not principal_header or not json.loads(principal_header).get('principal_id'):
        return jsonify({'error': 'Unauthorized'}), 403

    data = request.json
    assignment = Assignment.query.get(data['id'])
    if not assignment:
        return jsonify({'error': 'Assignment not found'}), 404

    assignment.grade = data['grade']
    assignment.state = 'GRADED'
    db.session.commit()
    return jsonify({'data': assignment.to_dict()}), 200

