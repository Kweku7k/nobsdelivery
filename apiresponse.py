from flask import json


class ApiResponse:
    def __init__(self, data, code, message, status):
        self.data = data
        self.code = code
        self.message = message
        self.status = status

    def to_json(self):
        return json.dumps({
            "data": self.data,
            "code": self.code,
            "message": self.message,
            "status": self.status
        })
    
    def to_dict(self):
        return {
            "data": self.data,
            "code": self.code,
            "message": self.message,
            "status": self.status
        }   
    
    def __str__(self):
        return self.to_json()