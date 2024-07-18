@app.route('/principal/assignments', methods=['GET'])
def get_principal_assignments():
    principal_header = request.headers.get('X-Principal')
    if not principal_header or not json.loads(principal_header).get('principal_id'):
        return jsonify({'error': 'Unauthorized'}), 403
    
    assignments = Assignment.query.filter(Assignment.state.in_(['SUBMITTED', 'GRADED'])).all()
    return jsonify({'data': [assignment.to_dict() for assignment in assignments]}), 200
