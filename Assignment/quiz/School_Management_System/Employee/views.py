from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Show_Employees(request):
    Employees = [
        {
            'ID': 1,
            'Name': 'John Doe',
            'Department': 'Sales',
            'Position': 'Sales Manager',
            'Salary': '$60,000'
        },
        {
            'ID': 2,
            'Name': 'Jane Smith',
            'Department': 'Marketing',
            'Position': 'Marketing Director',
            'Salary': '$70,000'
        },
        {
            'ID': 3,
            'Name': 'Michael Johnson',
            'Department': 'HR',
            'Position': 'HR Specialist',
            'Salary': '$50,000'
        }
    ]

    return render(request,"Employee/Show_Employees.html", context = {'employees': Employees})
    
def Employees_Page(request):
    return render(request,"Employee/Employee_Page.html")
    
def Edit_Employees(request):
    Employee={
            'ID': 1,
            'Name': 'John Doe',
            'Department': 'Sales',
            'Position': 'Sales Manager',
            'Salary': '$60,000'
        }
    return render(request,"Employee/Edit_Employee.html",Employee)
def Delete_Employee(request):
    Employees = [
        {
            'ID': 1,
            'Name': 'John Doe',
            'Department': 'Sales',
            'Position': 'Sales Manager',
            'Salary': 60000
        },
        {
            'ID': 2,
            'Name': 'Jane Smith',
            'Department': 'Marketing',
            'Position': 'Marketing Director',
            'Salary': 70000
        },
        {
            'ID': 3,
            'Name': 'Michael Johnson',
            'Department': 'HR',
            'Position': 'HR Specialist',
            'Salary': 50000
        }
    ]
    return render(request,"Employee/Delete_Employee.html",context = {'employees': Employees})