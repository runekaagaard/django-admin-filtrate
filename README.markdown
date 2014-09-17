## About ##
This Django app makes it easier to create custom filters in the change list of
Django Admin and supplies a `TreeFilter` and a `DateRangeFilter` too. Se below.

Tested on Django 1.2.3 and from @15ea9a9 1.3.1.

## Updating to 1.3 support ##
I will write proper docs, things are getting messy here, but here is the
lowdown.

### New settings required ###
As I found out, you can't reliably convert the django date formats to
Datepicker formats. So this commit introduces these two new settings:

    FILTRATE = {
		# See http://jqueryui.com/demos/datepicker/#localization.
		'datepicker_region': 'en-GB',
		# See http://docs.jquery.com/UI/Datepicker/formatDate.
		'datepicker_date_format': 'yy-mm-dd',
	}

So if the above defaults does not suit you, you have to change them your self. 
Check out the Datepicker documentation to see how to use them.

### lookup_allowed() ###
Django 1.2.4 introduces restrictions on which lookups that can be queried
in the url, so at the moment the end user are responsible for
checking for those, as in this example:

    class CaseAdmin(admin.ModelAdmin):
		list_filter = ['client']
	
		def lookup_allowed(self, key, *args, **kwargs):
			if 'client__start_date' in key:
				return True
			else:
				return super(CaseAdmin, self).lookup_allowed(key, *args, **kwargs)

### Undefined Media() class bug ###
Time and my Python meta-fu is running out, and I couldn't fix it
so its not neccessary to define an empty Media() class as in:

    class CaseAdmin(admin.ModelAdmin):
		class Media():
			pass
			
## The FiltrateFilter ##
The base class that adds support for custom html in the content of the filter
and for using `Media()` classes.

## TreeFilter ##
A recursive tree filter using the excellent library http://www.jstree.com/. 

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
    client = models.ForeignKey(Client)
    register_filter(client, CompanyDepartmentFilter)
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
    caselicense = models.ForeignKey(Licence)
    register_filter(caselicense, CaseLicenseStartDateFilter)
	...
```

## Installation ##

* Clone the repo and symlink or copy the "filtrate" folder to your apps folder.
* Add `filtrate` to your installed apps, before `django.contrib.admin`.
* Add the "filtrate/templates" folder to your template folders.

### Static files ###

FlexSelect requires "django.contrib.staticfiles" installed to work out of the 
box. If it is not then the js and css files must be installed manually. 
Read more about "django.contrib.staticfiles" at 
https://docs.djangoproject.com/en/1.3/ref/contrib/staticfiles/.
