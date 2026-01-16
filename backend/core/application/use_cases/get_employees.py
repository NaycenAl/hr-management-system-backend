from backend.core.domain.ports.employee_repository import EmployeeRepository


class GetEmployees:
    def __init__(self, repo: EmployeeRepository):
        self.repo = repo

    def execute(self):
        return self.repo.get_all()