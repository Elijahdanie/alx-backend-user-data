#!/usr/bin/env python3

"""
.......
"""

from api.v1.auth.auth import Auth
import uuid
from typing import TypeVar
from models.user import User

class SessionAuth(Auth):
    """
    ........
    """
    user_id_by_session_id = {}
    def create_session(self, user_id: str = None) -> str:
        """
        .........
        """
        if user_id is None or type(user_id) is not str:
            return None
        session_id = uuid.uuid4()
        self.user_id_by_session_id[session_id] = user_id
        return str(session_id)
    
    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        ........
        """
        if session_id is None or type(session_id) is not str:
            return None
        return self.user_id_by_session_id.get(session_id)
    
    def current_user(self, request=None) -> TypeVar('User'):
        """
        ........
        """
        if request is None:
            return None
        session_id = self.session_cookie(request)
        if session_id is None:
            return None
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return None
        return User.get(user_id)
    
    def destroy_session(self, request= None) -> bool:
        """
        ........
        """
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if session_id is None:
            return False
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return False
        self.user_id_by_session_id.pop(session_id)
        return True
