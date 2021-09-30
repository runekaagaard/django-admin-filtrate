from django.db import models

from filtrate.filters import DateRangeFilter

class CaseClientDateRangeFilter(DateRangeFilter):
    field_name = 'client__start_date'

    def get_title(self):
        return "By clients start date"

class Client(models.Model):
    start_date = models.DateField()
    name = models.CharField(max_length=80)

class Case(models.Model):
    client = models.ForeignKey(Client)
