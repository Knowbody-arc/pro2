from django.db import models

# Create your models here.
class cal(models.Model):
    value_a=models.IntegerField()
    value_b=models.IntegerField()
    result=models.FloatField(max_length=20)
