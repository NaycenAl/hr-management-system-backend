# core/domain/ports/employee_repository.py
from abc import ABC, abstractmethod
from typing import List
from ..entities.employee import Employee

class EmployeeRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Employee]:
        pass

    @abstractmethod
    def get_by_id(self, employee_id: int) -> Employee:
        pass

    @abstractmethod
    def save(self, employee: Employee) -> Employee:
        pass

    @abstractmethod
    def delete(self, employee_id: int) -> None:
        pass