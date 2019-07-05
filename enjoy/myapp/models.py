from django.db import models

# Create your models here.
class Emp(models.Model):
    f_name=models.CharField(max_length=10)
    l_name=models.CharField(max_length=10)
    #image=models.FileField()
    contact=models.IntegerField()
    email=models.EmailField(max_length=30)
    class Meta:
        db_table = "student"