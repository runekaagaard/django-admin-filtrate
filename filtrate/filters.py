import json

from django.contrib.admin.filterspecs import FilterSpec
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe
from django.utils.datastructures import MultiValueDictKeyError
from django.core.exceptions import ImproperlyConfigured

class FiltrateFilter(FilterSpec):
    """
    The base django_admin_filtrate filter. It requires overriding of 
    `get_title()` and `get_content()` methods. If your are using a form, adding 
    `_form_duplicate_getparams()` inside the form html tags might come in handy.
    
    Requires the altered template for "filter.html".
    """
    def __init__(self, f, request, params, model, model_admin):
        super(FiltrateFilter, self).__init__(f, request, params, model, 
                                             model_admin)
        self.request = request
        self.params = params
        self.model = model
        self.model_admin = model_admin
    
    def _form_duplicate_getparams(self):
        """Replicates the get parameters as hidden form fields."""
        s = '<input type="hidden" name="%s" value="%s"/>'
        return "".join([s % (k,v) for k,v in self.request.GET.iteritems() 
                        if k not in ('e', self.field_name)])
        
    def title(self):
        """Triggers the alternate rendering in "filter.html"."""
        return '__filtrate__'
    
    def choices(self, cl):
        """As only title and choices is passed to "filter.html" template, we
        sets title to "__filtrate__" and passes real title and content from 
        here. 
        """
        return [{
            'title': self.get_title(),
            'content': self.get_content(),
        }]
    
    # Must be overridden.
    
    def get_title(self):
        """The title of the filter. Must include "After" in the beginning."""
        raise NotImplementedError()
    
    def get_content(self):
        """The content part of the filter in html."""
        raise NotImplementedError()

class TreeFilter(FiltrateFilter):
    """
    A tree filter for models. Uses the jsTree jQuery plugin found at 
    http://www.jstree.com/ in the frontend.
    
    Overiding classes needs to implement `field_name`, `get_title()` and 
    `get_tree()`.
    """
    
    def __init__(self, f, request, params, model, model_admin):
        super(TreeFilter, self).__init__(f, request, params, model, 
                                             model_admin)
        try:
            self.selected_nodes = self.request.GET.__getitem__(
                                                     self.field_name).split(",")
            self.selected_nodes = map(int, self.selected_nodes)
        except MultiValueDictKeyError:
            self.selected_nodes = []
        if not self.field_name:
            raise ImproperlyConfigured('The "field_name" class attribute '
                                       'must be implemented.')
        
    def _tree_to_json(self, tree):
        """Recusively walks through the tree and generate json in a format
        suitable for jsTree.""" 
        def parse_tree(tree, cur_tree):
            for node in tree:
                if type(node) == type(tuple()):
                    # Is a parent node.
                    title = force_unicode(node[0])
                    new_tree = []
                    cur_tree.append({
                        'data': title,
                        'children': new_tree,
                    })
                    parse_tree(node[1], new_tree)
                else:
                    # Is a leaf node.
                    title = force_unicode(node)
                    cur_tree.append({
                        "attr" : { 
                            "obj_id": node.pk, 
                            "is_selected": node.pk in self.selected_nodes, 
                        },                   
                        'data': force_unicode(node),
                    })

        json_tree = []
        parse_tree(tree, json_tree)
        return json.dumps(json_tree)
        
    def get_content(self):
        """Return html for entire filter."""
        return mark_safe("""
            <div class="treefilter">
                <textarea style="display: none;">%s</textarea>
                <form action_method="get">
                    <div class="tree"></div>
                    <input class="checked" type="hidden" name="%s" value=""/>
                    <input type="submit" value="Send" />
                    %s
                </form>
            </div>
        """ % (self._tree_to_json(self.get_tree()), self.field_name, 
               self._form_duplicate_getparams()))
    
    # Must be overridden.
    
    # The POST field name with the trailing '__in'.
    # I.E. "client__department__id__in". The objects returned from `get_tree()`
    # should fit with this.
    field_name = None
    
    def get_title(self):
        """The title of the filter. Must include "After" in the beginning."""
        raise NotImplementedError()
    
    def get_tree(self):
        """
        Must return a tree of model instances as a tuple of objects or tuples 
        as:
        ( # Root level.
            obj1,  
            obj2,
            ( # Nested level.
                obj3,
                obj4,
                ( # More nested level.
                    obj3,
                    obj4,
                ),
            ),
        ) 
        """
        raise NotImplementedError