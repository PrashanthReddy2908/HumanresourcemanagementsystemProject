# HumanresourcemanagementsystemProject
creating basic human resource managment system 

1. Project Overview

The Human Resource Management System (HRMS) is a web-based application developed using Django and Django REST Framework (DRF). The system manages employee data, tracks attendance, and generates departmental reports. The project demonstrates CRUD operations, API integration, authentication handling, and a simple UI to view records.

Main Modules:

Employee Management

Attendance Tracking

Departmental Reporting

2. Technologies Used
Category	Technology
Backend	Python 3.13, Django 6.0.1, Django REST Framework
Frontend	HTML5, CSS3, Bootstrap (optional for styling)
Database	MySQL 8.0
Tools	Postman, VS Code, Git, GitHub
3. Project Setup
Step 1: Clone the repository
git clone https://github.com/githubusername/HumanresourcemanagementsystemProject.git
cd HumanresourcemanagementsystemProject

Step 2: Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows

source venv/bin/activate # Linux/Mac

Step 3: Install Requirements
pip install -r requirements.txt OR
pip freeze > requirements.txt

Step 4: Configure Database

Update settings.py with your MySQL credentials:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hrms_db',
        'USER': 'root',
        'PASSWORD': '<your_password>',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

Step 5: Run Migrations
python manage.py makemigrations
python manage.py migrate

Step 6: Run Server
python manage.py runserver


Access the app at: http://127.0.0.1:8000/

4. File Structure
HRMS_Project/
│
├── hrms_project/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── employees/
│   ├── models.py       # Employee & Attendance Models
│   ├── views.py        # APIs and templates
│   ├── serializers.py  # DRF Serializers
│   ├── urls.py         # App-level URLs
│   └── templates/
│       ├── home.html
│       ├── employee_list.html
│       ├── attendance_detail.html
│       └── department_report.html
│
├── manage.py
└── requirements.txt

5. Features & API Endpoints
5.1 Employee Management

Add Employee (POST):

POST /employees/api/employee_data/
Body (JSON):
{
    "name": "John Doe",
    "email": "john@example.com",
    "address": "123 Street",
    "designation": "Developer",
    "department": "IT",
    "date_of_joining": "2026-01-01"
}


List Employees (GET):

GET /employees/api/employee_list/

5.2 Attendance Tracking

Mark Attendance (POST):

POST /employees/api/mark_attendance/
Body (JSON):
{
    "employee": 1,
    "in_time": "09:00:00",
    "out_time": "17:00:00",
    "date": "2026-01-11"
}


Employee Attendance (GET):

GET /employees/api/emp_attendance/<employee_id>/

5.3 Reporting

Department-wise employee count (GET)

GET /employees/report/

6. Sample Outputs
Employee List
ID	Name	Email	Designation	Department	Date of Joining
1	John Doe	john@example.com
	Developer	IT	2026-01-01
2	Jane Smith	jane@example.com
	Manager	HR	2025-12-15
Attendance Detail
Employee	Date	In Time	Out Time
John Doe	2026-01-11	09:00:00	17:00:00
Jane Smith	2026-01-11	09:15:00	17:15:00
Department Report
Department	Employee Count
IT	5
HR	3
Finance	2
7. Future Improvements

Add authentication & authorization for API endpoints

Implement UI using Bootstrap or React for better UX

Export reports as PDF or Excel

Add employee leave management

8. Docstrings & Documentation

All functions, views, and classes in views.py and models.py include proper docstrings explaining purpose, parameters, and return values.

9. Submission Instructions

Zip the project folder

Include the README.md file

Push to GitHub repository