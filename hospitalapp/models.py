from django.db import models

# Create your models here.

class DoctorData(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    dep=models.CharField(max_length=50)
    mono=models.IntegerField()

    class Meta:
        db_table="doctordata"