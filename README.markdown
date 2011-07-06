## About ##

So far only supplies two classes: The base class `FiltrateFilter` that lets you
create your own custom filters and `TreeFilter` that creates a cool expandable
tree using the jsTree jquery plugin.

## Installation ##

* Clone the repo and symlink or copy the "filtrate" folder to your apps folder.
* Add `filtrate` to your installed apps.
* Add the "filtrate/templates" to your template dirs.
* Symlink or copy the "filtrate/static/filtrate" folder to your static folder.
* Make sure the following javascript files is included on the change list view.
  This can be done by overriding the "admin/change_list.html" template and
  adding something like:

```html
<script type="text/javascript" src="/static/filtrate/js/jstree/jquery.jstree.js"></script>
<script type="text/javascript" src="/static/filtrate/js/filtertree.js"></script>
```

## Usage example ##
```python
from filtrate.filters import TreeFilter

# The Filter.
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
    register_filter(client, CompanyDepartmentFilter)
	...
```