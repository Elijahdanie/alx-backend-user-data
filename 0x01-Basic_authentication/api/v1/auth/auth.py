#!/usr/bin/env python3

"""
This module works on
user authentication
"""

from typing import List, TypeVar
from flask import request

class Auth:

    """
    This class handles auth
    """
    def __init__(self) -> None:
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Checks if authentication is required
        """
        if not path or not excluded_paths or len(excluded_paths) == 0:
            return True
        if path[-1] !=  '/':
            path += '/'
        if path in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """
        ........
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        ........
        """
        return None
