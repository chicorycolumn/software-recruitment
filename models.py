from datetime import date

from pydantic import BaseModel


class User(BaseModel):
    id: int
    firstname: str
    surname: str
    email: str
    primary_trust: str
    start_date: date
    end_date: date
