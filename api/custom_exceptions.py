from fastapi import HTTPException


class NotFoundError(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail="record not found")
