from django.urls import path
from . import views

urlpatterns=[
    path('',views.home),
    path('api/employees/add/',views.add_employees),
    path('api/employees/',views.get_employees),
    path('employees/',views.employee_list),
    path('attendance/<int:employee_id>/',views.attendance_details),
    path('api/attendance/mark/<int:employee_id>/',views.mark_attendance),
    path('report/',views.department_report),
]