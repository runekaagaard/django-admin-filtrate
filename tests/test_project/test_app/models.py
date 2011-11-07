from django.db import models

from filtrate import register_filter
from filtrate.filters import DateRangeFilter

class CaseDateRangeFilter(DateRangeFilter):
    field_name = 'start_date'

    def get_title(self):
        return "By case start date"

class Case(models.Model):
	start_date = models.DateField()
	register_filter(start_date, CaseDateRangeFilter)
