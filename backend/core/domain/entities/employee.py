# core/domain/entities/employee.py
from dataclasses import dataclass
from datetime import date

@dataclass
class Employee:
    id: int
    first_name: str
    last_name: str
    email: str
    hire_date: date