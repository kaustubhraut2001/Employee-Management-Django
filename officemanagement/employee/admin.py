from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Departments)
admin.site.register(Role)
admin.site.register(Employees)

