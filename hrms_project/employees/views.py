from django.shortcuts import get_object_or_404, render, get_list_or_404
from django.http import JsonResponse
from .models import Employee, Attendance
from django.views.decorators.csrf import csrf_exempt
import json

from hrms_project.employees import models

def home(request):
    """
        home page of the HRMS application.
    
    """

    return render(request, 'employees/home.html')

@csrf_exempt
def add_employees(request):
    """
    API to add a new employee
    """
    if request.method == 'POST':
        data = json.loads(request.body)
        employee = Employee.objects.create(
            name=data['name'],
            email=data['email'],
            address=data['address'],
            designation=data['designation'],
            department=data['department'],
            date_of_joining=data['date_of_joining']
        )
        return JsonResponse({'message': 'Employee added successfully'},status=200)
    return JsonResponse({'error': 'Invalid HTTP method'},status=400)

def get_employees(request):
    """
    API to get list of all employees
    """
    employees=list(Employee.objects.values())
    return JsonResponse(employees, safe=False)


def employee_list(request):
    """   
    API to retrive all employees and dispaly
    """
    employees=Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

@csrf_exempt
def mark_attendence(request,employee_id):
    if request.method == 'POST':
        data=json.loads(request.body)
        employee = get_object_or_404(Employee, id=employee_id)
        Attendance.objects.created(
            employee=employee,
            date=data['date'],
            in_time=data['in_time'],
            out_time=data['out_time']
        )
        return JsonResponse({'message': 'Attendance marked successfully'})

def attendance_details(request,employee_id):
    """  
    Display attendance details of employee.
    """
    employee=get_list_or_404(Employee, id=employee_id)
    attendance = Attendance.objects.filter(employee=employee)

    return render(
        request,
        'employee_details.html',
        {'employee': employee, 'attendance': attendance}
    )

def deparment_report(request):
    """  
    Display department wise employee count.

    """

    report=Employee.objects.values('department').annotate(count=models.count('id'))
    return render(
        request,
        'department_report.html',
        {'report': report}
    )


# Create your views here.
