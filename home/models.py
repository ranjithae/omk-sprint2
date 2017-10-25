from django.db import models
from django.contrib.auth.models import Permission, User
from django.core.validators import MinLengthValidator
from django.core.validators import MaxLengthValidator
from django.core.validators import RegexValidator
from django.utils import timezone
# Create your models here.

regex=r'[0-9]'

class Employee(models.Model):
    Employee_name = models.CharField(max_length=50)
    Employee_phone = models.CharField(max_length=10, validators=[MinLengthValidator(10), RegexValidator(regex)],
                                      help_text="Phone Number should be 10 digits")
    Employee_email = models.EmailField(max_length=50, default='X@gmail.com')
    Employee_Address= models.CharField(max_length=500)
    Employee_Id= models.CharField(max_length=10)

    def __str__(self):
      return str(self.Employee_name)


class Mentor(models.Model):
    Mentor_email = models.EmailField(max_length=50, default='X@gmail.com')
    Mentor_name = models.CharField(max_length=50)
    Mentor_phone = models.CharField(max_length=10, validators=[MinLengthValidator(10), RegexValidator(regex)],
                                    help_text="Phone Number should be 10 digits")
    Mentor_Address=models.CharField(max_length=500)
    Mentor_Gender=models.CharField(max_length=1, default ='X' ,help_text="Enter F or M")
    Mentor_Id=models.CharField(max_length=10)
#    student_count = models.IntegerField(max_digits=10) (we should do the hardcode in later sprint)

    def __str__(self):
       return str(self.Mentor_name)

class Student(models.Model):
     Student_id= models.CharField(max_length=15)
     Student_name=models.CharField(max_length=50)
     Student_email = models.EmailField(max_length=25, default='X@gmail.com')
     Student_grade = models.CharField(max_length=2, default='F')
     Parents_email = models.EmailField(max_length=25, default='X@gmail.com')
     Parents_phone = models.CharField(validators=[MinLengthValidator(10), RegexValidator(regex)], max_length=10)
     School= models.CharField(max_length=50)
     Men_name =models.ForeignKey(Mentor,related_name='Menemail')
     Emp_name= models.ForeignKey(Employee, related_name='Empemail')

     def __str__(self):
      return str(self.Men_name)

     def __str__(self):
       return str(self.Emp_name)

class Appointment(models.Model):
    Sname = models.ForeignKey(Student, related_name='Appointment')
    Mname = models.ForeignKey(Mentor, related_name='Appointment')
    Sid = models.ForeignKey(Student, related_name='Appointment2')


    def __str__(self):
        return str(self.sname)







