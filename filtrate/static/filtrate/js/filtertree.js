// Make sure we have a jQuery var for jsTree.
if (typeof jQuery === 'undefined') jQuery = django.jQuery;

(function($) { $(function() {
	"use strict";
	if (!filtrate.is_active()) return;
	var path = 'div.filtrate div.content > div.treefilter'; 
	$(path + ' > textarea').each(function() {
		var tree = $(this).parent().find('form > div.tree');
		tree.jstree({ 
			"themes" : { "theme": "classic", "dots": true, "icons": false },
			"plugins": [ "themes", "json_data", "ui", "checkbox" ],
			"json_data": { "data": $.parseJSON($(this).val()), },
		}).bind("loaded.jstree", {'tree': tree}, function (event) {
			$(this).find('li[is_selected=true]').each(function() {
				$.jstree._reference($(event.data.tree)).check_node(this);
			});
		});
	});
	$(path + ' input[type=submit]').click(function() {
		var form = $(this).parent();
		var tree = form.find('.tree');
		var checked = $.jstree._reference($(tree)).get_checked(false, true);
		checked = $.map(checked, function(n) {
			// Parent nodes without "obj_id" will be discarded.
			return $(n).attr('obj_id');
		}).join(",");
		form.find('input.checked').val(checked);
	});
	
});})(jQuery);
