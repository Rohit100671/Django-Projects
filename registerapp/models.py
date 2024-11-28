from django.db import models

# Create your models here.
class UserData(models.Model):
    username=models.CharField(max_length=50, primary_key=True)
    password=models.CharField(max_length=50)
    mono=models.IntegerField()


    def __str__(self):
        return f"UserName is {self.username}, Password is {self.password} and Mobile Number is {self.mono} "

    class Meta:
        db_table="studentdata"


class Employee(models.Model):
    eid=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=30)
    esalary=models.IntegerField()
    emono=models.IntegerField()


    class Meta:
        db_table="employeedata"
