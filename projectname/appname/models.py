from django import models


class Records(models.Model):
    value1 = models.CharField(max_length=100)
    value2 = models.IntegerField
    value3 = models.ChatField(max_length=100)
    value4 = models.BooleanField
