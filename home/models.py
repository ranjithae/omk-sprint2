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
     Student_id= models.IntegerField(max_length=10)
     Student_name=models.CharField(max_length=50)
     Student_email=models.CharField(max_length=25)
     Student_grade = models.CharField(max_length=2, default='F')
     Parents_email= models.CharField(max_length=25)
     Parents_phone=models.CharField(max_length=15)
     School= models.CharField(max_length=50)
     Mentor_email =models.ForeignKey(Mentor, related_name= 'Mentor_email')
     Employee_email= models.ForeignKey(Employee, related_name='Employee_email')

def __str__(self):
    return str(self.Student)

class Appointment(models.Model):
    Student_name = models.ForeignKey(Student, related_name='Student_name')
    Mentor_name = models.CharField(max_length=50)
    Student_id = models.ForeignKey(Student, related_name='Student_id')


def __str__(self):
    return str(self.Appointment)







