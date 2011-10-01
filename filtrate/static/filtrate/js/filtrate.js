jQuery = jQuery || django.jQuery.noConflict(false);

var filtrate = filtrate || {};

filtrate.is_active = function() {
	return jQuery('#changelist-filter div.filtrate').length !== 0;
}