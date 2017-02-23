import json
import jsonfield


from django.db import models
from django.db.models.functions import Concat

from filer.fields.file import FilerFileField

# Create your models here.


class Json(models.Model):
    id = models.AutoField(primary_key=True)
    SEASONS = (("Sp", "Spring"),
               ("Su", "Summer"),
               ("F","Fall"),
               ("W", "Winter"))
    year = models.CharField(max_length=4)
    season = models.CharField(max_length=2, choices=SEASONS)
    json_file = FilerFileField(null=True, blank=True)

    def __str__(self):
        return self.season + " " + self.year

class Show(models.Model):
    name = models.CharField(max_length=500)
    MALID = models.IntegerField()
    ANNID = models.IntegerField()
    notes = models.CharField(max_length=500)
    simulcast = models.CharField(max_length=500)
    type = models.CharField(max_length=50)
    name_lower = models.CharField(max_length=500)
    missing_airdate = models.BooleanField()
    missing_airtime = models.BooleanField()
    is_short = models.BooleanField()
    commentary = models.BooleanField()
    simulcast_delay_orig = models.DecimalField(decimal_places=1, max_digits=2)
    simulcast_delay = models.BooleanField()
    simulcast_invalid = models.BooleanField()
    fansub = models.BooleanField()
    has_translation = models.BooleanField()
    simulcast_class = models.CharField(max_length=100)
    fansub_class = models.CharField(max_length=100)
    airdate_u = models.IntegerField()


