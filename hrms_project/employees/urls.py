from django.urls import path
from .views import *

urlpatterns=[
    path('', home),
    path('employees/', employee_list),
    path('employees/<int:employee_id>/', employee_detail),
    path('report/', report),



   #API endpoints
    path('api/employee_data/',add_employee),
    path('api/employee_list/',list_employees),
    path('api/employees_list/',EmployeeListView.as_view()),
    path('api/mark_attendance/',mark_attendance),
    path('api/emp_attendance/', AttendanceCreateView.as_view()),
    path('api/emp_attendance/<int:employee_id>/',employee_attendance),

]