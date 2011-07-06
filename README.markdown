## About ##

Stub

## Installation ##

* Clone the repo and symlink or copy the "filtrate" folder to your apps folder.
* Add `filtrate` to your installed apps.
* Add the "filtrate/templates" to your template dirs.
* Symlink or copy the "filtrate/static/filtrate" folder to your static folder.
* Make sure the following javascript files is included on the change list view.
  This can be done by overriding the "admin/change_list.html" template and
  adding something like:

	<script type="text/javascript" src="/static/filtrate/js/jstree/jquery.jstree.js"></script>
	<script type="text/javascript" src="/static/filtrate/js/filtertree.js"></script>