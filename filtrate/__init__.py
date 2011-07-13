import json

from django.contrib.admin.filterspecs import FilterSpec
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe
from django.utils.datastructures import MultiValueDictKeyError

REGISTERED_FILTERS = []
def register_filter(field, filter):
    """
    Registers a model field with a filter, and at the same time registers the
    filter.
    """
    unique_name = "_".join([filter.__module__.replace('.', '_'), 
                            filter.__name__])
    if not unique_name in REGISTERED_FILTERS:
        REGISTERED_FILTERS.append(unique_name)
        callback = lambda f: getattr(f, unique_name, False)
        FilterSpec.filter_specs.insert(0, (callback, filter))
        setattr(field, unique_name, True)