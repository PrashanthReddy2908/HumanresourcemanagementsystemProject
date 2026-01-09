from django.db import models

class Employee(models.Model):

    """
    stores employees basic information
    
    """
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True, null=True, blank=False)
    address=models.TextField()
    designation=models.CharField(max_length=150)
    department=models.CharField(max_length=100)
    dateofjoining=models.DateField()

    def __str__(self):
        return self.name
    
class Attendance(models.Model):
    employee=models.ForeignKey(Employee, on_delete=models.CASCADE)
    date=models.DateField()
    in_time=models.TimeField()
    out_time=models.TimeField()

    def __str__(self):
        return f"{self.employee.name}-{self.date}"