## About ##
This Django app makes it easier to create custom filters in the change list of
Django Admin and supplies a `TreeFilter` and a `DateRangeFilter` too. Se below.

## The FiltrateFilter ##
The base class that adds support for custom html in the content of the filter
and for using `Media()` classes.

## TreeFilter ##
A recursive tree filter using the excellent library. http://www.jstree.com/. 

### Example ###
```python
# The Filter.
from filtrate.filters import TreeFilter
from itertools import groupby
class CompanyDepartmentFilter(TreeFilter):
    field_name = "client__department__id__in"
    
    def get_title(self):
        return 'By Department'
    
    def get_tree(self):
        from company.models import Department
        qs = Department.objects.all().order_by('company_order', 'company')
        return groupby(qs, lambda obj: getattr(obj, 'company'))

# The model.
from filtrate import register_filter
class Case(Model):
    ...
    register_filter(field_name, CompanyDepartmentFilter)
	...
```

## DateRangeFilter ##
Filters results in a given date range using the jQueryUI datepicker plugin.

### Example ###
```python
# The Filter.
from filtrate.filters import DateRangeFilter

class CaseLicenseStartDateFilter(DateRangeFilter):
    field_name = 'caselicense__start_date'
    
    def get_title(self):
        return "By license start date"

# The model.
from filtrate import register_filter
class Case(Model):
    ...
    register_filter(field_name, CaseLicenseStartDateFilter)
	...
```

## Installation ##

* Clone the repo and symlink or copy the "filtrate" folder to your apps folder.
* Add `filtrate` to your installed apps.
* Add the "filtrate/templates" to your template dirs.

### Static files ###

FlexSelect requires "django.contrib.staticfiles" installed to work out of the 
box. If it is not then the js and css files must be installed manually. 
Read more about "django.contrib.staticfiles" at 
https://docs.djangoproject.com/en/1.3/ref/contrib/staticfiles/.