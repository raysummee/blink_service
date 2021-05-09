import platform
import json


class SystemInfo:
    def minimalInfo(self):
        return json.dumps({
            "machine": platform.machine(),
            "system": platform.platform()
        })
