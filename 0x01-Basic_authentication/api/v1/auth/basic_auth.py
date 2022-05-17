#!/usr/bin/env python3

from typing import TypeVar, Tuple
from auth.auth import Auth
from base64 import b64decode
from api.v1.views import User


class BasicAuth(Auth):

    """
    Demonstrates basic authentication
    """

    def __init__(self) -> None:
        super().__init__()


    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """
        Extracts the encoded base64 string from
        authorization token
        """
        if authorization_header is None:
            return None
        if type(authorization_header) not in [str]:
            return None
        parse_auth = authorization_header.split(' ')
        if len(parse_auth) != 2 or parse_auth[0] != 'Basic':
            return None
        else:
            return parse_auth[1]


    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """
        Decodes the base64 string
        """
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None
        try:
            bdata = base64_authorization_header.encode('utf-8')
            return b64decode(bdata).decode('utf-8')
        except Exception:
            return None


    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> Tuple(str, str):
        """
        This function parses the decoded base64 string
        and returns the email and username
        """
        if decoded_base64_authorization_header is None:
            return None
        if type(decoded_base64_authorization_header) is not str:
            return None
        if ':' not in decoded_base64_authorization_header:
            return None
        parsedinfo = decoded_base64_authorization_header.split(':')
        return (parsedinfo[0], parsedinfo[1])


    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """
        This function gets the user from the database
        """
        isemail = user_email is None or type(user_email) is not str
        ispwd = user_pwd is None or type(user_pwd) is not str
        if isemail or ispwd:
            return None
        try:
            users = User.search({'email': user_email})
            validate = users is not None or len(users) != 0
            if validate:
                for user in users:
                    if user.is_valid_password(user_pwd):
                        return user
            return None
        except Exception:
            return None


    def current_user(self, request=None) -> TypeVar('User'):
        """
        This function returns the current user for the session
        """
        a_header = self.authorization_header(request)
        b64string = self.extract_base64_authorization_header(a_header)
        ddata = self.decode_base64_authorization_header(b64string)
        pdata = self.extract_user_credentials(ddata)
        user = self.user_object_from_credentials(pdata[0], pdata[1])
        return user
