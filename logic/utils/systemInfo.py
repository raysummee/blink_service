import platform
import json
import socket


class SystemInfo:
    def minimalInfo(self):
        return json.dumps({
            "machine": platform.machine(),
            "system": platform.platform()
        })

    def qrInfo(self):
        return json.dumps({
            "machine": platform.node(),
            "address": socket.gethostbyname(socket.gethostname()),
            "username": "user",
            "password": "test1234"
        })
