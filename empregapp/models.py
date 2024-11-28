from django.db import models

# Create your models here.

class EmpData(models.Model):
    empid=models.IntegerField(primary_key=True)
    empname=models.CharField(max_length=50)
    empdep=models.CharField(max_length=50)
    empmono=models.IntegerField()

    class Meta:
        db_table="newemployee"
