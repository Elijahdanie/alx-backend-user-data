#!/usr/bin/env python3

from auth.auth import Auth
from base64 import b64decode


class BasicAuth(Auth):
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

    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):
        pass
