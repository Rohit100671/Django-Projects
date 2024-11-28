from django.db import models

# Create your models here.

class UserData(models.Model):
    username=models.CharField(max_length=50, primary_key=True)
    password=models.CharField(max_length=50)

    class Meta():
        td_table="userdata"