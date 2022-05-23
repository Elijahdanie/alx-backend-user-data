#!/ur/bin/env python3

"""
........
"""

from os import getenv
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User

@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def auth_login():
    """ POST /api/v1/auth_session/login
    Return:
      - User object JSON represented
    """
    email = request.form.get('email')
    pass_word = request.form.get('password')
    if email is None:
        return jsonify({'error': 'email missing'}), 400
    if pass_word is None:
        return jsonify({'error': 'password missing'}), 400
    users = User.search({'email': email})
    if len(users) == 0:
        return jsonify({'error': 'no user found for this email'}), 404
    if len(users) > 0:
        user = users[0]
    if not User.is_valid_password(user, pass_word):
        return jsonify({'error': 'wrong password'}), 401
    from api.v1.app import auth
    session_id = auth.create_session(user.id)
    res = jsonify(user.to_json())
    res.set_cookie(getenv('SEESION_NAME'), session_id)
    return res
