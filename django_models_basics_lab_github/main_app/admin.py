from django.contrib import admin
from .models import Employee, Department, Project

admin.site.register(Employee)
admin.site.register(Project)