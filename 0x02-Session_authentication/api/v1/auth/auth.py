#!/usr/bin/env python3

"""
This module works on
user authentication
"""

from typing import List, TypeVar
from flask import request


class Auth():

    """
    This class handles auth
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Checks if authentication is required
        """
        if path is None or excluded_paths is None or not len(excluded_paths):
            return True
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """
        This function fetches the auth header
        """
        if request is None:
            return None
        if not request.headers.get("Authorization"):
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        ..........
        """
        return None

    def session_cookie(self, request=None) -> str:
        """
        This function fetches the session cookie
        """
        if request is None:
            return None
        if not request.cookies.get("SESSION_NAME"):
            return None
        return request.cookies.get("SESSION_NAME")