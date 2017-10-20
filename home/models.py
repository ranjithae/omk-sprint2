from django.db import models

# Create your models here.

class Employee(models.Model):
    Employee_name = models.CharField(max_length=50)
    Employee_phone = models.CharField(max_length=50)
    Employee_email = models.CharField(max_length=50)


def __str__(self):
    return str(self.Employee)


class Mentor(models.Model):
    Mentor_email = models.CharField(max_length=50)
    Mentor_name = models.CharField(max_length=50)
    Mentor_phone = models.CharField(max_length=50)
#    student_count = models.IntegerField(max_digits=10) (we should do the hardcode in later sprint)


def __str__(self):
    return str(self.Employee)



class Student(models.Model):
     Student_id= models.CharField(max_length=15)
     Student_name=models.CharField(max_length=50)
     Student_email=models.CharField(max_length=25)
     Student_grade = models.CharField(max_length=2, default='F')
     Parents_email= models.CharField(max_length=25)
     Parents_phone=models.CharField(max_length=15)
     School= models.CharField(max_length=50)
     Men_email =models.ForeignKey(Mentor, related_name= 'Student')
     Emp_email= models.ForeignKey(Employee, related_name='Student')

def __str__(self):
    return str(self.Student)

class Appointment(models.Model):
    Sname = models.ForeignKey(Student, related_name='Appointment')
    Mname = models.ForeignKey(Mentor, related_name='Appointment')
    Sid = models.ForeignKey(Student, related_name='Appointment2')


def __str__(self):
    return str(self.Appointment)







