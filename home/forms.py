from django import forms
from .models import Employee, Mentor, Student

class EmployeeForm(forms.ModelForm):
    class Meta:
         model = Employee
         fields = ('Employee_name','Employee_phone','Employee_Address', 'Employee_Id' )



class MentorForm(forms.ModelForm):
    class Meta:
         model = Mentor
         fields = ('Mentor_name','Mentor_phone','Mentor_Address' ,'Mentor_Sex' ,'Mentor_Id')

class StudentForm(forms.ModelForm):
    class Meta:
         model = Student
         fields = ('Student_id','Student_name','Student_email','Student_grade',
                   'Parents_email','Parents_phone','School','Men_email','Emp_email')


