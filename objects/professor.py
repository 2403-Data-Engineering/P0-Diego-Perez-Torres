from dataclasses import dataclass

@dataclass
class Professor:
    primary_key: int
    first_name: str
    last_name: str
    department: str
    email: str