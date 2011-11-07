if (typeof jQuery === 'undefined') jQuery = django.jQuery;

var filtrate = filtrate || {};

filtrate.is_active = function() {
	return jQuery('#changelist-filter div.filtrate').length !== 0;
}
