
from .models import EmployeeModel
from ...domain.entities.employee import Employee
from ...domain.ports.employee_repository import EmployeeRepository


class DjangoEmployeeRepository(EmployeeRepository):
    def get_all(self):
        return [Employee(id=e.id, first_name=e.first_name, last_name=e.last_name, email=e.email, hire_date=e.hire_date) for e in EmployeeModel.objects.all()]

    def get_by_id(self, employee_id: int):
        e = EmployeeModel.objects.get(id=employee_id)
        return Employee(id=e.id, first_name=e.first_name, last_name=e.last_name, email=e.email, hire_date=e.hire_date)

    def save(self, employee: Employee):
        if hasattr(employee, "id") and employee.id:
            e = EmployeeModel.objects.get(id=employee.id)
            e.first_name = employee.first_name
            e.last_name = employee.last_name
            e.email = employee.email
            e.hire_date = employee.hire_date
        else:
            e = EmployeeModel.objects.create(
                first_name=employee.first_name,
                last_name=employee.last_name,
                email=employee.email,
                hire_date=employee.hire_date
            )
        e.save()
        employee.id = e.id
        return employee

    def delete(self, employee_id: int):
        EmployeeModel.objects.filter(id=employee_id).delete()