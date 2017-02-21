import json
import jsonfield


from django.db import models
from filer.fields.file import FilerFileField

# Create your models here.


class JSON(models.Model):
    id = models.AutoField(primary_key=True)
    SEASONS = (("Sp", "Spring"),
               ("Su", "Summer"),
               ("F","Fall"),
               ("W", "Winter"))
    year = models.IntegerField(max_length=4)
    season = models.CharField(max_length=2, choices=SEASONS)
    json_file = FilerFileField(null=True, blank=True)
    json_encode = jsonfield.JSONField(json_file)


class Show(models.Model):
    json_id = models.ForeignKey('JSON',on_delete=models.CASCADE,)
    show = models.CharField(max_length=500)
