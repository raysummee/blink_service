import platform
import json
import socket

from flask_jwt_extended import create_access_token


class SystemInfo:
    @staticmethod
    def qr_info(ip):
        return json.dumps({
            "machine": platform.node(),
            "address": ip,
            "token": create_access_token(identity="username"),
        })
