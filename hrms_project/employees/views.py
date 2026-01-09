from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employee, Attendance
from .serializers import EmployeeSerializer,AttendanceSerializers
from django.db.models import Count
from django.shortcuts import render
from rest_framework import status

@api_view(['POST'])
def add_employee(request):
    """  
    Api to add new employee
    """
    serializers = EmployeeSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)

    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_employees(request):
    """  
    API to retrieve all Employee
    """
    employees = Employee.objects.all()
    serializers = EmployeeSerializer(employees,many = True)
    return Response(serializers.data)

@api_view(['POST'])
def mark_attendance(request):
    serializers = AttendanceSerializers(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response({'message': 'Attendance marked successfully'},status = 200)
    return Response({'message': 'something went wrong!'})


@api_view(['GET'])
def employee_attendance(request, employee_id):
    """  
    API to get attendance of a particular Employee
    """
    attendance = Attendance.objects.filter(employee_id = employee_id)
    serializers = AttendanceSerializers(attendance,many=True)
    return Response(serializers.data,safe=False)



def home(request):
    return render(request, 'home.html')

def employee_list(request):
    employee = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employee})

def employee_detail(request,employee_id):
    attendance = Attendance.objects.filter(employee_id=employee_id)
    return render(request, 'attendance_detail.html', {'attendance': attendance})

def report(request):
    report_data = Employee.objects.values('department').annotate(count=Count('id'))
