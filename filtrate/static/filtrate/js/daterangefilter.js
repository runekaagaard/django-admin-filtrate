(function($, that) { $(function() {
	if (!filtrate.is_active() 
	    || typeof that.filtrate.language_code === 'undefined') return;
	var regional = $.datepicker.regional[that.filtrate.language_code];
	regional['dateFormat'] = formats['DATE_FORMAT'];
	$('input.filtrate_date').datepicker(regional);

	$('input.filtrate_date').each(function() {
		var id = $(this).attr('id').replace('__alt', '');
		$(this).datepicker("option", "altField", "#" + id);
		$(this).datepicker("option", "altFormat", 'yy-mm-dd');
	});
	
	$('form.filtrate_daterange_form input[type=submit]').click(function() {
		$(this).parent().find('.filtrate_date').attr('disabled', 'disabled');
	});
	
});})(jQuery || django.jQuery, this);