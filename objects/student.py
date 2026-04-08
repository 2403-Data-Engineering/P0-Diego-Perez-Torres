from dataclasses import dataclass


@dataclass
class Student:
    primary_key: int
    first_name: str
    last_name: str
    major: str
    email: str
    year: str