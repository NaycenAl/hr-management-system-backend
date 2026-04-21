from rest_framework.views import APIView
from rest_framework.response import Response

from core.application.use_cases.get_employees import GetEmployees
from core.infrastructure.persistence.repositories import DjangoEmployeeRepository


class EmployeeListView(APIView):
    def get(self, request):
        use_case = GetEmployees(DjangoEmployeeRepository())
        employees = use_case.execute()
        data = [{"id": e.id, "first_name": e.first_name, "last_name": e.last_name, "email": e.email} for e in employees]
        return Response(data)