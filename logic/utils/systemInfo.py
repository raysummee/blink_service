import platform
import json
import socket


class SystemInfo:
    def minimalInfo(self):
        return json.dumps({
            "machine": platform.machine(),
            "system": platform.platform()
        })

    def qrInfo(self, ip):
        return json.dumps({
            "machine": platform.node(),
            "address": ip,
            "username": "user",
            "password": "test1234"
        })
