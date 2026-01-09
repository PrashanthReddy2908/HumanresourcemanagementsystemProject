from django.urls import path
from .views import *

urlpatterns=[
    path('', home),
    path('employees/', employee_list),
    path('employees/<int:employee_id>/', employee_detail),
    path('report/', report),



#   API endpoints
    path('api/add_employee/',add_employee),
    path('api/employees/',list_employees),
    path('api/attendance/',mark_attendance),
    path('api/attendance/<int:employee_id>/',employee_attendance),
]