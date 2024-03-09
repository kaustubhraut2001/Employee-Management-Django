from django.db import models

# Create your models here.


class Departments(models.Model):
	name = models.CharField(max_length=100)
	location = models.CharField(max_length=100)


class Role(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=100)


class Employees(models.Model):
	name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	age = models.IntegerField()
	salary = models.IntegerField()
	department = models.ForeignKey(Departments, on_delete=models.CASCADE)
	position = models.ForeignKey(Role, on_delete=models.CASCADE)
	phone = models.CharField(max_length=100)
	hire_date = models.DateField()