from django.db import models

# Create your models here.

class StudentForm(models.Model):
    username=models.CharField(max_length=50, primary_key=True)
    password=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    mono=models.IntegerField()
    imagepath=models.CharField(max_length=50)


    class Meta:
        db_table="studentformdata"