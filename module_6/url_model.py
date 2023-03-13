import json


class UrlModel:
    def __init__(self, url: str, is_ok: bool, status_code):
        self.url = url
        self.is_ok = is_ok
        self.status_code = status_code

    def dump(self):
        return {'url': self.url,
                'is_ok': self.is_ok,
                'status_code': self.status_code}


class UrlModelEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UrlModel):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)
