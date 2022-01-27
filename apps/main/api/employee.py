from rest_framework.viewsets import ModelViewSet

from main.models import Employee
from main.serializers.employee import EmployeeSerializer


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    search_fields = ['full_name', ]
    ordering_fields = ['created_date', ]
