from django.shortcuts import render , redirect
from templates import  *
# from models import *

# Create your views here.


def index(request):
	return render(request, 'index.html')

def add_employee(request):
	if request.method == 'POST':

		name  = request.POST["name"]
		last_name = request.POST["last_name"]
		email = request.POST["email"]
		phone = request.POST["phone"]
		address = request.POST["address"]
		salary = request.POST["salary"]
		position = request.POST["position"]
		department = request.POST["department"]
		hire_date = request.POST["hire_date"]
		employee = Employees(name=name, last_name=last_name, email=email, phone=phone, address=address, salary=salary, position=position, department=department, hire_date=hire_date)
		employee.save()
	return render(request, 'add_employee.html')

def remove_employee(request):
	return render(request, 'remove_employee.html')

def edit_employee(request):
	return render(request, 'edit_employee.html')