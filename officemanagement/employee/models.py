from django.db import models

# Create your models here.


class Departments(models.Model):
	name = models.CharField(max_length=100)
	location = models.CharField(max_length=100)

	def __str__(self):
		return self.name


class Role(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=100)
	def __str__(self): # we write this method to show the name of the role in the admin panel as we are not able to see it directly
		return self.name + ' - ' + self.description



class Employees(models.Model):
	name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	age = models.IntegerField()
	salary = models.IntegerField()
	department = models.ForeignKey(Departments, on_delete=models.CASCADE) # here we user CASCADE to delete the department if it is deleted
	position = models.ForeignKey(Role, on_delete=models.CASCADE)
	phone = models.CharField(max_length=100)
	hire_date = models.DateField()

	def __str__(self):
		return self.name + ' ' + self.last_name + ' - ' + self.position.name + ' - ' + self.department.name