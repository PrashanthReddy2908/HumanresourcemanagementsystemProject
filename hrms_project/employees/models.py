from django.db import models

class Employee(models.Model):

    """
    stores employees basic information
    
    """
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True, null=True)
    address=models.TextField()
    designation=models.CharField(max_length=150)
    department=models.CharField(max_length=100)
    date_of_joining=models.DateField()

    def __str__(self):
        return self.name
    
class Attendance(models.Model):
    employee=models.ForeignKey(Employee, on_delete=models.CASCADE)
    date=models.DateField()
    in_time=models.TimeField()
    out_time=models.TimeField()
    status = models.CharField(
        max_length=20,
        default="Present"
    )

    def __str__(self):
        return f"{self.employee.name}-{self.date}"