from django.db import models
from django.contrib.auth.models import Permission, User
# Create your models here.

class Employee(models.Model):
    Employee_name = models.CharField(max_length=50)
    Employee_phone = models.CharField(max_length=10)
    #Employee_email = models.CharField(max_length=50)
    Employee_Address= models.CharField(max_length=500)
    Employee_Id= models.CharField(max_length=10)

    def __str__(self):
      return str(self.Employee_name)


class Mentor(models.Model):
    #Mentor_email = models.CharField(max_length=50)
    Mentor_name = models.CharField(max_length=50)
    Mentor_phone = models.CharField(max_length=10)
    Mentor_Address=models.CharField(max_length=500)
    Mentor_Gender=models.CharField(max_length=1, default ='X')
    Mentor_Id=models.CharField(max_length=10)
#    student_count = models.IntegerField(max_digits=10) (we should do the hardcode in later sprint)

    def __str__(self):
       return str(self.Mentor_name)

class Student(models.Model):
     Student_id= models.CharField(max_length=15)
     Student_name=models.CharField(max_length=50)
     Student_email=models.CharField(max_length=25)
     Student_grade = models.CharField(max_length=2, default='F')
     Parents_email= models.CharField(max_length=25)
     Parents_phone=models.CharField(max_length=15)
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







