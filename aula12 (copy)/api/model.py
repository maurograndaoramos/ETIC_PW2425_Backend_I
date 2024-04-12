from pydantic import BaseModel


class Alumni(BaseModel):
    name: str
    id: str
    age: int
    course: str
    graduated: bool
    graduated_year: int
    gpa: int

