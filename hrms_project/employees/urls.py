from django.urls import path
from .views import *

app_name = 'employees'

# -------------------------------------------------
#           HTML pages
# -------------------------------------------------
urlpatterns=[
    path('', home, name='home'),
    path('employees/', employee_list, name='employee_list'),
    path('employees/<int:employee_id>/', employee_detail, name='employee_detail'),
    path('report/', report, name='report'),


# ----------------------------------------------------------------
            # API endpoints
# ------------------------------------------------------------------
    path('api/employee_data/', add_employee, name='add_employee'),
    path('api/employee_list/', list_employees, name='list_employees'),
    path('api/employees_list/', EmployeeListView.as_view(), name='employees_list'),
    path('api/mark_attendance/', mark_attendance, name='mark_attendance'),
    path('api/emp_attendance/', AttendanceCreateView.as_view(), name='emp_attendance'),
    path('api/emp_attendance/<int:employee_id>/', employee_attendance, name='employee_attendance'),
]