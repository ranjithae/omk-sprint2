from django.contrib import admin
from .models import Employee, Mentor, Student




class EmployeeList(admin.ModelAdmin):
    list_display = ('Employee_name', 'Employee_phone', 'Employee_Address', 'Employee_Id')
    search_fields = ('Employee_name', 'Employee_email','Employee_Id')


class MentorList(admin.ModelAdmin):
    list_display = ('Mentor_name', 'Mentor_phone', 'Mentor_Id','Mentor_Address','Mentor_Sex')
    search_fields = ('Mentor_name', 'Mentor_email','Mentor_Id')

class StudentList(admin.ModelAdmin):
    list_display = ('Student_id', 'Student_name', 'Student_email', 'Parents_email',
                    'Parents_phone', 'School', 'Men_email','Emp_email')
    search_fields = ('Student_name', 'Mentor_email', 'Student_id', 'School')

admin.site.register(Employee,EmployeeList )
admin.site.register(Mentor,MentorList)
admin.site.register(Student, StudentList)