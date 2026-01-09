from rest_framework import serializers
from .models import Employee, Attendance

class EmployeeSerializer(serializers.ModelSerializer):
    """  Serializer for Employee model
    """
    class Meta:
        model = Employee
        fields = '__all__'


class AttendanceSerializers(serializers.ModelSerializer):
    """  Serailizers for Attendance
    """

    class Meta:
        model = Attendance
        fields = '__all__'